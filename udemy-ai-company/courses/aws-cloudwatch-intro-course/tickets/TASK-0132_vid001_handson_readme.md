# Task Summary
Task ID: TASK-0132
Title: VID-001 CloudWatch入門ハンズオンREADMEを作成する

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
- `courses/aws-cloudwatch-intro-course/qa/cloudwatch_source_verification_report.md`
- `docs/CLOUDFORMATION_RULES.md`
- `docs/QUALITY_GATE.md`
Dependencies:
- TASK-0130
- TASK-0131

# Deliverables
Expected Output:
- `courses/aws-cloudwatch-intro-course/README.md`
- `courses/aws-cloudwatch-intro-course/handson/README.md`
- CloudWatch Metrics/Logs/Alarm/Dashboardの確認手順
- コスト注意
- 削除または後片付け手順
- 失敗時の確認ポイント

# Quality Gate
Definition of Done:
- README通りにCloudWatchの全体像を確認できる
- 初学者が迷いやすいMetrics/Logs/Alarm/Dashboardの違いが整理されている
- 原則としてAWSリソース作成なし、または作成が必要な場合は別チケット化されている
- CloudFormationを使う場合は教材ハンズオン用途であることを説明している
- 実運用ではCDK/Terraformで管理する考え方を補足している
- Worker != Reviewer が守られている
Mission/Vision/Values Alignment:
- 受講者がREADME通りに再現できることを優先する

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- AWSリソース作成はこのチケットでは実行しない
- チケットなし作業禁止

# Blocking
Blocked By:
- TASK-0130
- TASK-0131
- CEO approval to start VID-001 course production
Notes:
- VID-001のハンズオン範囲は「概念図とサンプルメトリクス確認」。
- GitHub Issue: #139 https://github.com/toma1110/udemy2/issues/139
