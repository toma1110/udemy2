# Task Summary
Task ID: TASK-0032
Title: aws-slo-adoption-course Section 2 Lecture 2 のGPT-Image2スライドを生成する

# Ownership
Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Done

# Inputs
Input Files:
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s2-l2_script.md
- udemy-ai-company/docs/STYLE_GUIDE.md
- udemy-ai-company/courses/aws-slo-adoption-course/course_spec.md
Dependencies:
- TASK-0031 reviewed

# Deliverables
Expected Output:
- udemy-ai-company/courses/aws-slo-adoption-course/slides/s2-l2/slide_001.png ... slide_00N.png
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s2-l2_slide_generation_report.md

# Quality Gate
Definition of Done:
- GPT-Image2でPNG生成されている
- スライド枚数が台本と一致している
- スライド内容が `s2-l2_script.md` と一致している
- エラーバジェットを残量、判断、消費の関係として視覚化している
- Section 1とS2-L1の視覚トーンが大きくずれていない
- 表示テキストは検索しやすい正式表記を使い、ナレーション本文とは分けて扱う
- 生成メディアはGit追跡しない

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- バーンレートの詳細図解をSection 6より先に説明しすぎない

# Blocking
Blocked By: TASK-0031
Notes:
