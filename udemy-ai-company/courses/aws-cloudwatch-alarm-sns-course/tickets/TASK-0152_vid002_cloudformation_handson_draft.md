# Task Summary
Task ID: TASK-0152
Title: VID-002 CloudFormationハンズオンのテンプレートとREADMEを作る

# Ownership
Department: engineering
Owner AI: AI-Engineer-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Done
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none until stack create/update/delete

# Inputs
Input Files:
- `courses/aws-cloudwatch-alarm-sns-course/course_spec.md`
- `courses/aws-cloudwatch-alarm-sns-course/qa/aws_source_verification_report.md`
- `docs/CLOUDFORMATION_RULES.md`
Dependencies:
- TASK-0151

# Deliverables
Expected Output:
- `courses/aws-cloudwatch-alarm-sns-course/cloudformation/template.yaml`
- `courses/aws-cloudwatch-alarm-sns-course/cloudformation/README.md`
- `courses/aws-cloudwatch-alarm-sns-course/cloudformation/validate.sh`
- `courses/aws-cloudwatch-alarm-sns-course/cloudformation/smoke_test.sh`

# Quality Gate
Definition of Done:
- CloudFormation validate-templateが成功する
- stack create/update/deleteは未実行で、CEO承認ゲートが明記されている
- SNS email confirmation、Topic Policy、暗号化Topic注意がREADMEにある
- 削除手順がある
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- stack create/update/deleteはCEO承認後のみ
- チケットなし作業禁止

# Blocking
Blocked By:
- CEO approval required before stack create/update/delete verification
Notes:
- GitHub Issue: #152 https://github.com/toma1110/udemy2/issues/152
- Static validation completed: `aws cloudformation validate-template` PASS.
- stack create/update/delete remains blocked until CEO approval.
