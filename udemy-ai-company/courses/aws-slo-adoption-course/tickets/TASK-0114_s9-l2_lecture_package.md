# Task Summary
Task ID: TASK-0114
Title: Section 9 Lecture 2 の完成動画を制作しDriveへアップロードする

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
- Section 7 GPT-Image2版はCEO確認中

# Deliverables
Expected Output:
- `scripts/s9-l2_script.md`
- `scripts/s9-l2_script.json`
- `slides/s9-l2/slide_*.png`
- `slides/s9-gpt-image2-sources/s9-l2/slide_*.png`
- `slides/s9-l2/contact_sheet.png`
- `audio/s9-l2/slide_*.wav`
- `audio/s9-l2/voicevox_report.json`
- `video/s9-l2/s9-l2.mp4`
- `video/s9-l2/build_report.json`
- `video/s9-l2/drive_upload.json`
- `qa/s9-l2_*_report.md`

# Quality Gate
Definition of Done:
- `course_spec.md` と `lectures.md` に整合している
- VOICEVOXナレーションチェックを通過している
- GPT-Image2で8枚のスライドを生成している
- AWS Batch Fargate 2段ジョブでVOICEVOX音声とMP4を生成している
- MP4 faststart true、decode check OK
- Google Drive upload and anyone-reader sharing verified
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- チケットなし作業禁止
- S7配下を変更しない

# Blocking
Blocked By:
Notes:
- GitHub Issue: #121
