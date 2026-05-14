# Task Summary
Task ID: TASK-0103
Title: Section 6 Lecture 4 の完成動画を制作しDriveへアップロードする

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
- `docs/VOICEVOX_RULES.md`
Dependencies:
- Section 5 production is running in another chat; do not modify s5 assets

# Deliverables
Expected Output:
- `scripts/s6-l4_script.md`
- `scripts/s6-l4_script.json`
- `slides/s6-l4/slide_*.png`
- `audio/s6-l4/slide_*.wav`
- `video/s6-l4/s6-l4.mp4`
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
- GitHub Issue: #101

## Completion Notes

- 2026-05-11 completed via AWS Batch two-stage render. Video duration=133.64s. Drive URL: https://drive.google.com/file/d/1BQRUVcUmiIVjd92G_Icax_VvJGon6MHK/view?usp=drivesdk
