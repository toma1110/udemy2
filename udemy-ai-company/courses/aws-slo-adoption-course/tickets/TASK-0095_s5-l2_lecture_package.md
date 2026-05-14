# Task Summary
Task ID: TASK-0095
Title: Section 5 Lecture 2 の完成動画を制作しDriveへアップロードする

# Ownership
Department: engineering / production
Owner AI: AI-Engineer-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Done

# Inputs
Input Files:
- `course_spec.md`
- `lectures.md`
- `cloudformation/template.yaml`
- `cloudformation/README.md`
Dependencies:
- TASK-0094 in progress

# Deliverables
Expected Output:
- `scripts/s5-l2_script.md`
- `scripts/s5-l2_script.json`
- `slides/s5-l2/slide_*.png`
- `audio/s5-l2/slide_*.wav`
- `video/s5-l2/s5-l2.mp4`
- Google Drive URL
- QA reports

# Quality Gate
Definition of Done:
- TemplateのParameters、Resources、Outputsを初心者向けに説明している
- Application Signals SLOはオプション扱いを明記している
- GPT-Image2 source evidenceを保存している
- VOICEVOXナレーションチェックを通過している
- MP4 faststart true、decode check OK
- Drive metadataと共有設定を確認している
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- CloudFormationを前提にする
- チケットなし作業禁止

# Blocking
Blocked By:
Notes:
- GitHub Issue: #93
- Completed: 2026-05-11
- Drive URL: https://drive.google.com/file/d/1phpHj8-ZMQrT7vDNX9UxiBRMREVZyyI2/view?usp=drivesdk
- QA report: `qa/section5_completion_report.md`
