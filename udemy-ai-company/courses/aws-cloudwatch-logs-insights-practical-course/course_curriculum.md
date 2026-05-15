# Course Curriculum

## Course

- Course ID: `aws-cloudwatch-logs-insights-practical-course`
- Course Title: `AWS CloudWatch Logs Insights実践: 障害調査クエリ集`
- Source Candidate: `VID-004`
- Source of Truth: `course_spec.md`

## Section 1: クエリの安全運転と基本形

### Section Learning Objectives

- Logs Insightsでロググループと時間範囲を絞る理由を説明できる
- `@timestamp`、`@message`、`@logStream`、`@log` を使ってログを読む入口を作れる
- `fields`、`filter`、`sort`、`limit` の基本形を読める

### Hands-on Resource Title

`Logs Insights安全運転チェック`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Production Status |
| --- | --- | --- | --- | --- |
| `s1-l1` | Logs Insights実践の地図 | 障害調査でLogs Insightsが担当する範囲を説明できる | 調査フロー地図 | Planned |
| `s1-l2` | ロググループと時間範囲 | スキャン量を抑える実行前チェックを説明できる | Logs Insights安全運転チェック | Planned |
| `s1-l3` | 基本構文: fields/filter/sort/limit | 直近ログとエラー検索の基本クエリを読める | 基本クエリ読解 | Planned |

## Section 2: 障害調査クエリ集

### Section Learning Objectives

- エラー、例外、タイムアウトを探すクエリを選べる
- `stats` と `bin()` で時間帯ごとの傾向を集計できる
- JSONフィールド、`parse`、requestId、`dedup` を使った追跡の考え方を説明できる

### Hands-on Resource Title

`障害調査クエリ集`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Production Status |
| --- | --- | --- | --- | --- |
| `s2-l1` | エラーと例外を探す | ERROR、Exception、timeout、5xxの探し方を説明できる | エラー検索クエリ | Planned |
| `s2-l2` | stats/binで傾向を見る | 時間ごとの件数、上位エラー、遅延パーセンタイルを集計できる | 傾向集計クエリ | Planned |
| `s2-l3` | parseとrequestId追跡 | 非構造ログから値を取り出し、requestIdで一連の出来事を追える | requestId追跡クエリ | Planned |

## Section 3: 2026年版の発展機能

### Section Learning Objectives

- `pattern` と `anomaly` の使いどころを説明できる
- `JOIN`、subquery、`SOURCE` の対象と制約を説明できる
- 実務で「まず小さく、必要な時だけ広げる」クエリ設計を選べる

### Hands-on Resource Title

`2026年版Logs Insights発展機能メモ`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Production Status |
| --- | --- | --- | --- | --- |
| `s3-l1` | pattern/anomalyで未知の変化を見る | ログパターンと異常検知を調査入口として説明できる | pattern/anomaly読解 | Planned |
| `s3-l2` | JOIN/subquery/SOURCEの入口 | 複数ロググループ相関、入れ子クエリ、タグ指定の位置づけを説明できる | JOIN/subquery/SOURCEメモ | Planned |

## Hands-on Resources

| Resource Title | Location | Required AWS Resources | Notes |
| --- | --- | --- | --- |
| Logs Insights安全運転チェック | `handson/README.md#logs-insights安全運転チェック` | なし | AWSアカウントなしでも読解可能 |
| 基本クエリ読解 | `handson/queries/01_recent_events.sql` | 任意の既存ロググループ | 実行する場合は時間範囲を短くする |
| エラー検索クエリ | `handson/queries/02_error_search.sql` | 任意の既存ロググループ | ログ形式に合わせて条件を調整 |
| 傾向集計クエリ | `handson/queries/03_error_trend.sql` | 任意の既存ロググループ | `bin(5m)` を基本にする |
| requestId追跡クエリ | `handson/queries/06_request_trace.sql` | requestIdを含むログ | サンプルログで読解可能 |
| 2026年版発展機能メモ | `handson/README.md#2026年版の発展機能` | 任意 | 実行は上級者向け |

## Final Deliverables

- `scripts/*_script.md`
- `scripts/*_script.json`
- `slides/*_gpt_image_prompts.md`
- GPT-Image2 source PNG and fitted final PNG
- VOICEVOX WAV
- MP4 video
- QA report
- Google Drive upload report
