# TASK-0221: Publish Application Signals public repository

## Task Summary

- Task ID: `TASK-0221`
- Title: `Publish Application Signals public repository`
- GitHub Issue: `#195`
- GitHub Repository: `toma1110/cloudwatch-application-signals-practical-cfn`

## Ownership

- Department: `engineering`
- Owner AI: `AI-Engineer-01`
- Reviewer AI: `AI-QA-01`

## Execution

- Priority: `high`
- Status: `ready for review`

## Inputs

- `udemy-ai-company/courses/aws-cloudwatch-application-signals-practical-course/course_spec.md`
- `udemy-ai-company/public_repo/cloudwatch-application-signals-practical-cfn/`
- `udemy-ai-company/docs/PUBLIC_REPO_RULES.md`

## Deliverables

- Public GitHub repository created.
- Current public-ready CloudFormation handson files pushed to the public repository.
- Parent repository references updated with the public URL.

## Quality Gate

- Public repo does not include parent repository history.
- Internal local paths and AWS account IDs are not included in published files.
- Shell scripts pass `bash -n`.
- CloudFormation template passes `aws cloudformation validate-template`.
- AWS resource creation, update, delete, and Application Signals runtime verification remain CEO-approved operations only.
- Worker AI and Reviewer AI are different.

## Constraints

- Planner != Worker
- Worker != Reviewer
- Public repo working copy belongs under `udemy-ai-company/public_repo/<repo-name>/`
- Do not publish internal production materials, QA-only notes, videos, audio, or slide assets

## Blocking

- Blocked By: none
- Notes: Published repository is for CloudFormation handson files only.
