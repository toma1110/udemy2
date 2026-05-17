# AWS CloudWatch Logs Insights実践 カリキュラム

Source of Truth: `course_spec.md`

## Course

- Course ID: `aws-cloudwatch-logs-insights-practical-course`
- Course Title: `AWS CloudWatch Logs Insights実践: 障害調査クエリ集`
- Course Information: `course_infomation.md`
- Target Lecture Count: 8
- Target Main Lecture Runtime: 32〜40分
- Current Audit Result: 2026-05-17に通常レクチャー8本を再生成済み。合計2058.560秒、約34.31分で、Udemy標準コースの30分要件を満たしている。

## Curriculum Review Gate

- 2026-05-17にCEOがカリキュラムを承認済み。
- プロモーション動画は通常レクチャーの30分要件に含めない。
- 2026-05-17に全レクチャーの台本、VOICEVOX音声、MP4を一括で再生成済み。
- 完成動画のスライドと表示文字はGPT-Image2由来PNGに限定する。
- WorkerとReviewerは分離する。

## Section 1: クエリの安全運転と基本形

Section Learning Goal: Logs Insightsで調査を始める前に、ロググループ、時間範囲、基本構文、スキャン量を安全に扱える。

Hands-on Resource Title: `Logs Insights安全運転チェック`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Target Runtime | Production Status |
| --- | --- | --- | --- | --- | --- |
| `s1-l1` | Logs Insights実践の地図 | 障害調査でLogs Insightsが担当する範囲と、Metrics/Alarmとの違いを説明できる | 調査フロー地図 | 4〜5分 | Produced - runtime remediated 2026-05-17 |
| `s1-l2` | ロググループと時間範囲 | スキャン量を抑えるために、対象ロググループと時間範囲を絞る理由を説明できる | Logs Insights安全運転チェック | 4〜5分 | Produced - runtime remediated 2026-05-17 |
| `s1-l3` | 基本構文: fields/filter/sort/limit | 直近ログを見る基本形、並び替え、件数制限、料金注意を説明できる | 基本クエリ読解 | 4〜5分 | Produced - runtime remediated 2026-05-17 |

## Section 2: 障害調査クエリ集

Section Learning Goal: エラー、例外、傾向、遅延、requestId追跡を、実務で使うクエリの型として選べる。

Hands-on Resource Title: `障害調査クエリ集`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Target Runtime | Production Status |
| --- | --- | --- | --- | --- | --- |
| `s2-l1` | エラーと例外を探す | ERROR、Exception、timeout、5xxを探すクエリと、誤検知しやすい条件を説明できる | エラー検索クエリ | 4〜5分 | Produced - runtime remediated 2026-05-17 |
| `s2-l2` | stats/binで傾向を見る | `stats` と `bin()` で時間ごとの件数、上位エラー、遅延傾向を集計できる | 傾向集計クエリ | 4〜5分 | Produced - runtime remediated 2026-05-17 |
| `s2-l3` | parseとrequestId追跡 | JSONログ、非構造ログ、`parse`、requestId、`dedup` の使い分けを説明できる | requestId追跡クエリ | 4〜5分 | Produced - runtime remediated 2026-05-17 |

## Section 3: 2026年版の発展機能

Section Learning Goal: `pattern`、`anomaly`、`JOIN`、subquery、`SOURCE` を、無理に実行せず読み方と使いどころから判断できる。

Hands-on Resource Title: `2026年版Logs Insights発展機能メモ`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Target Runtime | Production Status |
| --- | --- | --- | --- | --- | --- |
| `s3-l1` | pattern/anomalyで未知の変化を見る | ログパターンと異常検知を、未知の変化を見つける入口として説明できる | pattern/anomaly読解 | 4〜5分 | Produced - runtime remediated 2026-05-17 |
| `s3-l2` | JOIN/subquery/SOURCEの入口 | 複数ロググループ相関、入れ子クエリ、タグ指定クエリの位置づけと注意点を説明できる | JOIN/subquery/SOURCEメモ | 4〜5分 | Produced - runtime remediated 2026-05-17 |

## Hands-on Resources

| Resource Title | Location | Required AWS Resources | Notes |
| --- | --- | --- | --- |
| Logs Insights安全運転チェック | `handson/README.md#logs-insights安全運転チェック` | なし | AWSアカウントなしでも読解可能 |
| 基本クエリ読解 | `handson/queries/01_recent_events.sql` | 任意の既存ロググループ | 実行する場合は時間範囲を短くする |
| エラー検索クエリ | `handson/queries/02_error_search.sql` | 任意の既存ロググループ | ログ形式に合わせて条件を調整 |
| 傾向集計クエリ | `handson/queries/03_error_trend.sql` | 任意の既存ロググループ | `bin(5m)` を基本にする |
| requestId追跡クエリ | `handson/queries/06_request_trace.sql` | requestIdを含むログ | サンプルログで読解可能 |
| 2026年版発展機能メモ | `handson/README.md#2026年版の発展機能` | 任意 | 実行は上級者向け |

## Definition of Done

- 通常レクチャー8本が存在する。
- 講義本編の合計動画尺が30分以上である。
- CEO承認後に全レクチャーを再生成し、短尺版をそのまま完成扱いにしない。
- 台本、GPT-Image2スライド、VOICEVOX音声、MP4、QAレポート、Drive upload reportが各レクチャーに存在する。
