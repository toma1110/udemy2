#!/usr/bin/env python3
"""GitHub Issue watcher for AI-PM-01.

The watcher is intentionally conservative:
- first run creates a baseline instead of processing every existing issue
- only issues marked auto-execute are queued
- billing-sensitive AWS work is blocked until CEO approval is present
- when enabled, every open issue except CEO approval waiting tickets is closed
"""

from __future__ import annotations

import argparse
import json
import re
import shlex
import subprocess
import sys
import time
from pathlib import Path
from typing import Any


COMPANY_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STATE_FILE = COMPANY_ROOT / ".pm_state" / "github_issues.json"
DEFAULT_QUEUE_DIR = COMPANY_ROOT / ".pm_queue"

AUTO_LABEL = "auto-execute"
APPROVAL_REQUIRED_LABEL = "approval-required"
CEO_APPROVED_LABEL = "ceo-approved"
PM_QUEUED_LABEL = "pm-queued"
PM_PARENT_LABEL = "pm-parent"
PM_CHILD_LABEL = "pm-child"
NEEDS_BREAKDOWN_LABEL = "needs-breakdown"
FEEDBACK_CHILD_LABEL = "feedback"
IN_PROGRESS_LABEL = "in-progress"
BLOCKED_LABEL = "blocked"
DONE_LABEL = "done"
REVIEW_LABEL = "review"

COMMENT_AUTO_COMMANDS = (
    "/auto-execute",
    "/pm-run",
)

COMMENT_BREAKDOWN_COMMANDS = (
    "/pm-breakdown",
    "/breakdown",
)

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

INCOMPLETE_KEYWORDS = (
    "未完了",
    "未実施",
    "実行環境待ち",
    "実行できません",
    "起動不能",
    "failed",
    "error",
    "blocked",
)

FEEDBACK_KEYWORDS = (
    "お願いします",
    "修正",
    "追加",
    "作り直し",
    "気になる",
    "読み方",
    "ルール",
    "不要",
    "クローズしてください",
    "/close",
)

COMPLETION_REPORT_KEYWORDS = (
    "対応内容:",
    "反映済み:",
    "qa:",
    "drive metadata",
    "faststart=true",
    "decode ok",
    "アップロードしました",
    "アップロード完了",
    "確認対象はこちら",
    "修正版を作成",
    "修正版アップロード",
    "production/upload complete",
)

