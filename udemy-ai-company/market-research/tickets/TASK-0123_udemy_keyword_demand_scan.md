# Task Summary
Task ID: TASK-0123
Title: Udemy内外の検索キーワード需要を調査して動画テーマ候補に変換する

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
- `market-research/udemy_research_plan.md`
- `market-research/udemy_competitor_scan.md`
- `docs/MISSION_VISION_VALUES.md`
Dependencies:
- TASK-0121
- TASK-0122

# Deliverables
Expected Output:
- `market-research/udemy_keyword_demand_scan.md`
- 検索キーワード一覧
- キーワードごとの学習意図
- 初学者向け/実務者向けの分類
- ハンズオン化できる動画テーマ案
- 競合過多/狙い目/検証必要の分類

# Quality Gate
Definition of Done:
- Udemy検索候補、Udemyカテゴリ、一般検索で確認できる関連キーワードを記録している
- AWS/SRE領域に寄せたキーワードに絞っている
- 受講者の検索意図を日本語で説明している
- 50本候補リストに流用できるテーマ案を20件以上出している
- Worker != Reviewer が守られている
Mission/Vision/Values Alignment:
- 市場需要から逆算しつつ、受講者が再現できるAWS/SRE教材へつなげる

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- follow docs/MISSION_VISION_VALUES.md
- 外部有料SEOツールは使わない
- 誇張した需要表現をしない
- チケットなし作業禁止

# Blocking
Blocked By:
Notes:
- 数値が取れない場合は、表示順位、関連講座数、レビュー数などの代理指標で記録する
- GitHub Issue: #130 https://github.com/toma1110/udemy2/issues/130
- Output: `market-research/udemy_keyword_demand_scan.md`
- Completed: 2026-05-13
