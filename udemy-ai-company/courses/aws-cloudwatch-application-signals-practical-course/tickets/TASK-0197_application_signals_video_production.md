# Task Summary

Task ID: `TASK-0197`
Title: Application Signals実践コースの全レクチャー動画を作成してDriveへ配置する

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
- `course_spec.md`
- `course_curriculum.md`
- `scripts/*_script.json`
- `slides/*_gpt_image2_prompts.md`
- `cloudformation/docs/VALIDATION.md`
- `docs/GPT_IMAGE_RULES.md`
- `docs/VIDEO_QUALITY_BASELINE.md`
- `docs/GOOGLE_DRIVE_RULES.md`

Dependencies:
- `TASK-0194`
- `TASK-0195`
- `TASK-0196`

## Deliverables

Expected Output:
- プロモーション動画 1本
- 通常レクチャー動画 11本
- GPT-Image2由来ソースPNG 71枚
- 完成動画用PNG 71枚
- VOICEVOX音声 71本
- 各動画の `build_report.json`
- 各動画の `drive_upload.json`
- `qa/course_video_production_report.md`
- `qa/course_drive_upload_report.md`

## Quality Gate

Definition of Done:
- 表示文字を含む完成スライドはGPT-Image2由来PNGである
- ローカル文字合成したスライドPNGを完成動画に使っていない
- VOICEVOX音声とスライド数が一致している
- 全MP4がdecode check OK
- 全MP4がfaststart true
- 全MP4に2秒のtail padを入れている
- Google Drive review upload and anyone-reader sharing verified
- CloudFormation template validation OK
- Worker != Reviewer

## Constraints

Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth
- Google DriveアップロードはCEO/QAレビュー用であり、Udemy公開作業ではない

## Blocking

Blocked By:
- none

Notes:
- 2026-05-16: プロモーション動画1本、通常レクチャー11本を生成済み。
- 2026-05-16: `ffmpeg -v error` による全MP4 decode check OK。
- 2026-05-16: Google Driveレビュー用アップロード完了。全ファイルでanyone-reader共有を確認済み。
- Reviewer AIによる最終QAは未実施。
