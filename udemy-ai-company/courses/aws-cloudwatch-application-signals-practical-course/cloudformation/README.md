# CloudFormationハンズオン

このディレクトリには、Application Signals実践講座のCloudFormationテンプレートを配置します。

公開用作業コピーは `udemy-ai-company/public_repo/cloudwatch-application-signals-practical-cfn/` に配置します。

## 方針

- サンプルアプリと低頻度トラフィックをCloudFormationで作る
- Application Signalsを有効化する
- Application Signals SLOはメトリクス確認後にオプションで作る
- 自動トラフィック停止、更新、削除を必須手順にする
- 実行系コマンドはCEO承認後にのみ実行する

## 構成ファイル

- `template.yaml`
- `validate.sh`
- `smoke_test.sh`
- `stop_traffic.sh`
- `docs/VALIDATION.md`

## テンプレートを読む

主なリソース:

- `AWS::ApplicationSignals::Discovery`
- `AWS::ApplicationSignals::ServiceLevelObjective`（初回createでは無効、メトリクス確認後のupdateで有効化）
- `AWS::Lambda::Function`
- `AWS::IAM::Role`
- `AWS::Logs::LogGroup`
- `AWS::Scheduler::Schedule`
- `AWS::Scheduler::ScheduleGroup`

標準構成はLambda 2本です。

```text
EventBridge Scheduler
  -> Traffic Generator Lambda
      -> Sample API Lambda
          -> normal / slow / error / recovery

Application Signals
  -> Services
  -> Application Map
  -> Service detail
  -> SLO
```

Lambda Function URLは使いません。公開HTTPエンドポイントを作らず、Traffic GeneratorからLambda InvokeでSample APIを呼び出します。

## 作成する

AWSリソースを作成します。CEO承認後にのみ実行します。

```bash
export AWS_REGION=us-east-1
export STACK_NAME=appsignals-demo-dev
export PROJECT_NAME=appsignals-demo

./validate.sh validate
./validate.sh create
./validate.sh smoke
```

Application SignalsのServices画面に反映されるまで数分かかる場合があります。

## シナリオを切り替える

`SCENARIO` を変えてstack updateします。

```bash
SCENARIO=normal ./validate.sh update
SCENARIO=slow ./validate.sh update
SCENARIO=error ERROR_RATE_PERCENT=100 ./validate.sh update
SCENARIO=recovery ./validate.sh update
```

シナリオ:

| Scenario | 動作 | 見るポイント |
| --- | --- | --- |
| `normal` | Sample APIが正常応答する | 正常時のCall volume、Latency、Availability |
| `slow` | Sample APIが意図的に遅延する | Latency悪化 |
| `error` | Sample APIが例外を出す | Fault/Error、Availability低下 |
| `recovery` | 正常応答へ戻す | 回復後のグラフ |

## SLOを確認する

初回createではApplication Signals SLOを作りません。

理由: Application SignalsのSLOは、対象サービスまたは操作が標準メトリクスを報告した後でないと作成できません。まずアプリと低頻度トラフィックを作成し、Services画面または `smoke_test.sh` でサービスが見えることを確認します。

メトリクス確認後、以下でAvailability SLOを有効化します。

```bash
CREATE_APPLICATION_SIGNALS_SLO=true ./validate.sh update
CREATE_APPLICATION_SIGNALS_SLO=true ./validate.sh smoke
```

作成されるSLO:

- Name: `${PROJECT_NAME}-availability-slo`
- Type: request-based SLO
- Target service: `${PROJECT_NAME}-sample-api`
- Environment: `lambda:default`
- SLI: `AVAILABILITY`

## 停止と削除

ハンズオン後は、まず自動トラフィックを止めます。

```bash
./stop_traffic.sh
```

その後、スタックを削除します。

```bash
./validate.sh delete
```

CloudWatch Logs、Application Signals、SLO、Lambda、EventBridge Schedulerなどで料金が発生する場合があります。削除後にBilling / Cost Explorerも確認してください。

## 実装前に確認すること

- AWS Lambda Layer for OpenTelemetry ARN
- 対応リージョン
- 最小権限IAM
- EventBridge Schedulerの低頻度実行設定
- Application Signals課金要素
- 削除後に残る可能性があるサービスリンクロールやログの扱い

## 公式仕様確認メモ

- LambdaでApplication Signalsを有効化するには、AWS Lambda Layer for OpenTelemetry、`AWS_LAMBDA_EXEC_WRAPPER=/opt/otel-instrument`、`CloudWatchLambdaApplicationSignalsExecutionRolePolicy` が必要
- `AWS::ApplicationSignals::Discovery` はサービス検出用のサービスリンクロールを作成する
- Application Signals SLOは、対象サービス/操作がメトリクスを報告した後で作る
- SLO、Application Signals、CloudWatch Logs、Lambda、EventBridge Schedulerは料金が発生する可能性がある
