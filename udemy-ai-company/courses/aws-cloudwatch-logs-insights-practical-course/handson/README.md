# Logs Insights Hands-on

## Goal

CloudWatch Logs Insightsで、障害調査に使うクエリの型を読める状態にします。

標準手順ではAWSリソースを作成しません。既存ロググループがある場合だけ、短い時間範囲で任意実行します。AWSアカウントや既存ログがない場合は、`sample_logs/` と `queries/` を読んで完了できます。

## Logs Insights安全運転チェック

クエリ実行前に必ず確認します。

| Check | Why |
| --- | --- |
| 必要なロググループだけ選ぶ | スキャン量を増やさない |
| 時間範囲を短くする | 直近5分から15分で始める |
| まず `limit` を付ける | 結果を小さく見る |
| 不要な実行中クエリをキャンセルする | コンソールを閉じてもクエリは完了まで動く可能性がある |
| Dashboardに追加しない | 更新のたびにクエリが走る可能性がある |
| JOIN/subquery/SOURCEは読解から始める | スキャン範囲とコストが広がりやすい |

## Files

| Path | Purpose |
| --- | --- |
| `sample_logs/application.jsonl` | 構造化アプリログの読解用 |
| `sample_logs/api_access.jsonl` | APIアクセスログの読解用 |
| `sample_logs/lambda_report.txt` | Lambda REPORTログの読解用 |
| `queries/*.sql` | Logs Insightsクエリ集 |

## Step 1: サンプルログを読む

`sample_logs/application.jsonl` の1行を見て、フィールドを確認します。

```json
{"timestamp":"2026-05-15T09:00:02Z","service":"checkout","level":"ERROR","requestId":"req-1003","path":"/checkout","statusCode":502,"durationMs":1420,"errorType":"PaymentTimeout","message":"payment provider timeout after 1200ms"}
```

| Field | Meaning |
| --- | --- |
| `service` | どのサービスのログか |
| `level` | INFO、WARN、ERRORなど |
| `requestId` | 一連の処理を追うキー |
| `statusCode` | HTTP結果 |
| `durationMs` | 処理時間 |
| `errorType` | エラー分類 |

## Step 2: 基本クエリを読む

最初に読むクエリ:

- `queries/01_recent_events.sql`
- `queries/02_error_search.sql`
- `queries/03_error_trend.sql`

読む順番:

1. `fields` で表示列を選ぶ
2. `filter` で対象を絞る
3. `sort` で並べる
4. `limit` で件数を抑える
5. `stats` と `bin()` で集計する

## Step 3: 障害調査クエリ集

| Query | Use case |
| --- | --- |
| `01_recent_events.sql` | 直近ログを確認する |
| `02_error_search.sql` | ERROR、Exception、timeoutを探す |
| `03_error_trend.sql` | エラー件数を時間帯で見る |
| `04_top_error_types.sql` | 多いエラー種別を探す |
| `05_latency_percentiles.sql` | 遅いエンドポイントを探す |
| `06_request_trace.sql` | requestIdで一連の出来事を追う |
| `07_dedup_requests.sql` | 同じrequestIdの重複を抑える |
| `08_lambda_slow_reports.sql` | Lambda REPORTログから遅い実行を探す |
| `09_pattern_anomaly.sql` | ログパターンと異常を読む |
| `10_join_subquery_source.sql` | JOIN/subquery/SOURCEの入口を読む |

## Step 4: 既存ロググループで任意実行する

AWSアカウントと既存ロググループがある場合だけ行います。

1. CloudWatchコンソールを開く。
2. Logs Insightsを開く。
3. 必要なロググループだけを選ぶ。
4. 時間範囲を直近5分から15分にする。
5. `01_recent_events.sql` をコピーして実行する。
6. 結果件数とスキャン量を確認する。
7. 不要なクエリはキャンセルする。

既存ログの形式に合わせて、`level`、`statusCode`、`requestId` などのフィールド名は変更します。

## Step 5: 調査の型

障害時は以下の順番で考えます。

| Step | Question | Query |
| --- | --- | --- |
| 1 | 何が最近起きたか | `01_recent_events.sql` |
| 2 | エラーはあるか | `02_error_search.sql` |
| 3 | どの時間帯で増えたか | `03_error_trend.sql` |
| 4 | どの種類が多いか | `04_top_error_types.sql` |
| 5 | 遅い処理はどれか | `05_latency_percentiles.sql` |
| 6 | 1つのリクエストを追えるか | `06_request_trace.sql` |
| 7 | 重複を抑えて見られるか | `07_dedup_requests.sql` |

## 2026年版の発展機能

### pattern/anomaly

`pattern` はログメッセージを似た形にまとめます。`anomaly` はそのパターンの中から通常と違うものを見つけます。

使いどころ:

- エラー文言が多すぎて、人間が読み切れない
- 新しいログパターンが出ていないか見たい
- まず分類してから深掘りしたい

注意:

- Standard log class向けの機能として扱う
- 実行範囲を小さく始める

### JOIN/subquery/SOURCE

`JOIN` は複数ロググループのイベントを共通キーで結びます。subqueryは内側のクエリ結果を外側の条件に使います。`SOURCE` はCLI/APIでロググループを指定する時に使い、タグ指定にも対応します。

使いどころ:

- API GatewayログとLambdaログをrequestIdでつなぐ
- 下流サービスで失敗したrequestIdだけ、上流ログで追う
- タグでロググループをまとめて選びたい

注意:

- スキャン範囲が広がりやすい
- JOINは条件や制約を理解してから使う
- `SOURCE` はコンソールではなくCLI/API向け

## Completion Criteria

- Logs Insightsでロググループと時間範囲を絞る理由を説明できる
- `@timestamp`、`@message`、`@logStream`、`@log` を説明できる
- `fields`、`filter`、`sort`、`limit` の基本形を読める
- `stats` と `bin()` の集計を説明できる
- エラー検索、傾向集計、requestId追跡のクエリを選べる
- `pattern`、`anomaly`、`JOIN`、subquery、`SOURCE` の位置づけを説明できる
- 標準手順でAWSリソースを新規作成していない

## Production IaC Note

実運用でCloudWatch Logs、Alarm、Dashboardを管理する場合は、CDKまたはTerraformを使う前提で設計します。

CloudFormationは、教材ハンズオンで受講者が追加ツールなしにREADME通り再現するための選択肢として扱います。
