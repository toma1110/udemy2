# Task Summary

Task ID: `TASK-0169`
GitHub Issue: https://github.com/toma1110/udemy2/issues/160
Title: AWS課金事故防止入門 course_spec 作成

## Ownership

Department: Strategy
Owner AI: AI-Strategy-01
Reviewer AI: AI-QA-01

## Execution

Priority: high
Status: Done
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none

## Inputs

Input Files:
- `market-research/udemy_video_idea_scoring_top10.md`
- `market-research/next_course_decision_pack.md`
- `templates/course_spec_template.md`

Dependencies:
- CEO approval in chat for next course selection
- `CR-0001_cost_safety_course_creation.md`

## Deliverables

Expected Output:
- `course_spec.md`
- `course_curriculum.md`
- `README.md`
- `course_infomation.md`
- initial `handson/README.md`
- initial `cloudformation/README.md`
- initial `qa/aws_source_verification_report.md`

## Quality Gate

Definition of Done:
- Source of Truthが明確
- Budgets、Cost Explorer、Cost Anomaly Detectionの公式ソースが参照されている
- AWS実行、Billing/Cost API実行、CloudFormation stack操作のCEO承認ゲートが明記されている
- GPT-Image2とVOICEVOXの制作ルールが明記されている
- Worker and Reviewer are different

Mission/Vision/Values Alignment:
- AWS学習者の課金不安を減らし、低コストで再現しやすい学習導線を作る

## Constraints

Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth
- AWS/billing-related execution requires CEO approval

## Blocking

Blocked By:
- None

Notes:
- Course ID: `aws-cost-safety-course`
