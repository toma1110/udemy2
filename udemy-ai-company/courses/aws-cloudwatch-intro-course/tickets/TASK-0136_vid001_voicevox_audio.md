# Task Summary
Task ID: TASK-0136
Title: VID-001講座のVOICEVOX音声素材を生成する

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
- `courses/aws-cloudwatch-intro-course/scripts/s1-l1_script.json`
- `docs/VOICEVOX_RULES.md`
Dependencies:
- TASK-0133

# Deliverables
Expected Output:
- `courses/aws-cloudwatch-intro-course/audio/s1-l1/*.wav`
- `courses/aws-cloudwatch-intro-course/qa/s1-l1_voicevox_generation_report.md`

# Quality Gate
Definition of Done:
- VOICEVOXで音声が生成されている
- slide数とaudio数が一致している
- 英字略語、空白読み、伏字、カッコふりがなが読み上げ本文に残っていない
- 生成設定とファイル一覧がレポートに残っている
- Worker != Reviewer が守られている
Mission/Vision/Values Alignment:
- 音声品質を事前チェックし、初学者が聞き取りやすい教材にする

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- VOICEVOX音声前提
- チケットなし作業禁止

# Blocking
Blocked By:
- TASK-0133
- CEO approval to start VID-001 course production
Notes:
- VOICEVOXサーバー未起動の場合はBlocked理由をIssueに記録する。
- GitHub Issue: #143 https://github.com/toma1110/udemy2/issues/143
