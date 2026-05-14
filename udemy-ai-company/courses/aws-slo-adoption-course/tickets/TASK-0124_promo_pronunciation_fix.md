# Task Summary
Task ID: TASK-0124
Title: promo_slo_adoption動画のVOICEVOX読み方を修正する

# Ownership
Department: production
Owner AI: AI-Production-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Done
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none

# Inputs
Input Files:
- `courses/aws-slo-adoption-course/scripts/promo_video_script.md`
- `courses/aws-slo-adoption-course/scripts/promo_video_script.json`
- `docs/VOICEVOX_RULES.md`
- `tools/narration_checker.py`
Dependencies:
- TASK-0123

# Deliverables
Expected Output:
- `promo_video_script.md/json` の読み上げ表記修正
- VOICEVOX読み方ルールとチェッカーの更新
- `audio/promo_slo_adoption/slide_*.wav` の再生成
- `video/promo_slo_adoption/promo_slo_adoption.mp4`
- `video/promo_slo_adoption/promo_slo_adoption.30fps.mp4`
- QA記録

# Quality Gate
Definition of Done:
- `そんな方向け` は `そんなかたむけ` と読ませる
- 対象者を指す `方` は `かた` と読ませる
- VOICEVOXナレーションチェックを通過している
- MP4 faststart true、decode check OK
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- 本修正はローカル音声・動画生成のみで、AWS課金作業を含まない

# Blocking
Blocked By:
- none
Notes:
- CEO指摘: `そんな方向け:そんなかたむけ`、`方:かた`
- 2026-05-14: 台本、読み方ルール、チェッカー、ローカルVOICEVOX生成ルール、Batch VOICEVOX workerの安全網を更新。
- 2026-05-14: `audio/promo_slo_adoption/slide_*.wav` を再生成し、`promo_slo_adoption.mp4` と `promo_slo_adoption.30fps.mp4` を再ビルド。
- 2026-05-14: `narration_checker.py`、JSON検証、MP4 decode、faststart確認を通過。
- 2026-05-14: Google Driveへ読み方修正版を別名アップロード。File ID: `15dBkmo9Ia1AZcdPy88ETibV6wYZT7Duc`
