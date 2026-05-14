# AWSで学ぶSLO導入実践：SLI設計・エラーバジェット・SRE運用レビュー

## Course Title

AWSで学ぶSLO導入実践：SLI設計・エラーバジェット・SRE運用レビュー

## Target Audience

- SREになりたいインフラエンジニア、クラウドエンジニア、バックエンドエンジニア
- CloudWatchで監視はしているが、SLI/SLOに結びつけられていない人
- アラート対応はしているが、信頼性を数値で説明できない人
- 「99.9%の根拠」「エラーバジェットの使い方」「バーンレート通知」を現場で説明できるようになりたい人
- SREチーム立ち上げ、またはSREロールへのキャリア移行を検討している人

## Prerequisites

- AWS CLIを設定済みである
- CloudFormationの基本操作を理解している
- CloudWatch Alarm、Dashboard、Metricsの基本を知っている
- HTTPステータスコード、レイテンシ、エラー率の意味を理解している
- Bashを実行できる環境がある

## Learning Objectives

- SLI、SLO、SLA、エラーバジェットの違いを説明できる
- ユーザー体験から逆算してSLIを選定できる
- 可用性、レイテンシ、エラー率のSLOを設計できる
- CloudWatchでSLO用メトリクス、Alarm、Dashboardを構築できる
- Application SignalsのSLO機能で何ができるかを説明できる
- バーンレートを使ってエラーバジェット消費を監視できる
- 開発チーム、PM、経営層へSLO導入の価値を説明できる
- SLOレビューを週次/月次の運用に組み込める

## Course Promise

受講後、自分のサービスに適したSLIを選び、SLOとエラーバジェットを設計し、AWS上で計測、可視化、バーンレート通知、関係者への説明まで進められる状態になります。

## Differentiation

- SLOの概念説明だけで終わらず、AWS上で再現できるハンズオンにする
- CloudFormationでSLO関連リソースを管理し、README通りに再現できる品質を目指す
- CloudWatch Application Signalsの現行SLO機能も扱い、古い自作Alarm講座だけにしない
- SLOを「作る」だけでなく、エラーバジェットを意思決定に使うところまで扱う
- 開発チーム、PM、経営層への説明テンプレートを含める
- VOICEVOX読み上げ品質を前提に、SLO/SLIは音声上「エスエルオー」「エスエルアイ」で統一する

## Chapter Structure

1. SLO導入で解決する現場課題
   - アラートが鳴り止まない現場の正体
   - 信頼性を数値で語れない問題
   - SREを目指す人がSLOを学ぶ意味

2. SLI、SLO、SLA、エラーバジェットの関係
   - SLIは何を測るか
   - SLOはどの水準を目指すか
   - SLAは外部への約束
   - エラーバジェットは意思決定の余白

3. ユーザー体験からSLIを選ぶ
   - 可用性、レイテンシ、エラー率
   - p95/p99を使う理由
   - CPU使用率をSLIにしない理由
   - AWSサービス別のSLI選定: ALB、API Gateway、ECS、Lambda、RDS

4. AWSでSLOを計測する
   - CloudWatch MetricsでSLIを表現する
   - Application SignalsでLatencyとAvailabilityを扱う
   - period-based SLOとrequest-based SLOの違い
   - 30日データを使ったSLO Recommendationsの位置づけ

5. CloudFormationでSLO基盤を作る
   - Custom Metricを使った低コストSLOハンズオン
   - `AWS::ApplicationSignals::ServiceLevelObjective` の考え方
   - Alarm、SNS、Dashboardの構成
   - stack create、update、smoke test、delete

6. エラーバジェットとバーンレート
   - エラーバジェットの計算
   - バーンレートとは何か
   - 短期窓と長期窓の組み合わせ
   - バーンレートAlarmの設計

7. SLOダッシュボードを作る
   - 見るべき指標と見せるべき指標を分ける
   - 現在の達成率、残りエラーバジェット、バーンレート
   - 運用担当向けとマネジメント向けの表示差分

8. SLOを組織に導入する
   - 開発チームへの説明
   - PM、経営層への報告
   - リリース判断とエラーバジェットの関係
   - SLOが形骸化するパターン

9. SLOレビューを運用に組み込む
   - 週次レビュー
   - 月次レビュー
   - インシデント対応との連動
   - SLOを育てる改善サイクル

## Hands-on Scope

