# Task Summary
Task ID: TASK-0120
Title: プロモーション動画のスライドをGPT Image2で再生成して再アップロードする

# Ownership
Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: CEO Review
Auto Execute: yes
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
- GitHub Issue #126 CEO comment
Dependencies:
- TASK-0119
- Existing promo narration and VOICEVOX audio
- GPT Image2 generation capability

# Deliverables
Expected Output:
- GPT Image2 regenerated promo slide PNGs
- Updated promo contact sheet
- Rebuilt promo video MP4
- Decode/build validation report
- Google Drive URL for CEO review
- Issue comment with result

# Quality Gate
Definition of Done:
- Slides are regenerated from GPT Image2 or GPT Image2-derived PNG assets
- Visual direction is richer and more appealing than the previous Pillow slides
- Slides are not cluttered and remain readable in video
- Narration/audio count still matches slide count
- MP4 is 1920x1080, 16:9, H.264, AAC stereo
- MP4 decode validation passes
- Google Drive upload is available for CEO review
- Worker != Reviewer が守られている
Mission/Vision/Values Alignment:
- 受講したいと思えるプロモーション動画にし、SLOをAWS上で運用できる状態へ進める講座価値を明確に伝える

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- follow docs/MISSION_VISION_VALUES.md
- GPT-Image2/PNGスライド前提を維持する
- VOICEVOX音声前提を維持する
- チケットなし作業禁止

# Blocking
Blocked By:
Notes:
- Source comment: https://github.com/toma1110/udemy2/issues/126#issuecomment-4445593813
- CEO request: `gpt immage2を使ってスライド再生成をお願いします。受講したいと思える動画にしたいです。ごちゃごちゃしすぎず、かつリッチにお願いしますー！`
- Previous output: `video/promo/promo.30fps.mp4`
- Previous Drive URL: https://drive.google.com/file/d/1L4rjbl2zXEE0z3fML-xlttIBZxO_ghRy/view?usp=drivesdk
- GitHub Issue: #127
- New output: `video/promo/promo.30fps.mp4`
- New Drive URL: https://drive.google.com/file/d/15IlfcpRWIxstWpieUOuSHRkQsj3HU_xw/view?usp=drivesdk
- Slide generation report: `qa/promo_gpt_image2_slide_generation_report.md`
- Video build report: `qa/promo_gpt_image2_video_build_report.md`
