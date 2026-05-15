# AWS CloudWatch入門: Metrics・Logs Insights・Alarm・Dashboardで学ぶ監視の基本

## Purpose

CloudWatchの主要部品を、初学者が迷わない「地図」として整理し、Logs Insightsでログを読み始められる状態まで育てる入門コースです。

## Course Files

| Path | Role |
| --- | --- |
| `course_spec.md` | この講座のSource of Truth |
| `course_curriculum.md` | セクション、レクチャー、学習目標、ハンズオンリソースの一覧 |
| `handson/README.md` | リソース作成なしで進める確認手順 |
| `scripts/lectures.md` | レクチャー一覧と制作状態 |
| `scripts/*_script.md` | VOICEVOX向け台本 |
| `scripts/*_script.json` | 音声生成と動画生成用の構造化台本 |
| `slides/*_gpt_image_prompts.md` | GPT-Image2用スライド生成プロンプト |
| `slides/<lecture>/` | 最終スライドPNGとcontact sheet |
| `slides/<section>-gpt-image2-sources/<lecture>/` | GPT-Image2生成元PNG |
| `audio/<lecture>/` | VOICEVOX音声 |
| `video/<lecture>/` | 完成MP4 |
| `qa/` | 公式情報確認、音声、動画、教材QAレポート |

## Sections

| Section | Title | Goal |
| --- | --- | --- |
| 1 | CloudWatchの地図 | CloudWatchの部品を役割ごとに分けて説明できる |
| 2 | Logs Insightsでログを読む | 基本クエリを読み、障害調査の入口を作れる |
| 3 | Alarm/Dashboardと調査フロー | 監視情報を見て、次に深掘りする場所を判断できる |

## Lectures

| Lecture | Title | Goal |
| --- | --- | --- |
| `s1-l1` | CloudWatchの地図 | Metrics、Logs、Alarm、Dashboardの違いとつながりを説明できる |
| `s1-l2` | Metricsの基本 | namespace、metric、dimension、statistic、periodを使ってメトリクスを探す考え方を説明できる |
| `s1-l3` | Logsの基本 | log group、log stream、ログイベントを区別し、メトリクスとの違いを説明できる |
| `s2-l1` | Logs Insights入門 | `fields`、`filter`、`sort`、`limit`、`stats`、`bin`の基本形を読める |
| `s2-l2` | Logs Insightsで障害調査 | 最近のエラー、エラー件数、遅延、リクエスト単位の追跡という調査の型を説明できる |
| `s3-l1` | Alarm/Dashboardと次の一歩 | Alarm、Dashboard、Metrics、Logs Insightsを使った障害時の見始め方を説明できる |

## Hands-on Policy

- 本コースではAWSリソースを作成しない。
- AWSアカウントがある場合はCloudWatchコンソールを確認する。
- 既存ロググループがある場合だけ、Logs Insightsで短い時間範囲のサンプルクエリを試す。
- AWSアカウントや既存ログがない場合でも、`handson/README.md` の表とクエリ読解で完了できる。
- 手順外でダッシュボード、アラーム、ログ投入、カスタムメトリクス作成をしない。

## IaC Policy

- 本コースではCloudFormationテンプレートを使わない。
- 後続ハンズオンでAWSリソースを作る場合は、受講者が追加ツールなしに再現できるようCloudFormationを使うことがある。
- 実運用では、保守性とチーム開発を考慮してCDKまたはTerraformを使う前提で説明する。

## Quality Gate

- `course_spec.md` が存在する
- 公式情報確認レポートが存在する
- README手順がリソース作成なしで再現可能である
- 台本がVOICEVOXナレーションチェックを通過している
- 完成動画スライドはGPT-Image2由来である
- ローカル文字合成スライドを完成動画に使っていない
- スライド数、音声数、動画素材数が一致している
- WorkerとReviewerが分離されている

## References

- Amazon CloudWatch User Guide: What is Amazon CloudWatch?
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html
- Amazon CloudWatch User Guide: Amazon CloudWatch concepts
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html
- Amazon CloudWatch Logs User Guide: CloudWatch Logs Insights query syntax
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html
- Amazon CloudWatch Logs User Guide: Sample queries
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-examples.html
