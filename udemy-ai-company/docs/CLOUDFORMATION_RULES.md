# CLOUDFORMATION_RULES

このファイル名は既存参照との互換性のために維持する。内容は「CloudFormationを実運用IaCの原則にする」ルールではなく、教材ハンズオンでCloudFormationを使う場合のルールである。

## 基本方針

- CloudFormationは、受講者がAWS CLIだけで再現しやすい教材ハンズオン向けの標準選択肢とする
- 実運用のIaCはAWS CDKまたはTerraformを推奨する
- AWS中心でアプリケーションコードと近い形で管理したい実運用ではAWS CDKを優先候補にする
- マルチクラウド、サードパーティProvider、既存Terraform資産が重要な実運用ではTerraformを優先候補にする
- CloudFormationハンズオンでは、初学者が読めるテンプレートを優先する
- 過度に抽象化しない
- README通りに再現できることを最優先にする
- stack作成/更新/削除など課金につながるAWS実行はCEO承認後にだけ行う
- AWSサービス仕様、制約、廃止予定、ベストプラクティスは `awsknowledge` で確認し、検索語、確認結果、参照URLをQAレポートまたはIssueに残す

## テンプレート設計

- `AWSTemplateFormatVersion` と `Description` を書く
- Parametersを明確にする
- Outputsを明確にする
- リソース名は学習者が識別しやすい名前にする
- コストが発生するリソースにはREADMEで注意を書く
- 削除手順を必ず用意する

## IAM

- IAMは必要な場合だけ作成する
- 最小権限にする
- `*` 権限は原則禁止
- やむを得ない場合は理由をREADMEとQAレポートに書く

## 検証

各CloudFormationハンズオンディレクトリには以下を置く。

- `template.yaml`
- `validate.sh`
- `smoke_test.sh`
- `README.md`

`validate.sh` は以下を想定する。

- cfn validate
- 利用可能な場合は `awsiac` によるCloudFormationテンプレート検証
- stack create
- stack update
- smoke test
- stack delete

`smoke_test.sh` は作成された主要リソースが存在することを確認する。

`awsiac` が利用できない場合は、未使用理由と代替検証結果をハンズオン検証レポートまたはIssueに明記する。`awsiac` 検証は補助ゲートであり、`aws cloudformation validate-template`、実際のstack create/update/delete、`smoke_test.sh` の代替にはしない。

## stack naming rule

形式:

`{course-slug}-{environment}-{purpose}`

例:

- `sample-aws-sre-dev-monitoring`
- `aws-sre-intro-dev-dashboard`
- `cloudwatch-hands-on-test-alert`

制約:

- 小文字英数字とハイフンを使う
- 講座名またはレッスン名が推測できるようにする
- 個人名を含めない
- 本番環境と検証環境を区別する

## コスト注意

- CloudWatch Alarm、Dashboard、ログ、メトリクスには料金が発生する場合がある
- ハンズオン後は削除手順を必ず実行する
- 無料利用枠に依存した説明は、時期やアカウント状態で変わるため注意書きを入れる
- AI-PM-01は課金影響があるCloudFormation検証Issueを `approval-required` にし、`ceo-approved` が付くまで自動実行しない

## 実運用IaCとの関係

- 教材内では、CloudFormationは「学習用に準備を少なくするための再現手段」と説明する
- 実運用では、チーム開発、テスト、再利用性、レビュー容易性、既存資産との統合を考慮してCDKまたはTerraformを選ぶ
- CloudFormationハンズオンを扱う講座でも、必要に応じて「実運用ではCDK/Terraformへ発展させる」補足を入れる
- CloudFormationだけを許可する説明や、Terraformを特殊例外として扱う説明はしない
