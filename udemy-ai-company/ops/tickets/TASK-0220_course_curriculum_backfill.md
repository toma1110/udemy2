# TASK-0220: course_curriculum.md backfill and runtime gate alignment

## Task Summary

- Task ID: `TASK-0220`
- Title: `course_curriculum.md backfill and runtime gate alignment`
- GitHub Issue: `#194`

## Ownership

- Department: `production`
- Owner AI: `AI-Production-01`
- Reviewer AI: `AI-QA-01`

## Execution

- Priority: `high`
- Status: `ready for review`

## Inputs

- `udemy-ai-company/courses/*/course_spec.md`
- `udemy-ai-company/courses/*/course_infomation.md`
- `udemy-ai-company/ops/course_video_inventory_audit_20260517.md`

## Deliverables

- Existing `course_curriculum.md` files updated to reflect current video audit state, target lecture runtime, CEO approval gate, GPT-Image2, VOICEVOX, and Worker/Reviewer separation.
- Missing `course_curriculum.md` files added for production course directories.
- Sample course curriculum added as a scaffold-only reference.

## Quality Gate

- Every course directory with `course_spec.md` also has `course_curriculum.md`.
- `course_curriculum.md` keeps `course_spec.md` as Source of Truth.
- Runtime-short courses do not keep `Produced` as the only status; regeneration or missing production status is explicit.
- Video generation is blocked until CEO approval of `course_spec.md`, `course_infomation.md`, and `course_curriculum.md`.
- CloudFormation or AWS execution remains gated by CEO approval.
- Worker AI and Reviewer AI are different.

## Constraints

- Planner != Worker
- Worker != Reviewer
- `course_spec.md` is Source of Truth
- Completed video slides must be GPT-Image2-derived PNGs
- Audio generation uses VOICEVOX

## Blocking

- Blocked By: CEO review of updated curriculum files before video generation
- Notes: This task updates planning documents only. It does not generate videos or execute AWS operations.
