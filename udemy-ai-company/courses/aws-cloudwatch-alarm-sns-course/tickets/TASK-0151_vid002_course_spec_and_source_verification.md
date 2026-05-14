# Task Summary
Task ID: TASK-0151
Title: VID-002 CloudWatch Alarm + SNS通知のcourse_specとAWS仕様確認を作る

# Ownership
Department: strategy
Owner AI: AI-Strategy-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Done
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none

# Inputs
Input Files:
- `market-research/udemy_sellable_video_candidates_50.md`
- `market-research/udemy_video_idea_scoring_top10.md`
- `docs/VIDEO_QUALITY_BASELINE.md`
Dependencies:
- TASK-0150

# Deliverables
Expected Output:
- `courses/aws-cloudwatch-alarm-sns-course/course_spec.md`
- `courses/aws-cloudwatch-alarm-sns-course/qa/aws_source_verification_report.md`

# Quality Gate
Definition of Done:
- VID-002の対象者、学習目標、Course Promise、Out of Scopeが明記されている
- AWS::CloudWatch::Alarm、AWS::SNS::Topic、AWS::SNS::Subscriptionの公式確認がある
- SNSメール確認と暗号化Topicの注意点が反映されている
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- AWS仕様はawsknowledgeで確認する
- チケットなし作業禁止

# Blocking
Blocked By:
- none
Notes:
- GitHub Issue: #151 https://github.com/toma1110/udemy2/issues/151
