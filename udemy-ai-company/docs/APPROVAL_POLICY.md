# APPROVAL_POLICY

This policy defines human approval gates and logged operations in AI制作会社.

## Allowed With Logging In Current Operations

The current EC2 operation model allows Codex to run with full working permissions. These actions are not blocked by the Discord bot, but they must be recorded in Issue comments, local logs, and Discord notifications when detected:

- CloudFormation stack create, update, delete, or deploy
- AWS operations required by the approved task scope
- Google Drive uploads for CEO/QA review, including anyone-reader sharing in the configured review folder
- `git push`
- `git merge`

## Always Requires Human Approval

- Publishing course content
- Changing, replacing, or deleting final approved Google Drive materials
- External posting outside the repository
- Irreversible destructive operations outside the approved task scope

## Google Drive Review Uploads

Google Drive is the normal review surface for CEO and QA video checks. If a video has passed local build validation and the task is for CEO/QA review, Codex must upload it to the configured Google Drive folder without asking for prior CEO approval, save `drive_upload.json`, and comment the Drive URL on the Issue.

This review upload is not a publish action. Udemy publishing, external posting, or modifying final approved Drive assets still requires explicit CEO approval.

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
