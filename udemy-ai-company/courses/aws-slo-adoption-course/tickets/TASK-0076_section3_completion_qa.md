# Task Summary
Task ID: TASK-0076
Title: aws-slo-adoption-course Section 3 の動画完了QAを行う

# Ownership
Department: qa
Owner AI: AI-QA-01
Reviewer AI: AI-Production-01

# Execution
Priority: high
Status: Done

# Inputs
Input Files:
- course_spec.md
- lectures.md
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s3-l*_*.md
Dependencies:
- TASK-0075 done

# Deliverables
Expected Output:
- udemy-ai-company/courses/aws-slo-adoption-course/qa/section3_completion_report.md

# Quality Gate
Definition of Done:
- Section 3の全講義動画が存在する
- 全講義の台本、スライド、音声、動画、Driveレポートがそろっている
- WorkerとReviewerの分離が守られている
- CEOスポット聴取に回せる状態である

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
