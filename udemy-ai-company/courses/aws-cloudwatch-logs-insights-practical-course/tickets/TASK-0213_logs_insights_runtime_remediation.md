# Task Summary

Task ID: `TASK-0213`
Title: Logs Insights実践コースを30分以上のUdemy成立尺へ是正する
GitHub Issue: #187

## Ownership

Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

## Execution

Priority: high
Status: Blocked
Auto Execute: spec/course info drafting only; pause before video generation
Requires CEO Approval: yes, before video generation
Cost Impact: non-AWS content generation only

## Inputs

Input Files:
- `course_spec.md`
- `course_curriculum.md`
- `course_infomation.md`
- `scripts/*_script.md`
- `scripts/*_script.json`
- `qa/audio_video_build_report.md`
- `udemy-ai-company/ops/course_video_inventory_audit_20260517.md`

Dependencies:
- `TASK-0212` existing course video inventory audit
- CEO priority decision against current production queue

## Deliverables

Expected Output:
- updated `course_spec.md` with a planned runtime of at least 30 minutes
- updated `course_infomation.md` reflecting final lecture count and runtime
- updated `course_curriculum.md` if lecture structure changes
- revised scripts for all affected lectures after CEO approval
- regenerated GPT-Image2 slide PNGs where script changes require visual changes
- regenerated VOICEVOX audio and MP4s for all affected lectures after CEO approval
- updated QA and drive-upload follow-up plan

## Quality Gate

Definition of Done:
- CEO approved `course_spec.md` and `course_infomation.md` before video regeneration starts
- final course has at least 5 lectures and at least 30 minutes of lecture video content
- promo video is not counted toward the 30-minute requirement
- Logs Insights query explanations remain technically accurate
- no AWS Logs Insights query execution or Google Drive mutation is performed in this ticket unless separately approved
- GPT-Image2 source evidence is preserved for final slides
- VOICEVOX narration checker passes before audio generation
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
- CEO approval of updated `course_spec.md` and `course_infomation.md` before video regeneration

Notes:
- Current audit: 8 lecture MP4s, about 11.7 minutes total. The course needs roughly 18.3 additional lecture minutes or equivalent approved restructuring.
