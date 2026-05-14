# Task Summary
Task ID: TASK-0017
Title: aws-slo-adoption-course Section 1 Lecture 3 のGPT-Image2スライドを生成する

# Ownership
Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Blocked

# Inputs
Input Files:
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s1-l3_script.md
- udemy-ai-company/docs/STYLE_GUIDE.md
- udemy-ai-company/courses/aws-slo-adoption-course/course_spec.md
Dependencies:
- TASK-0016 reviewed

# Deliverables
Expected Output:
- udemy-ai-company/courses/aws-slo-adoption-course/slides/s1-l3/slide_001.png ... slide_00N.png
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s1-l3_slide_generation_report.md

# Quality Gate
Definition of Done:
- GPT-Image2でPNG生成されている
- スライド枚数が台本と一致している
- スライド内容が `s1-l3_script.md` と一致している
- 図解はスライドPNG内に含まれている
- S1-L1/S1-L2と視覚トーンが大きくずれていない
- 表示テキストは学習者が検索しやすい正式表記を使い、ナレーション本文とは分けて扱う
- 生成メディアはGit追跡しない

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- READMEや未検証ハンズオン手順と矛盾する画面を作らない

# Blocking
Blocked By: TASK-0016
Notes:
