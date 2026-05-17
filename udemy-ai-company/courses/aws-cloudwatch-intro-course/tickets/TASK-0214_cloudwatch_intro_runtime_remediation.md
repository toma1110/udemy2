# Task Summary

Task ID: `TASK-0214`
Title: CloudWatch入門コースを30分以上のUdemy成立尺へ是正する
GitHub Issue: #188

## Ownership

Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

## Execution

Priority: high
Status: Done
Auto Execute: completed after CEO requested video production and Drive upload
Requires CEO Approval: satisfied by CEO request on 2026-05-17
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
- updated `course_spec.md` with 30.12 minutes actual lecture video runtime
- updated `course_infomation.md`
- revised scripts, VOICEVOX audio, MP4s, and Drive metadata after CEO approval
- updated course-level QA and Drive upload reports

## Quality Gate

Definition of Done:
- CEO requested CloudWatch Intro video production and Drive upload on 2026-05-17
- final course has at least 5 lectures and at least 30 minutes of lecture video content
- promo video is not counted toward the 30-minute requirement
- CloudWatch overview, metrics, logs, alarms, and dashboard positioning remain accurate
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
- Previous audit: 6 lecture MP4s, about 12.3 minutes total.
- Completed 2026-05-17: 6 lecture MP4s, 30.12 minutes total, uploaded to Google Drive.
- QA report: `qa/TASK-0214_runtime_remediation_qa_report.md`
