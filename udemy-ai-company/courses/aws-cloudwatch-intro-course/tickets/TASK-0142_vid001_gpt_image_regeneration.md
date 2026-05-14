# Task Summary
Task ID: TASK-0142
Title: VID-001をGPT-Image2由来スライドで再生成し、動画を差し替える

# Ownership
Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Done
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none

# Inputs
Input Files:
- `courses/aws-cloudwatch-intro-course/course_spec.md`
- `courses/aws-cloudwatch-intro-course/scripts/s1-l1_script.json`
- `courses/aws-cloudwatch-intro-course/slides/s1-l1_storyboard.md`
- `courses/aws-cloudwatch-intro-course/audio/s1-l1/slide_*.wav`
- `docs/GPT_IMAGE_RULES.md`
Dependencies:
- TASK-0141
- Existing VID-001 local-renderer video

# Deliverables
Expected Output:
- `courses/aws-cloudwatch-intro-course/slides/s1-gpt-image2-sources/s1-l1/slide_*.png`
- `courses/aws-cloudwatch-intro-course/slides/s1-l1/slide_*.png`
- `courses/aws-cloudwatch-intro-course/slides/s1-l1/contact_sheet.png`
- `courses/aws-cloudwatch-intro-course/video/s1-l1/s1-l1.mp4`
- `courses/aws-cloudwatch-intro-course/qa/s1-l1_slide_generation_report.md`
- `courses/aws-cloudwatch-intro-course/qa/s1-l1_video_build_report.md`
- `courses/aws-cloudwatch-intro-course/qa/s1-l1_content_qa_report.md`
- `courses/aws-cloudwatch-intro-course/qa/s1-l1_drive_upload_report.md`

# Quality Gate
Definition of Done:
- GPT-Image2で10枚のsource PNGを生成している
- 表示文字もGPT-Image2で生成している
- GPT-Image2 source PNGと最終PNGの対応表がある
- ローカル描画のみのスライドPNGを完成動画に使っていない
- ローカル文字合成したスライドPNGを完成動画に使っていない
- 既存VOICEVOX音声とスライド数が一致している
- MP4 faststart true、decode check OK
- Google Drive upload and anyone-reader sharing verified
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- `docs/GPT_IMAGE_RULES.md` に従う
- チケットなし作業禁止

# Blocking
Blocked By:
- none
Notes:
- 既存のローカルrenderer版動画は差し替え対象。
- GitHub Issue: #149 https://github.com/toma1110/udemy2/issues/149
- GPT-Image2で文字入りsource PNGを10枚生成済み。
- 文字合成なしで1920 x 1080へフィットし、既存VOICEVOX音声と再結合済み。
- Drive upload: https://drive.google.com/file/d/1JzSBq-AtW2JkA96w8AQWTLuU_B2gZwsv/view?usp=drivesdk
