# AWSアラート設計入門: 良いアラートと悪いアラート

## Course Title

AWSアラート設計入門: 良いアラートと悪いアラート

## Course ID

`aws-alert-design-practical-course`

## Source Candidate

- Market research ID: `VID-005`
- Candidate title: `良いアラートと悪いアラート: Alert Fatigueを防ぐ`
- Market basis: `C-01`, `K-02`, `P-06`
- Score: 88
- Priority: high
- GitHub Issue: `#169` / `TASK-0195`

## Course Positioning

本コースは、CloudWatch AlarmやSNS通知の操作前に必要な「アラート設計の判断基準」を学ぶ短尺講座です。

既存の `aws-cloudwatch-alarm-sns-course` は、CloudFormationでAlarmとSNS通知を作るハンズオンを主役にします。本コースでは、設定値そのものよりも、どのアラートを鳴らすべきか、どの通知を鳴らすべきでないか、受け取った人が何をすべきかを設計する力に絞ります。

## Target Audience

- CloudWatch Alarmを作れるが、どの条件で通知すべきか迷う人
- SRE、DevOps、クラウド運用に進みたい初学者
- アラートが多すぎて重要な通知が埋もれる問題を避けたい人
- Runbookやオンコール設計の入口を学びたい人
- 既存CloudWatch入門、Alarm + SNS講座、SLO導入講座の前後に学ぶ補助教材が欲しい人

## Prerequisites

- AWS CloudWatch、SNS、メトリクス、ログの基本用語を知っている
- エラー率、レイテンシ、可用性、CPU使用率の違いを聞いたことがある
- SLO、Runbook、オンコールの詳細経験は不要
- AWS CLIやCloudFormationの実行環境は不要

## Learning Objectives

受講後、受講者は以下を説明または実行できる状態になります。

- 良いアラートの条件を、Actionable、Timely、Meaningfulの3点で説明できる
- 悪いアラートの典型例として、鳴りすぎ、原因だけ、Owner不在、Runbook不在を指摘できる
- CloudWatch AlarmのPeriod、Evaluation Periods、Datapoints to Alarmを、M out of Nの考え方で説明できる
- missing dataの扱いを、常時出るメトリクスとエラー時だけ出るメトリクスで分けて考えられる
- Composite Alarmがアラート数を減らすための選択肢になることを説明できる
- アラートにSeverity、Owner、Runbook、Escalationを入れる理由を説明できる
- 既存のアラートを「深夜3時に起こされても動けるか」でレビューできる

## Course Promise

受講後、CloudWatch Alarmをただ作るのではなく、鳴らすべきアラート、鳴らすべきでないアラート、通知後に取るべき行動を自分で判断できる状態になります。

## Differentiation

- 操作説明ではなく、現場で困るAlert Fatigueを主題にする
- 悪い例から良い例への改善を、短尺動画でも使える形にする
- CloudWatch Alarmの評価設定を、単なる用語ではなくノイズ削減の設計判断として説明する
- Runbook、Owner、Severity、Escalationまで含める
- 実AWSのリソース作成を標準範囲にせず、低コスト・低リスクで学べる
- 既存のCloudWatch Alarm + SNS講座、Runbook講座、SLO講座へ自然に接続する

## Chapter Structure

詳細なセクション別カリキュラムは `course_curriculum.md` を正とします。

1. 良いアラートと悪いアラート
   - `s1-l1` 深夜3時に動けるアラートとは
   - `s1-l2` 悪いアラートを良いアラートへ直す

2. Alert Fatigueを防ぐ設計
   - `s2-l1` 鳴りすぎるアラートを減らす
   - `s2-l2` Owner、Runbook、Escalationを決める

3. AWSメトリクスに落とす
   - `s3-l1` CloudWatch Alarmの評価設定を読む
   - `s3-l2` Missing dataとComposite Alarmの使いどころ

## Hands-on Scope

