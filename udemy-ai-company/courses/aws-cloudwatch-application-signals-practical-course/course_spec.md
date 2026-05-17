# AWS CloudWatch Application Signals実践: サンプルアプリで学ぶAPM・Service Map・SLO監視

## Course Title

AWS CloudWatch Application Signals実践: サンプルアプリで学ぶAPM・Service Map・SLO監視

## Course ID

`aws-cloudwatch-application-signals-practical-course`

## Source Candidate

- Market research ID: `VID-005`
- Candidate title: `AWS CloudWatch Application Signals実践`
- Strategic source: `aws-slo-adoption-course` の補足扱いだったApplication Signalsを、実アプリ観測編として独立させる
- Priority: high

## Course Positioning

本コースは、CloudWatch Application Signalsを主役にした実践コースです。

既存のCloudWatch入門やSLO導入講座では、Metrics、Alarm、Dashboard、SLO設計を安全に学びました。本コースでは、サンプルアプリをAWS上にデプロイし、実際の通信を発生させながら、Application SignalsのServices、Application Map、Service detail、Latency、Availability、Fault、Error、SLOの見方を体験します。

標準ハンズオンは、低頻度の自動トラフィック、停止手順、削除手順、コスト確認を必須にした短時間検証用です。常時高負荷を発生させる教材にはしません。

## Target Audience

- CloudWatchの基本は知っているが、APMやApplication Signalsを実際に触ったことがない人
- Lambda、ECS、EKS、EC2などのアプリケーション監視をSLOへつなげたい人
- SRE、DevOps、クラウド運用としてサービスのLatency、Availability、Fault、Errorを説明したい人
- OpenTelemetry、X-Ray、APMの入口をAWSマネージド機能で体験したい人
- 既存SLO講座の次に、実アプリを使った観測とSLO運用を学びたい人

## Prerequisites

- AWSアカウントを持っている
- CloudFormation、Lambda、IAM、CloudWatch、EventBridge Schedulerを操作できる権限がある
- AWS CLIをインストールし、認証情報を設定できる
- Lambda、HTTP、レイテンシ、エラー率の基本用語を理解している
- AWS利用料金が発生する可能性を理解し、検証後に削除できる
- CDK、Terraform、ECS、EKSの事前知識は必須にしない

## Learning Objectives

受講後、受講者は以下を説明または実行できる状態になります。

- CloudWatch Application Signalsが収集するLatency、Availability、Fault、Error、Call volumeの意味を説明できる
- Application SignalsのServices、Application Map、Service detailを使い、サービス状態と依存関係を確認できる
- サンプルアプリに正常、遅延、エラーの通信を発生させ、画面上の変化を読み取れる
- Application SignalsのSLOとCloudWatch Alarm/Dashboardの違いを説明できる
- SLO Recommendations、Service-Level SLO、SLO Performance Reportが短時間ハンズオンではなく、実運用データ前提の機能であることを説明できる
- Application Signalsの課金要素と、自動トラフィック停止・削除手順を説明できる
- 教材ハンズオンのCloudFormationと、実運用IaCのCDK/Terraformを分けて説明できる

## Course Promise

受講後、CloudWatch Application Signalsを単なる新機能としてではなく、実アプリの通信、サービス状態、依存関係、SLO監視に結びつけて説明できる状態になります。

## Differentiation

- Application Signalsを説明だけで終わらせず、サンプルアプリの通信で体験する
- 常時高負荷ではなく、低頻度・停止可能な自動トラフィックにする
- Services、Application Map、Service detail、SLOの読み方を運用担当目線で扱う
- SLO導入講座で補足扱いだったApplication Signalsを、独立した実践編として深掘りする
- SLO Recommendationsなど30日データが必要な機能は、短時間ハンズオンに無理に含めず、制約として説明する
- CloudFormationは教材再現用、実運用IaCはCDKまたはTerraform推奨という方針を維持する

## Chapter Structure

詳細なセクション別カリキュラムは `course_curriculum.md` を正とします。

1. Application Signalsの地図
   - `s1-l1` Application Signalsで何が見えるか
   - `s1-l2` ハンズオン構成とコスト安全策

2. CloudFormationでサンプルアプリを作る
   - `s2-l1` テンプレート全体を読む
   - `s2-l2` サンプルアプリと低頻度トラフィックをデプロイする
   - `s2-l3` 正常、遅延、エラーのシナリオを切り替える

