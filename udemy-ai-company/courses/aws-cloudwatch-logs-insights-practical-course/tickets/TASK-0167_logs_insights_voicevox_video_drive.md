# Task Summary

Task ID: `TASK-0167`
Title: Logs Insights実践コース音声・動画・Driveアップロード

## Ownership

Department: Production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

## Execution

Priority: high
Status: Done

## Inputs

Input Files:
- `scripts/*_script.json`
- `slides/<lecture>/slide_*.png`

Dependencies:
- `TASK-0166`

## Deliverables

Expected Output:
- VOICEVOX WAV
- MP4 videos
- Google Drive metadata
- Drive upload reports

## Quality Gate

Definition of Done:
- 音声数とスライド数が一致する
- MP4が再生可能
- Faststartが付与されている
- Drive URLが記録されている
- Worker and Reviewer are different

## Constraints

Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth

## Blocking

Blocked By:
- None

Notes:
- 2026-05-15: VOICEVOX WAV 48本、MP4 8本、Drive metadata 8件を作成済み。
- AWSリソース作成は不要。動画制作とDrive uploadは通常制作作業。
