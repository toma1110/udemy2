#!/usr/bin/env python3
"""Discord Command Center for AI制作会社.

Discord is the command UI. GitHub Issues remain the progress ledger.
This bot creates and reads Issues, writes approval requests, queues codex exec
runs, and writes execution progress back to GitHub Issues.
"""

from __future__ import annotations

import asyncio
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from string import Template
from typing import Any

import discord
import yaml
from codex_runner import CodexRunner
from discord import app_commands
from queue_manager import RunQueue, RunRequest
from run_guard import RunGuard
from services.codex_execution_service import CodexExecutionService
from services.discord_notification_service import DiscordNotificationService
from services.github_issue_service import GitHubIssueService


APP_ROOT = Path(__file__).resolve().parent
COMPANY_ROOT = APP_ROOT.parent
DEFAULT_CONFIG_PATH = APP_ROOT / "config.example.yaml"
DEFAULT_STATE_FILE = COMPANY_ROOT / ".pm_state" / "discord_issue_updates.json"
DEFAULT_TASK_PROMPT = APP_ROOT / "prompts" / "codex_task_prompt.md"
DEFAULT_APPROVAL_PROMPT = APP_ROOT / "prompts" / "approval_request_prompt.md"
DEFAULT_LOG_DIR = APP_ROOT / "logs" / "codex-runs"

APPROVAL_REQUIRED_LABEL = "approval-required"
BLOCKED_LABEL = "blocked"
PM_LABEL = "pm"
OPS_LABEL = "ops"
VALID_PRIORITIES = {"high", "medium", "low"}


@dataclass
class Config:
    discord_token: str
    github_token: str
    github_repo: str
    guild_id: int | None
    notify_channel_id: int | None
    poll_seconds: int
    state_file: Path
    default_labels: list[str]
    task_prompt_path: Path
    approval_prompt_path: Path
    workspace_root: Path
    workspace_environment: str
    allowed_workspace_environments: list[str]
    codex_command: str
    codex_timeout_seconds: int
    codex_log_dir: Path
    max_parallel_runs: int


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def env_int(name: str) -> int | None:
    value = os.getenv(name, "").strip()
    return int(value) if value else None


def load_config() -> Config:
    config_path = Path(os.getenv("COMMAND_CENTER_CONFIG", DEFAULT_CONFIG_PATH))
    raw = load_yaml(config_path)

    discord_raw = raw.get("discord", {})
    github_raw = raw.get("github", {})
    notify_raw = raw.get("notifications", {})
    codex_raw = raw.get("codex", {})
    queue_raw = raw.get("queue", {})

    discord_token = os.getenv("DISCORD_BOT_TOKEN", "").strip()
    github_token = os.getenv("GITHUB_TOKEN", "").strip()
    github_repo = os.getenv("GITHUB_REPOSITORY", github_raw.get("repo", "")).strip()

    if not discord_token:
        raise SystemExit("DISCORD_BOT_TOKEN is required.")
    if not github_token:
        raise SystemExit("GITHUB_TOKEN is required.")
    if not github_repo or "/" not in github_repo:
        raise SystemExit("GITHUB_REPOSITORY must be set as owner/repo.")

    return Config(
        discord_token=discord_token,
        github_token=github_token,
        github_repo=github_repo,
        guild_id=env_int("DISCORD_GUILD_ID") or discord_raw.get("guild_id"),
        notify_channel_id=env_int("DISCORD_NOTIFY_CHANNEL_ID") or notify_raw.get("channel_id"),
        poll_seconds=int(os.getenv("COMMAND_CENTER_POLL_SECONDS", notify_raw.get("poll_seconds", 60))),
        state_file=Path(os.getenv("COMMAND_CENTER_STATE_FILE", notify_raw.get("state_file", DEFAULT_STATE_FILE))),
        default_labels=list(github_raw.get("default_labels", [PM_LABEL, OPS_LABEL])),
        task_prompt_path=Path(os.getenv("CODEX_TASK_PROMPT_PATH", codex_raw.get("task_prompt_path", DEFAULT_TASK_PROMPT))),
        approval_prompt_path=Path(
            os.getenv("CODEX_APPROVAL_PROMPT_PATH", codex_raw.get("approval_prompt_path", DEFAULT_APPROVAL_PROMPT))
        ),
        workspace_root=Path(os.getenv("AI_COMPANY_WORKSPACE_ROOT", codex_raw.get("workspace_root", "/home/ubuntu/workspace"))),
        workspace_environment=os.getenv("AI_COMPANY_WORKSPACE_ENV", codex_raw.get("workspace_environment", "production")),
        allowed_workspace_environments=list(codex_raw.get("allowed_workspace_environments", ["production", "qa", "research"])),
        codex_command=os.getenv(
            "CODEX_EXEC_COMMAND",
            codex_raw.get("command", "codex exec --sandbox danger-full-access --ask-for-approval never -"),
        ),
        codex_timeout_seconds=int(os.getenv("CODEX_EXEC_TIMEOUT_SECONDS", codex_raw.get("timeout_seconds", 7200))),
        codex_log_dir=Path(os.getenv("CODEX_RUN_LOG_DIR", codex_raw.get("log_dir", DEFAULT_LOG_DIR))),
        max_parallel_runs=int(os.getenv("COMMAND_CENTER_MAX_PARALLEL_RUNS", queue_raw.get("max_parallel_runs", 1))),
    )


