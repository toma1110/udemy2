# Task Summary

Task ID: `TASK-0175`
Title: AWS課金事故防止入門 VOICEVOX音声・動画生成・Driveアップロード

## Ownership

Department: Production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

## Execution

Priority: high
Status: Backlog
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none

## Inputs

Input Files:
- `course_spec.md`
- `scripts/`
- `slides/`
- `udemy-ai-company/docs/VOICEVOX_RULES.md`
- `udemy-ai-company/docs/GPT_IMAGE_RULES.md`

Dependencies:
- `TASK-0174`

## Deliverables

Expected Output:
- VOICEVOX WAV files
- audio generation reports
- MP4 files
- video build reports
- Google Drive upload reports

## Quality Gate

Definition of Done:
- 音声はVOICEVOX
- 動画はGPT-Image2由来PNGのみ
- スライド順、音声順、台本が一致
- Drive URLがQAに記録されている
- Worker and Reviewer are different

## Constraints

Rules:
- course_spec is source of truth
- Google Drive一括アップロード方式を使う

## Blocking

Blocked By:
- TASK-0174
