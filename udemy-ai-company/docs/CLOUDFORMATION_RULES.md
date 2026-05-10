# CLOUDFORMATION_RULES

## 基本方針

- IaCは原則CloudFormationを使う
- Terraform講座を作る場合のみTerraformを使う
- 初学者が読めるテンプレートを優先する
- 過度に抽象化しない
- README通りに再現できることを最優先にする

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

各CloudFormationディレクトリには以下を置く。

- `template.yaml`
- `validate.sh`
- `smoke_test.sh`
- `README.md`

`validate.sh` は以下を想定する。

- cfn validate
- stack create
- stack update
- smoke test
- stack delete

`smoke_test.sh` は作成された主要リソースが存在することを確認する。

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
