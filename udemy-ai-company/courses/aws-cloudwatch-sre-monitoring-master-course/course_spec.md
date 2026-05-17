# AWS CloudWatch/SRE監視実践マスター：Logs Insights・Alarm・SLO・運用改善

## Course Title

AWS CloudWatch/SRE監視実践マスター：Logs Insights・Alarm・SLO・運用改善

## Target Audience

- AWS監視をCloudWatchで始めたが、Logs、Metrics、Alarm、Dashboardの全体像がつながっていない人
- 障害調査、通知設計、Runbook、SLOレビューまで一連の運用として学びたい人
- SRE、クラウドエンジニア、インフラエンジニア、バックエンドエンジニアを目指す人
- CloudWatch Logs Insightsで調査クエリを書けるようになりたい人
- AlarmやSNS通知を作ったものの、通知疲れや重要度設計に悩んでいる人
- Application Signals、SLI/SLO、エラーバジェットをAWS運用に結びつけたい人
- AWSハンズオンで課金、IAM、CloudFormation rollbackが不安な人

## Prerequisites

- AWSアカウントを持っている、またはAWSの基本操作を学習できる環境がある
- CloudWatch、CloudWatch Logs、CloudWatch Alarmという名前を聞いたことがある
- AWS CLIをインストールし、認証情報とリージョンを設定できる
- Bashコマンドをコピーして実行できる
- HTTPステータスコード、レイテンシ、エラー率の意味をおおまかに理解している
- CloudFormationは教材ハンズオン再現用に使うため、基本操作を知っていると理解しやすい
- 実運用のIaCは、所属チームの方針に応じてCDKまたはTerraformで設計する前提を持てる

## Learning Objectives

- CloudWatch Metrics、Logs、Logs Insights、Alarm、Dashboard、Application Signalsの役割を説明できる
- Logs Insightsで障害調査に使う `fields`、`filter`、`parse`、`stats`、`sort` の基本パターンを使える
- CloudWatch Alarm、SNS、Composite Alarm、Metric Mathを使う場面を判断できる
- アラートのOwner、Severity、Runbookリンク、通知先を設計できる
- CloudFormationで教材用の監視基盤をREADME通りに作成、更新、確認、削除できる
- Application SignalsのLatency、Availability、Fault、Error、Service Map、SLO機能の使いどころを説明できる
- SLI、SLO、SLA、エラーバジェット、バーンレートをAWS監視設計へ接続できる
- Runbookを使って、アラート発生後の5分、15分、30分の初動対応を整理できる
- CloudFormation rollback、IAM AccessDenied、課金不安を安全に切り分けられる
- 週次・月次のSLOレビューで、信頼性の状態と改善アクションを説明できる

## Course Promise

受講後、CloudWatchを単なるメトリクス確認ツールとしてではなく、ログ調査、通知設計、初動対応、SLOレビュー、改善バックログまでつながるAWS監視運用の基盤として設計できる状態になります。

## Differentiation

- CloudWatchの機能紹介だけで終わらず、障害調査、通知設計、Runbook、SLOレビューまで一続きの運用として扱う
- 短尺講座の再録ではなく、章末演習、統合演習、設計レビュー、シナリオ型演習を追加する
- CloudFormationで低コストな教材ハンズオンを作り、README通りに再現できる品質を目指す
- Application Signalsは現行機能、課金、計装前提、30日データが必要な機能を分けて説明する
- 実運用IaCはCDKまたはTerraform推奨とし、CloudFormationは初学者が再現しやすい教材手段として位置づける
- 課金安全、IAM権限、CloudFormation rollbackを本編の安全設計として扱う
- VOICEVOX読み上げ品質を前提に、略語やAWS用語の読み方を統一する

## Bundle Relationship

この講座は、以下の短尺バンドルを統合する長尺旗艦コース候補です。

| Source Bundle | Integrated Topics | Long-Form Additions |
| --- | --- | --- |
| `BUNDLE-001 CloudWatch監視入門バンドル` | CloudWatch全体像、Logs Insights、Alarm/SNS | 章末演習、統合ログ調査、通知設計レビュー |
| `BUNDLE-002 SRE運用入門バンドル` | アラート設計、Runbook、SLO導入 | 初動対応シミュレーション、SLOレビュー会議 |
| `BUNDLE-003 発展監視・APMバンドル` | Application Signals、SLI/SLO、Lambdaエラー率 | Service Mapから原因仮説を作る演習 |
| `BUNDLE-004 AWS学習安全・トラブルシュートバンドル` | 課金安全、CloudFormation rollback、IAM AccessDenied | ハンズオン前後の安全チェックと失敗時の証跡保存 |

