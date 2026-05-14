# Task Summary
Task ID: TASK-0097
Title: Section 5 Lecture 4 の完成動画を制作しDriveへアップロードする

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
- `cloudformation/smoke_test.sh`
- `cloudformation/README.md`
Dependencies:
- TASK-0096 in progress

# Deliverables
Expected Output:
- `scripts/s5-l4_script.md`
- `scripts/s5-l4_script.json`
- `slides/s5-l4/slide_*.png`
- `audio/s5-l4/slide_*.wav`
- `video/s5-l4/s5-l4.mp4`
- Google Drive URL
- QA reports

# Quality Gate
Definition of Done:
- smoke testの確認対象が明確
- Output取得、SNS、Alarm、Dashboard確認を説明している
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
- GitHub Issue: #95
- Completed: 2026-05-11
- Drive URL: https://drive.google.com/file/d/1eQt7abrh_Q-UgZurQJxiUMJOcfwWrgOn/view?usp=drivesdk
- QA report: `qa/section5_completion_report.md`
