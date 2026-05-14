# Task Summary
Task ID: TASK-0025
Title: aws-slo-adoption-course Section 2 Lecture 1 の台本を作成する

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

# Deliverables
Expected Output:
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s2-l1_script.md
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s2-l1_script_review_report.md

# Quality Gate
Definition of Done:
- `lectures.md` の Section 2 Lecture 1「SLI、SLO、SLAを一枚で理解する」に沿っている
- SLIは「何を測るか」、SLOは「どの水準を目指すか」、SLAは「外部への約束」として明確に区別している
- エラーバジェットとの関係を導入し、詳細説明はS2-L2へ自然につないでいる
- 旧素材をそのままコピーせず、現行 `course_spec.md` に合わせて再編集している
- ナレーション本文はVOICEVOX向けに「エスエルアイ」「エスエルオー」「エスエルエー」と読める表記にしている
- `python3 tools/narration_checker.py courses/aws-slo-adoption-course/scripts/s2-l1_script.md --warnings-ok` が成功する
- 1スライド1メッセージで、8〜10枚前後の構成になっている。枚数を変える場合はQA Notesに理由を残す

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- ナレーション本文に英字略語を残さない
- 表示テキストと読み上げ本文を混同しない

# Blocking
Blocked By:
Notes:
- Section 2の最初の講義なので、概念の正確さと聞きやすさを優先する。
- 2026-05-10 TASK-0024 CEO承認済み。
