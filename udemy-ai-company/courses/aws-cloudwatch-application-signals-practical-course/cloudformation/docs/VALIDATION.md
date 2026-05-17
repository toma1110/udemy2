# CloudFormation Validation

Course: `aws-cloudwatch-application-signals-practical-course`

## 2026-05-16 Template Validation

実行内容:

```bash
cd udemy-ai-company/courses/aws-cloudwatch-application-signals-practical-course/cloudformation
./validate.sh validate
```

結果:

- PASS: `aws cloudformation validate-template`
- PASS: `bash -n validate.sh`
- PASS: `bash -n smoke_test.sh`
- PASS: `bash -n stop_traffic.sh`
- PASS: CloudFormation text safety check

出力:

```text
Template validation succeeded: cloudformation/template.yaml
```

公開用作業コピー:

- Path: `udemy-ai-company/public_repo/cloudwatch-application-signals-practical-cfn/`
- Template and validation commits are recorded in the public repo working copy history.

## 2026-05-16 Lifecycle Validation

CEO承認後、以下の一時スタックで作成、シナリオ更新、SLO作成、停止、削除まで実行しました。

- Region: `us-east-1`
- Stack: `appsignals-demo-202605161232`
- ProjectName: `appsignals-demo`
- Account: `<aws-account-id>`

実行結果:

- PASS: `./validate.sh create`
  - Stack status: `CREATE_COMPLETE`
- PASS: `./validate.sh smoke`
  - EventBridge Scheduler: `ENABLED`, `rate(1 minute)`
  - Traffic generator response: `{"scenario": "normal", "request_count": 1, "errors": []}`
  - Application Signals service discoveryは初回直後に数分遅延したが、その後 `${PROJECT_NAME}-sample-api` と `${PROJECT_NAME}-traffic-generator` が `INSTRUMENTED` として表示された
- PASS: `SCENARIO=slow ./validate.sh update`
  - Stack status: `UPDATE_COMPLETE`
  - Traffic generator response: `{"scenario": "slow", "request_count": 1, "errors": []}`
- PASS: `SCENARIO=error ERROR_RATE_PERCENT=100 ./validate.sh update`
  - Stack status: `UPDATE_COMPLETE`
  - Traffic generator response included `FunctionError: Unhandled`
  - Fault/Errorを確実に観察できるよう、`error` シナリオの既定失敗率を100%へ変更した
- PASS: `CREATE_APPLICATION_SIGNALS_SLO=true ./validate.sh update`
  - Stack status: `UPDATE_COMPLETE`
  - SLO ARN: `arn:aws:application-signals:us-east-1:<aws-account-id>:slo/appsignals-demo-availability-slo`
  - `get-service-level-objective` result: `Name=appsignals-demo-availability-slo`, `EvaluationType=RequestBased`
- PASS: `./validate.sh stop-traffic`
  - EventBridge Scheduler: `DISABLED`
- PASS: `./validate.sh delete`
  - Stack delete completed

削除後確認:

- PASS: CloudFormation stack `appsignals-demo-202605161232` does not exist
- PASS: EventBridge Scheduler group `appsignals-demo-traffic` does not exist
- PASS: Lambda function `appsignals-demo-sample-api` does not exist
- PASS: Lambda function `appsignals-demo-traffic-generator` does not exist
- PASS: CloudWatch Logs group prefix `/aws/lambda/appsignals-demo` returned no log groups
- PASS: Application Signals SLO `appsignals-demo-availability-slo` does not exist

補足:

- Application Signalsのサービス検出とメトリクス表示には数分の遅延がある
- 過去メトリクスやログ由来の表示はCloudWatch上に一定期間残る可能性があるが、実行中のサンプルリソースとスケジュールは削除済み
- `./validate.sh full` は未実行。手順ごとの結果を確認するため、今回は個別コマンドでライフサイクルを実行した

## 重要な制約

- 初回createでは `CreateApplicationSignalsSlo=false` を使う
- Application SignalsのServices画面または `smoke_test.sh` で `${PROJECT_NAME}-sample-api` が見えてから、`CREATE_APPLICATION_SIGNALS_SLO=true ./validate.sh update` を実行する
- Application Signals SLOは、対象サービスまたは操作が標準メトリクスを報告する前には作成できない
- ハンズオン後は `./stop_traffic.sh` と `./validate.sh delete` を実行する
