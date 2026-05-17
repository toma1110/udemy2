# Task Summary

Task ID: `TASK-0194`
Title: Application Signals実践コースのプロモーション動画を作成する

## Ownership

Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

## Execution

Priority: high
Status: Review
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none

## Inputs

Input Files:
- `courses/aws-cloudwatch-application-signals-practical-course/course_spec.md`
- `courses/aws-cloudwatch-application-signals-practical-course/course_infomation.md`
- `courses/aws-cloudwatch-application-signals-practical-course/course_curriculum.md`
- `courses/aws-cloudwatch-application-signals-practical-course/scripts/promo_video_script.md`
- `courses/aws-cloudwatch-application-signals-practical-course/scripts/promo_video_script.json`
- `courses/aws-cloudwatch-application-signals-practical-course/slides/promo_aws-cloudwatch-application-signals-practical-course_gpt_image2_prompts.md`
- `docs/PROMOTION_VIDEO_RULES.md`
- `docs/GPT_IMAGE_RULES.md`
- `docs/VIDEO_QUALITY_BASELINE.md`
- `templates/promo_video_qa_report_template.md`

Dependencies:
- `TASK-0191`
- `TASK-0192`

## Deliverables

Expected Output:
- `slides/promo_aws-cloudwatch-application-signals-practical-course_gpt_image2_sources/`
- `slides/promo_aws-cloudwatch-application-signals-practical-course/`
- `audio/promo_aws-cloudwatch-application-signals-practical-course/`
- `video/promo_aws-cloudwatch-application-signals-practical-course/promo_aws-cloudwatch-application-signals-practical-course.mp4`
- `qa/promo_aws-cloudwatch-application-signals-practical-course_*_report.md`
- Google Drive review upload

## Quality Gate

Definition of Done:
- 通常レクチャー `s1-l1` を代用していない
- 表示文字もGPT-Image2で生成している
- ローカル文字合成したスライドPNGを完成動画に使っていない
- AWSリソース作成なしで制作する
- Application Signalsの料金注意を弱めていない
- VOICEVOX音声とスライド数が一致している
- MP4 faststart true、decode check OK
- Drive URL and anyone-reader sharing verified
- Worker != Reviewer

## Constraints

Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth
- `docs/PROMOTION_VIDEO_RULES.md` に従う

## Blocking

Blocked By:
- GPT-Image2 slide generation
- VOICEVOX audio generation

Notes:
- AWS stack create/update/deleteはこのチケットでは実行しない。
- 2026-05-16: `promo_video_script.md`、`promo_video_script.json`、GPT-Image2プロンプトを作成済み。
- 2026-05-16: `tools/narration_checker.py` でナレーションチェック済み。
- 2026-05-16: GPT-Image2由来スライド、VOICEVOX音声、MP4生成、decode check、faststart確認、Google Driveレビュー用アップロードを完了。
- Google Drive URL: https://drive.google.com/file/d/1dfogS6mt5sBoKs7G4Ax6P0KrScK4cMhs/view?usp=drivesdk
- QA詳細: `qa/course_video_production_report.md` と `qa/course_drive_upload_report.md` を参照。
- Reviewer AIによる最終QAは未実施。
