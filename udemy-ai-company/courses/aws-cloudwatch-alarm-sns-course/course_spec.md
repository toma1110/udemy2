# CloudFormationで作るCloudWatch Alarm + SNS通知

## Course Title

CloudFormationで作るCloudWatch Alarm + SNS通知

## Course ID

`aws-cloudwatch-alarm-sns-course`

## Source Candidate

- Market research ID: `VID-002`
- Candidate title: `CloudFormationで作るCloudWatch Alarm + SNS通知`
- Market basis: `C-03`, `C-04`, `K-02`, `K-05`, `P-02`
- Score: 92
- Priority: high

## Target Audience

- CloudWatch Alarmを作ったことがないAWS初学者
- メール通知つきの監視ハンズオンを小さく再現したい人
- SREやクラウド運用に進む前に、通知まで含めたAlarmの流れを理解したい人
- CloudFormationで作成、更新、削除まで管理する練習をしたい人

## Prerequisites

- AWSアカウントを持っている
- CloudFormation、CloudWatch、SNSを利用できるIAM権限がある
- 通知確認用のメールアドレスを1つ用意できる
- AWS CLIは任意。CloudFormationコンソールで進められる構成を基本にする
- CDK、Terraformの事前準備は不要

## Learning Objectives

- CloudWatch Alarmがメトリクス、条件、状態、アクションで動くことを説明できる
- しきいち、期間、評価回数、データポイントの関係を説明できる
- SNS TopicとEmail Subscriptionの役割を説明できる
- メールSubscriptionが `PendingConfirmation` のままだと通知が届かないことを説明できる
- CloudFormationでSNS Topic、Subscription、Topic Policy、CloudWatch Alarmを作成できる
- メールSubscriptionは受信者の確認が必要であることを説明できる
- AlarmからSNS通知が届かない時の確認ポイントを説明できる
- stack update/deleteを含めて、README通りに後片付けできる
- 教材ハンズオンのCloudFormationと実運用IaCのCDK/Terraformを混同せず説明できる

## Course Promise

受講後、CloudFormationを使ってCloudWatch AlarmとSNS通知の最小構成を作成し、通知確認、更新、削除までREADME通りに再現できる状態になります。

## Differentiation

- 作成だけでなく、確認、更新、削除まで扱う
- SNSメール確認、AlarmActions、Topic Policy、暗号化時の注意点を初学者向けに整理する
- CloudFormationは教材ハンズオン用、実運用ではCDK/Terraform推奨という位置づけを明確にする
- VID-001と同等以上のGPT-Image2スライド品質で、Alarmと通知の流れを図解する

## Chapter Structure

詳細なセクション別カリキュラムは `course_curriculum.md` を正とします。

1. Alarm + SNS通知の地図
   - `s1-l1` Alarm + SNS通知の最小構成
   - `s1-l2` CloudWatch Alarmの評価条件
   - `s1-l3` SNS Topicとメール確認

2. CloudFormationで作る
   - `s2-l1` CloudFormationテンプレートを読む
   - `s2-l2` Stack作成と通知テスト

3. 運用と後片付け
   - `s3-l1` 更新・削除・トラブルシュート

## Hands-on Resource Titles

- `Alarm + SNS通知の全体像チェックシート`
- `CloudFormationテンプレート読解とStack作成手順`
- `更新・削除・トラブルシュート確認リスト`

## Hands-on Scope

- CloudFormationテンプレートを使ってSNS Topic、Email Subscription、Topic Policy、CloudWatch Alarmを作る
- CloudFormationコンソール手順を主経路にする
- AWS CLI手順は任意の確認手順として扱う
- Alarm用メトリクスは学習用namespaceを使い、アプリケーションやEC2などの長時間稼働リソースは作らない
- 通知テストはSNS publishを基本にし、Alarm state testはCLI任意手順にする

## Hands-on IaC Scope

- 教材ハンズオン: CloudFormation
- 実運用IaC: CDKまたはTerraformを推奨
- Terraform講座ではTerraformを教材対象として扱う

## CloudFormation Scope

- `AWS::SNS::Topic`
- `AWS::SNS::Subscription`
- `AWS::SNS::TopicPolicy`
- `AWS::CloudWatch::Alarm`

## Cost Warning

CloudWatch Alarm、SNS通知、CloudWatchの利用状況により料金が発生する可能性があります。ハンズオン後は必ず削除手順を実行します。

本講座では、EC2、RDS、ALBなど長時間稼働する高コストリソースは作りません。

## Udemy成立尺是正結果

2026-05-17の既存コース動画監査では、通常レクチャーMP4は6本存在するが、合計尺は約13.3分でUdemy標準コースの30分要件に届いていない。

2026-05-17に、CEOの動画作成依頼を動画再生成承認として扱い、全6レクチャーの台本、VOICEVOX音声、MP4を再生成した。

是正後の制作結果:

- レクチャー数は現行の6本を維持した
- 講義本編の合計動画尺は2115.726秒、35.26分
- Alarm評価条件、SNSメール確認、CloudFormationテンプレート読解、通知が届かない時の切り分け、削除確認をナレーションで拡張した
- プロモーション動画は30分要件に含めていない
- 完成動画は既存のGPT-Image2由来スライドPNGとVOICEVOX音声で再生成した
- MP4は全6本でfaststartとdecode検証に合格した
- Google Driveアップロードは2026-05-17に完了し、URLを `qa/course_drive_upload_report.md` に記録した

## Promotion Video Scope

公開前に、講座全体を紹介するプロモーション動画を通常レクチャーとは別に作成する。

- 目的: CloudWatch AlarmとSNS通知を小さく作り、通知確認、更新、削除まで学びたい受講者へ講座価値を伝える
- 主な訴求: CloudFormationで最小構成を再現できる、メール確認や通知が届かない時の確認ポイントまで扱う、実運用IaCはCDK/Terraform推奨と分けて説明する
- 必須素材: `scripts/promo_video_script.md`、GPT-Image2 source PNG、GPT-Image2由来最終PNG、VOICEVOX音声、MP4、Drive upload report
- 制作ルール: `docs/PROMOTION_VIDEO_RULES.md`、`docs/GPT_IMAGE_RULES.md`、`docs/VIDEO_QUALITY_BASELINE.md` に従う
- 禁止: 通常レクチャー `s1-l1` をプロモーション動画の代用にしない

## Definition of Done

- AWS公式ドキュメントに基づく仕様確認レポートが存在する
- 通常レクチャーが5本以上、講義本編の合計動画尺が30分以上である（2026-05-17時点で6本、35.26分）
- 動画再生成前にCEOが動画作成を依頼している
- CloudFormationテンプレート、README、validate script、smoke test scriptが存在する
- stack create/update/deleteはCEO承認後にだけ実行し、結果を検証レポートに残す
- 台本とREADMEが一致している
- `course_curriculum.md` にセクションタイトル、セクション学習目標、ハンズオンリソースタイトルがある
- スライドと表示文字はGPT-Image2生成である
- VID-001品質基準と比較し、品質低下がないことをQAで確認する
- VOICEVOX音声、MP4、Drive URL、QAレポートが作成済みである
- プロモーション動画の台本、GPT-Image2素材、VOICEVOX音声、MP4、Drive URL、QAレポートが存在する
- WorkerとReviewerが別AIである

## Out of Scope

- 本番監視基盤の設計代行
- KMS customer managed keyを使った暗号化SNS Topicの完全実装
- CDKまたはTerraformによる本番IaC実装
- Lambda、EC2、ALBなど監視対象アプリケーションの構築
- SMS、Slack、Webhook通知
- 複数アカウント、複数リージョン通知設計

## References

- AWS::CloudWatch::Alarm
  - https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-alarm.html
- AWS::SNS::Topic
  - https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sns-topic.html
- AWS::SNS::Subscription
  - https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sns-subscription.html
- CloudWatch alarm with encrypted SNS topic
  - https://repost.aws/knowledge-center/cloudwatch-configure-alarm-sns
- SNS notifications from CloudWatch alarm triggers
  - https://repost.aws/knowledge-center/cloudwatch-receive-sns-for-alarm-trigger
