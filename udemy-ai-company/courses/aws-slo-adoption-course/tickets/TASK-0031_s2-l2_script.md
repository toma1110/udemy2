# Task Summary
Task ID: TASK-0031
Title: aws-slo-adoption-course Section 2 Lecture 2 の台本を作成する

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
- TASK-0025 reviewed

# Deliverables
Expected Output:
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s2-l2_script.md
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s2-l2_script_review_report.md

# Quality Gate
Definition of Done:
- `lectures.md` の Section 2 Lecture 2「エラーバジェットは何を決めるための数字か」に沿っている
- エラーバジェットを「信頼性をどこまで使えるかを判断する余白」として説明している
- リリース判断、改善優先度、障害対応の判断材料として使う流れを説明している
- バーンレートの詳細はSection 6へ譲り、ここでは関係性の導入に留めている
- ナレーション本文はVOICEVOX向けに読みやすい日本語である
- `python3 tools/narration_checker.py courses/aws-slo-adoption-course/scripts/s2-l2_script.md --warnings-ok` が成功する
- 1スライド1メッセージで、8〜10枚前後の構成になっている。枚数を変える場合はQA Notesに理由を残す

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- ナレーション本文に英字略語を残さない
- 計算式だけに偏らず、意思決定で使う意味を説明する

# Blocking
Blocked By: TASK-0024, TASK-0025
Notes:
