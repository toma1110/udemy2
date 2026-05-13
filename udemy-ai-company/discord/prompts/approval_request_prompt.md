# Approval Request Prompt

GitHub Issue: #${issue_number} ${issue_title}
Issue URL: ${issue_url}

## Human Approval Required

This task must stop until a human approves the requested action.

## Reason

${reason}

## Approval Required For

- Publishing
- External posting or final public sharing
- Any irreversible or destructive operation

CloudFormation create/update/delete, `git push`, and `git merge` are allowed by the current EC2 operation policy, but must be logged in Issue comments, local execution logs, and Discord notifications.

## How To Approve

Record approval in the Issue with one of:

- `ceo-approved` label
- `/approve-cost` comment
- Explicit CEO approval comment

Until approval is recorded, Codex and automation must not perform the gated action.
