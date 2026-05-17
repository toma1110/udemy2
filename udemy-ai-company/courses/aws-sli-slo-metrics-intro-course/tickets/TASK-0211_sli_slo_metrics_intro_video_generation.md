# Task Summary

Task ID: `TASK-0211`
Title: SLI/SLOをAWSメトリクスに落とす短尺入門をUdemy成立コースとして最後まで動画生成する
GitHub Issue: #184

## Course Completion Scope

このチケットは、1本の短尺動画ではなく、Udemyコースとして成立する最小構成まで `course_spec.md` を拡張し、最後のレクチャーまで全動画を生成するチケットである。

作業開始時に、現行の1レクチャーspecを最低5レクチャー、合計30分以上のUdemy公開可能な構成へ拡張する。動画作成開始前に、拡張後の `course_spec.md` と `course_infomation.md` をCEO確認へ出し、承認後に `course_spec.md` と `course_curriculum.md` をSource of Truthとして、全レクチャーの台本、GPT-Image2スライド、VOICEVOX音声、MP4を一括生成する。

## Pre-Video CEO Review Gate

- AI-Production-01は、先に `course_spec.md`、`course_curriculum.md`、`course_infomation.md` を更新する
- 台本、GPT-Image2スライド、VOICEVOX音声、MP4生成はCEOが `course_spec.md` と `course_infomation.md` を確認・承認するまで開始しない
- CEO承認後は、このコース内の全レクチャー動画を一括生成してよい
- 承認前に作成してよい成果物は、コース設計、カリキュラム、販売ページ情報、制作計画までとする

## Ownership

Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

## Execution

Priority: medium
Status: Blocked
Auto Execute: spec/course info drafting only; pause before video generation
Requires CEO Approval: yes, before video generation
Cost Impact: non-AWS content generation only
Production Order: 5 of 5

## Inputs

Input Files:
- `udemy-ai-company/courses/aws-sli-slo-metrics-intro-course/course_spec.md`
- `udemy-ai-company/courses/aws-sli-slo-metrics-intro-course/handson/aws_metric_sli_mapping.md`
- `udemy-ai-company/courses/aws-sli-slo-metrics-intro-course/handson/positioning_review_against_slo_course.md`
- `udemy-ai-company/courses/aws-sli-slo-metrics-intro-course/scripts/s1-l1_script_plan.md`
- `udemy-ai-company/courses/aws-sli-slo-metrics-intro-course/slides/s1-l1_gpt_image2_prompts.md`
- `udemy-ai-company/courses/aws-sli-slo-metrics-intro-course/video/s1-l1_video_spec.md`
- `udemy-ai-company/docs/GPT_IMAGE_RULES.md`
- `udemy-ai-company/docs/VOICEVOX_RULES.md`
- `udemy-ai-company/docs/VIDEO_QUALITY_BASELINE.md`

Dependencies:
- `TASK-0204` course/video spec completed
- `TASK-0210` full course video generation and production QA completed

## Deliverables

Expected Output:
- `course_spec.md` updated to at least 5 lectures and at least 30 minutes planned runtime
- `course_curriculum.md`
- `course_infomation.md`
- `scripts/<lecture_id>_*.md`
- `scripts/<lecture_id>_*.json`
- `slides/<section>-gpt-image2-sources/<lecture_id>/slide_*.png`
- `slides/<lecture_id>-final/slide_*.png`
- `audio/<lecture_id>/slide_*.wav`
- `audio/<lecture_id>/voicevox_report.md`
- `video/<lecture_id>/<lecture_id>.mp4` for every lecture in the expanded course spec
- `video/<lecture_id>/build_report.json`
- `video/<lecture_id>/frame_check_*.png`
- `qa/<lecture_id>_slide_generation_report.md`
- `qa/<lecture_id>_voicevox_generation_report.md`
- `qa/<lecture_id>_video_build_report.md`
- `qa/course_video_completion_report.md`

## Quality Gate

Definition of Done:
- `course_spec.md` がUdemy公開最小ラインの5レクチャー以上、合計30分以上の動画構成になっている
- 動画作成前にCEOが `course_spec.md` と `course_infomation.md` を確認・承認している
- 全レクチャーの完成台本が `course_spec.md` とAWSメトリクスSLIマッピングに整合している
- 全レクチャーのMP4が生成されている
- 既存SLO実践コースの代替ではなく入口動画として成立している
- ALB/API Gateway/Lambda/RDSのメトリクス候補が正確
- 内部指標をユーザー体験SLIとして誤説明していない
- 実AWS/CloudWatch/Application Signals/CloudFormation操作を行っていない
- 完成動画スライドはGPT-Image2由来PNGのみを使用している
- GPT-Image2 source evidenceと最終PNGの対応が残っている
- VOICEVOXナレーションチェックが通過している
- 全MP4がfaststart true、decode check OK、末尾無音余白あり
- `qa/course_video_completion_report.md` でコース全体QAがPASSしている
- Worker != Reviewer

Mission/Vision/Values Alignment:
- SLO実践コースへ自然に接続する短尺入口教材を作る

## Constraints

Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth
- follow docs/MISSION_VISION_VALUES.md
- follow docs/GPT_IMAGE_RULES.md
- follow docs/VOICEVOX_RULES.md
- AWS execution requires CEO approval if any demo is added
- video generation requires CEO approval of `course_spec.md` and `course_infomation.md` first

## Blocking

Blocked By:
- `TASK-0210` completion QA

Notes:
- Scope is full course video generation through the final lecture. Google Drive upload is a separate future ticket.
- Real AWS/Application Signals setup remains out of scope.
- Before video generation starts, stop at `course_spec.md` and `course_infomation.md` CEO review.
- Sequential production policy: start this only after the GitHub Actions OIDC full course video package is complete and QA-passed.
