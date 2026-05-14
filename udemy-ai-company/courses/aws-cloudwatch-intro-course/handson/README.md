# VID-001 Hands-on: CloudWatchの地図を確認する

## Goal

CloudWatchの4つの基本部品を、作る前に説明できる状態にします。

| 部品 | 何を見るか | ひとことで |
| --- | --- | --- |
| Metrics | 数値の時系列 | どれくらいか |
| Logs | 出来事の記録 | 何が起きたか |
| Alarm | 条件と状態 | 危ないか |
| Dashboard | 表示面 | まとめて見る |

## Prerequisites

- 必須のAWSリソース作成はありません。
- AWSアカウントがある場合はCloudWatchコンソールを開けると理解しやすくなります。
- AWSアカウントがない場合は、このREADMEの表を埋めるだけで完了できます。

## Do Not Create Resources

このハンズオンでは以下を作成しません。

- CloudWatch Dashboard
- CloudWatch Alarm
- Custom Metric
- Log Group
- SNS Topic
- CloudFormation stack

## Step 1: Metricsの場所を確認する

AWSアカウントがある場合:

1. AWSマネジメントコンソールでCloudWatchを開く。
2. 左メニューからMetricsを開く。
3. `AWS/EC2`、`AWS/Lambda`、`AWS/Billing` などのnamespaceが見えるか確認する。
4. 既存リソースがない場合は、namespaceが少なくても問題ない。

確認すること:

| 観点 | メモ |
| --- | --- |
| namespaceは何のまとまりか | サービスや用途ごとのメトリクスの棚 |
| metricは何か | 時間ごとに並ぶ数値 |
| dimensionは何か | どの対象の数値かを決めるラベル |

## Step 2: Logsの場所を確認する

AWSアカウントがある場合:

1. CloudWatchの左メニューからLogsを開く。
2. Log groupsを確認する。
3. 既存アプリケーションがなければ、ロググループが空でも問題ない。

確認すること:

| 観点 | メモ |
| --- | --- |
| log group | ログのまとまり |
| log stream | 同じまとまり内の細かい流れ |
| metricsとの違い | 数値ではなく出来事の記録 |

## Step 3: Alarmsの場所を確認する

AWSアカウントがある場合:

1. CloudWatchの左メニューからAlarmsを開く。
2. All alarmsを確認する。
3. 既存アラームがなくても問題ない。

確認すること:

| 観点 | メモ |
| --- | --- |
| OK | 条件を超えていない状態 |
| ALARM | 条件を超えている状態 |
| INSUFFICIENT_DATA | 判断に必要なデータが足りない状態 |
| action | 通知や自動処理につながる部分 |

## Step 4: Dashboardsの場所を確認する

AWSアカウントがある場合:

1. CloudWatchの左メニューからDashboardsを開く。
2. 既存ダッシュボードがあるか確認する。
3. 新規作成はしない。

確認すること:

| 観点 | メモ |
| --- | --- |
| dashboard | 複数の情報を見る表示面 |
| widget | 表示部品 |
| データ源 | メトリクス、アラーム、ログなど |

## Step 5: 自分の言葉で地図を書く

以下を埋めて完了です。

| 質問 | 回答 |
| --- | --- |
| Metricsは何を見る場所か |  |
| Logsは何を見る場所か |  |
| Alarmは何を判断するものか |  |
| Dashboardは何のために使うか |  |
| 障害時は最初にどこを見るか |  |

## Completion Criteria

- Metrics、Logs、Alarm、Dashboardを1文ずつ説明できる
- Dashboardがデータ保存場所ではなく表示面だと説明できる
- Alarmがメトリクスと条件をもとに状態を判断すると説明できる
- リソースを新規作成していない

## Cost and Cleanup

このREADME通りに進める限り、リソース作成はありません。

手順外でダッシュボード、アラーム、カスタムメトリクス、ログ投入をした場合は、CloudWatch料金が発生する可能性があります。手順外で作成したものは自分で削除してください。

## Production IaC Note

実運用でCloudWatchのアラーム、ダッシュボード、ロググループを管理する場合は、CDKまたはTerraformを使う前提で設計します。

CloudFormationは、講座内ハンズオンで受講者が追加ツールなしにREADME通り再現するための選択肢として扱います。
