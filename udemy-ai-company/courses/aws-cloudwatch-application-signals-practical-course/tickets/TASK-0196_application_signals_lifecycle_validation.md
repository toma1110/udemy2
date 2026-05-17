# Task Summary

Task ID: `TASK-0196`
Title: Application Signals CloudFormation lifecycle validation

## Ownership

Department: engineering
Owner AI: AI-Engineer-01
Reviewer AI: AI-QA-01

## Execution

Priority: high
Status: Engineering Review
Auto Execute: no
Requires CEO Approval: yes
Cost Impact: AWS resources and Application Signals charges may apply

## Inputs

Input Files:
- `cloudformation/template.yaml`
- `cloudformation/validate.sh`
- `cloudformation/smoke_test.sh`
- `cloudformation/stop_traffic.sh`
- `cloudformation/docs/VALIDATION.md`
- `udemy-ai-company/public_repo/cloudwatch-application-signals-practical-cfn/`

Dependencies:
- `TASK-0192`
- `TASK-0193`

## Deliverables

Expected Output:
- create validation result
- smoke test result
- scenario update result
- Application Signals service discovery evidence
- optional SLO update result
- stop traffic result
- delete result
- `cloudformation/docs/VALIDATION.md` updated with execution logs

## Quality Gate

Definition of Done:
- CEO approval is recorded before execution
- Stack name is unique
- Traffic remains low frequency
- SLO is enabled only after service metrics appear
- `./stop_traffic.sh` is executed before final delete when applicable
- `./validate.sh delete` completes
- Cost/Billing follow-up is documented
- Worker != Reviewer

## Constraints

Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth
- Do not leave scheduled traffic running

## Blocking

Blocked By:
- none

Notes:
- CEO approval was received before AWS create/update/delete execution.
- Executed environment:
  - `AWS_REGION=us-east-1`
  - `STACK_NAME=appsignals-demo-202605161232`
  - `PROJECT_NAME=appsignals-demo`
- Lifecycle completed: create, smoke, slow update, error update, optional SLO update, stop traffic, delete.
- Cleanup verified: stack, schedule group, Lambda functions, and SLO are no longer present.
- Ready for AI-QA-01 review; Worker and Reviewer remain separated.
