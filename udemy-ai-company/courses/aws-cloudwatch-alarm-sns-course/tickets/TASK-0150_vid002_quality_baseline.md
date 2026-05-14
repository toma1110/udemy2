# Task Summary
Task ID: TASK-0150
Title: VID-001の動画品質をVID-002以降の制作基準として固定する

# Ownership
Department: qa
Owner AI: AI-QA-01
Reviewer AI: AI-Production-01

# Execution
Priority: high
Status: Done
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none

# Inputs
Input Files:
- `docs/GPT_IMAGE_RULES.md`
- `courses/aws-cloudwatch-intro-course/qa/s1-l1_slide_generation_report.md`
- `courses/aws-cloudwatch-intro-course/qa/s1-l1_drive_upload_report.md`
Dependencies:
- CEO request: この動画の質を崩さないように続ける

# Deliverables
Expected Output:
- `docs/VIDEO_QUALITY_BASELINE.md`
- `docs/QUALITY_GATE.md` の品質比較項目更新

# Quality Gate
Definition of Done:
- VID-001のDrive URLとQAレポートを基準として記録している
- GPT-Image2文字生成、ローカル文字合成禁止、contact sheet確認が基準に含まれている
- VID-001基準より明らかに品質が低いスライドは再生成するルールになっている
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- チケットなし作業禁止

# Blocking
Blocked By:
- none
Notes:
- GitHub Issue: #150 https://github.com/toma1110/udemy2/issues/150