CEO_APPROVAL_WAITING_PATTERNS = (
    r"CEO\s*承認\s*待ち",
    r"CEO\s*確認\s*待ち",
    r"CEO\s*レビュー\s*待ち",
    r"公開\s*承認\s*待ち",
    r"最終\s*承認\s*待ち",
    r"Ready\s+for\s+Publish",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="AI-PM-01 GitHub Issue watcher and auto-execution gate."
    )
    parser.add_argument("--repo", help="GitHub repository in owner/name format.")
    parser.add_argument("--limit", type=int, default=1000, help="Max open issues to scan.")
    parser.add_argument(
        "--state-file",
        type=Path,
        default=DEFAULT_STATE_FILE,
        help="Local file that stores last seen Issue update timestamps.",
    )
    parser.add_argument(
        "--queue-dir",
        type=Path,
        default=DEFAULT_QUEUE_DIR,
        help="Directory for generated AI execution prompts.",
    )
    parser.add_argument(
        "--baseline",
        action="store_true",
        help="Record current Issue timestamps and exit without queueing work.",
    )
    parser.add_argument(
        "--process-initial",
        action="store_true",
        help="Process existing issues even when no state file exists.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write state, queue prompts, and update GitHub labels/comments.",
    )
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Run the executor command for queued issues. Requires --apply.",
    )
    parser.add_argument(
        "--close-non-approval",
        action="store_true",
        help="Close every open issue except tickets waiting for CEO approval.",
    )
    parser.add_argument(
        "--executor",
        help="Command that receives the generated prompt on stdin, for example: codex exec",
    )
    parser.add_argument(
        "--poll-seconds",
        type=int,
        default=0,
        help="Poll interval. 0 means run once.",
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


def comments_text(comments: list[dict[str, Any]]) -> str:
    return "\n".join(comment.get("body") or "" for comment in comments)


def comment_body(comment: dict[str, Any]) -> str:
    return comment.get("body") or ""


def is_pm_comment(comment: dict[str, Any]) -> bool:
    return comment_body(comment).lstrip().startswith("AI-PM-01:")


def is_completion_report_comment(comment: dict[str, Any]) -> bool:
    lowered = comment_body(comment).lower()
    return any(keyword.lower() in lowered for keyword in COMPLETION_REPORT_KEYWORDS)


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


def has_auto_command(text: str) -> bool:
    lowered = text.lower()
    return any(command in lowered for command in COMMENT_AUTO_COMMANDS)


def has_breakdown_command(text: str) -> bool:
    lowered = text.lower()
    return any(command in lowered for command in COMMENT_BREAKDOWN_COMMANDS)


def is_auto_candidate(issue: dict[str, Any], comments: list[dict[str, Any]] | None = None) -> bool:
    labels = issue_labels(issue)
    body = issue.get("body") or ""
    comment_body = comments_text(comments or [])
    return (
        AUTO_LABEL in labels
        or truthy(get_field(body, "Auto Execute"))
        or truthy(get_field(body, "Auto Execute After Approval"))
        or has_auto_command(comment_body)
    )


def has_terminal_or_blocking_label(issue: dict[str, Any]) -> bool:
    labels = issue_labels(issue)
    return bool(labels.intersection({BLOCKED_LABEL, DONE_LABEL, PM_QUEUED_LABEL, IN_PROGRESS_LABEL}))


def is_child_issue(issue: dict[str, Any]) -> bool:
    labels = issue_labels(issue)
    body = issue.get("body") or ""
    return PM_CHILD_LABEL in labels or "Parent Issue:" in body


def processed_comment_ids(comments: list[dict[str, Any]]) -> set[str]:
    processed: set[str] = set()
    for comment in comments:
        body = comment_body(comment)
        for match in re.finditer(r"Processed Comment:\s*([A-Za-z0-9_:-]+)", body):
            processed.add(match.group(1))
    return processed


def comment_id(comment: dict[str, Any]) -> str:
    return str(comment.get("id") or comment.get("url") or "")


def latest_actionable_feedback(comments: list[dict[str, Any]]) -> dict[str, Any] | None:
    processed = processed_comment_ids(comments)
    for comment in reversed(comments):
        cid = comment_id(comment)
        body = comment_body(comment)
        if not body or is_pm_comment(comment) or is_completion_report_comment(comment):
            continue
        if cid and cid in processed:
            return None
        return comment if any(keyword.lower() in body.lower() for keyword in FEEDBACK_KEYWORDS) else None
    return None


def is_close_request(text: str) -> bool:
    lowered = text.lower()
    return "クローズしてください" in text or "/close" in lowered


def infer_assignment(issue: dict[str, Any], comments: list[dict[str, Any]] | None = None) -> dict[str, str]:
    body = issue.get("body") or ""
    text = f"{issue.get('title') or ''}\n{body}\n{comments_text(comments or [])}".lower()

    if any(keyword in text for keyword in ("qa", "レビュー", "確認待ち", "品質", "quality")):
        return {
            "department": "qa",
            "owner": "AI-QA-01",
            "reviewer": "AI-Ops-01",
            "source": "inferred: qa keywords",
        }

    if any(keyword in text for keyword in ("動画", "スライド", "gpt-image2", "voicevox", "台本", "音声", "教材")):
        return {
            "department": "production",
            "owner": "AI-Production-01",
            "reviewer": "AI-QA-01",
            "source": "inferred: production keywords",
        }

    if any(keyword in text for keyword in ("cloudformation", "template.yaml", "aws batch", "fargate", "ecr", "ハンズオン", "環境構築", "deploy")):
        return {
            "department": "engineering",
            "owner": "AI-Engineer-01",
            "reviewer": "AI-QA-01",
            "source": "inferred: engineering keywords",
        }

    if any(keyword in text for keyword in ("course_spec", "企画", "章立て", "構成", "学習目標")):
        return {
            "department": "strategy",
            "owner": "AI-Strategy-01",
            "reviewer": "AI-QA-01",
            "source": "inferred: strategy keywords",
        }

    return {
        "department": "ops",
        "owner": "AI-Ops-01",
        "reviewer": "AI-QA-01",
        "source": "inferred: default ops",
    }


def resolve_assignment(issue: dict[str, Any], comments: list[dict[str, Any]] | None = None) -> dict[str, str]:
    body = issue.get("body") or ""
    inferred = infer_assignment(issue, comments)
    department = get_field(body, "Department") or inferred["department"]
    owner = get_field(body, "Owner AI") or inferred["owner"]
    reviewer = get_field(body, "Reviewer AI") or inferred["reviewer"]
    source = "issue body"
    if not get_field(body, "Owner AI") or not get_field(body, "Reviewer AI"):
        source = inferred["source"]

    return {
        "department": department,
        "owner": owner,
        "reviewer": reviewer,
        "source": source,
    }


def worker_reviewer_error(issue: dict[str, Any], comments: list[dict[str, Any]] | None = None) -> str | None:
    assignment = resolve_assignment(issue, comments)
    owner = assignment["owner"]
    reviewer = assignment["reviewer"]
    if owner == reviewer:
        return "Owner AIとReviewer AIが同一です。"
    return None


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


def extract_section_number(text: str) -> int | None:
    patterns = (
        r"(?<![a-zA-Z0-9])s\s*[-_ ]?(\d+)",
        r"\bsection\s*(\d+)",
        r"セクション\s*(\d+)",
        r"第\s*(\d+)\s*章",
    )
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return int(match.group(1))
    return None


def infer_course_slug(issue: dict[str, Any]) -> str:
    body = issue.get("body") or ""
    course = get_field(body, "Course")
    if course:
        return course

    courses_dir = COMPANY_ROOT / "courses"
    courses = [path.name for path in courses_dir.iterdir() if path.is_dir()] if courses_dir.exists() else []
    if len(courses) == 1:
        return courses[0]
    if "aws-slo" in f"{issue.get('title') or ''}\n{body}".lower():
        return "aws-slo-adoption-course"
    if "sample" in f"{issue.get('title') or ''}\n{body}".lower():
        return "sample-aws-sre-course"
    return "aws-slo-adoption-course"


def parse_lectures(course_slug: str, section_number: int) -> list[dict[str, str]]:
    lectures_path = COMPANY_ROOT / "courses" / course_slug / "lectures.md"
    if not lectures_path.exists():
        return []

    lectures: list[dict[str, str]] = []
    in_section = False
    for line in lectures_path.read_text(encoding="utf-8").splitlines():
        section_match = re.match(r"^##\s+Section\s+(\d+)\s*:", line)
        if section_match:
            in_section = int(section_match.group(1)) == section_number
            continue
        if not in_section:
            continue

        lecture_match = re.match(
            r"^\|\s*(\d+)-(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|",
            line,
        )
        if not lecture_match:
            continue
        if lecture_match.group(1) == "Lecture":
            continue
        lectures.append(
            {
                "section": lecture_match.group(1),
                "lecture": lecture_match.group(2),
                "title": lecture_match.group(3).strip(),
                "type": lecture_match.group(4).strip(),
                "owner": lecture_match.group(5).strip(),
                "reviewer": lecture_match.group(6).strip(),
            }
        )
    return lectures


def is_large_request(issue: dict[str, Any], comments: list[dict[str, Any]]) -> bool:
    if is_child_issue(issue):
        return False
    labels = issue_labels(issue)
    if PM_PARENT_LABEL in labels:
        return False

    body = issue.get("body") or ""
    text = f"{issue.get('title') or ''}\n{body}\n{comments_text(comments)}"
    lowered = text.lower()

    if has_breakdown_command(text):
        return True

    section_number = extract_section_number(text)
    if section_number and any(keyword in lowered for keyword in ("動画", "video", "作成", "制作", "再作成", "アップロード")):
        return True

    broad_keywords = ("全部", "全体", "まとめて", "一括", "セクション", "section")
    deliverable_keywords = ("動画", "スライド", "voicevox", "gpt-image2", "qa", "レビュー", "cloudformation")
    return any(keyword in lowered for keyword in broad_keywords) and any(
        keyword in lowered for keyword in deliverable_keywords
    )


def task_id(prefix: str, parent_number: int, index: int) -> str:
    return f"PM-{parent_number:04d}-{prefix}-{index:02d}"


def render_lecture_child_body(
    parent: dict[str, Any],
    course_slug: str,
    lecture: dict[str, str],
    index: int,
    sensitive: bool,
    approved: bool,
) -> str:
    section = lecture["section"]
    lecture_no = lecture["lecture"]
    lecture_key = f"s{section}-l{lecture_no}"
    task = task_id("VIDEO", parent["number"], index)
    return f"""# Task Summary
Task ID: {task}
Title: Section {section} Lecture {lecture_no} GPT-Image2版の完成動画を制作しDriveへアップロードする
Parent Issue: #{parent["number"]}
Course: {course_slug}

# Ownership
Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Backlog
Auto Execute: yes
Requires CEO Approval: {"yes" if sensitive else "no"}
Cost Impact: {"AWS Batch/Fargate render and Google Drive upload" if sensitive else "none"}

# Inputs
Input Files:
- `courses/{course_slug}/course_spec.md`
- `courses/{course_slug}/lectures.md`
- `courses/{course_slug}/scripts/{lecture_key}_script.md`
- `courses/{course_slug}/scripts/{lecture_key}_script.json`
- `courses/{course_slug}/audio/{lecture_key}/slide_*.wav`
Dependencies:
- Parent Issue #{parent["number"]}
- GPT-Image2生成物を最終スライド元にする

# Deliverables
Expected Output:
- `courses/{course_slug}/slides/{lecture_key}/slide_*.png`
- `courses/{course_slug}/slides/s{section}-gpt-image2-sources/{lecture_key}/slide_*.png`
- `courses/{course_slug}/slides/{lecture_key}/contact_sheet.png`
- `courses/{course_slug}/video/{lecture_key}/{lecture_key}.mp4`
- `courses/{course_slug}/video/{lecture_key}/build_report.json`
- `courses/{course_slug}/video/{lecture_key}/drive_upload.json`
- `courses/{course_slug}/qa/{lecture_key}_slide_generation_report.md`
- `courses/{course_slug}/qa/{lecture_key}_video_build_report.md`
- `courses/{course_slug}/qa/{lecture_key}_drive_upload_report.md`

# Quality Gate
Definition of Done:
- GPT-Image2で必要枚数のスライドを生成している
- GPT-Image2生成元PNGと最終PNGの対応が記録されている
- VOICEVOX音声とスライド数が一致している
- AWS Batch Fargate render jobでMP4を生成している
- MP4 faststart true、decode check OK
- Google Drive upload and anyone-reader sharing verified
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- チケットなし作業禁止
- 親Issue範囲外を変更しない

# Blocking
Blocked By:
Notes:
- Lecture Title: {lecture["title"]}
- Lecture Type: {lecture["type"]}
- Billing Approval: {"CEO approved on parent" if approved else "not required"}
"""


def render_section_qa_child_body(parent: dict[str, Any], course_slug: str, section_number: int, count: int) -> str:
    task = task_id("QA", parent["number"], count + 1)
    return f"""# Task Summary
Task ID: {task}
Title: Section {section_number} GPT-Image2版の動画完了QAとCEO確認待ちにする
Parent Issue: #{parent["number"]}
Course: {course_slug}

# Ownership
Department: qa
Owner AI: AI-QA-01
Reviewer AI: AI-Ops-01

# Execution
Priority: high
Status: Waiting for child tasks
Auto Execute: no
Requires CEO Approval: no
Cost Impact: none

# Inputs
Input Files:
- `courses/{course_slug}/scripts/s{section_number}-l*_script.md`
- `courses/{course_slug}/slides/s{section_number}-l*/`
- `courses/{course_slug}/audio/s{section_number}-l*/`
- `courses/{course_slug}/video/s{section_number}-l*/`
Dependencies:
- Parent Issue #{parent["number"]}
- Section {section_number} の各Lecture動画制作Issue

# Deliverables
Expected Output:
- `courses/{course_slug}/qa/section{section_number}_completion_report.md`
- Section {section_number} のDrive URL一覧
- 品質ゲートサマリー

# Quality Gate
Definition of Done:
- Section {section_number} の全動画がMP4 faststart true、decode check OK
- Google Drive upload and sharing verified
- GPT-Image2 slide generation reportが各Lectureにある
- VOICEVOX report and render report are recorded
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth

# Blocking
Blocked By:
Notes:
- 子Lecture Issue完了後に `auto-execute` または `/pm-run` を付ける
"""


def render_feedback_child_body(parent: dict[str, Any], feedback: dict[str, Any]) -> str:
    body = comment_body(feedback)
    cid = comment_id(feedback)
    title_hint = "CEOフィードバック対応"
    if "読み方" in body or "ルール" in body:
        title_hint = "VOICEVOX読み方ルール更新"
    elif "作り直し" in body or "修正" in body:
        title_hint = "動画フィードバック修正"

    return f"""# Task Summary
Task ID: {task_id("FEEDBACK", parent["number"], 1)}
Title: {title_hint}
Parent Issue: #{parent["number"]}

# Ownership
Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Backlog
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none

# Inputs
Input Files:
- 親Issue #{parent["number"]} のCEOコメント
- `udemy-ai-company/docs/VOICEVOX_RULES.md`
- `udemy-ai-company/tools/narration_checker.py`
Dependencies:
- 親Issueの確認対象成果物

# Deliverables
Expected Output:
- CEOコメントに対する対応
- 必要に応じたVOICEVOX読み方ルール更新
- 必要に応じたQAコメント

# Quality Gate
Definition of Done:
- CEOコメントの各指摘に対応または不要理由を記録している
- 動画再作成不要と明記された場合は動画を再作成しない
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- 親Issueの範囲外を変更しない

# Blocking
Blocked By:
Notes:
- Source Comment: {cid}

## CEO Feedback

{body}
"""


def find_existing_children(parent_number: int, repo: str | None) -> list[dict[str, Any]]:
    search = f'"Parent Issue: #{parent_number}"'
    result = gh(
        ["issue", "list", "--state", "all", "--limit", "100", "--search", search, "--json", "number,title,url"],
        repo=repo,
    )
    if result.returncode != 0:
        print(f"[warn] child search failed for #{parent_number}: {result.stderr.strip()}", file=sys.stderr)
        return []
    return [issue for issue in json.loads(result.stdout) if issue.get("number") != parent_number]


def create_issue(title: str, body: str, labels: list[str], repo: str | None) -> str | None:
    args = ["issue", "create", "--title", title, "--body", body]
    if labels:
        args.extend(["--label", ",".join(labels)])
    result = gh(args, repo=repo)
    if result.returncode != 0:
        print(f"[warn] issue create failed: {result.stderr.strip()}", file=sys.stderr)
        return None
    return result.stdout.strip()


def handle_review_feedback(issue: dict[str, Any], comments: list[dict[str, Any]], args: argparse.Namespace) -> bool:
    labels = issue_labels(issue)
    if REVIEW_LABEL not in labels:
        return False

    feedback = latest_actionable_feedback(comments)
    if not feedback:
        return False

    number = issue["number"]
    body = comment_body(feedback)
    cid = comment_id(feedback)

    if is_close_request(body):
        if args.apply:
            add_labels(number, [DONE_LABEL], args.repo)
            remove_labels(number, [REVIEW_LABEL], args.repo)
            comment_issue(number, f"AI-PM-01: CEOのクローズ依頼を検知しました。\n\nProcessed Comment: {cid}", args.repo)
            gh(["issue", "close", str(number), "--comment", "AI-PM-01: CEO確認完了のためクローズします。"], repo=args.repo)
        print(f"[pm] review #{number}: close requested")
        return True

    if not args.apply:
        print(f"[pm] dry-run feedback child for #{number}: {cid}")
        return True

    child_title = f"[Task] {task_id('FEEDBACK', number, 1)} {issue.get('title', '')} のCEOフィードバック対応"
    child_body = render_feedback_child_body(issue, feedback)
    child_url = create_issue(
        child_title,
        child_body,
        [PM_CHILD_LABEL, FEEDBACK_CHILD_LABEL, "production", "high", AUTO_LABEL],
        args.repo,
    )
    comment_issue(
        number,
        "AI-PM-01: CEOフィードバックコメントを検知し、対応チケットを作成しました。\n\n"
        f"- {child_url}\n\n"
        f"Processed Comment: {cid}",
        args.repo,
    )
    print(f"[pm] review #{number}: created feedback child {child_url}")
    return True


def decompose_issue(issue: dict[str, Any], comments: list[dict[str, Any]], args: argparse.Namespace) -> bool:
    number = issue["number"]
    text = f"{issue.get('title') or ''}\n{issue.get('body') or ''}\n{comments_text(comments)}"
    section_number = extract_section_number(text)
    course_slug = infer_course_slug(issue)
    sensitive = is_billing_sensitive(issue)
    approved = is_ceo_approved(issue, args.repo, comments) if sensitive else False

    existing_children = find_existing_children(number, args.repo)
    if existing_children:
        child_lines = "\n".join(f"- #{child['number']} {child['title']}: {child['url']}" for child in existing_children)
        if args.apply:
            add_labels(number, [PM_PARENT_LABEL, PM_QUEUED_LABEL], args.repo)
            comment_issue(number, f"AI-PM-01: 既存の子チケットを検出したため、新規作成はしません。\n\n{child_lines}", args.repo)
        print(f"[pm] parent #{number}: existing children found")
        return True

    if not section_number:
        if args.apply:
            add_labels(number, [NEEDS_BREAKDOWN_LABEL, BLOCKED_LABEL], args.repo)
            comment_issue(
                number,
                "AI-PM-01: 大きい依頼として検知しましたが、Section番号を特定できませんでした。"
                "`s6`、`Section 6` などをIssue本文またはコメントに追記してください。",
                args.repo,
            )
        print(f"[pm] parent #{number}: section not found")
        return True

    lectures = parse_lectures(course_slug, section_number)
    if not lectures:
        if args.apply:
            add_labels(number, [NEEDS_BREAKDOWN_LABEL, BLOCKED_LABEL], args.repo)
            comment_issue(
                number,
                f"AI-PM-01: `{course_slug}/lectures.md` から Section {section_number} の講義一覧を取得できませんでした。",
                args.repo,
            )
        print(f"[pm] parent #{number}: lectures not found")
        return True

    if sensitive and not approved:
        if args.apply:
            add_labels(number, [APPROVAL_REQUIRED_LABEL, BLOCKED_LABEL], args.repo)
            comment_issue(
                number,
                "AI-PM-01: 子チケット分解は可能ですが、AWS課金につながる実行が含まれるため停止しました。"
                "`ceo-approved` ラベル、または `/approve-cost` コメントでCEO承認を記録してください。",
                args.repo,
            )
        print(f"[pm] parent #{number}: approval required before breakdown")
        return True

    if not args.apply:
        print(f"[pm] dry-run breakdown #{number}: section {section_number}, {len(lectures)} lecture tasks")
        return True

    labels_base = [PM_CHILD_LABEL]
    if sensitive and approved:
        labels_base.append(CEO_APPROVED_LABEL)

    created_urls: list[str] = []
    for index, lecture in enumerate(lectures, start=1):
        title = (
            f"[Task] {task_id('VIDEO', number, index)} "
            f"Section {section_number} Lecture {lecture['lecture']} GPT-Image2版の完成動画を制作しDriveへアップロードする"
        )
        body = render_lecture_child_body(issue, course_slug, lecture, index, sensitive, approved)
        labels = [*labels_base, "production", "high", AUTO_LABEL]
        url = create_issue(title, body, labels, args.repo)
        if url:
            created_urls.append(url)

    qa_title = f"[Task] {task_id('QA', number, len(lectures) + 1)} Section {section_number} GPT-Image2版の動画完了QAとCEO確認待ちにする"
    qa_body = render_section_qa_child_body(issue, course_slug, section_number, len(lectures))
    qa_url = create_issue(qa_title, qa_body, [PM_CHILD_LABEL, "qa", "high", REVIEW_LABEL], args.repo)
    if qa_url:
        created_urls.append(qa_url)

    add_labels(number, [PM_PARENT_LABEL, PM_QUEUED_LABEL], args.repo)
    child_lines = "\n".join(f"- {url}" for url in created_urls)
    comment_issue(
        number,
        f"AI-PM-01: 大きい依頼として検知し、Section {section_number} を子チケットへ分解しました。\n\n"
        f"{child_lines}\n\n"
        "親Issueは進捗管理用として扱います。各子チケットの完了後、QAチケットを実行してください。",
        args.repo,
    )
    print(f"[pm] parent #{number}: created {len(created_urls)} children")
    return True


def approval_in_text(text: str) -> bool:
    if not text:
        return False
    return bool(
        re.search(r"/approve-cost\b", text, re.IGNORECASE)
        or re.search(r"CEO\s*Approval\s*:\s*approved", text, re.IGNORECASE)
        or re.search(r"CEO承認\s*:\s*承認", text)
        or re.search(r"CEO承認済", text)
    )


def fetch_comments(issue_number: int, repo: str | None) -> list[dict[str, Any]]:
    data = gh_json(["issue", "view", str(issue_number), "--json", "comments"], repo=repo)
    return data.get("comments") or []


def is_ceo_approved(issue: dict[str, Any], repo: str | None, comments: list[dict[str, Any]] | None = None) -> bool:
    labels = issue_labels(issue)
    if CEO_APPROVED_LABEL in labels:
        return True
    if approval_in_text(issue.get("body") or ""):
        return True

    comments = comments if comments is not None else fetch_comments(issue["number"], repo)
    return any(approval_in_text(comment.get("body") or "") for comment in comments)


def has_ceo_waiting_phrase(issue: dict[str, Any]) -> bool:
    text = f"{issue.get('title') or ''}\n{issue.get('body') or ''}"
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in CEO_APPROVAL_WAITING_PATTERNS)


