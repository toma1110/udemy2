# Task Summary
Task ID: TASK-0137
Title: VID-001講座の音声レビューを実施する

# Ownership
Department: qa
Owner AI: AI-QA-01
Reviewer AI: AI-Ops-01

# Execution
Priority: medium
Status: CEO Approval Required
Auto Execute: yes
Requires CEO Approval: yes
Cost Impact: none

# Inputs
Input Files:
- `courses/aws-cloudwatch-intro-course/audio/s1-l1/`
- `courses/aws-cloudwatch-intro-course/scripts/s1-l1_script.json`
- `courses/aws-cloudwatch-intro-course/qa/s1-l1_voicevox_generation_report.md`
- `docs/VOICEVOX_RULES.md`
Dependencies:
- TASK-0136

# Deliverables
Expected Output:
- `courses/aws-cloudwatch-intro-course/qa/s1-l1_audio_review_report.md`
- 承認または差戻し

# Quality Gate
Definition of Done:
- 音声数とスライド数が一致している
- 無音、極端なノイズ、読み飛ばしがない
- CloudWatch、Metrics、Logs、Alarm、Dashboardの読みが自然
- 修正が必要な場合は具体箇所を記録している
- Worker != Reviewer が守られている
Mission/Vision/Values Alignment:
- QAで聞き取り品質を担保する

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- QA担当は音声素材を直接修正しない
- チケットなし作業禁止

# Blocking
Blocked By:
- TASK-0136
- CEO approval to start VID-001 course production
Notes:
- 差戻し時はTASK-0133またはTASK-0136へ戻す。
- GitHub Issue: #144 https://github.com/toma1110/udemy2/issues/144