def load_template(path: Path, fallback: str) -> Template:
    text = path.read_text(encoding="utf-8") if path.exists() else fallback
    return Template(text)


def get_field(body: str, name: str) -> str:
    pattern = re.compile(rf"^{re.escape(name)}\s*:\s*(.*?)\s*$", re.IGNORECASE | re.MULTILINE)
    match = pattern.search(body or "")
    return match.group(1).strip() if match else ""


def label_names(issue: dict[str, Any]) -> list[str]:
    return [label["name"] for label in issue.get("labels", []) if label.get("name")]


def truncate(text: str, limit: int = 1850) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 20] + "\n... truncated ..."


def now_task_id() -> str:
    return "DISCORD-" + datetime.now(UTC).strftime("%Y%m%d%H%M%S")


def render_task_issue_body(title: str, description: str, priority: str, interaction: discord.Interaction) -> str:
    return f"""# Task Summary
Task ID: {now_task_id()}
Title: {title}
Source: Discord Command Center

# Ownership
Department: ops
Owner AI: AI-PM-01
Reviewer AI: AI-Ops-01

# Execution
Priority: {priority}
Status: Backlog
Auto Execute: no
Requires CEO Approval: no
Cost Impact: none

# Inputs
Input Files:
- Discord request from `{interaction.user}` in channel `{interaction.channel}`
Dependencies:
- `/task_run` starts codex exec on EC2 through the run queue

# Deliverables
Expected Output:
- GitHub Issue progress ledger
- Codex execution prompt
- Progress comments from Codex during work

# Quality Gate
Definition of Done:
- Work is tracked in this Issue
- Codex posts progress comments before, during, and after execution
- Worker != Reviewer
- CloudFormation/git push/git merge operations are logged when detected
- Human approval is requested before publishing, external posting, or irreversible destructive operations
Mission/Vision/Values Alignment:
- Discord is used only as command and progress UI; GitHub Issue remains the source of operational truth.

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- GitHub Issue is a progress ledger, not a full-autonomy trigger
- Discord Bot starts codex exec only through Queue control
- CloudFormation create/update/delete, git push, and git merge are allowed but must be logged
- Publishing, external posting, and irreversible destructive operations require human approval

# Blocking
Blocked By:
Notes:

## Discord Request

{description}
"""


