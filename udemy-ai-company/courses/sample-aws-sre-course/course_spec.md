# AWS SRE入門：CloudFormationで作る監視基盤ハンズオン

## Course Title

AWS SRE入門：CloudFormationで作る監視基盤ハンズオン

## Target Audience

- AWSの基本操作は知っているが、監視基盤を体系的に作ったことがない人
- SREや運用改善に興味がある初学者
- CloudFormationで小さな監視構成を作り、削除まで体験したい人

## Prerequisites

- AWSアカウントを持っている
- AWS CLIを設定済みである
- CloudFormation、CloudWatch、SNSの名前を聞いたことがある
- Bashを実行できる環境がある

## Learning Objectives

- CloudFormationでCloudWatch Alarm、SNS Topic、Dashboardを作成できる
- 監視、通知、可視化の最小構成を説明できる
- READMEに沿ってスタック作成、更新、検証、削除を実行できる
- SREにおける監視基盤の役割を初学者向けに説明できる

## Course Promise

受講後、低コストなAWS監視基盤の最小構成をCloudFormationで作り、検証し、削除できるようになります。

## Differentiation

- 監視の概念説明だけで終わらず、CloudFormationで実際に構築する
- README再現性を品質ゲートに含める
- 作成、更新、削除までを1つのハンズオンとして扱う

## Chapter Structure

1. SREと監視基盤の全体像
2. CloudWatch Alarm、SNS、Dashboardの役割
3. CloudFormationテンプレートの読み方
4. スタック作成と検証
5. スタック更新と削除
6. 運用で見るべき改善ポイント

## Hands-on Scope

- CloudFormationテンプレートを検証する
- CloudWatch Alarmを作成する
- SNS Topicを作成する
- CloudWatch Dashboardを作成する
- smoke testで存在確認する
- スタック更新を実行する
- スタック削除を実行する

## CloudFormation Scope

この範囲は教材ハンズオン用です。受講者が追加ツールを用意せずREADME通りに再現できるようにCloudFormationを使います。実運用IaCではCDKまたはTerraformを使う前提で考えます。

対象リソース:

- `AWS::CloudWatch::Alarm`
- `AWS::SNS::Topic`
- `AWS::SNS::Subscription` はメールアドレス指定時のみ
- `AWS::CloudWatch::Dashboard`

## Cost Warning

CloudWatch Alarm、CloudWatch Dashboard、SNSには利用状況やAWSアカウントの無料利用枠により料金が発生する場合があります。ハンズオン後は削除手順を実行してください。

## Definition of Done

- `cloudformation/template.yaml` が存在する
- `validate.sh full` が成功する
- `smoke_test.sh` がAlarm、SNS、Dashboardの存在を確認する
- README通りに第三者が再現できる
- 動画手順とREADMEが一致する
- WorkerとReviewerが別AIである

## Out of Scope

- 本番レベルの監視設計
- 複数AWSアカウント構成
- PagerDuty、Slackなど外部通知連携
- Terraform実装
- 高度なログ分析