## Chapter Structure

1. 長尺コースのロードマップとAWS学習安全
   - コースのゴール、短尺講座との違い
   - ハンズオン実行前の課金、リージョン、権限確認
   - CloudFormationは教材用、実運用IaCはCDK/Terraformという前提

2. CloudWatchの全体像
   - Metrics、Logs、Alarm、Dashboard、Events、Application Signalsの地図
   - 監視、可観測性、インシデント対応、SLO運用の関係
   - CloudWatch料金の注意点

3. MetricsとDashboardの基礎
   - Namespace、Metric、Dimension、Statistic、Period
   - Dashboardで見るべき指標と見せるべき指標
   - Metric Mathと低コストなCustom Metricsの考え方

4. CloudWatch LogsとLogs Insights
   - Log Group、Log Stream、保存期間、検索範囲
   - Logs Insights query syntax
   - `fields`、`filter`、`parse`、`stats`、`sort`
   - 障害調査クエリ集とコストを抑える検索手順

5. Alarm、SNS、通知設計
   - Metric Alarm、Composite Alarm、Missing Data、Evaluation Period
   - SNS通知、通知先、確認メール
   - 通知疲れを避けるSeverity、Owner、Runbookリンク

6. CloudFormationで監視基盤を作る
   - 教材用テンプレートの読み方
   - validate、create、update、smoke test、delete
   - README通り再現できることを合格条件にする

7. Application SignalsとAPMの入口
   - Service Map、Latency、Availability、Fault、Error
   - 実アプリ計装、ADOT、リクエスト課金、SLO課金の考え方
   - SLO Recommendations、Service-Level SLO、SLO Performance Reportの使いどころ

8. SLI/SLO、エラーバジェット、バーンレート
   - SLI、SLO、SLAの違い
   - 可用性、レイテンシ、エラー率のSLI設計
   - エラーバジェットとバーンレート通知

9. Runbookと初動対応
   - アラート後5分、15分、30分の行動
   - 証跡保存、影響範囲確認、暫定対応、エスカレーション
   - Runbookを更新するレビュー観点

10. AWS学習安全とトラブルシュート
    - Cost Explorer、Budgets、削除チェック
    - CloudFormation rollbackのEvents読解
    - IAM AccessDeniedの切り分け

11. 統合Capstone: CloudWatch/SRE監視運用を作る
    - サンプルサービスの監視要求を読む
    - Logs Insights、Alarm、Dashboard、Runbook、SLOを統合する
    - 障害調査とSLOレビューを実施する

12. 運用改善と次の学習パス
    - 週次・月次レビュー
    - 改善バックログ化
    - CDK/Terraform、本番計装、外部SaaS監視への発展

## Hands-on Scope

本講座のハンズオンは、低コストで短時間に削除できる教材用環境に限定する。

- CloudWatch Logsのサンプルログ調査
- Logs Insightsクエリの実行と結果解釈
- CloudWatch Custom Metricsの投入
- Metric Alarm、Composite Alarm、SNS Topic、Dashboardの作成
- Runbookリンク、Owner、Severityの設計演習
- CloudFormation validate、create、update、smoke test、delete
- 低コストなSLO風ダッシュボードとバーンレート説明用メトリクス
- Application Signalsは、実アプリ計装と継続データが必要な範囲をデモまたは補講として扱う
- Capstoneでは、ログ調査、アラート設計、Runbook、SLOレビューを1つのシナリオに統合する

## Hands-on IaC Scope

教材ハンズオンではCloudFormationを使用する。

理由:

- 初学者が追加ツールなしで再現しやすい
- Udemy受講者がREADME通りに作成、確認、削除しやすい
- validate、create、update、smoke test、deleteを品質ゲート化しやすい

対象候補:

- `AWS::CloudWatch::Alarm`
- `AWS::CloudWatch::CompositeAlarm`
- `AWS::CloudWatch::Dashboard`
- `AWS::Logs::LogGroup`
- `AWS::SNS::Topic`
- `AWS::SNS::Subscription` は任意
- `AWS::IAM::Role` は必要最小限に限定
- `AWS::ApplicationSignals::ServiceLevelObjective` はオプションまたは補講として扱う

## Production IaC Positioning

