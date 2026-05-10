# SLO CloudFormationハンズオン

SRE向けSLO導入講座のCloudFormationハンズオンです。

デフォルトでは低コストなCloudWatch構成だけを作ります。Application Signals SLOは料金、サービスリンクロール、実メトリクス前提があるため、明示的に有効化した場合だけ作成します。

## 作成するリソース

- SNS Topic
- CloudWatch Alarm
  - Availability SLI用
  - Latency SLI用
- CloudWatch Dashboard
- Application Signals SLO
  - `ENABLE_APPLICATION_SIGNALS_SLO=true` の場合のみ

## コスト注意

CloudWatch Alarm、Dashboard、SNS、Custom Metrics、Application Signals、SLOには料金が発生する場合があります。検証後は必ず削除してください。

Application Signals SLOを有効化すると、初回作成時に `AWSServiceRoleForCloudWatchApplicationSignals` サービスリンクロールが自動作成される場合があります。このロールはスタック削除後も残る可能性があります。

## 使い方

テンプレート検証:

```bash
./validate.sh validate
```

スタック作成:

```bash
STACK_NAME=aws-slo-adoption-dev-slo AWS_REGION=us-east-1 ./validate.sh create
```

サンプルメトリクス投入:

```bash
STACK_NAME=aws-slo-adoption-dev-slo AWS_REGION=us-east-1 ./validate.sh put-metrics
```

存在確認:

```bash
STACK_NAME=aws-slo-adoption-dev-slo AWS_REGION=us-east-1 ./smoke_test.sh
```

スタック更新:

```bash
STACK_NAME=aws-slo-adoption-dev-slo AWS_REGION=us-east-1 DASHBOARD_TITLE="Updated SLO Dashboard" ./validate.sh update
```

スタック削除:

```bash
STACK_NAME=aws-slo-adoption-dev-slo AWS_REGION=us-east-1 ./validate.sh delete
```

作成、メトリクス投入、更新、検証、削除をまとめて確認:

```bash
STACK_NAME=aws-slo-adoption-dev-slo AWS_REGION=us-east-1 ./validate.sh full
```

## Application Signals SLOを有効化する場合

```bash
STACK_NAME=aws-slo-adoption-dev-slo \
AWS_REGION=us-east-1 \
ENABLE_APPLICATION_SIGNALS_SLO=true \
./validate.sh create
```

注意:

- SLO料金が発生する場合があります
- サービスリンクロールが自動作成される場合があります
- 実メトリクスが少ない環境ではSLO評価が教材通りに見えない場合があります

## 失敗時の確認ポイント

- AWS CLIの認証情報が設定されているか
- `AWS_REGION` が正しいか
- CloudFormation、CloudWatch、SNS、Application Signalsの権限があるか
- 同じ `STACK_NAME` の失敗スタックが残っていないか
- Application Signals SLOを有効化した場合、対象リージョンで利用可能か
