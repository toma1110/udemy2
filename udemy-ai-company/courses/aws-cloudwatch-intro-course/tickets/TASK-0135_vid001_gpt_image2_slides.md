# Task Summary
Task ID: TASK-0135
Title: VID-001講座のGPT-Image2スライドPNGを生成する

# Ownership
Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: CEO Approval Required
Auto Execute: yes
Requires CEO Approval: yes
Cost Impact: none

# Inputs
Input Files:
- `courses/aws-cloudwatch-intro-course/slides/s1-l1_storyboard.md`
- `courses/aws-cloudwatch-intro-course/scripts/s1-l1_script.json`
- `docs/STYLE_GUIDE.md`
Dependencies:
- TASK-0134

# Deliverables
Expected Output:
- `courses/aws-cloudwatch-intro-course/slides/s1-l1/slide_001.png` 以降
- `courses/aws-cloudwatch-intro-course/slides/s1-l1/contact_sheet.png`
- `courses/aws-cloudwatch-intro-course/qa/s1-l1_slide_generation_report.md`

# Quality Gate
Definition of Done:
- スライドPNGがGPT-Image2生成物またはGPT-Image2派生物である
- スライド数と台本JSONが一致している
- Metrics/Logs/Alarm/Dashboardの地図が視覚的に分かる
- contact sheetで文字切れ、重なり、過密を確認している
- 生成元、プロンプト概要、後処理内容をレポートに残している
- Worker != Reviewer が守られている
Mission/Vision/Values Alignment:
- 仕組みで制作品質を上げ、受講したいと思える教材にする

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- GPT-Image2 PNGスライド前提
- チケットなし作業禁止

# Blocking
Blocked By:
- TASK-0134
- CEO approval to start VID-001 course production
Notes:
- ローカル描画を最終スライド生成元にしない。
- GitHub Issue: #142 https://github.com/toma1110/udemy2/issues/142
