# Task Summary
Task ID: TASK-0092
Title: AWS Batch Fargateで生成したs3-l5動画をGoogle Driveへアップロードする

# Ownership
Department: ops
Owner AI: AI-Ops-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Done

# Inputs
Input Files:
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s3-l5_batch_fargate_render_report.md
- s3://udemy-render-batch-dev-renderartifactbucket-jw3jlecsukqc/aws-slo-adoption-course/s3-l5/output/s3-l5.mp4
Dependencies:
- TASK-0079 done

# Deliverables
Expected Output:
- Google Drive URL for `s3-l5-batch-fargate-20260511.mp4`
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s3-l5_batch_fargate_drive_upload_report.md

# Quality Gate
Definition of Done:
- AWS Batch Fargateで生成したMP4をGoogle Driveへアップロードしている
- 既存の正式 `s3-l5.mp4` と混同しないファイル名にしている
- Drive file IDとURLを記録している
- Drive metadataでsize、mimeType、trashedを確認している
- `anyone reader` の共有設定を確認している
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- チケットなし作業は禁止
- 既存の正式Drive動画は削除・更新しない

# Blocking
Blocked By:
Notes:
- 比較確認用のBatch生成動画として `s3-l5-batch-fargate-20260511.mp4` の名前でアップロードする。
