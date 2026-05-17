# AWS CloudWatch Logs Insights実践 カリキュラム入力表

このファイルはUdemyのコースカリキュラム作成時に使うレクチャー一覧です。`course_spec.md` と `course_infomation.md` をSource of Truthとして、各レクチャーで受講後に身についていること、ハンズオン有無、ハンズオンリソースタイトル、ハンズオンURL、動画再生成方針を明記します。

Course ID: `aws-cloudwatch-logs-insights-practical-course`
Course Title: `AWS CloudWatch Logs Insights実践: 障害調査クエリ集`
Source Candidate: `VID-004`
Standard Hands-on Policy: AWSリソース作成なし。サンプルログとクエリ読解を標準手順とし、既存ロググループがある受講者だけ短い時間範囲で任意実行する。
Planned Runtime: 通常レクチャー8本、講義本編合計32〜40分。プロモーション動画は30分要件に含めない。
Review Status: 動画再生成前に、CEOが `course_spec.md`、`course_infomation.md`、本 `course_curriculum.md` を確認・承認する。
PublicRepo: なし。標準ハンズオンはコース内 `handson/` のサンプルログとクエリ集を使う。

## Section 1: クエリの安全運転と基本形

セクションの学習目標: Logs Insightsで最初に確認するロググループ、時間範囲、自動生成フィールド、基本構文を理解し、スキャン量と料金を抑えながら調査を始められる。

| Lecture | レクチャータイトル | レクチャー完了後に身についていること | 予定尺 | ハンズオン | ハンズオンリソースタイトル | ハンズオンURL | 再生成ステータス |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Logs Insights実践の地図 | 障害調査でLogs Insightsが担当する範囲と、このコースで扱うクエリパターン全体を説明できる | 4〜5分 | なし | 調査フロー地図 | なし | CEO確認待ち |
| 2 | ロググループと時間範囲 | クエリ実行前にロググループと時間範囲を絞り、スキャン量と料金リスクを抑える判断ができる | 4〜5分 | あり | Logs Insights安全運転チェック | `handson/README.md#logs-insights安全運転チェック` | CEO確認待ち |
| 3 | 基本構文: fields/filter/sort/limit | `fields`、`filter`、`sort`、`limit` を使った直近ログ確認とエラー検索の基本形を読める | 4〜5分 | あり | 基本クエリ読解 | `handson/queries/01_recent_events.sql` | CEO確認待ち |

## Section 2: 障害調査クエリ集

セクションの学習目標: エラー、例外、タイムアウト、5xx、遅延、requestId追跡を目的別に整理し、障害調査時に最初のクエリを選べる。

| Lecture | レクチャータイトル | レクチャー完了後に身についていること | 予定尺 | ハンズオン | ハンズオンリソースタイトル | ハンズオンURL | 再生成ステータス |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | エラーと例外を探す | ERROR、Exception、timeout、5xxを探すクエリを目的別に使い分けられる | 4〜5分 | あり | エラー検索クエリ | `handson/queries/02_error_search.sql` | CEO確認待ち |
| 5 | stats/binで傾向を見る | `stats` と `bin()` で時間ごとの件数、上位エラー、遅延パーセンタイルを集計できる | 4〜5分 | あり | 傾向集計クエリ | `handson/queries/03_error_trend.sql` | CEO確認待ち |
| 6 | parseとrequestId追跡 | JSONログと非構造ログの読み方を分け、`parse` とrequestIdで一連の出来事を追跡できる | 4〜5分 | あり | requestId追跡クエリ | `handson/queries/06_request_trace.sql` | CEO確認待ち |

## Section 3: 2026年版の発展機能

セクションの学習目標: `pattern`、`anomaly`、`JOIN`、subquery、`SOURCE` の位置づけと注意点を理解し、実務では小さく始めて必要な時だけ調査範囲を広げる判断ができる。

| Lecture | レクチャータイトル | レクチャー完了後に身についていること | 予定尺 | ハンズオン | ハンズオンリソースタイトル | ハンズオンURL | 再生成ステータス |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | pattern/anomalyで未知の変化を見る | `pattern` と `anomaly` を、未知のログ変化や異常の入口として使う場面を説明できる | 4〜5分 | あり | pattern/anomaly読解 | `handson/queries/09_pattern_anomaly.sql` | CEO確認待ち |
| 8 | JOIN/subquery/SOURCEの入口 | 複数ロググループ相関、入れ子クエリ、タグ指定クエリの使いどころと制約を説明できる | 4〜5分 | あり | JOIN/subquery/SOURCEメモ | `handson/queries/10_join_subquery_source.sql` | CEO確認待ち |

## Hands-on Resources

| Resource Title | Location | Required AWS Resources | Notes |
| --- | --- | --- | --- |
| Logs Insights安全運転チェック | `handson/README.md#logs-insights安全運転チェック` | なし | 実行前にロググループ、時間範囲、limit、キャンセル方法を確認する |
| サンプルログ読解 | `handson/sample_logs/` | なし | AWSアカウントなしでもクエリの意図を読める |
| 基本クエリ読解 | `handson/queries/01_recent_events.sql` | 任意の既存ロググループ | 実行する場合は直近5〜15分など短い時間範囲にする |
| エラー検索クエリ | `handson/queries/02_error_search.sql` | 任意の既存ロググループ | ログ形式に合わせて条件を調整する |
| 傾向集計クエリ | `handson/queries/03_error_trend.sql` | 任意の既存ロググループ | `bin(5m)` を基本にし、広い期間を避ける |
| requestId追跡クエリ | `handson/queries/06_request_trace.sql` | requestIdを含むログ | サンプルログで読解可能。実ログ実行は任意 |
| pattern/anomaly読解 | `handson/queries/09_pattern_anomaly.sql` | 任意の既存ロググループ | まず読み方を扱い、実行は最小範囲にする |
| JOIN/subquery/SOURCEメモ | `handson/queries/10_join_subquery_source.sql` | 任意の既存ロググループ | 発展機能の入口として扱い、大量スキャンを避ける |

## Runtime Remediation Notes

2026-05-17時点の監査では、既存の通常レクチャーMP4は8本、合計約11.7分であり、Udemy標準コースとして確認するには短すぎます。本ファイルでは、レクチャー構成は8本のまま維持し、各レクチャーを4〜5分へ拡張する確認用カリキュラムとして再整理しています。

動画再生成時の方針:

- 各レクチャーはクエリの読み方、実務判断、料金注意、よくある失敗、復習を含める
- 完成動画スライドはGPT-Image2由来PNGだけを使う
- 完成動画に表示する文字もGPT-Image2に生成させる
- ナレーションはVOICEVOXを使う
- 動画再生成はCEO確認後に開始する
- WorkerとReviewerを分離する

## Final Deliverables After Approval

- `scripts/<lecture_id>_script.md`
- `scripts/<lecture_id>_script.json`
- `slides/<lecture_id>_gpt_image_prompts.md`
- GPT-Image2 source PNG and fitted final PNG
- VOICEVOX WAV
- MP4 video
- QA report
- Google Drive upload report
