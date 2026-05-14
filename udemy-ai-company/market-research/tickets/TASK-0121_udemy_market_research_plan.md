# Task Summary
Task ID: TASK-0121
Title: Udemyで売れる動画テーマ調査の設計と評価軸を作る

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
- `docs/MISSION_VISION_VALUES.md`
- `docs/TASK_MANAGEMENT.md`
- `docs/WORKFLOW.md`
- `market-research/README.md`
Dependencies:
- CEO request: Udemyで売れる動画のリサーチを行い、動画リストを50本以上作る

# Deliverables
Expected Output:
- `market-research/udemy_research_plan.md`
- 調査対象カテゴリ
- 調査ソース一覧
- 50本リスト用の評価軸
- スコアリング基準

# Quality Gate
Definition of Done:
- 「売れる」の判定を保証ではなく市場仮説として定義している
- Udemy上の需要、競合、受講者の悩み、制作容易性の評価軸がある
- 50本候補リストに使う列定義がある
- 外部有料ツール、課金API、AWS課金作業を使わない前提が明記されている
- Worker != Reviewer が守られている
Mission/Vision/Values Alignment:
- CEOが次に作る講座を判断でき、受講者がREADME通り再現できる教材企画につながる

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- follow docs/MISSION_VISION_VALUES.md
- 既存講座の `course_spec.md` は変更しない
- 新講座化はCEO承認後の別チケットで行う
- チケットなし作業禁止

# Blocking
Blocked By:
Notes:
- これは調査設計チケットであり、50本リスト本体は TASK-0125 で作成する
- GitHub Issue: #128 https://github.com/toma1110/udemy2/issues/128
- Output: `market-research/udemy_research_plan.md`
- Completed: 2026-05-13
