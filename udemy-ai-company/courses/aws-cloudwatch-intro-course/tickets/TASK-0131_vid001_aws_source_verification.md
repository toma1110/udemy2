# Task Summary
Task ID: TASK-0131
Title: VID-001 CloudWatch公式仕様と講座内説明を検証する

# Ownership
Department: engineering
Owner AI: AI-Engineer-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: CEO Approval Required
Auto Execute: yes
Requires CEO Approval: yes
Cost Impact: none

# Inputs
Input Files:
- `courses/aws-cloudwatch-intro-course/course_spec.md`
- `docs/QUALITY_GATE.md`
- `docs/CLOUDFORMATION_RULES.md`
Dependencies:
- TASK-0130

# Deliverables
Expected Output:
- `courses/aws-cloudwatch-intro-course/qa/cloudwatch_source_verification_report.md`
- CloudWatch Metrics/Logs/Alarms/Dashboardsの公式仕様確認
- 講座で説明してよい範囲とOut of Scope
- ハンズオンでAWSリソース作成が必要かどうかの判定

# Quality Gate
Definition of Done:
- AWS公式ドキュメントまたはawsknowledgeでCloudWatchの最新仕様を確認している
- Metrics、Logs、Alarms、Dashboardsの違いを正確に説明できる
- CloudWatch料金や無料枠に関わる断定を避け、注意書き方針を出している
- AWSリソース作成が必要な場合は別途CEO承認が必要と明記している
- Worker != Reviewer が守られている
Mission/Vision/Values Alignment:
- 未検証の技術説明を確定事項として教材化しない

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- follow docs/QUALITY_GATE.md
- AWSリソース作成は禁止
- チケットなし作業禁止

# Blocking
Blocked By:
- TASK-0130
- CEO approval to start VID-001 course production
Notes:
- This task is research/verification only.
- GitHub Issue: #138 https://github.com/toma1110/udemy2/issues/138
