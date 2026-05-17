# Task Summary

Task ID: `TASK-0215`
Title: CloudWatch Alarm/SNSコースを30分以上のUdemy成立尺へ是正する
GitHub Issue: #189

## Ownership

Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

## Execution

Priority: high
Status: Done
Auto Execute: completed for video generation and Google Drive upload after CEO requests on 2026-05-17
Requires CEO Approval: satisfied for video generation and Google Drive upload
Cost Impact: non-AWS content generation only

## Inputs

Input Files:
- `course_spec.md`
- `course_curriculum.md`
- `course_infomation.md`
- `scripts/*`
- `qa/*`
- `udemy-ai-company/ops/course_video_inventory_audit_20260517.md`

Dependencies:
- `TASK-0212` existing course video inventory audit
- CEO priority decision

## Deliverables

Expected Output:
- updated `course_spec.md` with at least 30 minutes planned lecture video runtime
- updated `course_infomation.md`
- revised scripts, GPT-Image2 slides, VOICEVOX audio, and MP4s after CEO approval
- updated course-level QA report
- Google Drive upload metadata and report

## Quality Gate

Definition of Done:
- CEO approved video regeneration by explicit request on 2026-05-17
- final course has 6 lectures and 2115.726 seconds / 35.26 minutes of lecture video content
- promo video is not counted toward the 30-minute requirement
- CloudWatch Alarm, SNS, threshold design, and cost warnings remain accurate
- GPT-Image2 and VOICEVOX production rules are preserved
- all MP4s pass faststart and decode checks
- Google Drive upload completed for all 6 MP4s
- Worker != Reviewer

## Constraints

Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth
- video generation was approved by CEO request on 2026-05-17
- AWS mutations require separate CEO approval
- Google Drive upload was approved by CEO request on 2026-05-17

## Blocking

Blocked By:
- None

Notes:
- Previous audit: 6 lecture MP4s, about 13.3 minutes total.
- Current production result: 6 lecture MP4s, 2115.726 seconds / 35.26 minutes total.
- Google Drive upload completed on 2026-05-17. URLs are recorded in `qa/course_drive_upload_report.md`.
