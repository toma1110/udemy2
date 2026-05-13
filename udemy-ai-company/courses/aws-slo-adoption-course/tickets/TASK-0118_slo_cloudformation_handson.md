# Task Summary
Task ID: TASK-0118
Title: SLO CloudFormationハンズオン教材を作成する

# Ownership
Department: engineering
Owner AI: AI-Engineer-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Engineering Review

# Inputs
Input Files:
- `course_spec.md`
- `docs/CLOUDFORMATION_RULES.md`
- `docs/QUALITY_GATE.md`
- `cloudformation/template.yaml`
- `cloudformation/README.md`
Dependencies:
- Section 9動画作成完了

# Deliverables
Expected Output:
- CloudFormationテンプレート
- README通りに実行できるハンズオン手順
- validate/create/update/delete/smoke test用スクリプト
- サンプルSLIメトリクス投入スクリプト
- ハンズオン検証レポート

# Quality Gate
Definition of Done:
- CloudFormation validate-template が成功する
- awsiac template validation が成功する
- READMEに前提、コスト注意、作成、検証、更新、削除、失敗時確認がある
- 可用性、レイテンシ、エラー率、バーンレートを扱う
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner ≠ Worker
- Worker ≠ Reviewer
- course_spec is source of truth
- CloudFormationを原則とする
- AWSリソース作成はコスト注意を明記する

# Blocking
Blocked By:
Notes:
- 実スタックのcreate/update/deleteは、この作業では未実行。CEOがAWS課金を許容したタイミングで `./validate.sh full` を実行する。
