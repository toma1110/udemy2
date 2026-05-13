from __future__ import annotations

import asyncio
from pathlib import Path
from string import Template
from typing import Any

from codex_runner import CodexRunner, CodexRunResult
from queue_manager import RunRequest
from run_guard import RunGuard
from services.discord_notification_service import DiscordNotificationService
from services.github_issue_service import GitHubIssueService


class CodexExecutionService:
    def __init__(
        self,
        github: GitHubIssueService,
        notifier: DiscordNotificationService,
        runner: CodexRunner,
        guard: RunGuard,
        task_prompt_path: Path,
    ) -> None:
        self.github = github
        self.notifier = notifier
        self.runner = runner
        self.guard = guard
        self.task_prompt_path = task_prompt_path

    async def execute(self, request: RunRequest) -> None:
        try:
            issue = await asyncio.to_thread(self.github.get_issue, request.issue_number)
            prompt = self.render_prompt(issue)
            guard_result = self.guard.validate(prompt, issue.get("body") or "")
            dangerous_operations = list(guard_result.dangerous_operations)
            dangerous = format_dangerous(dangerous_operations)

            await asyncio.to_thread(
                self.github.comment_issue,
                request.issue_number,
                "Discord Command Center: codex exec を開始します。\n\n"
                f"- Requested By: {request.requested_by}\n"
                f"- Workspace: `{guard_result.workspace}`\n"
                f"- Dangerous Operation Log: {dangerous}\n"
                "- Status: running\n\n"
                "次アクション: Codexの実行ログを待ちます。",
            )
            await self.notifier.send(
                f"[AI-PM-01]\nIssue #{request.issue_number} 開始\n"
                f"Workspace: {guard_result.workspace}\nDangerous Operation Log: {dangerous}"
            )

            await asyncio.to_thread(
                self.github.comment_issue,
                request.issue_number,
                "Discord Command Center: codex exec 実行中です。\n\n"
                f"- Workspace: `{guard_result.workspace}`\n"
                f"- Dangerous Operation Log: {dangerous}\n"
                "- Status: running",
            )
            result = await asyncio.to_thread(self.runner.run, request.issue_number, prompt, guard_result.workspace)
            dangerous_operations.extend(self.detect_from_log(result.log_path))
            dangerous = format_dangerous(dangerous_operations)
        except Exception as exc:  # noqa: BLE001 - execution result must be recorded.
            await self.record_error(request.issue_number, exc)
            return

        await self.record_result(result, dangerous)

    def render_prompt(self, issue: dict[str, Any]) -> str:
        fallback = """# Codex Exec Request

GitHub Issue: #${issue_number} ${issue_title}
Issue URL: ${issue_url}

Read `udemy-ai-company/AGENTS.md` first.
Use this Issue as the progress ledger and comment progress during work.

## Issue Body

${issue_body}
"""
        template_text = self.task_prompt_path.read_text(encoding="utf-8") if self.task_prompt_path.exists() else fallback
        return Template(template_text).safe_substitute(
            issue_number=issue["number"],
            issue_title=issue["title"],
            issue_url=issue["html_url"],
            priority="from-issue",
            workspace=str(self.guard.workspace),
            description=issue.get("body") or "",
            issue_body=issue.get("body") or "",
        )

    async def record_result(self, result: CodexRunResult, dangerous: str) -> None:
        status = "completed" if result.exit_code == 0 else "error"
        next_action = "Reviewer AIがIssueと差分を確認してください。" if result.exit_code == 0 else "ログを確認し、必要なら再実行またはBlocked化してください。"
        body = (
            f"Discord Command Center: codex exec が終了しました。\n\n"
            f"- Status: {status}\n"
            f"- Exit Code: {result.exit_code}\n"
            f"- Log Path: `{result.log_path}`\n"
            f"- Started At: {result.started_at}\n"
            f"- Completed At: {result.completed_at}\n"
            f"- Dangerous Operation Log: {dangerous}\n"
            f"- Next Action: {next_action}\n\n"
            "## stdout tail\n\n"
            "```text\n"
            f"{result.stdout_tail or '(empty)'}\n"
            "```\n\n"
            "## stderr tail\n\n"
            "```text\n"
            f"{result.stderr_tail or '(empty)'}\n"
            "```"
        )
        await asyncio.to_thread(self.github.comment_issue, result.issue_number, body)
        await self.notifier.send(
            f"[AI-PM-01]\nIssue #{result.issue_number} {status}\n"
            f"Exit Code: {result.exit_code}\n"
            f"Dangerous Operation Log: {dangerous}\n"
            f"Log: {result.log_path}"
        )

    async def record_error(self, issue_number: int, exc: Exception) -> None:
        await asyncio.to_thread(
            self.github.comment_issue,
            issue_number,
            "Discord Command Center: codex exec 起動前または実行中にエラーが発生しました。\n\n"
            f"- Status: error\n"
            f"- Error: `{exc}`\n"
            "- Next Action: run_guard、workspace、Codex設定、ログ保存先を確認してください。",
        )
        await self.notifier.send(f"[AI-PM-01]\nIssue #{issue_number} error\n{exc}")

    def detect_from_log(self, log_path: Path) -> list[str]:
        try:
            return self.guard.detect_dangerous_operations(log_path.read_text(encoding="utf-8"))
        except OSError:
            return []


def format_dangerous(operations: list[str]) -> str:
    unique = sorted(set(operations))
    return ", ".join(unique) if unique else "none"
