# Task Summary
Task ID: TASK-0016
Title: aws-slo-adoption-course Section 1 Lecture 3 の台本を作成する

# Ownership
Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Ready

# Inputs
Input Files:
- udemy-ai-company/courses/aws-slo-adoption-course/course_spec.md
- udemy-ai-company/courses/aws-slo-adoption-course/lectures.md
- udemy-ai-company/courses/aws-slo-adoption-course/asset_migration_plan.md
- udemy-ai-company/docs/STYLE_GUIDE.md
- udemy-ai-company/docs/VOICEVOX_RULES.md
- /home/ubuntu/workspace/udemy/courses/sre-slo-introduction/s1-l3/input.json
Dependencies:
- TASK-0015 completed

# Deliverables
Expected Output:
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s1-l3_script.md
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s1-l3_script_review_report.md

# Quality Gate
Definition of Done:
- `course_spec.md` と `lectures.md` の Section 1 Lecture 3 に沿っている
- コース全体のロードマップとして、Section 2以降への期待値を正確に示している
- Application Signals、CloudFormation、バーンレート、組織展開の扱いが course_spec と矛盾しない
- ナレーション本文はVOICEVOX向けに読みやすい表記である
- `触れる`、`方`、`上で` など読み分けが必要な漢字を避けている
- `python3 tools/narration_checker.py courses/aws-slo-adoption-course/scripts/s1-l3_script.md --warnings-ok` が成功する
- 1スライド1メッセージで、9枚前後の構成になっている。枚数を変える場合はQA Notesに理由を残す

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- 旧素材をそのままコピーしない
- ナレーション本文に英字を残さない

# Blocking
Blocked By:
Notes:
- S1-L3はSection 1の締めとして、S1-L1/S1-L2と重複しすぎない構成にする。
