# Task Summary
Task ID: TASK-0122
Title: Udemy競合講座を調査して売れている訴求と不足領域を抽出する

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
- `docs/MISSION_VISION_VALUES.md`
Dependencies:
- TASK-0121

# Deliverables
Expected Output:
- `market-research/udemy_competitor_scan.md`
- Udemy競合講座リスト
- 講座ごとの対象者、Promise、章立て、レビュー数、評価、更新日、訴求
- 競合が強い領域
- 競合が弱い領域
- 日本語教材として差別化できる候補

# Quality Gate
Definition of Done:
- AWS、SRE、DevOps、CloudFormation、監視、CI/CD、セキュリティ、コンテナ、生成AI運用の周辺講座を調査している
- 競合講座ごとに参照URLと調査日を記録している
- ベストセラー、レビュー数、評価、更新日を可能な範囲で記録している
- 競合の単なるコピーではなく、差別化仮説を明記している
- Worker != Reviewer が守られている
Mission/Vision/Values Alignment:
- 実務で役立つAWS/SRE教材を作るため、需要と競合を根拠付きで把握する

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- follow docs/MISSION_VISION_VALUES.md
- 調査結果は実行日のUdemy表示に基づくため、調査日を必ず残す
- 既存講座の `course_spec.md` は変更しない
- チケットなし作業禁止

# Blocking
Blocked By:
Notes:
- Udemyページの表示やランキングは日付で変わるため、確定事実ではなく市場シグナルとして扱う
- GitHub Issue: #129 https://github.com/toma1110/udemy2/issues/129
- Output: `market-research/udemy_competitor_scan.md`
- Completed: 2026-05-13
