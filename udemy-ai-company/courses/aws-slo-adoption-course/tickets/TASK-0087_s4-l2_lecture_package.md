# Task Summary
Task ID: TASK-0087
Title: Section 4 Lecture 2 の完成動画を制作しDriveへアップロードする

# Ownership
Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Done

# Inputs
Input Files:
- `course_spec.md`
- `lectures.md`
- AWS CloudWatch Application Signals official docs
Dependencies:
- TASK-0086 in progress

# Deliverables
Expected Output:
- `scripts/s4-l2_script.md`
- `scripts/s4-l2_script.json`
- `slides/s4-l2/slide_*.png`
- `audio/s4-l2/slide_*.wav`
- `video/s4-l2/s4-l2.mp4`
- Google Drive URL
- QA reports

# Quality Gate
Definition of Done:
- AWS公式情報を確認している
- GPT-Image2 source evidenceを保存している
- VOICEVOXナレーションチェックを通過している
- MP4 faststart true、decode check OK
- Drive sharing anyone reader true

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- ローカル描画だけで最終スライドを作らない

# Blocking
Blocked By:
Notes:
- GitHub Issue: #87
- Completed: 2026-05-11
- Drive URL: https://drive.google.com/file/d/1GY-DoU_Slpi-cEsSzsJrSkyzcbL4JsOe/view?usp=drivesdk
- Revision: TASK-0091 CEO feedback remediation applied
