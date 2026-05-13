# DISCORD_AUTOMATION

Discord Command Center provides semi-autonomous execution from Discord to Codex on EC2.

## Roles

- Discord: instruction UI and progress confirmation UI
- GitHub Issue: progress ledger
- Codex: execution engine
- AI-PM-01: progress management and queue visibility

## `/task_run` Flow

1. User runs `/task_run issue_number` in Discord.
2. Bot fetches the GitHub Issue.
3. Bot adds the run to the FIFO queue and comments the queue state on the Issue.
4. Queue worker renders the Codex execution prompt when capacity is available.
5. Queue worker validates the fixed workspace through `run_guard.py`.
6. Queue worker starts `codex exec` on EC2.
7. Bot comments start/running/completed/error states on the Issue.
8. Bot saves stdout/stderr to `discord/logs/codex-runs/`.
9. Bot posts queue/start/completion/error notifications to Discord.

## Policy

This is not issue-driven full autonomy. Execution starts from a Discord command and is recorded in GitHub Issues.

Codex may run with full EC2 permissions according to the current operation model. CloudFormation create/update/delete, `git push`, and `git merge` are not blocked, but they are logged as dangerous operations when detected.

Publishing and external posting require explicit human approval.
