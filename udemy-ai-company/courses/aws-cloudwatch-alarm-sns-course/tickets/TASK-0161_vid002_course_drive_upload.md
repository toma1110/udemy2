# Task Summary

Task ID: `TASK-0161`
Title: VID-002 course Google Drive upload

## Ownership

Department: Ops
Owner AI: AI-Ops-01
Reviewer AI: AI-QA-01

## Execution

Priority: high
Status: Done

## Inputs

Input Files:
- `video/*/*.mp4`
- `qa/*video_build_report.md`

Dependencies:
- `TASK-0160`

## Deliverables

Expected Output:
- Drive upload reports
- Drive metadata JSON

## Quality Gate

Definition of Done:
- All final MP4 files are uploaded
- Drive URLs are recorded
- Sharing is set to reviewer-accessible
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
- Existing `s1-l1` final uploaded asset can be reused and referenced.
- 追加5本をGoogle Driveへアップロード済み。
- 既存`s1-l1` pronunciation-fix版を講座1本目として参照。
