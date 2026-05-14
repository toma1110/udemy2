# Task Summary
Task ID: TASK-0129
Title: CloudFormation/CDK/Terraformの位置づけを修正する

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
- `docs/CLOUDFORMATION_RULES.md`
- `docs/QUALITY_GATE.md`
- `market-research/udemy_research_plan.md`
- `market-research/next_course_decision_pack.md`
Dependencies:
- CEO clarification on 2026-05-14: CloudFormationはハンズオン内の再現手段。実運用ではCDKかTerraformを使うべき。

# Deliverables
Expected Output:
- CloudFormationを実運用IaCの原則として扱う記述の修正
- 教材ハンズオンではCloudFormationを簡便な再現手段として扱う方針の明記
- 実運用ではCDKまたはTerraform推奨であることの明記
- 市場調査成果物とCEO判断パックの修正

# Quality Gate
Definition of Done:
- CloudFormationを全社の実運用標準とし、Terraformを特殊例外にする表現が残っていない
- CloudFormationはハンズオン教材向けの選択肢として説明されている
- 実運用IaCはCDKまたはTerraformを推奨している
- 既存のCloudFormationハンズオン講座自体は否定していない
- Worker != Reviewer が守られている
Mission/Vision/Values Alignment:
- 初学者がREADME通りに再現できる教材価値と、実務で使えるクラウド運用力の両方を守る

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- follow docs/MISSION_VISION_VALUES.md
- 既存講座の完成済みハンズオン資産は破壊しない
- チケットなし作業禁止

# Blocking
Blocked By:
Notes:
- CEO clarification is treated as approval for this policy correction.
- GitHub Issue: #136 https://github.com/toma1110/udemy2/issues/136
