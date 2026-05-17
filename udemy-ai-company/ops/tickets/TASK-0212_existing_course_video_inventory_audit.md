# Task Summary

Task ID: `TASK-0212`
Title: 既存コースのUdemy公開最小ライン動画数・尺監査
GitHub Issue: #186

## Ownership

Department: ops / production
Owner AI: AI-Ops-01
Reviewer AI: AI-QA-01

## Execution

Priority: high
Status: Review
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none

## Inputs

Input Files:
- `udemy-ai-company/courses/*/course_spec.md`
- `udemy-ai-company/courses/*/course_infomation.md`
- `udemy-ai-company/courses/*/video/**/*.mp4`
- Udemy Course Quality Checklist

Dependencies:
- CEO request on 2026-05-17: Logs Insights and existing courses may not meet Udemy course video requirements

## Deliverables

Expected Output:
- `udemy-ai-company/ops/course_video_inventory_audit_20260517.md`
- course-level remediation tickets for courses below Udemy minimum video requirements

## Quality Gate

Definition of Done:
- Promo videos and segment files are excluded from lecture video counts
- Normal lecture MP4 duration is measured with `ffprobe`
- Each course is classified against at least 5 lectures and at least 30 minutes of video content
- Logs Insights course is explicitly checked
- Remediation tickets preserve CEO review before any video generation
- Worker != Reviewer

## Constraints

Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth
- No video, audio, slide, AWS, or Google Drive mutation in this audit
- Remediation video generation requires CEO approval of `course_spec.md` and `course_infomation.md`

## Blocking

Blocked By:
- None

Notes:
- 2026-05-17: Audit found several existing courses have enough lecture count but less than 30 minutes of video content.