標準ハンズオンはAWSリソースを作らない設計演習にする。

- 悪いアラート文面をレビューする
- Severity、Owner、Runbook、Escalationを追加する
- CloudWatch AlarmのPeriod、Evaluation Periods、Datapoints to Alarmを設計する
- missing dataの扱いをメトリクス種別ごとに選ぶ
- Composite Alarmで通知数を減らす設計案を作る

## CloudFormation Scope

v1ではCloudFormationテンプレートを作成しない。

教材で実AWS例が必要になった場合のみ、既存 `aws-cloudwatch-alarm-sns-course` のCloudFormation構成を参照する。CloudFormationは教材再現用であり、実運用IaCはCDKまたはTerraformを推奨する。

## Cost Warning

標準範囲ではAWSリソースを作成しないため、AWS利用料金は発生しません。

追加検証としてCloudWatch Alarm、SNS、Composite Alarm、CloudFormation stackを作成する場合は料金が発生する可能性があるため、CEO承認後に実施し、削除手順をQAへ残します。

## Udemy成立尺是正完了実績

2026-05-17に、全6レクチャーの台本、GPT-Image2由来スライド、VOICEVOX音声、MP4生成、Google Driveアップロードを完了した。

- 完成レクチャー数: 6本
- 講義本編の合計動画尺: 1914.164秒、約31.90分
- Udemy成立尺ゲート: PASS、30分以上
- 未作成だった `s1-l2`、`s2-l1`、`s2-l2`、`s3-l1`、`s3-l2` も完成済み
- プロモーション動画は30分要件に含めていない
- 標準範囲ではAWSリソースを作成していない
- Driveアップロード報告: `qa/course_drive_upload_report.md`
- 動画制作QA報告: `qa/course_video_production_report.md`

## Production Rules

- 完成動画のスライドPNGは必ずGPT-Image2由来にする
- 完成動画に表示するタイトル、短いラベル、図解内テキストもGPT-Image2に生成させる
- ローカル描画のみのスライドは下書き・検証用に限る
- ローカル文字合成したスライドを完成動画に使わない
- 音声はVOICEVOXを使う
- コース画像もGPT-Image2由来PNGにし、QA後にGoogle Driveへアップロードする
- WorkerとReviewerを分離する

## Definition of Done

- `course_spec.md` がSource of Truthとして成立している
- 通常レクチャーが5本以上、講義本編の合計動画尺が30分以上である
- CEO依頼に基づき2026-05-17に動画生成とDriveアップロードを完了している
- AWS公式ドキュメントに基づく仕様確認レポートが存在する
- `course_infomation.md` にUdemy登録情報、歓迎メッセージ、お祝いメッセージがある
- `course_curriculum.md` にセクションタイトル、学習目標、制作対象レクチャーがある
- `scripts/s1-l1_good_bad_alerts_script.md` に初回動画台本がある
- `slides/s1-l1_gpt_image2_prompts.md` にGPT-Image2プロンプトがある
- 台本、スライド計画、QA計画が一致している
- スライドと表示文字はGPT-Image2生成である
- VOICEVOX音声、MP4、Drive URL、QAレポートが作成済みである
- コース画像、Drive URL、画像QAレポートが作成済みである
- WorkerとReviewerが別AIである

## Out of Scope

- 本番監視基盤の設計代行
- PagerDuty、Opsgenie、Slack連携の実装
- AWS Incident Managerの実装
- CloudFormationテンプレートの新規作成
- CDKまたはTerraformによる本番IaC実装
- 複数アカウント、複数リージョンの通知設計
- 実オンコール体制の運用代行

## References

- CloudWatch alarm evaluation
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-evaluation.html
- CloudWatch missing data treatment
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarms-and-missing-data.html
- CloudWatch recommended alarms
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.html
- CloudWatch composite alarms
  - https://aws.amazon.com/blogs/mt/improve-monitoring-efficiency-using-amazon-cloudwatch-composite-alarms-2/
