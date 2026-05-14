# Task Summary
Task ID: TASK-0134
Title: VID-001講座のGPT-Image2向けスライド設計を作成する

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
- `courses/aws-cloudwatch-intro-course/course_spec.md`
- `courses/aws-cloudwatch-intro-course/scripts/s1-l1_script.md`
- `docs/STYLE_GUIDE.md`
Dependencies:
- TASK-0133

# Deliverables
Expected Output:
- `courses/aws-cloudwatch-intro-course/slides/s1-l1_storyboard.md`
- スライドごとの目的
- GPT-Image2用プロンプト概要
- 図解方針
- contact sheet確認観点

# Quality Gate
Definition of Done:
- 1スライド1メッセージになっている
- Metrics/Logs/Alarm/Dashboardの関係が図解される
- ごちゃごちゃせず、短尺入門として見やすい
- READMEや台本と矛盾しない
- GPT-Image2生成前提である
- Worker != Reviewer が守られている
Mission/Vision/Values Alignment:
- 図解はスライドPNG内に含め、AWSリソースの関係を明確にする

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- GPT-Image2 PNGスライド前提
- チケットなし作業禁止

# Blocking
Blocked By:
- TASK-0133
- CEO approval to start VID-001 course production
Notes:
- このチケットではPNG生成までは行わない。
- GitHub Issue: #141 https://github.com/toma1110/udemy2/issues/141