3. Application Signalsで見る
   - `s3-l1` Servicesで状態を見る
   - `s3-l2` Application Mapで依存関係を見る
   - `s3-l3` Service detailでLatency、Fault、Errorを読む

4. SLOと運用判断につなげる
   - `s4-l1` Application Signals SLOを作る
   - `s4-l2` SLO RecommendationsとPerformance Reportの前提
   - `s4-l3` 後片付け、停止、コスト確認

## Hands-on Scope

- CloudFormationで短時間検証用サンプルアプリを作る
- Application Signalsを有効化するためのアカウント設定、ロール、計装設定を扱う
- 低頻度の自動トラフィックを発生させる
- 正常、遅延、エラーのシナリオを切り替える
- Application SignalsのServices、Application Map、Service detailを確認する
- Application Signals SLOを1つ作成し、SLIとSLOの関係を確認する
- 自動トラフィック停止、stack update、stack delete、コスト確認を必須にする

## Hands-on Architecture Direction

初版の標準構成は、Lambdaを中心に設計する。

- サンプルAPI Lambda
- 低頻度トラフィック発生用Lambda
- EventBridge Schedulerによる1分に1回程度の低頻度呼び出し
- CloudWatch Application Signals有効化
- Application Signals SLO
- CloudWatch Logs
- 削除確認用Outputs

ECS/Fargate版は、Application Signalsのsidecar構成が実務的だが、初版では重くなりやすいためOut of Scopeとする。上級補講または第2弾で扱う。

## Public Repository Scope

Publicリポジトリは `udemy-ai-company/public_repo/<repo-name>/` 配下で作業する。

候補:

- Repo name: `cloudwatch-application-signals-practical-cfn`
- Local working copy: `udemy-ai-company/public_repo/cloudwatch-application-signals-practical-cfn/`
- Public URL: 未公開。公開時に `course_curriculum.md` とREADMEへ反映する
- 内容:
  - CloudFormationテンプレート
  - `validate.sh`
  - `smoke_test.sh`
  - `stop_traffic.sh`
  - `README.md`
  - `docs/VALIDATION.md`

## CloudFormation Scope

候補リソース:

- `AWS::ApplicationSignals::Discovery`
- `AWS::ApplicationSignals::ServiceLevelObjective`
- `AWS::Lambda::Function`
- `AWS::Lambda::Permission`
- `AWS::Logs::LogGroup`
- `AWS::IAM::Role`
- `AWS::Scheduler::Schedule`
- `AWS::Scheduler::ScheduleGroup`

実装時の注意:

- Application SignalsのLambda計装にはAWS Lambda Layer for OpenTelemetry ARNが必要になるため、対応リージョンとLayer ARNを公式ドキュメントで確認してから実装する
- 自動トラフィックは初期値を低頻度にし、停止パラメータまたは停止コマンドを必須にする
- `create`、`update`、`delete`、`full` はCEO承認後にのみ実行する

## Cost Warning

本コースはAWSリソースを作成し、Application Signalsの利用料金が発生する可能性があります。

課金要素:

- Lambda実行
- CloudWatch Logs
- Application Signals
- Application Signals SLO
- EventBridge Scheduler
- CloudWatchメトリクス、アラーム等を追加した場合の料金

必須ルール:

- 自動トラフィックは低頻度にする
- 長時間放置しない
- ハンズオン後にトラフィック停止とスタック削除を行う
- 料金ページとCost Explorer/Billingを確認する
- 料金は断定せず、AWS公式料金ページを確認する

## Udemy成立尺是正結果

2026-05-17の既存コース動画監査では、通常レクチャーMP4は11本存在するが、合計尺は約13.2分でUdemy標準コースの30分要件に届いていなかった。

2026-05-17にCEOがApplication Signals動画作成とDriveアップロードを依頼し、通常レクチャー11本を再生成した。再生成後の講義本編は合計2049.580秒、約34.16分で、30分以上の要件を満たす。

是正内容:

- レクチャー数は現行の11本を維持した
- 各レクチャーをおおむね3分前後に再設計した
- Application Signalsの画面名紹介だけで終わらせず、観測前提、サンプル通信、画面の読み方、SLO判断、停止・削除・コスト確認を順に説明する構成へ拡張した
- 既存のGPT-Image2由来スライドPNGを完成動画に使用した
- VOICEVOX音声とMP4を全通常レクチャー分再生成した
- 2026-05-17にGoogle Driveレビュー用アップロードを完了し、URLを `qa/course_drive_upload_report.md` に記録した
- プロモーション動画は30分要件に含めていない

