# Task Summary
Task ID: TASK-0115
Title: Section 9 Lecture 3 の完成動画を制作しDriveへアップロードする

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
- `scripts/s9-l3_script.md`
- `scripts/s9-l3_script.json`
- `slides/s9-l3/slide_*.png`
- `slides/s9-gpt-image2-sources/s9-l3/slide_*.png`
- `slides/s9-l3/contact_sheet.png`
- `audio/s9-l3/slide_*.wav`
- `audio/s9-l3/voicevox_report.json`
- `video/s9-l3/s9-l3.mp4`
- `video/s9-l3/build_report.json`
- `video/s9-l3/drive_upload.json`
- `qa/s9-l3_*_report.md`

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
- GitHub Issue: #122
