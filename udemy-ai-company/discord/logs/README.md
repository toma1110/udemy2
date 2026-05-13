# Discord Command Center Logs

Runtime logs are written locally and are not committed to Git.

Default Codex run log path:

```text
discord/logs/codex-runs/issue-<number>-<timestamp>.log
```

Each log contains:

- codex exec command
- fixed workspace
- start and completion timestamps
- exit code
- prompt
- stdout
- stderr

The GitHub Issue comment records the log path after each run.
