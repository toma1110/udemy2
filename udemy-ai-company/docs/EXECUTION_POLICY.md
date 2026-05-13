# EXECUTION_POLICY

This policy defines how Discord-triggered Codex execution is controlled.

## Execution

- `/task_run` is the execution command.
- `codex exec` runs on EC2 through subprocess.
- Working directory is fixed to `/home/ubuntu/workspace/production` by default.
- Future workspace environments are `production`, `qa`, and `research`.
- Default maximum parallel runs is `1`.
- Default timeout is `7200` seconds.

## Dangerous Operations

The following operations are allowed in the current environment but must be logged:

- CloudFormation create/update/delete/deploy
- `git push`
- `git merge`

The bot records dangerous operation detection in:

- GitHub Issue comments
- local Codex run logs
- Discord notifications

## Human Approval

Publishing and external posting require explicit human approval.

When a task needs approval, use `/approval_request issue_number reason`.

## Prohibited Bot Behavior

The Discord bot must not:

- bypass the run queue
- run more than the configured parallel limit
- change workspace outside the configured environment
- hide execution logs
- approve its own gated actions
