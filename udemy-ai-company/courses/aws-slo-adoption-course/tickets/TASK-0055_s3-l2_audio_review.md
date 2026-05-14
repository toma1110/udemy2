# Task Summary
Task ID: TASK-0055
Title: aws-slo-adoption-course Section 3 Lecture 2 の音声聴取QAと読み修正を行う

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
- udemy-ai-company/docs/STYLE_GUIDE.md
- udemy-ai-company/docs/VOICEVOX_RULES.md
Dependencies:
- TASK-0054 done

# Deliverables
Expected Output:
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s3-l2_audio_review_report.md

# Quality Gate
Definition of Done:
- WorkerとReviewerが分離されている
- 英字略語、誤読、長すぎる文を確認している
- 修正が必要な場合は台本へ戻して再生成する
- 最終的に動画生成へ進める状態である

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
