# Task Summary
Task ID: TASK-0096
Title: Section 5 Lecture 3 の完成動画を制作しDriveへアップロードする

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
- `cloudformation/validate.sh`
- `cloudformation/template.yaml`
Dependencies:
- TASK-0095 in progress

# Deliverables
Expected Output:
- `scripts/s5-l3_script.md`
- `scripts/s5-l3_script.json`
- `slides/s5-l3/slide_*.png`
- `audio/s5-l3/slide_*.wav`
- `video/s5-l3/s5-l3.mp4`
- Google Drive URL
- QA reports

# Quality Gate
Definition of Done:
- create、put-metrics、確認対象を説明している
- SNS、Alarm、Dashboardの関係が明確
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
- GitHub Issue: #94
- Completed: 2026-05-11
- Drive URL: https://drive.google.com/file/d/1xxHKmBm-QxCsnP1kacwlIUjB8KrUubl7/view?usp=drivesdk
- QA report: `qa/section5_completion_report.md`
