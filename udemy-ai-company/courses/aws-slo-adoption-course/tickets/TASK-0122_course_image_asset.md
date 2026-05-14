# Task Summary
Task ID: TASK-0122
Title: Udemy登録用コース画像を作成してコース直下へ配置する

# Ownership
Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

# Execution
Priority: medium
Status: Done
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none

# Inputs
Input Files:
- `courses/aws-slo-adoption-course/course_infomation.md`
Dependencies:
- TASK-0121

# Deliverables
Expected Output:
- `courses/aws-slo-adoption-course/course_image.png`
- `courses/aws-slo-adoption-course/course_image_gpt_image2_source.png`
- `courses/aws-slo-adoption-course/qa/course_image_generation_report.md`

# Quality Gate
Definition of Done:
- Udemy推奨サイズの750x422 PNGが存在する
- 画像内にテキスト、ロゴ、読めるUIラベルを含めない
- AWS、SLO、監視、ダッシュボード、信頼性レビューを連想できる
- GPT-Image2生成元を保存している
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth

# Blocking
Blocked By:
- none
Notes:
- GitHub Issue: #158 https://github.com/toma1110/udemy2/issues/158
- Built-in GPT-Image2 image generation was used.
