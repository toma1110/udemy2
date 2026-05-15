# Lectures

## Course

- Course ID: `aws-cloudwatch-logs-insights-practical-course`
- Source of Truth: `../course_spec.md`
- Production policy: GPT-Image2 generated slide text, VOICEVOX narration, MP4 build
- Visual baseline: `../../docs/VIDEO_QUALITY_BASELINE.md`

## Section 1: クエリの安全運転と基本形

### Section Learning Objective

Logs Insightsを安全に実行する前提を理解し、基本クエリを読める。

### Hands-on Resource Title

`Logs Insights安全運転チェック`

| Lecture | Title | Goal | Deliverables |
| --- | --- | --- | --- |
| `s1-l1` | Logs Insights実践の地図 | 障害調査でLogs Insightsが担当する範囲を説明できる | `s1-l1_script.md`, `s1-l1_script.json`, GPT-Image2 slide PNG, VOICEVOX WAV, MP4 |
| `s1-l2` | ロググループと時間範囲 | スキャン量を抑える実行前チェックを説明できる | `s1-l2_script.md`, `s1-l2_script.json`, GPT-Image2 slide PNG, VOICEVOX WAV, MP4 |
| `s1-l3` | 基本構文: fields/filter/sort/limit | 直近ログとエラー検索の基本クエリを読める | `s1-l3_script.md`, `s1-l3_script.json`, GPT-Image2 slide PNG, VOICEVOX WAV, MP4 |

## Section 2: 障害調査クエリ集

### Section Learning Objective

エラー、傾向、遅延、requestId追跡の型を、現場ログへ合わせて選べる。

### Hands-on Resource Title

`障害調査クエリ集`

| Lecture | Title | Goal | Deliverables |
| --- | --- | --- | --- |
| `s2-l1` | エラーと例外を探す | ERROR、Exception、timeout、5xxの探し方を説明できる | `s2-l1_script.md`, `s2-l1_script.json`, GPT-Image2 slide PNG, VOICEVOX WAV, MP4 |
| `s2-l2` | stats/binで傾向を見る | 時間ごとの件数、上位エラー、遅延パーセンタイルを集計できる | `s2-l2_script.md`, `s2-l2_script.json`, GPT-Image2 slide PNG, VOICEVOX WAV, MP4 |
| `s2-l3` | parseとrequestId追跡 | 非構造ログから値を取り出し、requestIdで一連の出来事を追える | `s2-l3_script.md`, `s2-l3_script.json`, GPT-Image2 slide PNG, VOICEVOX WAV, MP4 |

## Section 3: 2026年版の発展機能

### Section Learning Objective

pattern/anomaly、JOIN、subquery、SOURCEの使いどころとコスト注意を説明できる。

### Hands-on Resource Title

`2026年版Logs Insights発展機能メモ`

| Lecture | Title | Goal | Deliverables |
| --- | --- | --- | --- |
| `s3-l1` | pattern/anomalyで未知の変化を見る | ログパターンと異常検知を調査入口として説明できる | `s3-l1_script.md`, `s3-l1_script.json`, GPT-Image2 slide PNG, VOICEVOX WAV, MP4 |
| `s3-l2` | JOIN/subquery/SOURCEの入口 | 複数ロググループ相関、入れ子クエリ、タグ指定の位置づけを説明できる | `s3-l2_script.md`, `s3-l2_script.json`, GPT-Image2 slide PNG, VOICEVOX WAV, MP4 |

## Lecture Design Rules

- クエリはAWS公式ドキュメントの構文に合わせる
- クエリ料金を抑える注意を各セクションで繰り返す
- 1スライド1メッセージにする
- 表示文字はGPT-Image2生成にする
- ローカル文字合成は禁止
- ナレーション本文はVOICEVOX向けに読みやすい日本語にする
- CloudFormationは教材ハンズオンの再現性用途として扱う
- 実運用IaCはCDKまたはTerraformを使う前提で説明する
