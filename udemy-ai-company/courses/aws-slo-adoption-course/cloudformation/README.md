# SLO CloudFormationハンズオン

このハンズオンでは、CloudFormationでSLO監視の最小構成を作ります。

目的は、SLOを抽象論で終わらせず、CloudWatch上で以下を確認できる状態にすることです。

- 可用性SLI
- レイテンシSLI
- エラー率
- エラーバジェット消費速度としてのバーンレート
- CloudWatch Alarm
- CloudWatch Dashboard
- SNS通知先

デフォルトでは、低コストなCloudWatch Custom Metrics構成だけを作ります。Application Signals SLOは料金、サービスリンクロール、実メトリクス前提があるため、明示的に有効化した場合だけ作成します。

## Source of Truth

- `../course_spec.md`

このREADMEと動画手順は、`course_spec.md` のHands-on Scopeに従います。

## 作成するリソース

- SNS Topic
- CloudWatch Alarm
  - Availability SLI低下
  - p99 Latency SLI超過
  - Error Rate超過
  - Fast Burn Rate超過
  - Slow Burn Rate超過
- CloudWatch Dashboard
  - Availability
  - Latency p99
  - Error Rate
  - Burn Rate
  - Requests and Errors
- Optional: Application Signals SLO
  - `ENABLE_APPLICATION_SIGNALS_SLO=true` の場合のみ

## 前提条件

- AWS CLI v2が利用できる
- AWS認証情報またはEC2 IAMロールが設定済み
- CloudFormation、CloudWatch、SNSを操作できる権限がある
- Bashを実行できる
- 検証リージョンを決めている

推奨リージョン:

```bash
export AWS_REGION=us-east-1
```

## コスト注意

CloudWatch Alarm、Dashboard、SNS、Custom Metrics、Application Signals、SLOには料金が発生する場合があります。検証後は必ず削除してください。

Application Signals SLOを有効化すると、初回作成時に `AWSServiceRoleForCloudWatchApplicationSignals` サービスリンクロールが自動作成される場合があります。このロールはスタック削除後も残る可能性があります。

## 1. 環境変数を設定する

```bash
cd /home/ubuntu/workspace/udemy2/udemy-ai-company/courses/aws-slo-adoption-course/cloudformation

export AWS_REGION=us-east-1
export STACK_NAME=aws-slo-adoption-dev-slo
export PROJECT_NAME=udemy-slo-sample
export SERVICE_NAME=sample-api
```

任意でしきい値を変更できます。

```bash
export AVAILABILITY_SLO_TARGET=99.9
export LATENCY_THRESHOLD_MS=300
export ERROR_RATE_THRESHOLD_PERCENT=1
export FAST_BURN_RATE_THRESHOLD=14
export SLOW_BURN_RATE_THRESHOLD=2
```

メール通知を試す場合だけ設定します。

```bash
export NOTIFICATION_EMAIL=you@example.com
```

SNSメール通知は、購読確認メールの承認が必要です。

## 2. テンプレートを検証する

```bash
./validate.sh validate
```

期待結果:

- CloudFormationテンプレート検証が成功する
- AWSリソースはまだ作成されない

## 3. スタックを作成する

```bash
./validate.sh create
```

作成後、CloudFormation Outputsに以下が出ます。

- `AlarmTopicArn`
- `AvailabilityAlarmName`
- `LatencyAlarmName`
- `ErrorRateAlarmName`
- `FastBurnRateAlarmName`
- `SlowBurnRateAlarmName`
- `DashboardName`

## 4. 正常系メトリクスを投入する

```bash
./validate.sh put-good
```

投入されるサンプル:

| Metric | Value |
| --- | ---: |
| Availability | 99.95% |
| Latency | 120ms |
| RequestCount | 1000 |
| ErrorCount | 1 |

CloudWatch AlarmとDashboardへの反映には数分かかる場合があります。

## 5. リソース存在確認を行う

```bash
./smoke_test.sh
```

確認内容:

- SNS Topicが存在する
- 5つのCloudWatch Alarmが存在する
- CloudWatch Dashboardが存在する
- Optional SLOを有効化した場合はSLO Outputが存在する

## 6. 異常系メトリクスを投入する

```bash
./validate.sh put-bad
```

投入されるサンプル:

| Metric | Value |
| --- | ---: |
| Availability | 98.80% |
| Latency | 650ms |
| RequestCount | 1000 |
| ErrorCount | 25 |

確認すること:

- AvailabilityがSLO目標を下回る
- Latency p99がしきい値を超える
- Error Rateが上がる
- Burn Rateが急上昇する

CloudWatch Alarmの状態変化には評価期間分の遅延があります。

## 7. スタック更新を試す

```bash
export DASHBOARD_TITLE="Updated SLO Adoption Dashboard"
./validate.sh update
```

確認すること:

- CloudFormation updateが成功する
- Dashboardのタイトルが更新される
- 既存AlarmとSNS Topicが維持される

## 8. 削除する

```bash
./validate.sh delete
```

削除後の注意:

- CloudFormation管理リソースは削除される
- CloudWatch Custom Metricsは即時削除できず、一定期間後に見えなくなる
- Application Signals SLOを有効化した場合、サービスリンクロールが残る場合がある

## まとめて検証する

新しい `STACK_NAME` で、validate、create、メトリクス投入、smoke test、update、deleteまで実行します。

```bash
export STACK_NAME=aws-slo-adoption-dev-slo-full
./validate.sh full
```

既存スタックがある名前では `full` は実行しません。

## Application Signals SLOを有効化する場合

通常の受講では必須ではありません。Application Signals SLOをCloudFormationで作る補講として扱います。

```bash
export ENABLE_APPLICATION_SIGNALS_SLO=true
./validate.sh create
```

注意:

- SLO料金が発生する場合があります
- 初回作成時にサービスリンクロールが自動作成される場合があります
- 実アプリケーションの計装や十分なメトリクスがない環境では、SLO評価が教材通りに見えない場合があります

## 失敗時の確認ポイント

AWS CLI認証:

```bash
aws sts get-caller-identity
```

CloudFormationイベント:

```bash
aws cloudformation describe-stack-events \
  --stack-name "$STACK_NAME" \
  --region "$AWS_REGION" \
  --max-items 20
```

Alarm確認:

```bash
aws cloudwatch describe-alarms \
  --alarm-names "$PROJECT_NAME-availability-slo-risk" \
  --region "$AWS_REGION"
```

Dashboard確認:

```bash
aws cloudwatch get-dashboard \
  --dashboard-name "$PROJECT_NAME-dashboard" \
  --region "$AWS_REGION"
```

よくある原因:

- `AWS_REGION` が想定と違う
- 同じ `STACK_NAME` の失敗スタックが残っている
- `PROJECT_NAME` が命名ルールに合っていない
- SNSメール購読が未承認
- CloudWatch Alarmの評価に数分かかっている
- Application Signals SLOを有効化したリージョンまたは権限が合っていない

## 学習ポイント

- SLIをCloudWatch Custom Metricsで表現する
- SLOしきい値をCloudFormation Parametersにする
- Error RateをMetric Mathで計算する
- Burn Rateを「実エラー率 ÷ 許容エラー率」で計算する
- Dashboardは運用担当と説明相手の両方を意識して設計する
- README通りに作成、更新、検証、削除できることを品質ゲートにする
