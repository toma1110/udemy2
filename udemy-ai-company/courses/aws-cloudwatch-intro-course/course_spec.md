# AWS CloudWatch入門: Metrics/Logs/Alarm/Dashboardの地図

## Course Title

AWS CloudWatch入門: Metrics/Logs/Alarm/Dashboardの地図

## Course ID

`aws-cloudwatch-intro-course`

## Source Candidate

- Market research ID: `VID-001`
- Candidate title: `AWS CloudWatch入門: Metrics/Logs/Alarm/Dashboardの地図`
- Market basis: `C-03`, `K-01`, `P-05`
- Differentiation source: 日本語、図解、短尺、初学者向け

## Target Audience

- AWSを学び始めたが、CloudWatchの用語が点で散らばって見える人
- Metrics、Logs、Alarm、Dashboardの違いを説明できず、監視学習で止まっている人
- SREや運用監視に進む前に、CloudWatchの全体像を短時間でつかみたい人
- 実務でダッシュボードやアラームを見ているが、裏側のつながりを整理したい人

## Prerequisites

- AWSマネジメントコンソールの基本的な画面遷移を見たことがある
- サーバー、ログ、メトリクス、通知という言葉を聞いたことがある
- AWSアカウントはあると望ましいが、本レクチャーの中心部分はリソース作成なしで学習できる
- AWS CLI、CloudFormation、CDK、Terraformの事前準備は不要

## Learning Objectives

- CloudWatchがAWSリソースとアプリケーションを監視するためのサービスであると説明できる
- Metrics、Logs、Alarm、Dashboardの役割を分けて説明できる
- namespace、metric、dimension、statistic、periodの基本関係を説明できる
- Alarmが「メトリクス」「条件」「状態」「アクション」で構成されることを説明できる
- Dashboardはデータ保存場所ではなく、メトリクスやアラームを見るための表示面だと説明できる
- 障害調査時に、Dashboard、Alarm、Metrics、Logsのどこから見始めるかを判断できる
- ハンズオン用CloudFormationと実運用IaCの位置づけを混同せず説明できる

## Course Promise

受講後、CloudWatchの画面や会話で出てくる主要部品を地図として理解し、次にCloudWatch Alarm、Logs Insights、SLO監視などを学ぶための土台を作れる状態になります。

## Differentiation

- 初学者が混乱しやすい「メトリクス」「ログ」「アラーム」「ダッシュボード」を1枚の地図で整理する
- AWS公式ドキュメントの用語に寄せつつ、実務での見方に翻訳する
- リソース作成を必須にせず、特別な準備なしで学べる短尺講座にする
- 後続のSRE、SLO、CloudWatch実践講座へ自然につながる導入動画にする
- VOICEVOXで読み上げやすい日本語にし、英字略語はナレーション内で読み表記へ寄せる

## Chapter Structure

本候補は1本の短尺動画として制作する。

1. CloudWatchの地図
   - 監視の入口としてのCloudWatch
   - 4つの基本部品

2. Metrics
   - 数値の時系列
   - namespace、metric、dimension
   - statisticとperiod

3. Logs
   - 出来事の記録
   - log groupとlog stream
   - メトリクスとの違い

4. Alarm
   - 条件と状態
   - 通知や自動アクションとの関係
   - OK、ALARM、INSUFFICIENT_DATAの考え方

5. Dashboard
   - 監視情報を見る画面
   - データソースではなく表示面
   - 障害調査時の見方

6. ハンズオンと実運用IaCの位置づけ
   - 本動画ではリソース作成なし
   - ハンズオンで作る場合はCloudFormationで再現性を優先
   - 実運用ではCDKまたはTerraformを使う前提

## Hands-on Scope

本動画のハンズオン範囲は「概念図とサンプルメトリクス確認」です。

- AWSリソース作成は必須にしない
- AWSアカウントがある場合はCloudWatchコンソールで画面を確認する
- 既存リソースがない場合でも、READMEの表と地図だけで完了できる
- CloudWatchの各画面で「何を見る場所か」を確認する
- ダッシュボード、アラーム、ロググループ、メトリクスを新規作成しない

## CloudFormation Scope

本動画ではCloudFormationテンプレートを作成しない。

理由:

- 初学者向けの地図動画であり、実リソース作成より概念整理を優先するため
- 「実行に特別な用意がいらない」ハンズオンにするため
- リソース作成を伴うCloudWatch実践動画は後続候補へ分離するため

位置づけ:

- CloudFormationは、講座内ハンズオンで受講者が追加ツールなしにREADME通り再現するための選択肢
- 実運用のIaCでは、チーム開発、抽象化、保守性を考慮してCDKまたはTerraformを使う前提
- Terraform講座ではTerraformを教材対象として扱う

## Cost Warning

本動画の中心ハンズオンではAWSリソースを作成しないため、追加課金が発生しない構成にする。

ただし、受講者が任意でCloudWatchリソースを作成した場合は、以下に料金が発生する可能性がある。

- カスタムメトリクス
- ログ取り込み、ログ保存、ログ検索
- アラーム
- ダッシュボード
- 通知連携

動画とREADMEでは、手順外のリソース作成をしないこと、作成した場合は削除することを明記する。

## Definition of Done

- `course_spec.md` がSource of Truthとして成立している
- AWS公式ドキュメントに基づく用語確認レポートが存在する
- `README.md` と `handson/README.md` が存在し、リソース作成なしで再現できる
- `scripts/s1-l1_script.md` と `scripts/s1-l1_script.json` が存在する
- ナレーション本文がVOICEVOX向けにチェック済みである
- スライド設計が存在し、1スライド1メッセージになっている
- スライドPNG、VOICEVOX音声、MP4、QAレポートが作成済みである
- WorkerとReviewerが別AIである

## Out of Scope

- CloudWatch Alarm、SNS、Dashboardの新規作成ハンズオン
- Logs Insightsクエリの実践
- CloudWatch Agent、OpenTelemetry、Application Signalsの導入
- SLO、エラーバジェット、バーンレート設計
- 本番監視基盤の設計代行
- マルチアカウント、マルチリージョンの運用設計
- CDKまたはTerraformによる本番IaC実装

## Voice and Terminology Rules

ナレーションでは以下の読みを優先する。

| 表記 | ナレーション |
| --- | --- |
| AWS | エーダブリューエス |
| CloudWatch | クラウドウォッチ |
| Metrics | メトリクス |
| Logs | ログ |
| Alarm | アラーム |
| Dashboard | ダッシュボード |
| Namespace | ネームスペース |
| Dimension | ディメンション |
| Statistic | スタティスティック |
| Period | ピリオド |
| CloudFormation | クラウドフォーメーション |
| CDK | シーディーケー |
| Terraform | テラフォーム |
| IaC | アイエーシー |

台本生成後は必ず以下を実行する。

```bash
python3 udemy-ai-company/tools/narration_checker.py udemy-ai-company/courses/aws-cloudwatch-intro-course/scripts
```

## References

- Amazon CloudWatch User Guide: What is Amazon CloudWatch?
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html
- Amazon CloudWatch User Guide: Amazon CloudWatch concepts
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html
- AWS Prescriptive Guidance: Logging and monitoring with Amazon CloudWatch
  - https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/cloudwatch.html
