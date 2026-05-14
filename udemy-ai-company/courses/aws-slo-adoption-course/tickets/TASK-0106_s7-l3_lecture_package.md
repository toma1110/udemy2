# Task Summary
Task ID: TASK-0106
Title: Section 7 Lecture 3 の完成動画を制作しDriveへアップロードする

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
- `docs/VOICEVOX_RULES.md`
Dependencies:
- Section 5 production is running in another chat; do not modify s5 assets

# Deliverables
Expected Output:
- `scripts/s7-l3_script.md`
- `scripts/s7-l3_script.json`
- `slides/s7-l3/slide_*.png`
- `audio/s7-l3/slide_*.wav`
- `video/s7-l3/s7-l3.mp4`
- Google Drive URL
- QA reports

# Quality Gate
Definition of Done:
- `course_spec.md` と `lectures.md` に整合している
- VOICEVOXナレーションチェックを通過している
- AWS Batch Fargate 2段ジョブでVOICEVOX音声とMP4を生成している
- MP4 faststart true、decode check OK
- Drive metadataと共有設定を確認している
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- チケットなし作業禁止
- s5配下を変更しない

# Blocking
Blocked By:
Notes:
- GitHub Issue: #104

## Completion Notes

- 2026-05-11 completed via AWS Batch two-stage render. Video duration=135.67s. Drive URL: https://drive.google.com/file/d/1GiCH-mg4UbpmF6xB6sBY1ABWDShGQTdv/view?usp=drivesdk
