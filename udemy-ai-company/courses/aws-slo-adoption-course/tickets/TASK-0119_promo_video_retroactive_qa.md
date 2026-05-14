# Task Summary
Task ID: TASK-0119
Title: プロモーション動画制作を遡及チケット化し、QA/アップロード判定に進める

# Ownership
Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: CEO Review
Auto Execute: no
Requires CEO Approval: no
Cost Impact: none

# Inputs
Input Files:
- `course_spec.md`
- `scripts/promo_video_script.md`
- `scripts/promo_video_script.json`
- `slides/promo/`
- `audio/promo/`
- `video/promo/`
- `qa/promo_video_build_report.md`
- `qa/promo_drive_upload_report.md`
Dependencies:
- Course structure and Section 1-9 production assets exist
- VOICEVOX local audio generation environment
- Promo slide renderer: `tools/render_promo_video_slides.py`

# Deliverables
Expected Output:
- Udemy course promotional video MP4
- Promo script Markdown and JSON
- 7 promo slide PNGs
- 7 VOICEVOX WAV files
- Contact sheet and frame check images
- Build report and QA evidence
- Google Drive URL for CEO review
- CEO review result

# Quality Gate
Definition of Done:
- Script and narration are aligned with `course_spec.md`
- Promo video is approximately 90 seconds
- Video is 1920x1080, 16:9, H.264, AAC stereo
- MP4 decode validation passes
- `faststart` is true
- Slide count and audio count match
- Narration risk check passes
- Worker != Reviewer が守られている
- Google Drive upload is available for CEO review
- Udemy publish/upload is handled by a separate approval-gated publication task
Mission/Vision/Values Alignment:
- SLOを概念だけでなくAWS上で運用できる状態へ進めるという講座価値を短く伝える

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- follow docs/MISSION_VISION_VALUES.md
- GPT-Image2/PNGスライド前提を維持する
- VOICEVOX音声前提を維持する
- チケットなしで追加制作、再生成、アップロードをしない

# Blocking
Blocked By:
- CEO promo video review
Notes:
- This is a retroactive ticket because the promo video assets were created before a ticket existed.
- Existing output: `video/promo/promo.30fps.mp4`
- Google Drive file: `promo_slo_course_20260513.mp4`
- Google Drive URL: https://drive.google.com/file/d/1L4rjbl2zXEE0z3fML-xlttIBZxO_ghRy/view?usp=drivesdk
- Drive metadata: `video/promo/drive_upload.json`
- Current validation evidence: `qa/promo_video_build_report.md`
- Drive upload evidence: `qa/promo_drive_upload_report.md`
- Local verification on 2026-05-13 confirmed duration 87.933333 seconds, 1920x1080, 30fps, H.264 video, AAC stereo audio.
- GitHub Issue: #126
