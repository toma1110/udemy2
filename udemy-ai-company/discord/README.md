# Discord Command Center

Discord Command Center connects Discord slash commands to GitHub Issues for AI制作会社.

Discord is used as the instruction and progress UI. GitHub Issues remain the progress ledger. Codex runs on EC2 through `codex exec` when `/task_run` is called.

The bot starts Codex through a queue. CloudFormation create/update/delete, `git push`, and `git merge` are not blocked in the current operation model, but they are detected and recorded as dangerous operation logs. Publishing and external posting still require explicit human approval.

## Commands

- `/task_create title description priority`
  - Creates a GitHub Issue from a large task.
  - Adds a Codex execution prompt as an Issue comment.
- `/task_status issue_number`
  - Shows Issue state, labels, Owner AI, Reviewer AI, priority, and URL.
- `/task_run issue_number`
  - Queues the Issue for `codex exec` on EC2.
  - Saves stdout/stderr to `logs/codex-runs/`.
  - Writes start/running/completed/error comments to the Issue.
- `/task_list status`
  - Lists Issues by `open`, `closed`, `all`, or an open Issue label such as `blocked`.
- `/approval_request issue_number reason`
  - Adds a human approval request comment and applies `approval-required` and `blocked`.
- `/help`
  - Shows command usage.

## Required Environment Variables

- `DISCORD_BOT_TOKEN`
  - Discord Bot token.
- `GITHUB_TOKEN`
  - GitHub fine-grained token with repository Issues read/write permission.
- `GITHUB_REPOSITORY`
  - Repository in `owner/repo` format. Example: `toma1110/udemy2`.

Optional:

- `DISCORD_GUILD_ID`
  - Guild ID for faster command registration during development.
- `DISCORD_NOTIFY_CHANNEL_ID`
  - Channel ID where Issue update notifications are posted.
- `COMMAND_CENTER_CONFIG`
  - Path to a YAML config file.
- `COMMAND_CENTER_POLL_SECONDS`
  - Issue update polling interval. Default: `60`.
- `COMMAND_CENTER_STATE_FILE`
  - Local state JSON path. Default is under `.pm_state/`.
- `COMMAND_CENTER_MAX_PARALLEL_RUNS`
  - Queue parallelism. Default: `1`.
- `AI_COMPANY_WORKSPACE_ROOT`
  - Workspace root. Default: `/home/ubuntu/workspace`.
- `AI_COMPANY_WORKSPACE_ENV`
  - Workspace environment. Default: `production`.
- `CODEX_EXEC_COMMAND`
  - Codex command. Default: `codex exec --sandbox danger-full-access --ask-for-approval never -`.
- `CODEX_EXEC_TIMEOUT_SECONDS`
  - Codex run timeout. Default: `7200`.
- `CODEX_RUN_LOG_DIR`
  - Runtime log directory. Default: `discord/logs/codex-runs`.

## Local Setup

```bash
cd /home/ubuntu/workspace/udemy2/udemy-ai-company/discord
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Set secrets in the shell or systemd environment. Do not commit them.

```bash
export DISCORD_BOT_TOKEN="..."
export GITHUB_TOKEN="..."
export GITHUB_REPOSITORY="toma1110/udemy2"
export DISCORD_GUILD_ID="..."
export DISCORD_NOTIFY_CHANNEL_ID="..."
export AI_COMPANY_WORKSPACE_ENV="production"
export COMMAND_CENTER_MAX_PARALLEL_RUNS="1"
```

Ensure the fixed workspace exists before using `/task_run`:

```bash
mkdir -p /home/ubuntu/workspace/production
```

Run:

```bash
python bot.py
```

## Discord Bot Creation

1. Open Discord Developer Portal.
2. Create an application.
3. Add a Bot user.
4. Enable the `applications.commands` OAuth2 scope.
5. Invite the bot to the target server with permission to send messages.
6. Copy the Bot token into `DISCORD_BOT_TOKEN`.
7. Copy the Guild ID into `DISCORD_GUILD_ID` for fast local slash-command sync.
8. Copy the notification channel ID into `DISCORD_NOTIFY_CHANNEL_ID` if update notifications are needed.

## systemd Example

Install the bundled service file:

```bash
sudo install -m 0644 /home/ubuntu/workspace/udemy2/udemy-ai-company/systemd/ai-company-bot.service /etc/systemd/system/ai-company-bot.service
```

Create the secret environment file outside Git:

```bash
mkdir -p /home/ubuntu/.config/ai-company
chmod 700 /home/ubuntu/.config/ai-company
nano /home/ubuntu/.config/ai-company/discord-command-center.env
chmod 600 /home/ubuntu/.config/ai-company/discord-command-center.env
```

Example content:

```text
DISCORD_BOT_TOKEN=replace-me
GITHUB_TOKEN=replace-me
DISCORD_GUILD_ID=replace-me
DISCORD_NOTIFY_CHANNEL_ID=replace-me
```

Enable and start:

```bash
sudo systemctl daemon-reload
sudo systemctl enable ai-company-bot.service
sudo systemctl start ai-company-bot.service
sudo systemctl status ai-company-bot.service
sudo systemctl restart ai-company-bot.service
sudo journalctl -u ai-company-bot.service -n 100 --no-pager
```

## Queue and Logs

- Default parallelism is `1`.
- If a run is already active, `/task_run` adds the Issue to the queue.
- Queue events are written to the Issue and Discord notification channel.
- Run logs are saved under `discord/logs/codex-runs/`.
- The Issue receives the log path, exit code, stdout tail, stderr tail, and next action.

## Security

- Never store Discord or GitHub tokens in the repository.
- Use the minimum GitHub token scope: Issues read/write for this repository.
- Do not grant repository contents write permission unless a future feature explicitly requires it.
- Keep secrets out of Git.
- Keep AWS credentials scoped to the EC2 role if AWS access is needed by Codex.
- Queue parallelism must stay at `1` until the production workflow is proven stable.
- CloudFormation create/update/delete, `git push`, and `git merge` are allowed by current policy but logged and notified.
- Human approval is required before publishing or external posting.