def has_ceo_approval_gate(issue: dict[str, Any]) -> bool:
    labels = issue_labels(issue)
    body = issue.get("body") or ""
    return bool(
        APPROVAL_REQUIRED_LABEL in labels
        or truthy(get_field(body, "Requires CEO Approval"))
        or has_field(body, "CEO Approval")
        or is_billing_sensitive(issue)
        or has_ceo_waiting_phrase(issue)
    )


def is_ceo_approval_waiting(
    issue: dict[str, Any],
    repo: str | None,
    comments: list[dict[str, Any]] | None = None,
) -> bool:
    return has_ceo_approval_gate(issue) and not is_ceo_approved(issue, repo, comments)


def load_state(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def save_state(path: Path, state: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(state, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")


def list_open_issues(repo: str | None, limit: int) -> list[dict[str, Any]]:
    fields = "number,title,updatedAt,labels,body,url"
    return gh_json(
        ["issue", "list", "--state", "open", "--limit", str(limit), "--json", fields],
        repo=repo,
    )


def add_labels(issue_number: int, labels: list[str], repo: str | None) -> None:
    if not labels:
        return
    result = gh(["issue", "edit", str(issue_number), "--add-label", ",".join(labels)], repo=repo)
    if result.returncode != 0:
        print(f"[warn] label update failed for #{issue_number}: {result.stderr.strip()}", file=sys.stderr)


def remove_labels(issue_number: int, labels: list[str], repo: str | None) -> None:
    for label in labels:
        result = gh(["issue", "edit", str(issue_number), "--remove-label", label], repo=repo)
        if result.returncode != 0:
            message = result.stderr.strip()
            if "not found" not in message.lower():
                print(f"[warn] label removal failed for #{issue_number}: {message}", file=sys.stderr)


def comment_issue(issue_number: int, body: str, repo: str | None) -> None:
    result = gh(["issue", "comment", str(issue_number), "--body", body], repo=repo)
    if result.returncode != 0:
        print(f"[warn] comment failed for #{issue_number}: {result.stderr.strip()}", file=sys.stderr)


def close_issue(issue_number: int, body: str, repo: str | None) -> None:
    result = gh(["issue", "close", str(issue_number), "--comment", body], repo=repo)
    if result.returncode != 0:
        print(f"[warn] close failed for #{issue_number}: {result.stderr.strip()}", file=sys.stderr)


def close_non_approval_issues(issues: list[dict[str, Any]], args: argparse.Namespace) -> None:
    for issue in issues:
        number = issue["number"]
        comments = fetch_comments(number, args.repo)
        if is_ceo_approval_waiting(issue, args.repo, comments):
            print(f"[pm] keep #{number}: waiting for CEO approval")
            if args.apply:
                add_labels(number, [APPROVAL_REQUIRED_LABEL, BLOCKED_LABEL], args.repo)
            continue

        print(f"[pm] close #{number}: not waiting for CEO approval")
        if not args.apply:
            continue

        add_labels(number, [DONE_LABEL], args.repo)
        remove_labels(number, [AUTO_LABEL, PM_QUEUED_LABEL, IN_PROGRESS_LABEL, REVIEW_LABEL, BLOCKED_LABEL], args.repo)
        close_issue(
            number,
            "AI-PM-01: CEO承認待ち以外のOpen Issueはクローズする運用に変更されたため、"
            "このIssueを自動クローズします。CEO承認が必要な作業は `approval-required` を付けて再作成してください。",
            args.repo,
        )


def current_state_from_issues(issues: list[dict[str, Any]]) -> dict[str, str]:
    return {str(issue["number"]): issue.get("updatedAt", "") for issue in issues}


def render_prompt(issue: dict[str, Any], sensitive: bool, approved: bool, assignment: dict[str, str]) -> str:
    body = issue.get("body") or ""
    owner = assignment["owner"]
    reviewer = assignment["reviewer"]
    department = assignment["department"]
    priority = get_field(body, "Priority") or "未設定"
    input_files = get_field(body, "Input Files") or "Issue本文を確認"
    expected_output = get_field(body, "Expected Output") or "Issue本文を確認"
    dod = get_field(body, "Definition of Done") or "Issue本文を確認"
    approval_status = "CEO承認済み" if approved else "承認不要"
    if sensitive and not approved:
        approval_status = "CEO承認なし"

    return f"""# AI-PM-01 Execution Request

GitHub Issue: #{issue["number"]} {issue.get("title", "")}
URL: {issue.get("url", "")}

## Assignment

- Department: {department}
- Owner AI: {owner}
- Reviewer AI: {reviewer}
- Assignment Source: {assignment["source"]}
- Priority: {priority}
- Billing-sensitive: {"yes" if sensitive else "no"}
- Approval Status: {approval_status}

## Required Instructions

- `udemy-ai-company/AGENTS.md` と該当講座の `course_spec.md` を最初に読むこと。
- このIssueの範囲外を変更しないこと。
- WorkerとReviewerを分離すること。
- AWS課金につながるコマンド、環境構築、CloudFormation stack作成/更新/削除、Fargate/Batch/ECR等はCEO承認なしに実行しないこと。
- 成果物、検証結果、未実施理由をIssueまたはQAレポートに残すこと。

## Inputs

{input_files}

## Expected Output

{expected_output}

## Definition of Done

{dod}

## Original Issue Body

{body}
"""


def queue_prompt(queue_dir: Path, issue: dict[str, Any], prompt: str) -> Path:
    queue_dir.mkdir(parents=True, exist_ok=True)
    path = queue_dir / f"issue-{issue['number']:04d}.md"
    path.write_text(prompt, encoding="utf-8")
    return path


def summarize_executor_output(stdout: str, stderr: str, max_chars: int = 3500) -> str:
    output = stdout.strip() or stderr.strip() or "(executor output is empty)"
    if len(output) <= max_chars:
        return output
    return output[-max_chars:]


def looks_incomplete(exit_code: int, summary: str) -> bool:
    if exit_code != 0:
        return True
    lowered = summary.lower()
    return any(keyword.lower() in lowered for keyword in INCOMPLETE_KEYWORDS)


def run_executor(executor: str, prompt: str, queue_path: Path) -> tuple[int, str]:
    cmd = shlex.split(executor)
    if not cmd:
        raise ValueError("--executor is empty")

    result = subprocess.run(
        cmd,
        input=prompt,
        text=True,
        capture_output=True,
        cwd=COMPANY_ROOT,
        check=False,
    )
    log_path = queue_path.with_suffix(".log")
    log_path.write_text(
        f"$ {executor}\n\n[exit_code]\n{result.returncode}\n\n[stdout]\n{result.stdout}\n\n[stderr]\n{result.stderr}\n",
        encoding="utf-8",
    )
    return result.returncode, summarize_executor_output(result.stdout, result.stderr)


def handle_changed_issue(issue: dict[str, Any], args: argparse.Namespace) -> None:
    number = issue["number"]
    title = issue.get("title", "")
    print(f"[pm] changed issue #{number}: {title}")

    comments = fetch_comments(number, args.repo)

    if not is_auto_candidate(issue, comments):
        if handle_review_feedback(issue, comments, args):
            return
        print(f"[pm] skip #{number}: auto-execute is not set")
        return

    if has_terminal_or_blocking_label(issue):
        print(f"[pm] skip #{number}: blocked or done")
        return

    if is_large_request(issue, comments):
        if decompose_issue(issue, comments, args):
            return

    separation_error = worker_reviewer_error(issue, comments)
    if separation_error:
        print(f"[pm] block #{number}: {separation_error}")
        if args.apply:
            add_labels(number, [BLOCKED_LABEL], args.repo)
            comment_issue(number, f"AI-PM-01: 自動実行を停止しました。理由: {separation_error}", args.repo)
        return

    sensitive = is_billing_sensitive(issue)
    approved = is_ceo_approved(issue, args.repo, comments) if sensitive else False

    if sensitive and not approved:
        print(f"[pm] block #{number}: CEO approval required")
        if args.apply:
            add_labels(number, [APPROVAL_REQUIRED_LABEL, BLOCKED_LABEL], args.repo)
            comment_issue(
                number,
                "AI-PM-01: このIssueはAWS課金につながる可能性があるため自動実行を停止しました。"
                "`ceo-approved` ラベル、または `/approve-cost` コメントでCEO承認を記録してください。",
                args.repo,
            )
        return

    assignment = resolve_assignment(issue, comments)
    prompt = render_prompt(issue, sensitive=sensitive, approved=approved, assignment=assignment)

    if not args.apply:
        print(f"[pm] dry-run queue #{number}")
        return

    queue_path = queue_prompt(args.queue_dir, issue, prompt)
    add_labels(number, [PM_QUEUED_LABEL], args.repo)
    comment_issue(
        number,
        "AI-PM-01: 自動実行キューに投入しました: "
        f"`{queue_path}`\n\n"
        f"- Owner AI: {assignment['owner']}\n"
        f"- Reviewer AI: {assignment['reviewer']}\n"
        f"- Assignment Source: {assignment['source']}",
        args.repo,
    )
    print(f"[pm] queued #{number}: {queue_path}")

    if args.execute:
        if not args.executor:
            raise ValueError("--execute requires --executor")
        add_labels(number, [IN_PROGRESS_LABEL], args.repo)
        exit_code, summary = run_executor(args.executor, prompt, queue_path)
        incomplete = looks_incomplete(exit_code, summary)
        remove_labels(number, [IN_PROGRESS_LABEL], args.repo)
        add_labels(number, [BLOCKED_LABEL if incomplete else REVIEW_LABEL], args.repo)
        comment_issue(
            number,
            f"AI-PM-01: executor `{args.executor}` が終了しました。exit_code={exit_code}。"
            f"ログ: `{queue_path.with_suffix('.log')}`\n\n"
            f"判定: {'blocked' if incomplete else 'review'}\n\n"
            "```text\n"
            f"{summary}\n"
            "```",
            args.repo,
        )
        print(f"[pm] executor exit #{number}: {exit_code}")


def run_once(args: argparse.Namespace) -> None:
    issues = list_open_issues(args.repo, args.limit)

    if args.close_non_approval and not args.baseline:
        close_non_approval_issues(issues, args)
        if args.apply:
            issues = list_open_issues(args.repo, args.limit)

    current_state = current_state_from_issues(issues)

    if args.baseline:
        save_state(args.state_file, current_state)
        print(f"[pm] baseline saved: {args.state_file} ({len(current_state)} issues)")
        return

    previous_state = load_state(args.state_file)
    if not previous_state and not args.process_initial:
        if args.apply:
            save_state(args.state_file, current_state)
            print(f"[pm] no previous state. baseline saved: {args.state_file}")
        else:
            print("[pm] no previous state. run with --baseline or --apply to create one.")
        return

    changed = [
        issue
        for issue in issues
        if previous_state.get(str(issue["number"])) != issue.get("updatedAt", "")
    ]

    if not changed:
        print("[pm] no changed issues")
    for issue in changed:
        handle_changed_issue(issue, args)

    if args.apply:
        save_state(args.state_file, current_state)


def main() -> int:
    args = parse_args()
    if args.execute and not args.apply:
        print("--execute requires --apply", file=sys.stderr)
        return 2

    while True:
        try:
            run_once(args)
        except Exception as exc:  # noqa: BLE001 - command-line tool should report and continue on polling.
            print(f"[pm] error: {exc}", file=sys.stderr)
            if args.poll_seconds <= 0:
                return 1

        if args.poll_seconds <= 0:
            return 0
        time.sleep(args.poll_seconds)


if __name__ == "__main__":
    raise SystemExit(main())
