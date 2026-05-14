# Task Summary
Task ID: TASK-0123
Title: SLO導入主語のpromo動画をGPT-Image2で再生成する

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
- `courses/aws-slo-adoption-course/course_spec.md`
- `courses/aws-slo-adoption-course/course_infomation.md`
- `courses/aws-slo-adoption-course/scripts/promo_video_script.md`
- `courses/aws-slo-adoption-course/scripts/promo_video_script.json`
- `docs/GPT_IMAGE_RULES.md`
- `docs/VIDEO_QUALITY_BASELINE.md`
Dependencies:
- TASK-0121

# Deliverables
Expected Output:
- `courses/aws-slo-adoption-course/slides/promo_slo_adoption_gpt_image2_prompts.md`
- `courses/aws-slo-adoption-course/slides/promo_slo_adoption_gpt_image2_sources/slide_*.png`
- `courses/aws-slo-adoption-course/slides/promo_slo_adoption/slide_*.png`
- `courses/aws-slo-adoption-course/audio/promo_slo_adoption/slide_*.wav`
- `courses/aws-slo-adoption-course/video/promo_slo_adoption/promo_slo_adoption.mp4`
- Google Drive review upload
- QA reports

# Quality Gate
Definition of Done:
- 表示文字もGPT-Image2で生成している
- ローカル文字合成したスライドPNGを完成動画に使っていない
- 旧タイトル `AWS SRE入門` を表示しない
- 旧訴求 `SLO導入とCloudFormationハンズオン` を主タイトルとして表示しない
- VOICEVOX音声とスライド数が一致している
- MP4 faststart true、decode check OK
- Google Drive upload and anyone-reader sharing verified
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- `docs/GPT_IMAGE_RULES.md` と `docs/VIDEO_QUALITY_BASELINE.md` に従う

# Blocking
Blocked By:
- none
Notes:
- GitHub Issue: #159 https://github.com/toma1110/udemy2/issues/159
- Existing promo MP4 is not modified in place; the regenerated version is output under `promo_slo_adoption`.
- Drive URL: https://drive.google.com/file/d/12lIPKIb8RnDzZqzQQPuIb4FMw9JqLVZG/view?usp=drivesdk
- QA reports:
  - `qa/promo_slo_adoption_slide_generation_report.md`
  - `qa/promo_slo_adoption_video_build_report.md`
  - `qa/promo_slo_adoption_drive_upload_report.md`
