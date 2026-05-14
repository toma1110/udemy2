# AWS CloudWatch入門: Metrics/Logs/Alarm/Dashboardの地図

## Purpose

CloudWatchの主要部品を、初学者が迷わない「地図」として整理する短尺講座です。

## Course Files

| Path | Role |
| --- | --- |
| `course_spec.md` | この講座のSource of Truth |
| `handson/README.md` | リソース作成なしで進める確認手順 |
| `scripts/s1-l1_script.md` | VOICEVOX向け台本 |
| `scripts/s1-l1_script.json` | 音声生成と動画生成用の構造化台本 |
| `slides/s1-l1/` | スライドPNG |
| `audio/s1-l1/` | VOICEVOX音声 |
| `video/s1-l1/` | 完成MP4 |
| `qa/` | 公式情報確認、音声、動画、教材QAレポート |

## Lecture

| Lecture | Title | Goal |
| --- | --- | --- |
| `s1-l1` | CloudWatchの地図 | Metrics、Logs、Alarm、Dashboardの違いとつながりを説明できる |

## Hands-on Policy

- 本動画ではAWSリソースを作成しない。
- AWSアカウントがある場合はCloudWatchコンソールを確認する。
- AWSアカウントがない場合でも、`handson/README.md` の表を使って完了できる。
- 手順外でダッシュボード、アラーム、ログ投入、カスタムメトリクス作成をしない。

## IaC Policy

- 本動画ではCloudFormationテンプレートを使わない。
- 後続ハンズオンでAWSリソースを作る場合は、受講者が追加ツールなしに再現できるようCloudFormationを使うことがある。
- 実運用では、保守性とチーム開発を考慮してCDKまたはTerraformを使う前提で説明する。

## Quality Gate

- `course_spec.md` が存在する
- 公式情報確認レポートが存在する
- README手順がリソース作成なしで再現可能である
- 台本がVOICEVOXナレーションチェックを通過している
- スライド数、音声数、動画素材数が一致している
- WorkerとReviewerが分離されている

## References

- Amazon CloudWatch User Guide: What is Amazon CloudWatch?
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html
- Amazon CloudWatch User Guide: Amazon CloudWatch concepts
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html
