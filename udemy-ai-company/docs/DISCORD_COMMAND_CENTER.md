# DISCORD_COMMAND_CENTER

Discord Command Center is the instruction and progress UI for AI制作会社.

It connects Discord slash commands to GitHub Issues and EC2-hosted `codex exec`. GitHub Issues remain the progress ledger, and execution remains Discord-command-driven rather than issue-driven full autonomy.

## Principles

- Discord is a UI, not the source of truth.
- GitHub Issue is the progress ledger.
- Codex execution is started by `/task_run` through a controlled queue.
- The bot generates prompts, starts `codex exec`, and records execution progress.
- CloudFormation create/update/delete, `git push`, and `git merge` are allowed in the current operation model, but they must be logged and notified.
- Publishing and external posting require human approval.

## Flow

1. CEO or operator runs `/task_create`.
2. Discord Bot creates a GitHub Issue.
3. Bot comments a Codex execution prompt on the Issue.
4. Operator runs `/task_run issue_number`.
5. Bot queues the run and starts `codex exec` on EC2 when capacity is available.
6. Codex and the bot comment progress on the Issue during work.
7. `/task_status` and `/task_list` show current Issue state from Discord.
8. Issue updates can be posted back to Discord through the notification channel.

## Commands

- `/task_create title description priority`
  - Register a large task as a GitHub Issue.
  - Generate a Codex task prompt.
- `/task_run issue_number`
  - Queue and start `codex exec` on EC2.
  - Save stdout/stderr logs and write execution comments to the Issue.
- `/task_status issue_number`
  - Show Issue progress fields.
- `/task_list status`
  - List Issues by open/closed/all or a label.
- `/approval_request issue_number reason`
  - Add a human approval request to the Issue.
- `/help`
  - Show command help.

## Non-goals

- No publishing.
- No external posting.
- No secret storage in Git.

## Operating Model

The bot should run on EC2 or a local workstation as a long-running Python process. For production-like operation, run it under systemd and keep tokens in systemd environment overrides or another secret manager outside Git.

Default execution is fixed to `/home/ubuntu/workspace/production`. Future workspace environments can be added as `qa` and `research` through config.

Issue update notifications are best-effort polling. They are for visibility, not for workflow correctness.
