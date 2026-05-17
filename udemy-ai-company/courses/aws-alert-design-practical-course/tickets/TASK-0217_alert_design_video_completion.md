# Task Summary

Task ID: `TASK-0217`
Title: Alert Design実践コースの未作成動画を完了しUdemy成立尺へ是正する
GitHub Issue: #191

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

## Inputs

Input Files:
- `course_spec.md`
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
- completed scripts, GPT-Image2 slides, VOICEVOX audio, and MP4s after CEO approval
- updated course-level QA report

## Quality Gate

Definition of Done:
- CEO approved `course_spec.md` and `course_infomation.md` before video generation starts
- final course has at least 5 lectures and at least 30 minutes of lecture video content
- all spec lectures have MP4s
- alert design examples remain operationally sound
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
- CEO priority decision
- CEO approval of updated `course_spec.md` and `course_infomation.md` before video generation

Notes:
- Current audit: 6 spec lectures, 1 lecture MP4, about 3.1 minutes total. Missing `s1-l2`, `s2-l1`, `s2-l2`, `s3-l1`, and `s3-l2`.