def render_codex_prompt(config: Config, issue: dict[str, Any], description: str, priority: str) -> str:
    fallback = """# Codex Task Prompt

GitHub Issue: #${issue_number} ${issue_title}
Issue URL: ${issue_url}
Priority: ${priority}
Workspace: ${workspace}

You are working for AI制作会社. Read `udemy-ai-company/AGENTS.md` first.
Use this Issue as the progress ledger. Comment progress before starting, at meaningful milestones, and at completion.

CloudFormation create/update/delete, git push, and git merge are allowed in the current operation model, but must be logged in Issue comments and Discord notifications when detected.
Do not publish content, change external sharing, or post outside the repository without human approval.

## Request

${description}
"""
    template = load_template(config.task_prompt_path, fallback)
    return template.safe_substitute(
        issue_number=issue["number"],
        issue_title=issue["title"],
        issue_url=issue["html_url"],
        priority=priority,
        workspace=str((config.workspace_root / config.workspace_environment).expanduser()),
        description=description,
    )


def render_approval_prompt(config: Config, issue: dict[str, Any], reason: str) -> str:
    fallback = """# Approval Request

GitHub Issue: #${issue_number} ${issue_title}
Issue URL: ${issue_url}

Human approval is required before proceeding.

Reason:
${reason}
"""
    template = load_template(config.approval_prompt_path, fallback)
    return template.safe_substitute(
        issue_number=issue["number"],
        issue_title=issue["title"],
        issue_url=issue["html_url"],
        reason=reason,
    )


