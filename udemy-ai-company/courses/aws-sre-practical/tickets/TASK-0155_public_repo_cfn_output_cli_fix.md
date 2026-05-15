# Task Summary
Task ID: TASK-0155
Title: aws-sre-cfn-templatesのCloudFormation OutputsとCLIコマンド不整合を修正する

# Ownership
Department: engineering
Owner AI: AI-Engineer-01
Reviewer AI: AI-QA-01

# Execution
Priority: high
Status: Done
Auto Execute: yes
Requires CEO Approval: no
Cost Impact: none

# Inputs
Input Files:
- `udemy-ai-company/public_repo/aws-sre-cfn-templates/cloudformation/01-base-infrastructure.yaml`
- `udemy-ai-company/public_repo/aws-sre-cfn-templates/cloudformation/02-cloudwatch-dashboard.yaml`
- `udemy-ai-company/public_repo/aws-sre-cfn-templates/cloudformation/05-alarms-sns.yaml`
- `udemy-ai-company/public_repo/aws-sre-cfn-templates/CLI_COMMANDS.md`
- `udemy-ai-company/public_repo/aws-sre-cfn-templates/README.md`
- `udemy-ai-company/docs/PUBLIC_REPO_RULES.md`
Dependencies:
- 受講者レビュー指摘: `ALBFullName` Outputs不足
- 受講者レビュー指摘: アラーム名 `sre-handson-high-cpu` と `sre-handson-cpu-high` の不一致

# Deliverables
Expected Output:
- `01-base-infrastructure.yaml` の Outputs に `ALBFullName` を追加する
- `CLI_COMMANDS.md` のアラーム名を実テンプレートの `sre-handson-cpu-high` に統一する
- 必要に応じてREADME/CLIにOutputs取得手順を追記する
- 受講者が `02-cloudwatch-dashboard.yaml` と `05-alarms-sns.yaml` の `ALBFullName` に入れる値を迷わない状態にする

# Quality Gate
Definition of Done:
- `ALBFullName` が `!GetAtt ALB.LoadBalancerFullName` として取得できる
- `02-cloudwatch-dashboard.yaml` と `05-alarms-sns.yaml` のパラメータ名と `01-base-infrastructure.yaml` の Outputs が一致する
- `CLI_COMMANDS.md` に `sre-handson-high-cpu` が残っていない
- `CLI_COMMANDS.md` と `05-alarms-sns.yaml` のアラーム名が一致する
- 課金リソースの作成、更新、削除は実行しない
- Worker != Reviewer が守られている

# Constraints
Rules:
- Planner != Worker
- Worker != Reviewer
- course_spec is source of truth
- チケットなし作業禁止
- Publicリポジトリ配布物は `udemy-ai-company/public_repo/aws-sre-cfn-templates/` 配下で修正する
- CloudFormationは教材ハンズオン用途に限定し、実運用IaC推奨はCDKまたはTerraformとする

# Impact Analysis
Scope:
- PublicリポジトリのCloudFormationテンプレートOutputsとCLI手順のみ
Risks:
- 既存スタック更新時にOutputs追加のみでリソース変更は発生しない想定
- 実AWS検証はCEO承認なしでは行わない
QA:
- 静的検索で名称不一致を確認する
- CloudFormation構文確認は可能な範囲で実施する

# Blocking
Blocked By:
- none
Notes:
- GitHub Issue: #155 https://github.com/toma1110/udemy2/issues/155
- `courses/aws-sre-practical/course_spec.md` は現時点で未配置。既存講座の公開配布物修正として、`PUBLIC_REPO_RULES.md`、公開リポジトリREADME、動画内案内との整合を優先する。
- Implementation completed:
  - `01-base-infrastructure.yaml` に `ALBFullName` Outputを追加
  - `02-cloudwatch-dashboard.yaml` の古い `ALBFullName` Defaultを削除
  - `README.md` と `CLI_COMMANDS.md` にOutputs取得手順を追加
  - `CLI_COMMANDS.md` のアラーム名を `sre-handson-cpu-high` に統一
- Static validation completed:
  - `aws cloudformation validate-template` PASS: `01-base-infrastructure.yaml`
  - `aws cloudformation validate-template` PASS: `02-cloudwatch-dashboard.yaml`
  - `aws cloudformation validate-template` PASS: `05-alarms-sns.yaml`
- Full stack create/update/delete verification not executed because it creates billable AWS resources and requires CEO approval.
- Final review cleanup completed:
  - Public `CLI_COMMANDS.md` の旧TODOアプリ表記と手動 clone 手順を削除し、UserDataで自動作成されるエラー率デモアプリの確認手順に更新
  - Course internal `CLI_COMMANDS.md` も同じ方針に合わせて更新
  - Public `README.md` の「手動セットアップ手順」FAQを、自動セットアップ確認手順の案内に更新
  - `TODO アプリ` / `sre-todo-app` / `git clone` の残存が公開資料と内部CLIにないことを確認
