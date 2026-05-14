# Task Summary
Task ID: TASK-0126
Title: 50本動画候補をスコアリングして優先上位10本を選ぶ

# Ownership
Department: strategy
Owner AI: AI-Strategy-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Done
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none

# Inputs
Input Files:
- `market-research/udemy_sellable_video_candidates_50.md`
- `market-research/udemy_research_plan.md`
- `docs/MISSION_VISION_VALUES.md`
Dependencies:
- TASK-0125

# Deliverables
Expected Output:
- `market-research/udemy_video_idea_scoring_top10.md`
- 50本候補のスコア表
- 上位10本の選定理由
- すぐ制作できる候補
- 追加検証が必要な候補
- 制作しない候補と理由

# Quality Gate
Definition of Done:
- 全50本以上に同じ評価軸でスコアが付いている
- 市場需要、競合ギャップ、制作容易性、再現性、収益仮説を分けて評価している
- 上位10本にCEO判断用の短い推薦理由がある
- 低スコア候補も削除せず、理由付きで残している
- Worker != Reviewer が守られている
Mission/Vision/Values Alignment:
- 売上仮説だけでなく、再現性と教材品質を含めて優先順位を決める

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- follow docs/MISSION_VISION_VALUES.md
- スコアは最終決定ではなくCEO判断の材料とする
- チケットなし作業禁止

# Blocking
Blocked By:
Notes:
- CEOの好みや既存販売戦略と異なる場合は、最終判断をCEOへ戻す
- GitHub Issue: #133 https://github.com/toma1110/udemy2/issues/133
- Output: `market-research/udemy_video_idea_scoring_top10.md`
- Scored candidates: 52
- Top 10 selected
- Completed: 2026-05-13
