# CloudWatch Source Verification Report

## Target

- Course: `aws-cloudwatch-intro-course`
- Lecture: `s1-l1`
- Source of Truth: `courses/aws-cloudwatch-intro-course/course_spec.md`
- Date: 2026-05-14

## Ownership

- Owner AI: AI-Engineer-01
- Reviewer AI: AI-QA-01
- Worker != Reviewer: OK

## Sources Checked

| Source | URL | Checked Points |
| --- | --- | --- |
| Amazon CloudWatch User Guide: What is Amazon CloudWatch? | https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html | CloudWatchの目的、リアルタイム監視、メトリクス、ログ、ダッシュボード、アラーム |
| Amazon CloudWatch User Guide: Amazon CloudWatch concepts | https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html | namespace、metric、dimension、statistic、period、alarmの概念 |
| AWS Prescriptive Guidance: Logging and monitoring with Amazon CloudWatch | https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/cloudwatch.html | CloudWatchによるメトリクス収集、アラーム、ダッシュボード、クロスリージョン表示 |

## Search Queries

- `Amazon CloudWatch metrics logs alarms dashboards concepts documentation`
- `Amazon CloudWatch concepts metrics namespaces dimensions alarms dashboards log groups Logs Insights documentation`

## Verified Facts

| Topic | Verification | Course Usage |
| --- | --- | --- |
| CloudWatchの役割 | CloudWatchはAWSリソースとAWS上で実行するアプリケーションをリアルタイムに監視するためのサービス | Slide 1で「監視情報を集めて見る場所」と説明する |
| Metrics | メトリクスは時系列のデータポイントであり、namespace、metric name、dimensionの組み合わせで識別される | Slide 2、7で数値の時系列として扱う |
| Namespace | namespaceはメトリクスのコンテナであり、AWSサービスのnamespaceは `AWS/サービス名` の形式 | Slide 7で「棚」の比喩として扱う |
| Dimension | dimensionはメトリクスを一意に識別する名前と値の組み合わせ | Slide 7で「どの対象の数字かを決めるラベル」と説明する |
| Logs | CloudWatch Logsはログデータを収集、保存、分析する | Slide 3で「出来事の記録」と説明する |
| Alarm | アラームは単一メトリクスを期間にわたって監視し、条件に応じてアクションを実行できる | Slide 4で「条件、状態、アクション」と説明する |
| Dashboard | ダッシュボードはメトリクスやアラームなどを1つのビューで表示する | Slide 5で「表示面であり保存場所ではない」と説明する |
| Region | メトリクスは作成されたリージョンに存在し、クロスリージョン表示機能は別途提供される | 本動画では高度論点として脚注扱いにする |
| Retention | メトリクスデータは新しいデータがない場合も一定期間保持されるが、初学者向け動画では詳細期間を主題にしない | 本動画では「数字が時系列で残る」とだけ扱う |

## Teaching Constraints

- 本動画ではリソース作成を行わない。
- CloudFormationは本動画のハンズオンでは使わない。
- CloudFormationを使う場合は、講座内ハンズオンの再現性を高めるための選択肢として扱う。
- 実運用IaCの推奨はCDKまたはTerraformとする。
- Logs Insights、Application Signals、SLO、CloudWatch Agentは後続講座の対象に分離する。

## Risk Review

| Risk | Mitigation |
| --- | --- |
| Dashboardをデータ保存場所と誤解させる | 「表示面」と明示し、データ源はメトリクスやログであると説明する |
| Alarmをログ監視そのものと誤解させる | まずメトリクスを監視するものとして説明し、ログからメトリクス化する話は後続に回す |
| CloudFormationを実運用の原則と誤解させる | course_spec、台本、READMEで「教材ハンズオン内の再現性用途」と明記する |
| 初学者に用語を詰め込みすぎる | 1スライド1メッセージ、用語は地図の中で最小限にする |

## Approval

Status: Ready for handson README and script creation

Approved By: AI-QA-01
