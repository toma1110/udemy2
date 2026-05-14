# Task Summary
Task ID: TASK-0077
Title: aws-slo-adoption-course Section 3 のCEO音声スポット聴取と最終承認を行う

# Ownership
Department: qa
Owner AI: AI-QA-01
Reviewer AI: AI-Strategy-01

# Execution
Priority: high
Status: Ready

# Inputs
Input Files:
- udemy-ai-company/courses/aws-slo-adoption-course/qa/section3_completion_report.md
- Google Drive videos
Dependencies:
- TASK-0076 done

# Deliverables
Expected Output:
- CEO approval note

# Quality Gate
Definition of Done:
- CEOがSection 3動画をスポット確認できる
- 問題があればchange requestとして起票する
- 問題がなければSection 4制作へ進める

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- チケットなし作業は禁止
- ナレーション本文に英字略語を残さない

# Blocking
Blocked By:
Notes:
- 2026-05-10 ユーザーから「s3も作成開始してください！」と制作開始承認済み。

- 2026-05-10 Issue #77 CEOコメントに基づき、S3をS2相当の文字入りスライドへ修正。修正版URLをIssue #77へコメント済み。再確認待ち。

- 2026-05-11 TASK-0084でS3-L1〜S3-L5をGPT-Image2再生成版へ差し替え、Google Driveアップロードまで完了。新URLは `qa/section3_completion_report.md` を参照。CEOスポット確認待ち。
