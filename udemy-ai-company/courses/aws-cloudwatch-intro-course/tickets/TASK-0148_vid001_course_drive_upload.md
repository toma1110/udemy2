# Task Summary

Task ID: `TASK-0148`
Title: `VID-001拡張コース6本をGoogle Driveへアップロードする`

## Ownership

Department: Ops
Owner AI: `AI-Ops-01`
Reviewer AI: `AI-QA-01`

## Execution

Priority: high
Status: done

## Inputs

Input Files:

- `video/s1-l1/s1-l1.mp4`
- `video/s1-l2/s1-l2.mp4`
- `video/s1-l3/s1-l3.mp4`
- `video/s2-l1/s2-l1.mp4`
- `video/s2-l2/s2-l2.mp4`
- `video/s3-l1/s3-l1.mp4`

Dependencies:

- `TASK-0146`
- `TASK-0147`

## Deliverables

Expected Output:

- Google Drive review URL for all 6 lectures
- `video/<lecture>/drive_upload.json` for newly uploaded lectures
- `qa/*_drive_upload_report.md`
- `qa/vid001_drive_upload_summary.md`

## Quality Gate

Definition of Done:

- Upload succeeds
- File is not trashed
- Sharing includes `anyone reader`
- Drive URL is recorded in QA
- Worker and Reviewer are separated

## Constraints

Rules:

- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth
- Google Drive upload is for CEO/QA review, not Udemy publishing

## Blocking

Blocked By:
Notes:

- `s1-l1` was already uploaded as the GPT-Image2 version on 2026-05-14.
- `s1-l2` through `s3-l1` were uploaded on 2026-05-15.
