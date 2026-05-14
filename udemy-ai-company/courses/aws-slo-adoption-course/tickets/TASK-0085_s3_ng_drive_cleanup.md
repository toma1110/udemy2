# Task Summary
Task ID: TASK-0085
Title: aws-slo-adoption-course Section 3 NG動画をGoogle Driveから削除し、Drive削除ルールを整備する

# Ownership
Department: ops
Owner AI: AI-Ops-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Done

# Inputs
Input Files:
- GitHub Issue #77 CEO comment
- udemy-ai-company/courses/aws-slo-adoption-course/qa/section3_completion_report.md
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s3-l*_drive_upload_report.md
Dependencies:
- TASK-0083 done

# Deliverables
Expected Output:
- Google Drive NG動画5本をtrashへ移動
- Drive cleanup QA report
- Google Drive削除ルール
- Issue #77 response comment

# Quality Gate
Definition of Done:
- 削除対象Drive file IDが明確である
- NG版だけが削除対象になっている
- `trashed=true` をDrive APIで確認している
- ルールが `docs/GOOGLE_DRIVE_RULES.md` に記録されている
- Issue #77に結果をコメントしている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- 同名検索だけで削除しない
- 原則trash移動とし、完全削除はCEO明示時のみ実行する

# Blocking
Blocked By:
Notes:

- 2026-05-11 CEOからNG動画削除とルール化の依頼あり。
- 2026-05-11 NG版S3動画5本をGoogle Drive trashへ移動し、`trashed=true` を確認。
- Google Drive削除ルールを `docs/GOOGLE_DRIVE_RULES.md` に追加。
- Cleanup report: `qa/s3_ng_drive_cleanup_report.md`
