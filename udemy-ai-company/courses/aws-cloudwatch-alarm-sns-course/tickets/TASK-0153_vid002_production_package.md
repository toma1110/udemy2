# Task Summary
Task ID: TASK-0153
Title: VID-002の台本、GPT-Image2プロンプト、VOICEVOX、動画を制作する

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
- `courses/aws-cloudwatch-alarm-sns-course/course_spec.md`
- `courses/aws-cloudwatch-alarm-sns-course/cloudformation/README.md`
- `courses/aws-cloudwatch-alarm-sns-course/cloudformation/template.yaml`
- `docs/GPT_IMAGE_RULES.md`
- `docs/VIDEO_QUALITY_BASELINE.md`
Dependencies:
- TASK-0152

# Deliverables
Expected Output:
- `courses/aws-cloudwatch-alarm-sns-course/scripts/s1-l1_script.md`
- `courses/aws-cloudwatch-alarm-sns-course/scripts/s1-l1_script.json`
- `courses/aws-cloudwatch-alarm-sns-course/slides/s1-l1_gpt_image_prompts.md`
- `courses/aws-cloudwatch-alarm-sns-course/slides/s1-gpt-image2-sources/s1-l1/slide_*.png`
- `courses/aws-cloudwatch-alarm-sns-course/slides/s1-l1/slide_*.png`
- `courses/aws-cloudwatch-alarm-sns-course/audio/s1-l1/slide_*.wav`
- `courses/aws-cloudwatch-alarm-sns-course/video/s1-l1/s1-l1.mp4`

# Quality Gate
Definition of Done:
- 表示文字もGPT-Image2で生成している
- ローカル文字合成したスライドPNGを完成動画に使っていない
- VID-001 baseline comparisonがPASS
- VOICEVOX音声とスライド数が一致している
- MP4 faststart true、decode check OK
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- `docs/GPT_IMAGE_RULES.md` と `docs/VIDEO_QUALITY_BASELINE.md` に従う
- チケットなし作業禁止

# Blocking
Blocked By:
- none
Notes:
- GitHub Issue: #153 https://github.com/toma1110/udemy2/issues/153
- Completed: script, GPT-Image2 source slides, GPT-Image2-derived final slides, VOICEVOX audio, and faststart MP4.
- QA reports:
  - `qa/s1-l1_slide_generation_report.md`
  - `qa/s1-l1_voicevox_generation_report.md`
  - `qa/s1-l1_audio_review_report.md`
  - `qa/s1-l1_video_build_report.md`