## Production Rules

- 完成動画のスライドPNGは必ずGPT-Image2由来にする
- 完成動画に表示するタイトル、短いラベル、図解内テキストもGPT-Image2に生成させる
- ローカル描画のみのスライドは下書き・検証用に限る
- ローカル文字合成したスライドを完成動画に使わない
- 音声はVOICEVOXを使う
- 1スライド1メッセージにする
- WorkerとReviewerを分離する

## Promotion Video Scope

公開前に、講座全体を紹介するプロモーション動画を通常レクチャーとは別に作成する。

- 目的: Application Signalsを実アプリで体験したい受講者へ、APM、Service Map、SLO監視を短く訴求する
- 主な訴求: サンプルアプリをCloudFormationで作る、低頻度通信でApplication Signalsの画面変化を見る、SLOと運用判断につなげる、停止・削除・コスト確認まで扱う
- 必須素材: `scripts/promo_video_script.md`、GPT-Image2 source PNG、GPT-Image2由来最終PNG、VOICEVOX音声、MP4、Drive upload report
- 制作ルール: `docs/PROMOTION_VIDEO_RULES.md`、`docs/GPT_IMAGE_RULES.md`、`docs/VIDEO_QUALITY_BASELINE.md` に従う
- 禁止: 通常レクチャー `s1-l1` をプロモーション動画の代用にしない

## Definition of Done

- `course_spec.md` がSource of Truthとして成立している
- 通常レクチャーが5本以上、講義本編の合計動画尺が30分以上である
- 動画再生成前にCEOが `course_spec.md` と `course_infomation.md` を確認・承認している
- AWS公式ドキュメントに基づく仕様確認レポートが存在する
- `course_infomation.md` にUdemy登録情報、歓迎メッセージ、お祝いメッセージがある
- `course_curriculum.md` にセクションタイトル、セクション学習目標、ハンズオンリソースタイトルがある
- CloudFormationテンプレート、README、validate script、smoke test script、stop traffic手順が存在する
- `aws cloudformation validate-template` が成功する
- CEO承認後にcreate/update/delete/full検証を行い、結果をQAレポートに残す
- 台本とREADMEが一致している
- スライドと表示文字はGPT-Image2生成である
- VOICEVOX音声、MP4、Drive URL、QAレポートが作成済みである
- プロモーション動画の台本、GPT-Image2素材、VOICEVOX音声、MP4、Drive URL、QAレポートが存在する
- WorkerとReviewerが別AIである

## Out of Scope

- ECS/Fargate sidecar構成
- EKS構成
- EC2常駐アプリ構成
- 本番APM設計の代行
- OpenTelemetry Collectorの詳細チューニング
- 30日データ前提のSLO Recommendationsを短時間ハンズオンで完了させること
- 高頻度・長時間の負荷生成
- CDK/Terraformによる本番IaC実装

## Voice and Terminology Rules

| 表記 | ナレーション |
| --- | --- |
| AWS | エーダブリューエス |
| CloudWatch | クラウドウォッチ |
| Application Signals | アプリケーションシグナルズ |
| APM | エーピーエム |
| Service Map | サービスマップ |
| Service detail | サービスディテール |
| Latency | レイテンシ |
| Availability | アベイラビリティ |
| Fault | フォルト |
| Error | エラー |
| SLO | エスエルオー |
| SLI | エスエルアイ |
| Lambda | ラムダ |
| EventBridge Scheduler | イベントブリッジスケジューラー |
| CloudFormation | クラウドフォーメーション |
| OpenTelemetry | オープンテレメトリー |
| ADOT | エードット |
| X-Ray | エックスレイ |
| CDK | シーディーケー |
| Terraform | テラフォーム |

## AWS Official Sources Checked

- CloudWatch Application Signals overview
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html
- Enable Application Signals on Lambda
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable-LambdaMain.html
- Enable Application Signals on Amazon ECS
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable-ECSMain.html
- `AWS::ApplicationSignals::Discovery`
  - https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-applicationsignals-discovery.html
- Application Signals SLO capabilities announcement
  - https://aws.amazon.com/about-aws/whats-new/2026/03/cloudwatch-application-signals-adds-slo-capabilities/
- Amazon CloudWatch Pricing
  - https://aws.amazon.com/cloudwatch/pricing/

- Application Map generally available announcement
  - https://aws.amazon.com/about-aws/whats-new/2025/10/application-map-generally-available-amazon-cloudwatch/
