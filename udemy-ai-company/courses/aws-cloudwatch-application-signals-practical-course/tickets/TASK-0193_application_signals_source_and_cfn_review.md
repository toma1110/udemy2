# Task Summary

Task ID: `TASK-0193`
Title: Application Signals course source and CloudFormation review

## Ownership

Department: qa
Owner AI: AI-QA-01
Reviewer AI: AI-Strategy-01

## Execution

Priority: high
Status: Backlog
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none

## Inputs

Input Files:
- `course_spec.md`
- `course_curriculum.md`
- `qa/aws_source_verification_report.md`
- `cloudformation/template.yaml`
- `cloudformation/validate.sh`
- `cloudformation/smoke_test.sh`
- `cloudformation/stop_traffic.sh`
- `cloudformation/docs/VALIDATION.md`
- `udemy-ai-company/public_repo/cloudwatch-application-signals-practical-cfn/`

Dependencies:
- `TASK-0191`
- `TASK-0192`

## Deliverables

Expected Output:
- `qa/course_creation_qa_report.md`
- Review findings for CloudFormation, README, public repo, cost warnings, and AWS source alignment

## Quality Gate

Definition of Done:
- Worker != Reviewer
- AWS official sources are cited
- CloudFormation validate result is confirmed
- create/update/delete are not falsely marked complete
- SLO delayed-creation constraint is explained
- Public repo path follows `docs/PUBLIC_REPO_RULES.md`
- Course messages, curriculum, and promotion scope are present

## Constraints

Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth
- Do not run AWS stack create/update/delete

## Blocking

Blocked By:
- None

Notes:
- This is a non-cost QA review. Full lifecycle validation is a separate CEO-approved activity.
