# Task Summary
Task ID: TASK-0192
Title: Application Signals CloudFormation hands-on implementation

# Ownership
Department: Engineering
Owner AI: AI-Engineer-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Engineering Review

# Inputs
Input Files:
- `course_spec.md`
- `handson/README.md`
- `cloudformation/README.md`

# Deliverables
Expected Output:
- `cloudformation/template.yaml`
- `cloudformation/validate.sh`
- `cloudformation/smoke_test.sh`
- `cloudformation/stop_traffic.sh`
- `cloudformation/docs/VALIDATION.md`
- Public repo implementation under `udemy-ai-company/public_repo/cloudwatch-application-signals-practical-cfn/`

# Quality Gate
Definition of Done:
- AWS official docs checked for Lambda Application Signals setup, OpenTelemetry Layer ARN, Application Signals Discovery, and pricing.
- `aws cloudformation validate-template` succeeds.
- Scripts pass `bash -n`.
- Template uses low-frequency traffic by default.
- Stop traffic and delete paths are explicit.
- No create/update/delete/full is executed without CEO approval.
- Worker and Reviewer are separated.

# Constraints
Rules:
- Planner != Worker
- Worker != Reviewer
- Public repo work copy must be under `udemy-ai-company/public_repo/<repo-name>/`
- CloudFormation is for hands-on reproduction. Production IaC recommendation remains CDK or Terraform.

# Blocking
Blocked By:
- CEO approval for AWS stack create/update/smoke/delete lifecycle validation

Notes:
- Consider Lambda-first implementation. ECS/Fargate sidecar is out of scope for initial course.
- Public repo scaffold has been created.
- Template and scripts were implemented on 2026-05-16.
- `./validate.sh validate` passed.
- AWS resource lifecycle validation remains pending.
