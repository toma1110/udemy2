# Task Summary
Task ID: TASK-0021
Title: aws-slo-adoption-course Section 1 Lecture 3 の完成動画をGoogle Driveへアップロードする

# Ownership
Department: ops
Owner AI: AI-Ops-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Blocked

# Inputs
Input Files:
- udemy-ai-company/courses/aws-slo-adoption-course/video/s1-l3/s1-l3.mp4
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s1-l3_video_build_report.md
Dependencies:
- TASK-0020 reviewed

# Deliverables
Expected Output:
- Google Drive URL for `s1-l3.mp4`
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s1-l3_drive_upload_report.md

# Quality Gate
Definition of Done:
- Google Driveへ `s1-l3.mp4` としてアップロードされている
- `--direct` 相当の運用で二重フォルダ化していない
- Drive上のMIME type、size、sharing、trashed状態を確認している
- Drive file が `trashed: false` である
- 共有リンクがIssueとQAレポートに記録されている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- CEO承認なしにPublished扱いにしない

# Blocking
Blocked By: TASK-0020
Notes:
