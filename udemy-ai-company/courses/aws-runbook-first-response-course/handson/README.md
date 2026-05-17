# Handson

本コースv1の標準ハンズオンは、AWSリソースを作成しないRunbook作成演習です。

## Exercise: CloudWatch Alarm用Runbookを書く

前提アラート:

```text
Alarm: [P2][Orders] API 5xx rate high
Trigger: 5分間の5xx率が2%を超過
Service: 注文API
```

作るもの:

- Trigger
- Owner
- Severity
- Scope
- First Checks
- Mitigation
- Escalation
- Communication
- Postmortem Link

## Review Questions

- 5分以内に確認することだけに絞れているか
- 誰が動くか明確か
- いつエスカレーションするか明確か
- 緩和策と原因調査を混同していないか
- 復旧後に何を記録するか明確か

## AWS実行

標準演習では実行しません。

実AWSでCloudWatch Alarm、Systems Manager Automation、Incident Manager、CloudFormationを利用する場合は、CEO承認後に別チケットを作成します。
