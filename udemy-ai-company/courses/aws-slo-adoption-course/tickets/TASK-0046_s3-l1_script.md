# Task Summary
Task ID: TASK-0046
Title: aws-slo-adoption-course Section 3 Lecture 1 の台本を作成する

# Ownership
Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

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
- TASK-0045 approved

# Deliverables
Expected Output:
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s3-l1_script.md
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s3-l1_script_review_report.md

# Quality Gate
Definition of Done:
- `lectures.md` の Section 3 Lecture 1「良いSLIの3条件」に沿っている
- 1スライド1メッセージで8〜10枚前後の構成になっている
- ナレーション本文はVOICEVOX向けに英字略語を残さない
- エスエルアイ、エスエルオー、エスエルエーの読みを統一する
- `narration_checker.py` が成功する

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
