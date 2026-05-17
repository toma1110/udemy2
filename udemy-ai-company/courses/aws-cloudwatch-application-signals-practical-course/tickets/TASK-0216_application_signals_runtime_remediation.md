# Task Summary

Task ID: `TASK-0216`
Title: Application Signals実践コースを30分以上のUdemy成立尺へ是正する
GitHub Issue: #190

## Ownership

Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

## Execution

Priority: high
Status: Done
Auto Execute: completed after CEO request
Requires CEO Approval: satisfied on 2026-05-17 before video generation and Drive upload
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
- regenerated 11 normal lecture MP4s totaling 34.16 minutes
- uploaded 11 remediated lecture MP4s to Google Drive

## Quality Gate

Definition of Done:
- CEO approved `course_spec.md` and `course_infomation.md` before video regeneration starts
- final course has at least 5 lectures and at least 30 minutes of lecture video content
- promo video is not counted toward the 30-minute requirement
- Application Signals, SLO, service map, and CloudWatch positioning remain accurate
- GPT-Image2 and VOICEVOX production rules are preserved
- all MP4s pass faststart and decode checks
- Worker != Reviewer

## Constraints

Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth
- video generation requires CEO approval of `course_spec.md` and `course_infomation.md` first
- AWS and Google Drive mutations require separate CEO approval

## Blocking

Blocked By:
- None

Notes:
- CEO requested Application Signals video creation through Drive upload on 2026-05-17.
- Regenerated 11 normal lecture MP4s with GPT-Image2-derived slides and VOICEVOX audio.
- Final local lecture runtime: 2049.580 seconds, about 34.16 minutes.
- Uploaded 11 normal lecture MP4s to Google Drive with anyone-reader sharing.
- No AWS CloudFormation create/update/delete/full, Application Signals activation, or AWS resource mutation was performed in this ticket.