def load_state(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def save_state(path: Path, state: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


class CommandCenterBot(discord.Client):
    def __init__(self, config: Config, github: GitHubIssueService) -> None:
        super().__init__(intents=discord.Intents.default())
        self.config = config
        self.github = github
        self.tree = app_commands.CommandTree(self)
        self._notifier_task: asyncio.Task[None] | None = None
        self.notifier = DiscordNotificationService(self, config.notify_channel_id)
        self.run_queue = RunQueue(max_parallel_runs=config.max_parallel_runs)
        self.execution_service = CodexExecutionService(
            github=github,
            notifier=self.notifier,
            runner=CodexRunner(config.codex_command, config.codex_timeout_seconds, config.codex_log_dir),
            guard=RunGuard(config.workspace_root, config.workspace_environment, config.allowed_workspace_environments),
            task_prompt_path=config.task_prompt_path,
        )

    async def setup_hook(self) -> None:
        register_commands(self)
        if self.config.guild_id:
            guild = discord.Object(id=self.config.guild_id)
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
        else:
            await self.tree.sync()
        if self.config.notify_channel_id:
            self._notifier_task = asyncio.create_task(self.issue_update_notifier())
        self.run_queue.start(self.execution_service.execute)

    async def issue_update_notifier(self) -> None:
        await self.wait_until_ready()
        channel = self.get_channel(self.config.notify_channel_id)
        if channel is None:
            channel = await self.fetch_channel(self.config.notify_channel_id)
        if not isinstance(channel, discord.abc.Messageable):
            print("Notify channel not found or not messageable.", file=sys.stderr)
            return

        while not self.is_closed():
            try:
                issues = await asyncio.to_thread(self.github.list_issues, "all", None, 30)
                state = load_state(self.config.state_file)
                next_state = dict(state)
                messages: list[str] = []

                for issue in issues:
                    key = str(issue["number"])
                    updated_at = issue.get("updated_at", "")
                    if key in state and state[key] != updated_at:
                        labels = ", ".join(label_names(issue)) or "none"
                        messages.append(
                            f"Issue updated: #{issue['number']} {issue['title']}\n"
                            f"- State: {issue['state']}\n"
                            f"- Labels: {labels}\n"
                            f"- URL: {issue['html_url']}"
                        )
                    next_state[key] = updated_at

                save_state(self.config.state_file, next_state)
                for message in messages[:10]:
                    await channel.send(truncate(message))
            except Exception as exc:  # noqa: BLE001 - notifier must keep running.
                print(f"issue notifier error: {exc}", file=sys.stderr)
            await asyncio.sleep(self.config.poll_seconds)


async def defer(interaction: discord.Interaction) -> None:
    if not interaction.response.is_done():
        await interaction.response.defer(thinking=True)


def register_commands(bot: CommandCenterBot) -> None:
    @bot.tree.command(name="task_create", description="大タスクをGitHub Issueへ登録し、Codex用プロンプトを生成します。")
    @app_commands.describe(title="タスクタイトル", description="依頼内容", priority="high / medium / low")
    async def task_create(interaction: discord.Interaction, title: str, description: str, priority: str = "medium") -> None:
        await defer(interaction)
        priority_normalized = priority.lower().strip()
        if priority_normalized not in VALID_PRIORITIES:
            await interaction.followup.send("priority は high / medium / low のいずれかにしてください。", ephemeral=True)
            return

        body = render_task_issue_body(title, description, priority_normalized, interaction)
        labels = sorted(set([*bot.config.default_labels, priority_normalized]))
        issue = await asyncio.to_thread(bot.github.create_issue, f"[Discord Task] {title}", body, labels)
        prompt = render_codex_prompt(bot.config, issue, description, priority_normalized)
        await asyncio.to_thread(
            bot.github.comment_issue,
            issue["number"],
            "Discord Command Center: Codex実行用プロンプトを生成しました。\n\n"
            "```markdown\n"
            f"{prompt}\n"
            "```",
        )
        await interaction.followup.send(
            truncate(
                f"GitHub Issueを作成しました。\n"
                f"- Issue: #{issue['number']} {issue['title']}\n"
                f"- URL: {issue['html_url']}\n"
                "- Codex用プロンプトはIssueコメントに保存済みです。"
            )
        )

    @bot.tree.command(name="task_run", description="IssueをQueueへ入れ、EC2上でcodex execを自動実行します。")
    @app_commands.describe(issue_number="Issue番号")
    async def task_run(interaction: discord.Interaction, issue_number: int) -> None:
        await defer(interaction)
        issue = await asyncio.to_thread(bot.github.get_issue, issue_number)
        request = RunRequest(
            issue_number=issue_number,
            requested_by=str(interaction.user),
            response_channel_id=interaction.channel_id,
        )
        queue_position = await bot.run_queue.submit(request)
        workspace = (bot.config.workspace_root / bot.config.workspace_environment).expanduser()
        await asyncio.to_thread(
            bot.github.comment_issue,
            issue_number,
            "Discord Command Center: `/task_run` によりcodex exec実行Queueへ追加しました。\n\n"
            f"- Requested By: {interaction.user}\n"
            f"- Queue Position: {queue_position}\n"
            f"- Active Runs: {bot.run_queue.active_runs}\n"
            f"- Max Parallel Runs: {bot.run_queue.max_parallel_runs}\n"
            f"- Workspace: `{workspace}`\n"
            "- Next Action: Queue順にEC2上でcodex execを起動します。",
        )
        await bot.notifier.send(
            f"[AI-PM-01]\nIssue #{issue_number} queued\n"
            f"Queue Position: {queue_position}\nWorkspace: {workspace}"
        )
        await interaction.followup.send(
            truncate(
                f"codex exec実行Queueへ追加しました。\n"
                f"- Issue: #{issue_number} {issue['title']}\n"
                f"- Queue Position: {queue_position}\n"
                f"- Active Runs: {bot.run_queue.active_runs}\n"
                f"- Max Parallel Runs: {bot.run_queue.max_parallel_runs}\n"
                f"- Workspace: {workspace}\n"
                f"- URL: {issue['html_url']}"
            )
        )

    @bot.tree.command(name="task_status", description="GitHub Issueの進捗を確認します。")
    @app_commands.describe(issue_number="Issue番号")
    async def task_status(interaction: discord.Interaction, issue_number: int) -> None:
        await defer(interaction)
        issue = await asyncio.to_thread(bot.github.get_issue, issue_number)
        body = issue.get("body") or ""
        labels = ", ".join(label_names(issue)) or "none"
        message = f"""Issue #{issue['number']}: {issue['title']}
- State: {issue['state']}
- Status: {get_field(body, "Status") or "not set"}
- Owner AI: {get_field(body, "Owner AI") or "not set"}
- Reviewer AI: {get_field(body, "Reviewer AI") or "not set"}
- Priority: {get_field(body, "Priority") or "not set"}
- Labels: {labels}
- Updated: {issue.get("updated_at")}
- URL: {issue["html_url"]}
"""
        await interaction.followup.send(truncate(message))

    @bot.tree.command(name="task_list", description="Issue一覧を確認します。statusはopen/closed/allまたはラベル名です。")
    @app_commands.describe(status="open / closed / all / blocked / review / ready / done など")
    async def task_list(interaction: discord.Interaction, status: str = "open") -> None:
        await defer(interaction)
        status_normalized = status.lower().strip()
        if status_normalized in {"open", "closed", "all"}:
            issues = await asyncio.to_thread(bot.github.list_issues, status_normalized, None, 10)
        else:
            issues = await asyncio.to_thread(bot.github.list_issues, "open", [status_normalized], 10)

        if not issues:
            await interaction.followup.send("該当Issueはありません。")
            return

        lines = [f"Issues ({status_normalized})"]
        for issue in issues:
            labels = ", ".join(label_names(issue)) or "none"
            lines.append(f"- #{issue['number']} [{issue['state']}] {issue['title']} ({labels})\n  {issue['html_url']}")
        await interaction.followup.send(truncate("\n".join(lines)))

    @bot.tree.command(name="approval_request", description="人間承認待ちコメントをIssueへ追加します。")
    @app_commands.describe(issue_number="Issue番号", reason="承認が必要な理由")
    async def approval_request(interaction: discord.Interaction, issue_number: int, reason: str) -> None:
        await defer(interaction)
        issue = await asyncio.to_thread(bot.github.get_issue, issue_number)
        prompt = render_approval_prompt(bot.config, issue, reason)
        await asyncio.to_thread(bot.github.add_labels, issue_number, [APPROVAL_REQUIRED_LABEL, BLOCKED_LABEL])
        await asyncio.to_thread(
            bot.github.comment_issue,
            issue_number,
            "Discord Command Center: 人間承認リクエストを登録しました。\n\n"
            "```markdown\n"
            f"{prompt}\n"
            "```",
        )
        await interaction.followup.send(
            truncate(
                f"承認リクエストをIssueへ追加しました。\n"
                f"- Issue: #{issue_number} {issue['title']}\n"
                f"- URL: {issue['html_url']}\n"
                "- Labels: approval-required, blocked"
            )
        )

    @bot.tree.command(name="help", description="Command Centerの使い方を表示します。")
    async def help_command(interaction: discord.Interaction) -> None:
        message = """Discord Command Center commands
- /task_create title description priority: 大タスクをGitHub Issueへ登録し、Codex用プロンプトをIssueコメントへ保存します。
- /task_run issue_number: IssueをQueueへ入れ、EC2上でcodex execを起動します。
- /task_status issue_number: Issueの状態、Owner/Reviewer、ラベル、URLを表示します。
- /task_list status: open/closed/allまたはラベル名でIssueを一覧します。
- /approval_request issue_number reason: 人間承認待ちコメントをIssueへ追加し、approval-required/blockedを付けます。
- /help: この説明を表示します。

重要: Botはcodex execをQueue制御下で起動します。CloudFormation、git push、git mergeはブロックせず危険操作ログとして記録します。進捗はIssueへ残します。
"""
        await interaction.response.send_message(truncate(message), ephemeral=True)


def main() -> int:
    config = load_config()
    github = GitHubIssueService(config.github_token, config.github_repo)
    bot = CommandCenterBot(config, github)
    bot.run(config.discord_token)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
