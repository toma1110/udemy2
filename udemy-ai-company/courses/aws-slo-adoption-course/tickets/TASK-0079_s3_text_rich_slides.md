# Task Summary
Task ID: TASK-0079
Title: aws-slo-adoption-course Section 3 スライドをS2相当の文字入り教材スライドへ修正する

# Ownership
Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Done

# Inputs
Input Files:
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s3-l1_script.md
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s3-l2_script.md
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s3-l3_script.md
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s3-l4_script.md
- udemy-ai-company/courses/aws-slo-adoption-course/scripts/s3-l5_script.md
- udemy-ai-company/courses/aws-slo-adoption-course/slides/s2-l*/contact_sheet.png
Dependencies:
- TASK-0078 approved

# Deliverables
Expected Output:
- udemy-ai-company/courses/aws-slo-adoption-course/slides/s3-l1/slide_001.png ... slide_008.png
- udemy-ai-company/courses/aws-slo-adoption-course/slides/s3-l2/slide_001.png ... slide_008.png
- udemy-ai-company/courses/aws-slo-adoption-course/slides/s3-l3/slide_001.png ... slide_008.png
- udemy-ai-company/courses/aws-slo-adoption-course/slides/s3-l4/slide_001.png ... slide_008.png
- udemy-ai-company/courses/aws-slo-adoption-course/slides/s3-l5/slide_001.png ... slide_008.png
- contact_sheet.png for each lecture
- updated slide generation QA report

# Quality Gate
Definition of Done:
- S2と同じく、スライド本文側に日本語ラベル、短文、カード、図解要素が入っている
- 1920x1080 PNGである
- 1スライド1メッセージを保っている
- 音声と台本は変更しない
- contact sheetで全体確認できる

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- CEOコメントの意図に沿い、S2と印象を揃える

# Blocking
Blocked By:
Notes:
- 文字入りスライドは日本語表示精度を優先し、既存のS2風レイアウトへ寄せる。
