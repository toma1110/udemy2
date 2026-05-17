# Task Summary

Task ID: `TASK-0222`
Title: Logs Insights是正後MP4をGoogle Driveへアップロードする
GitHub Issue: #196

## Ownership

Department: ops
Owner AI: AI-Ops-01
Reviewer AI: AI-QA-01

## Execution

Priority: high
Status: Done
Auto Execute: yes, CEO requested Drive upload
Requires CEO Approval: satisfied on 2026-05-17
Cost Impact: Google Drive review upload only

## Inputs

Input Files:
- `video/s1-l1/s1-l1.mp4`
- `video/s1-l2/s1-l2.mp4`
- `video/s1-l3/s1-l3.mp4`
- `video/s2-l1/s2-l1.mp4`
- `video/s2-l2/s2-l2.mp4`
- `video/s2-l3/s2-l3.mp4`
- `video/s3-l1/s3-l1.mp4`
- `video/s3-l2/s3-l2.mp4`
- `qa/audio_video_build_report.md`
- `qa/TASK-0213_runtime_remediation_qa_report.md`

Dependencies:
- `TASK-0213` local video generation completed
- Google Drive credentials configured in the environment

## Deliverables

Expected Output:
- regenerated lecture MP4s uploaded to the configured Google Drive folder
- `qa/<lecture>_drive_metadata.json` updated for all 8 lectures
- `video/<lecture>/drive_upload.json` saved for all 8 lectures
- `qa/drive_upload_summary.md` updated with current Drive URLs
- GitHub Issue updated with Drive URLs

## Quality Gate

Definition of Done:
- all 8 remediated MP4s are uploaded
- each uploaded file has `anyone reader` permission
- Drive metadata includes file ID, size, webViewLink, and permissions
- local metadata paths are recorded
- `course_spec.md`, `course_infomation.md`, and QA reports no longer say the remediated upload is pending
- Worker != Reviewer

## Constraints

Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth
- Google Drive upload is for CEO/QA review, not Udemy publishing
- AWS Logs Insights query execution and AWS resource mutation are out of scope

## Blocking

Blocked By:
- None

Notes:
- Existing 2026-05-15 Drive uploads were short videos and are superseded by the `TASK-0222` uploads.
- Uploaded 8 runtime-remediated MP4 files on 2026-05-17.
- Anyone-reader sharing verified for all uploaded files.
- Drive URLs are recorded in `qa/drive_upload_summary.md`.
