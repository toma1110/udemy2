# Handson

本コースv1の標準ハンズオンは、AWSリソースを作成しない設計演習です。

## Exercise 1: 悪いアラートをレビューする

悪い例:

```text
Alarm: CPUHigh
Message: CPUが80%を超えました。
Notify: #all-engineers
```

確認する観点:

- 影響範囲が分かるか
- Severityが分かるか
- Ownerが分かるか
- Runbookがあるか
- 次の5分で何をすべきか分かるか

## Exercise 2: 良いアラートへ直す

改善例:

```text
Alarm: [P2][Payments] API latency SLO burn warning
Condition: 5分間でP99 latency > 2s が 3 out of 5
Impact: 決済APIの一部ユーザーで応答遅延
Owner: payments-oncall
Runbook: docs/runbooks/payment-latency.md
Escalation: 15分で改善しない場合はincident-commanderへ連絡
```

## Exercise 3: CloudWatch設定に落とす

設計メモ:

- Period: 60 seconds
- Evaluation Periods: 5
- Datapoints to Alarm: 3
- Missing data: メトリクス種別により選ぶ
- Composite Alarm: ユーザー影響と原因候補を組み合わせて通知数を減らす

## AWS実行

標準演習では実行しません。

実AWSでCloudWatch Alarm、SNS、Composite Alarmを作成する場合は、CEO承認後に別チケットを作成します。
