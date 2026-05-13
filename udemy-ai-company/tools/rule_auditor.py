#!/usr/bin/env python3
"""AI-Ops-01 rule auditor for GitHub Issue driven operations.

The auditor reports rule drift and applies only low-risk label fixes:
- add `pm` to open managed issues
- add `approval-required` and `blocked` to open issues waiting for CEO approval

It does not close issues, start execution, approve work, or change deliverables.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


COMPANY_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JSON_OUT = COMPANY_ROOT / ".pm_state" / "rule_audit_latest.json"

AUDIT_LABEL = "rule-audit"
PM_LABEL = "pm"
OPS_LABEL = "ops"
APPROVAL_REQUIRED_LABEL = "approval-required"
CEO_APPROVED_LABEL = "ceo-approved"
BLOCKED_LABEL = "blocked"
DONE_LABEL = "done"
PM_QUEUED_LABEL = "pm-queued"
IN_PROGRESS_LABEL = "in-progress"

DEFAULT_AUDIT_TITLE = "AI-Ops Rule Audit"

BILLING_KEYWORDS = (
    "aws cloudformation deploy",
    "aws cloudformation create-stack",
    "aws cloudformation update-stack",
    "aws cloudformation delete-stack",
    "create-stack",
    "update-stack",
    "delete-stack",
    "deploy.sh",
    "submit_job",
    "submit-job",
    "start_image_build",
    "build_and_push",
    "docker push",
    "fargate",
    "batch",
    "ecr",
    "ecs",
    "lambda",
    "rds",
    "vpc",
    "cloudwatch alarm",
    "sns topic",
    "iam role",
    "aws環境",
    "環境構築",
    "スタック作成",
    "スタック更新",
    "スタック削除",
    "デプロイ",
    "課金",
    "料金",
    "コスト",
)

CEO_APPROVAL_WAITING_PATTERNS = (
    r"CEO\s*承認\s*待ち",
    r"CEO\s*確認\s*待ち",
    r"CEO\s*レビュー\s*待ち",
    r"公開\s*承認\s*待ち",
    r"最終\s*承認\s*待ち",
    r"Ready\s+for\s+Publish",
)

COURSE_SPEC_REQUIRED_KEYWORDS = (
    "cloudformation",
    "template.yaml",
    "ハンズオン",
    "動画",
    "スライド",
    "gpt-image2",
    "voicevox",
    "台本",
    "音声",
    "教材",
    "qa",
    "レビュー",
)

REQUIRED_AGENT_REFS = (
    "docs/MISSION_VISION_VALUES.md",
    "docs/PM_AUTOMATION.md",
    "docs/QUALITY_GATE.md",
)


@dataclass
class Finding:
    severity: str
    category: str
    target: str
    message: str
    recommendation: str


@dataclass
class FixAction:
    target: str
    action: str
    status: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="AI-Ops-01 rule consistency auditor.")
    parser.add_argument("--repo", help="GitHub repository in owner/name format.")
    parser.add_argument("--limit", type=int, default=1000, help="Max open issues to audit.")
    parser.add_argument("--apply", action="store_true", help="Apply low-risk label fixes and post audit comment.")
    parser.add_argument(
        "--audit-issue-title",
        default=DEFAULT_AUDIT_TITLE,
        help="Title of the single GitHub Issue used for audit history.",
    )
    parser.add_argument(
        "--json-out",
        type=Path,
        default=DEFAULT_JSON_OUT,
        help="Local JSON snapshot path. Use '-' to skip local JSON output.",
    )
    parser.add_argument(
        "--queued-hours",
        type=float,
        default=6.0,
        help="Warn when pm-queued or in-progress remains for this many hours.",
    )
    parser.add_argument(
        "--fail-on-critical",
        action="store_true",
        help="Exit with status 1 when critical findings are detected.",
    )
    return parser.parse_args()


def gh(args: list[str], repo: str | None = None, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
    cmd = ["gh", *args]
    if repo:
        cmd.extend(["--repo", repo])
    return subprocess.run(cmd, input=input_text, text=True, capture_output=True, check=False)


def gh_json(args: list[str], repo: str | None = None) -> Any:
    result = gh(args, repo=repo)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"gh returned invalid JSON: {exc}") from exc


def issue_labels(issue: dict[str, Any]) -> set[str]:
    labels = issue.get("labels") or []
    return {label.get("name", "") for label in labels if label.get("name")}


def get_field(body: str, name: str) -> str:
    pattern = re.compile(rf"^{re.escape(name)}\s*:\s*(.*?)\s*$", re.IGNORECASE | re.MULTILINE)
    match = pattern.search(body or "")
    return match.group(1).strip() if match else ""


def has_field(body: str, name: str) -> bool:
    pattern = re.compile(rf"^{re.escape(name)}\s*:", re.IGNORECASE | re.MULTILINE)
    return bool(pattern.search(body or ""))


def truthy(value: str) -> bool:
    normalized = value.strip().lower()
    return normalized in {"yes", "y", "true", "1", "auto", "自動", "はい", "あり", "必要"}


def falsey_or_empty(value: str) -> bool:
    normalized = value.strip().lower()
    return normalized in {"", "no", "n", "false", "0", "none", "n/a", "na", "なし", "無", "不要"}


def approval_in_text(text: str) -> bool:
    if not text:
        return False
    return bool(
        re.search(r"/approve-cost\b", text, re.IGNORECASE)
        or re.search(r"CEO\s*Approval\s*:\s*approved", text, re.IGNORECASE)
        or re.search(r"CEO承認\s*:\s*承認", text)
        or re.search(r"CEO承認済", text)
    )


def is_billing_sensitive(issue: dict[str, Any]) -> bool:
    labels = issue_labels(issue)
    body = issue.get("body") or ""
    title = issue.get("title") or ""
    haystack = f"{title}\n{body}".lower()

    if APPROVAL_REQUIRED_LABEL in labels:
        return True
    if truthy(get_field(body, "Requires CEO Approval")):
        return True

    cost_impact = get_field(body, "Cost Impact")
    if not falsey_or_empty(cost_impact):
        return True

    return any(keyword.lower() in haystack for keyword in BILLING_KEYWORDS)


def has_ceo_waiting_phrase(issue: dict[str, Any]) -> bool:
    text = f"{issue.get('title') or ''}\n{issue.get('body') or ''}"
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in CEO_APPROVAL_WAITING_PATTERNS)


def is_ceo_approved(issue: dict[str, Any]) -> bool:
    labels = issue_labels(issue)
    return CEO_APPROVED_LABEL in labels or approval_in_text(issue.get("body") or "")


def has_ceo_approval_gate(issue: dict[str, Any]) -> bool:
    body = issue.get("body") or ""
    labels = issue_labels(issue)
    return bool(
        APPROVAL_REQUIRED_LABEL in labels
        or truthy(get_field(body, "Requires CEO Approval"))
        or has_field(body, "CEO Approval")
        or is_billing_sensitive(issue)
        or has_ceo_waiting_phrase(issue)
    )


def is_ceo_approval_waiting(issue: dict[str, Any]) -> bool:
    return has_ceo_approval_gate(issue) and not is_ceo_approved(issue)


def parse_timestamp(value: str) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(UTC)
    except ValueError:
        return None


def should_require_course_spec(issue: dict[str, Any]) -> bool:
    text = f"{issue.get('title') or ''}\n{issue.get('body') or ''}".lower()
    return any(keyword.lower() in text for keyword in COURSE_SPEC_REQUIRED_KEYWORDS)


def is_audit_issue(issue: dict[str, Any], audit_title: str) -> bool:
    return issue.get("title") == audit_title or AUDIT_LABEL in issue_labels(issue)


def add_labels(issue_number: int, labels: list[str], repo: str | None) -> bool:
    if not labels:
        return True
    result = gh(["issue", "edit", str(issue_number), "--add-label", ",".join(labels)], repo=repo)
    if result.returncode != 0:
        print(f"[warn] label update failed for #{issue_number}: {result.stderr.strip()}", file=sys.stderr)
        return False
    return True


def list_open_issues(repo: str | None, limit: int) -> list[dict[str, Any]]:
    fields = "number,title,body,labels,url,updatedAt,createdAt"
    return gh_json(["issue", "list", "--state", "open", "--limit", str(limit), "--json", fields], repo=repo)


def find_audit_issue(repo: str | None, title: str) -> dict[str, Any] | None:
    issues = gh_json(
        ["issue", "list", "--state", "open", "--limit", "100", "--json", "number,title,url,labels"],
        repo=repo,
    )
    for issue in issues:
        if issue.get("title") == title:
            return issue
    return None


def create_audit_issue(repo: str | None, title: str) -> dict[str, Any]:
    body = (
        "AI-Ops-01が仕組みルールの整合性を定期チェックするための監査Issueです。\n\n"
        "- このIssueは自動監査コメントの集約先です。\n"
        "- AI-Ops-01は実装、レビュー、公開承認を行いません。\n"
        "- 軽微なラベル補正以外は報告に留めます。\n"
    )
    result = gh(
        ["issue", "create", "--title", title, "--body", body, "--label", f"{OPS_LABEL},{AUDIT_LABEL}"],
        repo=repo,
    )
    if result.returncode != 0:
        fallback = gh(["issue", "create", "--title", title, "--body", body], repo=repo)
        if fallback.returncode != 0:
            raise RuntimeError(fallback.stderr.strip() or fallback.stdout.strip())
    issue = find_audit_issue(repo, title)
    if not issue:
        raise RuntimeError("audit issue was created but could not be found")
    return issue


def comment_issue(issue_number: int, body: str, repo: str | None) -> None:
    result = gh(["issue", "comment", str(issue_number), "--body", body], repo=repo)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())


def audit_documents(findings: list[Finding]) -> None:
    agents = COMPANY_ROOT / "AGENTS.md"
    pm_automation = COMPANY_ROOT / "docs" / "PM_AUTOMATION.md"
    task_template = COMPANY_ROOT / ".github" / "ISSUE_TEMPLATE" / "task.md"

    if agents.exists():
        text = agents.read_text(encoding="utf-8")
        for required in REQUIRED_AGENT_REFS:
            if required not in text:
                findings.append(
                    Finding(
                        "warning",
                        "docs",
                        "AGENTS.md",
                        f"`{required}` が参照必須ファイルに含まれていません。",
                        "AGENTS.mdの参照必須ファイルへ追加してください。",
                    )
                )
    else:
        findings.append(Finding("critical", "docs", "AGENTS.md", "AGENTS.md が見つかりません。", "復旧してください。"))

    if pm_automation.exists():
        text = pm_automation.read_text(encoding="utf-8")
        for required in ("--close-non-approval", "CEO承認待ち"):
            if required not in text:
                findings.append(
                    Finding(
                        "warning",
                        "docs",
                        "docs/PM_AUTOMATION.md",
                        f"`{required}` の運用記述が見つかりません。",
                        "PM自動化ルールにCEO承認待ち以外のclose方針を明記してください。",
                    )
                )
    else:
        findings.append(
            Finding("critical", "docs", "docs/PM_AUTOMATION.md", "PM_AUTOMATION.md が見つかりません。", "復旧してください。")
        )

    if task_template.exists():
        text = task_template.read_text(encoding="utf-8")
        for required in ("Owner AI:", "Reviewer AI:", "Definition of Done:", "Mission/Vision/Values Alignment:"):
            if required not in text:
                findings.append(
                    Finding(
                        "warning",
                        "template",
                        ".github/ISSUE_TEMPLATE/task.md",
                        f"`{required}` がTaskテンプレートにありません。",
                        "Taskテンプレートへ必須欄を追加してください。",
                    )
                )
    else:
        findings.append(
            Finding("critical", "template", ".github/ISSUE_TEMPLATE/task.md", "Taskテンプレートが見つかりません。", "復旧してください。")
        )


def audit_single_issue(issue: dict[str, Any], args: argparse.Namespace, findings: list[Finding], fixes: list[FixAction]) -> None:
    if is_audit_issue(issue, args.audit_issue_title):
        return

    number = issue["number"]
    target = f"#{number} {issue.get('title') or ''}"
    body = issue.get("body") or ""
    labels = issue_labels(issue)
    owner = get_field(body, "Owner AI")
    reviewer = get_field(body, "Reviewer AI")
    dod = get_field(body, "Definition of Done")
    mvv = get_field(body, "Mission/Vision/Values Alignment")
    blocked_by = get_field(body, "Blocked By")
    updated_at = parse_timestamp(issue.get("updatedAt") or "")

    missing_fix_labels: list[str] = []
    if PM_LABEL not in labels:
        missing_fix_labels.append(PM_LABEL)

    if is_ceo_approval_waiting(issue):
        for label in (APPROVAL_REQUIRED_LABEL, BLOCKED_LABEL):
            if label not in labels:
                missing_fix_labels.append(label)
    else:
        findings.append(
            Finding(
                "warning",
                "pm-close-policy",
                target,
                "CEO承認待ちではないOpen Issueです。",
                "AI-PM-01の `--close-non-approval` でclose対象にしてください。",
            )
        )

    if args.apply and missing_fix_labels:
        ok = add_labels(number, sorted(set(missing_fix_labels)), args.repo)
        fixes.append(FixAction(target, f"add labels: {', '.join(sorted(set(missing_fix_labels)))}", "applied" if ok else "failed"))
    elif missing_fix_labels:
        fixes.append(FixAction(target, f"add labels: {', '.join(sorted(set(missing_fix_labels)))}", "dry-run"))

    if not owner:
        findings.append(Finding("warning", "issue-fields", target, "`Owner AI` が空です。", "Issue本文にOwner AIを記入してください。"))
    if not reviewer:
        findings.append(
            Finding("warning", "issue-fields", target, "`Reviewer AI` が空です。", "Issue本文にReviewer AIを記入してください。")
        )
    if owner and reviewer and owner == reviewer:
        findings.append(
            Finding(
                "critical",
                "separation",
                target,
                "Owner AIとReviewer AIが同一です。",
                "Worker != Reviewer になるようにReviewer AIを変更してください。",
            )
        )
    if not dod:
        findings.append(
            Finding("warning", "issue-fields", target, "`Definition of Done` が空です。", "完了条件を明記してください。")
        )
    if not mvv:
        findings.append(
            Finding(
                "warning",
                "issue-fields",
                target,
                "`Mission/Vision/Values Alignment` が空です。",
                "docs/MISSION_VISION_VALUES.mdとの整合性を記録してください。",
            )
        )
    if should_require_course_spec(issue) and "course_spec.md" not in body:
        findings.append(
            Finding(
                "warning",
                "source-of-truth",
                target,
                "`course_spec.md` への参照がありません。",
                "講座成果物に関わるIssueでは対象講座のcourse_spec.mdをInput Filesへ入れてください。",
            )
        )
    if is_billing_sensitive(issue) and not is_ceo_approved(issue):
        findings.append(
            Finding(
                "critical",
                "approval",
                target,
                "課金影響がある可能性があるが、CEO承認が未記録です。",
                "`approval-required` と `blocked` を付け、CEO承認後に `ceo-approved` または `/approve-cost` を記録してください。",
            )
        )
    if is_billing_sensitive(issue) and is_ceo_approved(issue):
        findings.append(
            Finding(
                "info",
                "approval",
                target,
                "CEO承認済みIssueがOpenのままです。",
                "承認内容を実行するTask Issueへ分離し、このIssueはcloseしてください。",
            )
        )
    if BLOCKED_LABEL in labels and not blocked_by:
        findings.append(
            Finding(
                "warning",
                "blocked",
                target,
                "`blocked` ラベルがありますが `Blocked By` が空です。",
                "Blocked理由、判断者、次の確認期限を記録してください。",
            )
        )
    if labels.intersection({PM_QUEUED_LABEL, IN_PROGRESS_LABEL}) and updated_at:
        hours = (datetime.now(UTC) - updated_at).total_seconds() / 3600
        if hours >= args.queued_hours:
            findings.append(
                Finding(
                    "warning",
                    "stale-processing",
                    target,
                    f"`pm-queued` または `in-progress` が {hours:.1f} 時間残っています。",
                    "AI-Ops-01が実行状況を確認し、必要ならblockedまたは再実行Issueに分けてください。",
                )
            )


def render_report(findings: list[Finding], fixes: list[FixAction], issue_count: int, audit_issue_url: str | None) -> str:
    now = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC")
    severity_counts = {severity: 0 for severity in ("critical", "warning", "info")}
    for finding in findings:
        severity_counts[finding.severity] = severity_counts.get(finding.severity, 0) + 1

    lines = [
        "AI-Ops-01 Rule Audit",
        "",
        f"- Time: {now}",
        f"- Audited Open Issues: {issue_count}",
        f"- Critical: {severity_counts.get('critical', 0)}",
        f"- Warning: {severity_counts.get('warning', 0)}",
        f"- Info: {severity_counts.get('info', 0)}",
        f"- Fix Actions: {len(fixes)}",
    ]
    if audit_issue_url:
        lines.append(f"- Audit Issue: {audit_issue_url}")

    lines.extend(["", "## Findings"])
    if not findings:
        lines.append("- No rule drift detected.")
    else:
        for finding in findings:
            lines.append(
                f"- [{finding.severity}] {finding.category} / {finding.target}: "
                f"{finding.message} Recommendation: {finding.recommendation}"
            )

    lines.extend(["", "## Low-risk Fixes"])
    if not fixes:
        lines.append("- No low-risk fixes needed.")
    else:
        for fix in fixes:
            lines.append(f"- [{fix.status}] {fix.target}: {fix.action}")

    return "\n".join(lines) + "\n"


def save_json(path: Path, payload: dict[str, Any]) -> None:
    if str(path) == "-":
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run(args: argparse.Namespace) -> int:
    findings: list[Finding] = []
    fixes: list[FixAction] = []
    audit_documents(findings)

    issues = list_open_issues(args.repo, args.limit)
    audit_issue_url: str | None = None
    for issue in issues:
        audit_single_issue(issue, args, findings, fixes)

    if args.apply:
        audit_issue_record = find_audit_issue(args.repo, args.audit_issue_title) or create_audit_issue(
            args.repo, args.audit_issue_title
        )
        audit_issue_url = audit_issue_record.get("url")
        if AUDIT_LABEL not in issue_labels(audit_issue_record) or OPS_LABEL not in issue_labels(audit_issue_record):
            add_labels(audit_issue_record["number"], [OPS_LABEL, AUDIT_LABEL], args.repo)

    report = render_report(findings, fixes, len(issues), audit_issue_url)
    payload = {
        "generated_at": datetime.now(UTC).isoformat(),
        "apply": args.apply,
        "audit_issue_title": args.audit_issue_title,
        "audit_issue_url": audit_issue_url,
        "issue_count": len(issues),
        "findings": [asdict(finding) for finding in findings],
        "fixes": [asdict(fix) for fix in fixes],
    }
    save_json(args.json_out, payload)

    if args.apply and audit_issue_url:
        audit_issue_record = find_audit_issue(args.repo, args.audit_issue_title)
        if audit_issue_record:
            comment_issue(audit_issue_record["number"], report, args.repo)

    print(report)
    if args.fail_on_critical and any(finding.severity == "critical" for finding in findings):
        return 1
    return 0


def main() -> int:
    try:
        return run(parse_args())
    except Exception as exc:  # noqa: BLE001 - command-line tool should print concise failure.
        print(f"[rule-audit] error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
