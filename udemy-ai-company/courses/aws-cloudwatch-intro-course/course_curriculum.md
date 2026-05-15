# Course Curriculum

## Course

- Course ID: `aws-cloudwatch-intro-course`
- Course title: `AWS CloudWatch入門: Metrics・Logs Insights・Alarm・Dashboardで学ぶ監視の基本`
- Source of Truth: `course_spec.md`

## Section 1: CloudWatchの地図

### Section Learning Objectives

- CloudWatchの主要部品を役割ごとに分けられる
- Metrics、Logs、Alarm、Dashboardの関係を説明できる
- メトリクスとログを混同せず、調査で見る場所を選べる

| Lecture | Title | Learning Objective | Hands-on Resource Title |
| --- | --- | --- | --- |
| `s1-l1` | CloudWatchの地図 | Metrics、Logs、Alarm、Dashboardの違いとつながりを説明できる | CloudWatch地図ワークシート |
| `s1-l2` | Metricsの基本 | namespace、metric、dimension、statistic、periodを使ってメトリクスを探す考え方を説明できる | Metrics確認メモ |
| `s1-l3` | Logsの基本 | log group、log stream、ログイベントを区別し、メトリクスとの違いを説明できる | Logs確認メモ |

## Section 2: Logs Insightsでログを読む

### Section Learning Objectives

- Logs Insightsの基本クエリを読める
- エラー調査で使う最初のクエリを選べる
- クエリ料金を抑えるために、ロググループと時間範囲を絞れる

| Lecture | Title | Learning Objective | Hands-on Resource Title |
| --- | --- | --- | --- |
| `s2-l1` | Logs Insights入門 | `fields`、`filter`、`sort`、`limit`、`stats`、`bin`の基本形を読める | Logs Insightsクエリ読解 |
| `s2-l2` | Logs Insightsで障害調査 | 最近のエラー、エラー件数、遅延、リクエスト単位の追跡という調査の型を説明できる | 障害調査クエリ集 |

## Section 3: Alarm/Dashboardと調査フロー

### Section Learning Objectives

- Alarmの状態とアクションの関係を説明できる
- Dashboardをデータ保存場所ではなく表示面として説明できる
- 障害時にDashboard、Alarm、Metrics、Logs Insightsの順番を選べる

| Lecture | Title | Learning Objective | Hands-on Resource Title |
| --- | --- | --- | --- |
| `s3-l1` | Alarm/Dashboardと次の一歩 | Alarm、Dashboard、Metrics、Logs Insightsを使った障害時の見始め方を説明できる | 障害調査の見始め方チェック |

## Hands-on Resources

| Resource Title | Location | Required AWS Resources | Notes |
| --- | --- | --- | --- |
| CloudWatch地図ワークシート | `handson/README.md` | なし | AWSアカウントがなくても実施可能 |
| Metrics確認メモ | `handson/README.md#metrics確認メモ` | なし | 既存メトリクスがあれば画面で確認 |
| Logs確認メモ | `handson/README.md#logs確認メモ` | なし | 既存ロググループがなくても読解で完了 |
| Logs Insightsクエリ読解 | `handson/README.md#logs-insightsクエリ読解` | 任意の既存ロググループ | 実行する場合は時間範囲を短くする |
| 障害調査クエリ集 | `handson/README.md#障害調査クエリ集` | 任意の既存ロググループ | 実行せず読むだけでも完了 |
| 障害調査の見始め方チェック | `handson/README.md#障害調査の見始め方チェック` | なし | 実務で見る順番を整理する |
