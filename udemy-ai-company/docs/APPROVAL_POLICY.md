# APPROVAL_POLICY

This policy defines human approval gates and logged operations in AI制作会社.

## Allowed With Logging In Current Operations

The current EC2 operation model allows Codex to run with full working permissions. These actions are not blocked by the Discord bot, but they must be recorded in Issue comments, local logs, and Discord notifications when detected:

- CloudFormation stack create, update, delete, or deploy
- AWS operations required by the approved task scope
- `git push`
- `git merge`

## Always Requires Human Approval

- Publishing course content
- Google Drive public sharing changes for final materials
- External posting outside the repository
- Irreversible destructive operations outside the approved task scope

## Approval Record

Approval must be recorded in the GitHub Issue before the gated action.

Accepted records:

- `ceo-approved` label
- `/approve-cost` comment
- Explicit CEO approval comment
- Filled `CEO Approval: approved` field

## Discord Command Center Rules

- `/approval_request` may request approval, but it does not approve.
- `/task_run` may start `codex exec` through the run queue.
- Discord Bot may add `approval-required` and `blocked`.
- Discord Bot must not add `ceo-approved`.
- Discord Bot must not bypass queue control or hide execution logs.
- Codex must stop before gated actions until approval is recorded.

## Codex Rules

Codex must comment on the Issue when approval is needed.

The comment must include:

- Requested action
- Reason
- Cost or safety impact
- Rollback or cleanup plan when applicable
- Exact command or operation that will be run after approval

After approval, Codex must comment again before execution and record the result.
