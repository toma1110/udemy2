# Task Summary
Task ID: TASK-0037
Title: aws-slo-adoption-course Section 2 Lecture 3 の台本を作成する

# Ownership
Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Done

# Inputs
Input Files:
- udemy-ai-company/courses/aws-slo-adoption-course/course_spec.md
- udemy-ai-company/courses/aws-slo-adoption-course/lectures.md
- udemy-ai-company/courses/aws-slo-adoption-course/asset_migration_plan.md
- udemy-ai-company/docs/STYLE_GUIDE.md
- udemy-ai-company/docs/VOICEVOX_RULES.md
- /home/ubuntu/workspace/udemy/courses/sre-slo-introduction/lectures.json
- /home/ubuntu/workspace/udemy/courses/aws-sre-practical/s6-l1/script.json
Dependencies:
- TASK-0024 approved
- TASK-0031 reviewed

# Deliverables
Expected Output:
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s2-l3_script.md
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s2-l3_script_review_report.md

# Quality Gate
Definition of Done:
- `lectures.md` の Section 2 Lecture 3「SLO導入前に確認する現場の前提条件」に沿っている
- ユーザー体験、サービス責任者、メトリクス有無、障害対応、リリース判断の前提を整理している
- Section 3の「ユーザー体験からSLIを選ぶ」へ自然につながる
- ワーク形式として、受講者が自分のサービスに当てはめられる確認観点を含めている
- ナレーション本文はVOICEVOX向けに読みやすい日本語である
- `python3 tools/narration_checker.py courses/aws-slo-adoption-course/scripts/s2-l3_script.md --warnings-ok` が成功する
- 1スライド1メッセージで、8〜10枚前後の構成になっている。枚数を変える場合はQA Notesに理由を残す

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- ナレーション本文に英字略語を残さない
- 組織導入の詳細をSection 8より先に説明しすぎない

# Blocking
Blocked By: TASK-0024, TASK-0031
Notes:
