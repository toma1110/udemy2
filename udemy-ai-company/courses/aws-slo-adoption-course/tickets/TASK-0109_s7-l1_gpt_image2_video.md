# Task Summary
Task ID: TASK-0109
Title: Section 7 Lecture 1 をGPT-Image2版で制作しDriveへアップロードする

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
- `scripts/s7-l1_script.md`
- `scripts/s7-l1_script.json`
- `audio/s7-l1/slide_*.wav`
Dependencies:
- S6 GPT-Image2版の制作方針を踏襲する

# Deliverables
Expected Output:
- `slides/s7-l1/slide_*.png`
- `slides/s7-gpt-image2-sources/s7-l1/slide_*.png`
- `slides/s7-l1/contact_sheet.png`
- `video/s7-l1/s7-l1.mp4`
- `video/s7-l1/build_report.json`
- `video/s7-l1/drive_upload.json`
- `qa/s7-l1_slide_generation_report.md`
- `qa/s7-l1_video_build_report.md`
- `qa/s7-l1_drive_upload_report.md`

# Quality Gate
Definition of Done:
- GPT-Image2で8枚のスライドを生成している
- VOICEVOX音声とスライド数が一致している
- AWS Batch Fargate render jobでMP4を生成している
- MP4 faststart true、decode check OK
- Google Drive upload and anyone-reader sharing verified
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- チケットなし作業禁止
- S6配下を変更しない

# Blocking
Blocked By:
Notes:
- GitHub Issue: #111
- Completed: 2026-05-12
- Batch job: `8c6ebde5-c852-4801-b4ca-6d1383c1b230`
- Drive URL: https://drive.google.com/file/d/1TePcU6JE22ZwOmzVs62trVtUSInJTOqO/view?usp=drivesdk
- QA: faststart true、decode check OK、anyone-reader sharing verified