- CloudFormationテンプレートを検証する
- サンプル用CloudWatch Custom Metricsを投入する手順を作る
- 可用性SLO、レイテンシSLO、エラー率SLOの設計例を作る
- `AWS::ApplicationSignals::ServiceLevelObjective` を使ったSLO定義を作る
- CloudWatch Alarmでバーンレート通知を作る
- SNS Topicで通知先を作る
- CloudWatch DashboardでSLO達成率、エラーバジェット、バーンレートを可視化する
- `validate.sh` でvalidate、create、update、smoke test、deleteを実行する
- Application SignalsのSLO Recommendations、Service-Level SLO、SLO Performance Reportは、30日データや実アプリ計装が必要なため、実装ハンズオンではなく補講/デモとして扱う

## CloudFormation Scope

本講座のハンズオン範囲では、受講者が追加ツールを用意せずREADME通りに再現しやすいようにCloudFormationで管理する。実運用IaCとしては、チームの開発体制や既存資産に応じてCDKまたはTerraformを使う前提で考える。

対象候補:

- `AWS::ApplicationSignals::ServiceLevelObjective`
- `AWS::CloudWatch::Alarm`
- `AWS::CloudWatch::Dashboard`
- `AWS::SNS::Topic`
- `AWS::SNS::Subscription` はメールアドレス指定時のみ
- `AWS::IAM::Role` は必要最小限に限定し、必要な場合のみ作る

注意:

- Application Signalsで初回SLO作成時、AWSが `AWSServiceRoleForCloudWatchApplicationSignals` サービスリンクロールを自動作成する場合がある
- READMEとQAレポートには、自動作成されるロール、必要権限、削除後に残る可能性がある管理リソースを明記する

CloudFormationで直接表現しにくい操作:

- Application SignalsのSLO Recommendations確認
- 30日間の実測データに基づく推奨値検証
- 実アプリケーション計装の完全再現

上記はREADMEで前提、制約、デモ扱いの理由を明記する。

## Cost Warning

CloudWatch Custom Metrics、Alarm、Dashboard、SNS、Application Signals、SLOには料金が発生する場合があります。特にApplication Signalsはリクエスト数やSLO数に応じて課金されるため、ハンズオンでは低トラフィック、短時間、削除手順必須で運用します。

各ハンズオンは以下を満たす必要があります。

- 想定リージョンを明記する
- 作成するリソースを明記する
- 料金が発生し得るポイントを明記する
- 削除手順を必ず用意する
- `validate.sh full` で削除まで確認する

## Definition of Done

- `course_spec.md` がSource of Truthとして成立している
- CloudFormationを教材ハンズオン用途に限定した範囲が定義されている
- Application Signalsの現行SLO機能を扱う範囲と制約が明記されている
- 低コスト版と現行AWS機能版の役割が分かれている
- VOICEVOX読み上げ方針が明記されている
- ハンズオンはREADME通りに再現できる
- `validate.sh`、`smoke_test.sh`、削除手順が存在する
- WorkerとReviewerが別AIである
- AI-QA-01による企画レビューが完了している

## Out of Scope

- 本番システムへの直接導入代行
- 既存アプリケーションの完全な計装移行
- 24時間以上の負荷試験
- Datadog、New Relic、Grafana Cloudなど外部SaaSでのSLO実装
- Kubernetes/EKSに特化した高度なSLO運用
- 複数AWSアカウント、複数リージョンをまたぐ本番運用設計
- SLA契約書の法務レビュー

## Voice and Terminology Rules

VOICEVOX読み上げでは以下を優先する。

- `SLO` は「エスエルオー」
- `SLI` は「エスエルアイ」
- `SLA` は「エスエルエー」
- `error budget` は「エラーバジェット」
- `burn rate` は「バーンレート」
- `Application Signals` は「アプリケーションシグナル」
- `CloudWatch` は「クラウドウォッチ」
- `AWS CLI` は「エーダブリューエスシーエルアイ」
- `STEP 5` や `ステップ 5` ではなく「ステップ5」

台本生成後は必ず以下を実行する。

```bash
python3 tools/narration_checker.py courses/aws-slo-adoption-course/scripts
```

## References

- Google SRE Book: Service Level Objectives
  - https://sre.google/sre-book/service-level-objectives/
- Google SRE Workbook: Implementing SLOs
  - https://sre.google/workbook/implementing-slos/
- Amazon CloudWatch: Service level objectives
  - https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html
- AWS CloudFormation: `AWS::ApplicationSignals::ServiceLevelObjective`
  - https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-applicationsignals-servicelevelobjective.html
- AWS What's New: Amazon CloudWatch Application Signals adds new SLO capabilities
  - https://aws.amazon.com/about-aws/whats-new/2026/03/cloudwatch-application-signals-adds-slo-capabilities/
