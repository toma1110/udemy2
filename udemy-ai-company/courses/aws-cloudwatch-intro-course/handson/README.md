# VID-001 Hands-on: CloudWatchの地図とLogs Insightsを確認する

## Goal

CloudWatchの基本部品を、作る前に説明できる状態にします。既存ログがある場合は、Logs Insightsの基本クエリも短い時間範囲で確認します。

| 部品 | 何を見るか | ひとことで |
| --- | --- | --- |
| Metrics | 数値の時系列 | どれくらいか |
| Logs | 出来事の記録 | 何が起きたか |
| Logs Insights | ログ検索と集計 | どこで何が多いか |
| Alarm | 条件と状態 | 危ないか |
| Dashboard | 表示面 | まとめて見る |

## Prerequisites

- 必須のAWSリソース作成はありません。
- AWSアカウントがある場合はCloudWatchコンソールを開けると理解しやすくなります。
- 既存ロググループがある場合だけ、Logs Insightsのサンプルクエリを任意で実行します。
- AWSアカウントや既存ログがない場合は、このREADMEの表とクエリ例を読むだけで完了できます。

## Do Not Create Resources

このハンズオンでは以下を作成しません。

- CloudWatch Dashboard
- CloudWatch Alarm
- Custom Metric
- Log Group
- SNS Topic
- CloudFormation stack
- サンプルアプリケーション

## Cost Safety

このREADME通りに進める限り、リソース作成はありません。

Logs Insightsを任意で実行する場合は、ログ検索のスキャン量に応じた料金が発生する可能性があります。以下を守ってください。

- 必要なロググループだけを選ぶ
- 時間範囲を短くする
- 実行中の不要なクエリはキャンセルする
- ダッシュボードにLogs Insights結果を追加しない
- 手順外でリソースを作成しない

## Step 1: CloudWatch地図ワークシート

以下を埋めて、まず地図を作ります。

| 質問 | 回答 |
| --- | --- |
| Metricsは何を見る場所か |  |
| Logsは何を見る場所か |  |
| Logs Insightsは何をする場所か |  |
| Alarmは何を判断するものか |  |
| Dashboardは何のために使うか |  |
| 障害時は最初にどこを見るか |  |

## Step 2: Metrics確認メモ

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
| statisticは何か | 平均、最大、合計など、期間内のまとめ方 |
| periodは何か | 1分、5分など、集計する時間幅 |

## Step 3: Logs確認メモ

AWSアカウントがある場合:

1. CloudWatchの左メニューからLogsを開く。
2. Log groupsを確認する。
3. 既存アプリケーションがなければ、ロググループが空でも問題ない。

確認すること:

| 観点 | メモ |
| --- | --- |
| log group | ログのまとまり |
| log stream | 同じまとまり内の細かい流れ |
| log event | 時刻とメッセージを持つ1つの出来事 |
| metricsとの違い | 数値ではなく出来事の記録 |

## Step 4: Logs Insightsクエリ読解

既存ロググループがある場合だけ、CloudWatch Logs Insightsを開きます。実行する場合は、時間範囲を直近5分から15分程度に絞ります。

### Query 1: 最近のログを見る

```sql
fields @timestamp, @message
| sort @timestamp desc
| limit 20
```

読むポイント:

| 行 | 意味 |
| --- | --- |
| `fields @timestamp, @message` | 表示する列を選ぶ |
| `sort @timestamp desc` | 新しい順に並べる |
| `limit 20` | 表示件数を20件に絞る |

### Query 2: エラーらしいログを見る

```sql
fields @timestamp, @message, @logStream
| filter @message like /ERROR/
| sort @timestamp desc
| limit 50
```

読むポイント:

| 行 | 意味 |
| --- | --- |
| `filter @message like /ERROR/` | メッセージにERRORを含む行へ絞る |
| `@logStream` | どの流れから出たログかを見る |

### Query 3: 時間ごとの件数を見る

```sql
fields @timestamp, @message
| filter @message like /ERROR/
| stats count(*) as errorCount by bin(5m)
| sort errorCount desc
```

読むポイント:

| 行 | 意味 |
| --- | --- |
| `stats count(*)` | 件数を数える |
| `by bin(5m)` | 5分ごとにまとめる |
| `sort errorCount desc` | 件数が多い時間帯を上に出す |

## Step 5: 障害調査クエリ集

このセクションは、実行しなくても読解で完了できます。対象ログの形式によって、そのまま動かない場合があります。

### 最近のエラー

```sql
fields @timestamp, @message, @logStream
| filter @message like /ERROR/ or @message like /Exception/
| sort @timestamp desc
| limit 100
```

### ラムダ関数の遅い実行を探す

```sql
filter @type = "REPORT"
| fields @timestamp, @requestId, @duration, @billedDuration, @memorySize, @maxMemoryUsed
| filter @duration > 1000
| sort @duration desc
| limit 20
```

### リクエスト単位で重複を抑える

```sql
fields @timestamp, @requestId, @message
| filter @message like /ERROR/
| dedup @requestId
| sort @timestamp desc
| limit 50
```

## Step 6: Alarmsの場所を確認する

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

## Step 7: Dashboardsの場所を確認する

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

## Step 8: 障害調査の見始め方チェック

以下の順番を、自分の言葉で説明できれば完了です。

| 順番 | 見る場所 | 目的 |
| --- | --- | --- |
| 1 | Dashboard | 全体の異常を見つける |
| 2 | Alarm | どの条件が問題か確認する |
| 3 | Metrics | 数字の変化と時間帯を確認する |
| 4 | Logs Insights | その時間帯の出来事を探す |
| 5 | 次の行動 | 通知、復旧、恒久対応へつなげる |

## Completion Criteria

- Metrics、Logs、Logs Insights、Alarm、Dashboardを1文ずつ説明できる
- namespace、metric、dimension、statistic、periodを区別できる
- log group、log stream、log eventを区別できる
- Logs Insightsの基本クエリを読める
- Dashboardがデータ保存場所ではなく表示面だと説明できる
- Alarmがメトリクスと条件をもとに状態を判断すると説明できる
- リソースを新規作成していない

## Production IaC Note

実運用でCloudWatchのアラーム、ダッシュボード、ロググループを管理する場合は、CDKまたはTerraformを使う前提で設計します。

CloudFormationは、講座内ハンズオンで受講者が追加ツールなしにREADME通り再現するための選択肢として扱います。
