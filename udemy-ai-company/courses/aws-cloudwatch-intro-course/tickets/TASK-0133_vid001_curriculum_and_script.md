# Task Summary
Task ID: TASK-0133
Title: VID-001講座の章立てとVOICEVOX向け台本を作成する

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
- `courses/aws-cloudwatch-intro-course/handson/README.md`
- `courses/aws-cloudwatch-intro-course/qa/cloudwatch_source_verification_report.md`
- `docs/STYLE_GUIDE.md`
- `docs/VOICEVOX_RULES.md`
Dependencies:
- TASK-0130
- TASK-0131
- TASK-0132

# Deliverables
Expected Output:
- `courses/aws-cloudwatch-intro-course/scripts/lectures.md`
- `courses/aws-cloudwatch-intro-course/scripts/s1-l1_script.md`
- `courses/aws-cloudwatch-intro-course/scripts/s1-l1_script.json`
- ナレーション品質チェック結果

# Quality Gate
Definition of Done:
- 講座は短尺入門として成立している
- Metrics/Logs/Alarm/Dashboardの地図が台本上で明確
- 動画手順とREADMEが一致している
- VOICEVOX向けに英字略語、空白、読み上げ不自然箇所が調整されている
- `tools/narration_checker.py` でチェックしている
- Worker != Reviewer が守られている
Mission/Vision/Values Alignment:
- 初学者にやさしく、実務上重要な論点を落とさない

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- follow docs/STYLE_GUIDE.md
- follow docs/VOICEVOX_RULES.md
- チケットなし作業禁止

# Blocking
Blocked By:
- TASK-0130
- TASK-0131
- TASK-0132
- CEO approval to start VID-001 course production
Notes:
- CloudWatchは読み上げ本文では必要に応じて「クラウドウォッチ」にする。
- GitHub Issue: #140 https://github.com/toma1110/udemy2/issues/140
