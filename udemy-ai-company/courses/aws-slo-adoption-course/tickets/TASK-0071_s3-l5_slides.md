# Task Summary
Task ID: TASK-0071
Title: aws-slo-adoption-course Section 3 Lecture 5 のGPT-Image2スライドを生成する

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
- TASK-0070 done

# Deliverables
Expected Output:
- udemy-ai-company/courses/aws-slo-adoption-course/slides/s3-l5/slide_001.png ...
- udemy-ai-company/courses/aws-slo-adoption-course/qa/s3-l5_slide_generation_report.md

# Quality Gate
Definition of Done:
- s3-l5_script.md の全スライドに対応するPNGがある
- 表示テキストは講義内容と一致している
- 図解はスライドPNG内に含める
- 1920x1080相当の動画素材として利用できる
- contact sheetで全体確認できる

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
