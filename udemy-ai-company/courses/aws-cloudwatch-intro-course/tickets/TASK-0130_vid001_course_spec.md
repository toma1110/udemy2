# Task Summary
Task ID: TASK-0130
Title: VID-001 AWS CloudWatch入門講座のcourse_spec.mdを作成する

# Ownership
Department: strategy
Owner AI: AI-Strategy-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: CEO Approval Required
Auto Execute: yes
Requires CEO Approval: yes
Cost Impact: none

# Inputs
Input Files:
- `market-research/udemy_sellable_video_candidates_50.md`
- `market-research/udemy_competitor_scan.md`
- `market-research/udemy_keyword_demand_scan.md`
- `market-research/learner_pain_review_scan.md`
- `market-research/udemy_video_idea_scoring_top10.md`
- `templates/course_spec_template.md`
- `docs/MISSION_VISION_VALUES.md`
- `docs/CLOUDFORMATION_RULES.md`
Dependencies:
- VID-001 selected by CEO
- TASK-0129 IaC positioning clarification

# Deliverables
Expected Output:
- `courses/aws-cloudwatch-intro-course/course_spec.md`
- Course Title
- Target Audience
- Learning Objectives
- Course Promise
- Differentiation
- Chapter Structure
- Hands-on Scope
- Hands-on IaC Scope
- Production IaC Positioning
- Cost Warning
- Definition of Done
- Out of Scope

# Quality Gate
Definition of Done:
- VID-001の市場根拠 C-03/K-01/P-05 が反映されている
- CloudWatch Metrics/Logs/Alarm/Dashboardの地図を学べる講座仕様になっている
- 初学者向けであり、過度なAWS構築講座になっていない
- CloudFormationは必要な場合のみ教材ハンズオン用と説明している
- 実運用IaCはCDK/Terraform推奨であることを明記している
- Worker != Reviewer が守られている
Mission/Vision/Values Alignment:
- AWS/SREの実務知識を、初学者がREADME通りに再現できる教材へ変換する

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- follow docs/MISSION_VISION_VALUES.md
- follow docs/CLOUDFORMATION_RULES.md
- チケットなし作業禁止

# Blocking
Blocked By:
- CEO approval to start VID-001 course production
Notes:
- Candidate source: VID-001 `AWS CloudWatch入門: Metrics/Logs/Alarm/Dashboardの地図`
- This is a planning/spec task. It does not create AWS resources.
- GitHub Issue: #137 https://github.com/toma1110/udemy2/issues/137
