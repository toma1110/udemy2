# CloudFormationハンズオン

CloudWatch Alarm、SNS Topic、CloudWatch Dashboardを作成する最小構成です。

## 前提

- AWS CLI v2
- AWS認証情報設定済み
- CloudFormation、CloudWatch、SNSを利用できる権限
- Bash実行環境

## 想定コスト

CloudWatch Alarm、Dashboard、SNSには料金が発生する場合があります。検証後は必ず削除してください。

## 使い方

テンプレート検証:

```bash
./validate.sh validate
```

スタック作成:

```bash
STACK_NAME=sample-aws-sre-dev-monitoring AWS_REGION=us-east-1 ./validate.sh create
```

存在確認:

```bash
STACK_NAME=sample-aws-sre-dev-monitoring AWS_REGION=us-east-1 ./smoke_test.sh
```

スタック更新:

```bash
STACK_NAME=sample-aws-sre-dev-monitoring AWS_REGION=us-east-1 ./validate.sh update
```

スタック削除:

```bash
STACK_NAME=sample-aws-sre-dev-monitoring AWS_REGION=us-east-1 ./validate.sh delete
```

作成、更新、検証、削除をまとめて確認:

```bash
STACK_NAME=sample-aws-sre-dev-monitoring AWS_REGION=us-east-1 ./validate.sh full
```

## 通知メールを設定する場合

SNSのメール購読を作る場合は `NOTIFICATION_EMAIL` を指定します。

```bash
STACK_NAME=sample-aws-sre-dev-monitoring \
AWS_REGION=us-east-1 \
NOTIFICATION_EMAIL=your-email@example.com \
./validate.sh create
```

メール購読は確認メールの承認が必要です。

Dashboardのタイトルを変えて更新差分を作る場合は `DASHBOARD_TITLE` を指定します。

```bash
STACK_NAME=sample-aws-sre-dev-monitoring \
AWS_REGION=us-east-1 \
DASHBOARD_TITLE="Updated SRE Metric" \
./validate.sh update
```

## 失敗時の確認ポイント

- AWS CLIの認証情報が設定されているか
- `AWS_REGION` が正しいか
- 同じ `STACK_NAME` のスタックが失敗状態で残っていないか
- CloudWatch、SNS、CloudFormationの権限があるか

## 削除確認

削除後、以下でスタックが存在しないことを確認します。

```bash
aws cloudformation describe-stacks \
  --stack-name sample-aws-sre-dev-monitoring \
  --region us-east-1
```

削除済みの場合は `does not exist` 系のエラーになります。