実運用ではCloudFormationを唯一の推奨手段とはしない。

- チーム開発、レビュー、再利用性、テスト容易性を重視する場合はCDKまたはTerraformを推奨する
- 教材ではCloudFormationで構造を理解し、実運用ではCDK/Terraformへ移す考え方を説明する
- 本番環境への直接適用は本講座の範囲外とする

## Cost Warning

CloudWatch Logs、Logs Insights、Custom Metrics、Alarm、Dashboard、SNS、Application Signals、SLOには料金が発生する場合があります。

各ハンズオンは以下を満たす必要があります。

- 想定リージョンを明記する
- 作成するリソースを明記する
- 料金が発生し得るポイントを明記する
- Logs Insightsは検索対象Log Groupと時間範囲を絞る
- Application Signalsはリクエスト数とSLO数に応じた料金が発生し得ることを説明する
- 削除手順を必ず用意する
- `validate.sh full` で削除まで確認する

## Promotion Video Scope

公開前に、講座全体を紹介するプロモーション動画を通常レクチャーとは別に作成する。

- 目的: CloudWatchをSRE監視運用へ発展させたい受講者へ講座価値を伝える
- 主な訴求: ログ調査、通知設計、Runbook、SLOレビュー、学習安全まで一気通貫で扱う
- 制作ルール: `docs/PROMOTION_VIDEO_RULES.md`、`docs/GPT_IMAGE_RULES.md`、`docs/VIDEO_QUALITY_BASELINE.md` に従う
- 禁止: 通常レクチャーをプロモーション動画の代用にしない

## Production Scope

- 想定本編時間: 10〜12時間
- 想定レクチャー数: 60前後
- 1レクチャー目安: 8〜14分
- 完成動画スライド: GPT-Image2由来PNGのみ
- ナレーション: VOICEVOX
- アップロード: Google Drive一括アップロード
- 既存短尺MP4の大量流用はしない

## Definition of Done

- `course_spec.md` がSource of Truthとして成立している
- `course_curriculum.md` に全セクション、全レクチャー、ハンズオン有無、想定時間がある
- `course_infomation.md` にUdemy登録画面へ入力できる情報がある
- バンドルとの関係と、短尺講座からの重複回避が明記されている
- CloudFormationを教材ハンズオン用途に限定した範囲が定義されている
- 実運用IaCはCDKまたはTerraform推奨として説明されている
- Application Signalsの現行SLO機能を扱う範囲と制約が明記されている
- 課金、安全、IAM、rollbackの注意がカリキュラム内に含まれている
- GPT-Image2とVOICEVOXの制作前提が明記されている
- ハンズオンはREADME通りに再現できる品質ゲートを持つ
- WorkerとReviewerが別AIである
- AI-QA-01による企画レビューが完了している

## Out of Scope

- 既存本番環境への直接導入代行
- 24時間以上の負荷試験
- Datadog、New Relic、Grafana Cloudなど外部SaaSの実装ハンズオン
- Kubernetes/EKSに特化した高度な分散トレーシング運用
- マルチアカウント、マルチリージョンの本番監視基盤構築
- 法務上のSLA契約書レビュー
- 既存短尺講座MP4の単純な再販売用連結

## Voice and Terminology Rules

VOICEVOX読み上げでは以下を優先する。

- `CloudWatch` は「クラウドウォッチ」
- `Logs Insights` は「ログズインサイト」
- `Application Signals` は「アプリケーションシグナル」
- `SLI` は「エスエルアイ」
- `SLO` は「エスエルオー」
- `SLA` は「エスエルエー」
- `SNS` は「エスエヌエス」
- `IAM` は「アイアム」
- `AWS CLI` は「エーダブリューエスシーエルアイ」
- `error budget` は「エラーバジェット」
- `burn rate` は「バーンレート」
- `rollback` は「ロールバック」

台本生成後は必ずナレーションチェッカーを実行する。

```bash
python3 tools/narration_checker.py courses/aws-cloudwatch-sre-monitoring-master-course/scripts
```

## References

- CloudWatch Logs Insights query syntax
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html
- CloudWatch Application Signals service level objectives
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html
- Amazon CloudWatch Application Signals adds new SLO capabilities
  - https://aws.amazon.com/about-aws/whats-new/2026/03/cloudwatch-application-signals-adds-slo-capabilities/
- AWS::CloudWatch::CompositeAlarm
  - https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-compositealarm.html
