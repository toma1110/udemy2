# AWS CloudWatch入門 カリキュラム

Source of Truth: `course_spec.md`

## Course

- Course ID: `aws-cloudwatch-intro-course`
- Course Title: `AWS CloudWatch入門: Metrics・Logs Insights・Alarm・Dashboardで学ぶ監視の基本`
- Course Information: `course_infomation.md`
- Target Lecture Count: 6
- Target Main Lecture Runtime: 30〜36分
- Current Audit Result: 2026-05-17時点で通常レクチャー6本、合計約12.3分。Udemy標準コースの30分要件を満たしていない。

## Curriculum Review Gate

- 動画再生成前にCEOが `course_spec.md`、`course_infomation.md`、この `course_curriculum.md` を確認・承認する。
- プロモーション動画は通常レクチャーの30分要件に含めない。
- CEO承認後は、全レクチャーの台本、GPT-Image2スライド、VOICEVOX音声、MP4を一括で再生成してよい。
- 完成動画のスライドと表示文字はGPT-Image2由来PNGに限定する。
- WorkerとReviewerは分離する。

## Section 1: CloudWatchの地図

Section Learning Goal: CloudWatchの主要部品を役割ごとに分け、Metrics、Logs、Alarm、Dashboardの関係を説明できる。

Hands-on Resource Title: `CloudWatch地図ワークシート`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Target Runtime | Production Status |
| --- | --- | --- | --- | --- | --- |
| `s1-l1` | CloudWatchの地図 | Metrics、Logs、Alarm、Dashboardの違いと、障害調査での位置づけを説明できる | CloudWatch地図ワークシート | 5〜6分 | Produced - regenerate for runtime |
| `s1-l2` | Metricsの基本 | namespace、metric、dimension、statistic、periodを使ってメトリクスを探す考え方を説明できる | Metrics確認メモ | 5〜6分 | Produced - regenerate for runtime |
| `s1-l3` | Logsの基本 | log group、log stream、ログイベントを区別し、Metricsとの違いを説明できる | Logs確認メモ | 5〜6分 | Produced - regenerate for runtime |

## Section 2: Logs Insightsでログを読む

Section Learning Goal: Logs Insightsの基本クエリを読み、エラー調査の入口を作れる。

Hands-on Resource Title: `Logs Insightsクエリ読解`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Target Runtime | Production Status |
| --- | --- | --- | --- | --- | --- |
| `s2-l1` | Logs Insights入門 | `fields`、`filter`、`sort`、`limit`、`stats`、`bin`の基本形を読める | Logs Insightsクエリ読解 | 5〜6分 | Produced - regenerate for runtime |
| `s2-l2` | Logs Insightsで障害調査 | 最近のエラー、エラー件数、遅延、リクエスト単位の追跡という調査の型を説明できる | 障害調査クエリ集 | 5〜6分 | Produced - regenerate for runtime |

## Section 3: Alarm/Dashboardと調査フロー

Section Learning Goal: Alarm、Dashboard、Metrics、Logs Insightsをつなげて、障害時に次に見る場所を判断できる。

Hands-on Resource Title: `障害調査の見始め方チェック`

| Lecture ID | Lecture Title | Learning Goal | Hands-on Resource Title | Target Runtime | Production Status |
| --- | --- | --- | --- | --- | --- |
| `s3-l1` | Alarm/Dashboardと次の一歩 | Alarm、Dashboard、Metrics、Logs Insightsを使った障害時の見始め方を説明できる | 障害調査の見始め方チェック | 5〜6分 | Produced - regenerate for runtime |

## Hands-on Resources

| Resource Title | Location | Required AWS Resources | Notes |
| --- | --- | --- | --- |
| CloudWatch地図ワークシート | `handson/README.md` | なし | AWSアカウントがなくても実施可能 |
| Metrics確認メモ | `handson/README.md#metrics確認メモ` | なし | 既存メトリクスがあれば画面で確認 |
| Logs確認メモ | `handson/README.md#logs確認メモ` | なし | 既存ロググループがなくても読解で完了 |
| Logs Insightsクエリ読解 | `handson/README.md#logs-insightsクエリ読解` | 任意の既存ロググループ | 実行する場合は時間範囲を短くする |
| 障害調査クエリ集 | `handson/README.md#障害調査クエリ集` | 任意の既存ロググループ | 実行せず読むだけでも完了 |
| 障害調査の見始め方チェック | `handson/README.md#障害調査の見始め方チェック` | なし | 実務で見る順番を整理する |

## Definition of Done

- 通常レクチャー6本が存在する。
- 講義本編の合計動画尺が30分以上である。
- CEO承認後に全レクチャーを再生成し、短尺版をそのまま完成扱いにしない。
- 台本、GPT-Image2スライド、VOICEVOX音声、MP4、QAレポート、Drive upload reportが各レクチャーに存在する。
