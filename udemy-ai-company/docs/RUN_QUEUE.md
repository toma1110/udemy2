# RUN_QUEUE

The run queue prevents Discord-triggered Codex executions from running out of control.

## Default

```yaml
max_parallel_runs: 1
```

Only one Codex run executes at a time. Additional `/task_run` requests wait in FIFO order.

## Queue Events

When a task is queued:

- Discord receives a queued notification
- GitHub Issue receives a queue comment
- Queue position is shown to the caller

When a task starts:

- GitHub Issue receives an execution start comment
- Discord receives a start notification

When a task completes or fails:

- GitHub Issue receives exit code, log path, stdout/stderr tail, and next action
- Discord receives completion or error notification

## Logs

Logs are saved to:

```text
udemy-ai-company/discord/logs/codex-runs/issue-<number>-<timestamp>.log
```

Logs are local runtime artifacts and are not committed to Git.
