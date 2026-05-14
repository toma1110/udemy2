# Task Summary
Task ID: TASK-0124
Title: 受講者レビューとQ&Aから売れる動画の痛点を抽出する

# Ownership
Department: strategy
Owner AI: AI-Strategy-01
Reviewer AI: AI-QA-01

# Execution
Priority: medium
Status: Done
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none

# Inputs
Input Files:
- `market-research/udemy_research_plan.md`
- `market-research/udemy_competitor_scan.md`
- `docs/MISSION_VISION_VALUES.md`
Dependencies:
- TASK-0121
- TASK-0122

# Deliverables
Expected Output:
- `market-research/learner_pain_review_scan.md`
- 低評価レビューで多い不満
- Q&Aで詰まりやすいテーマ
- 既存講座で説明不足になりやすい論点
- 動画化すると価値が出る痛点リスト

# Quality Gate
Definition of Done:
- レビューやQ&Aから、受講者が困っている具体論点を10件以上抽出している
- 「README通り再現できない」「古い」「説明が浅い」「環境差分で詰まる」などの痛点を分類している
- 痛点ごとに動画テーマへの変換案を書いている
- 個人情報や引用過多を避け、要約中心で記録している
- Worker != Reviewer が守られている
Mission/Vision/Values Alignment:
- 受講者の詰まりを教材設計に反映し、再現性の高い講座を作る

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- follow docs/MISSION_VISION_VALUES.md
- レビュー本文の長文転載は禁止
- 既存講座を中傷せず、教材改善の観点で記録する
- チケットなし作業禁止

# Blocking
Blocked By:
Notes:
- レビューやQ&Aが見られない場合は、その旨を記録し、公開情報だけで代替する
- GitHub Issue: #131 https://github.com/toma1110/udemy2/issues/131
- Output: `market-research/learner_pain_review_scan.md`
- Completed: 2026-05-13
