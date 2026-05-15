# Lectures

## Course

- Course ID: `aws-cloudwatch-intro-course`
- Source of Truth: `../course_spec.md`
- Production policy: VOICEVOX narration, GPT-Image2-derived slide PNG, MP4 build

## Section 1: CloudWatchの地図

| Lecture | Title | Goal | Deliverables |
| --- | --- | --- | --- |
| `s1-l1` | CloudWatchの地図 | Metrics、Logs、Alarm、Dashboardの違いとつながりを説明できる | script, GPT-Image2 slides, VOICEVOX WAV, MP4 |
| `s1-l2` | Metricsの基本 | namespace、metric、dimension、statistic、periodを使ってメトリクスを探す考え方を説明できる | script, GPT-Image2 slides, VOICEVOX WAV, MP4 |
| `s1-l3` | Logsの基本 | log group、log stream、ログイベントを区別し、メトリクスとの違いを説明できる | script, GPT-Image2 slides, VOICEVOX WAV, MP4 |

## Section 2: Logs Insightsでログを読む

| Lecture | Title | Goal | Deliverables |
| --- | --- | --- | --- |
| `s2-l1` | Logs Insights入門 | `fields`、`filter`、`sort`、`limit`、`stats`、`bin`の基本形を読める | script, GPT-Image2 slides, VOICEVOX WAV, MP4 |
| `s2-l2` | Logs Insightsで障害調査 | 最近のエラー、エラー件数、遅延、リクエスト単位の追跡という調査の型を説明できる | script, GPT-Image2 slides, VOICEVOX WAV, MP4 |

## Section 3: Alarm/Dashboardと調査フロー

| Lecture | Title | Goal | Deliverables |
| --- | --- | --- | --- |
| `s3-l1` | Alarm/Dashboardと次の一歩 | Alarm、Dashboard、Metrics、Logs Insightsを使った障害時の見始め方を説明できる | script, GPT-Image2 slides, VOICEVOX WAV, MP4 |

## Lecture Design Rules

- 1スライド1メッセージにする
- ナレーション本文はVOICEVOX向けに読みやすい日本語にする
- ナレーション本文には英字略語を残さない
- Logs Insightsのクエリは公式ドキュメントの構文に合わせる
- CloudFormationは講座内ハンズオンの再現性用途として扱う
- 実運用IaCはCDKまたはTerraformを使う前提で説明する
- 本コースではAWSリソースを作成しない
- 完成動画にはGPT-Image2由来スライドだけを使う
