# Task Summary
Task ID: TASK-0128
Title: Udemy市場リサーチ成果物をQAしてCEO判断前に整合性を確認する

# Ownership
Department: qa
Owner AI: AI-QA-01
Reviewer AI: AI-Ops-01

# Execution
Priority: high
Status: Done
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none

# Inputs
Input Files:
- `market-research/udemy_research_plan.md`
- `market-research/udemy_competitor_scan.md`
- `market-research/udemy_keyword_demand_scan.md`
- `market-research/learner_pain_review_scan.md`
- `market-research/udemy_sellable_video_candidates_50.md`
- `market-research/udemy_video_idea_scoring_top10.md`
- `market-research/next_course_decision_pack.md`
- `docs/MISSION_VISION_VALUES.md`
- `docs/TASK_MANAGEMENT.md`
Dependencies:
- TASK-0121
- TASK-0122
- TASK-0123
- TASK-0124
- TASK-0125
- TASK-0126
- TASK-0127

# Deliverables
Expected Output:
- `market-research/qa/market_research_qa_report.md`
- 調査根拠の確認結果
- 50本リストの件数確認
- スコアリング整合性レビュー
- Worker/Reviewer分離チェック
- CEO判断パックの承認または差戻し

# Quality Gate
Definition of Done:
- 50本以上の動画候補が存在することを確認している
- 各候補に市場根拠と差別化があることを確認している
- 調査日と参照元が主要成果物に記録されている
- 「売れる」と断定していないことを確認している
- CEO判断に必要な上位3候補が整理されている
- Worker != Reviewer が守られている
Mission/Vision/Values Alignment:
- 推測だけで講座制作に入らず、根拠と品質ゲートを通してCEO判断へ渡す

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- follow docs/MISSION_VISION_VALUES.md
- QA担当は市場リサーチ成果物を直接書き換えず、差戻し理由をレポートに記録する
- チケットなし作業禁止

# Blocking
Blocked By:
Notes:
- QA承認後、CEOが次講座候補を選ぶ
- GitHub Issue: #135 https://github.com/toma1110/udemy2/issues/135
- Output: `market-research/qa/market_research_qa_report.md`
- QA result: PASS
- Completed: 2026-05-13
