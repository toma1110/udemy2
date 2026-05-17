# Udemy Bundle Strategy

このドキュメントは、短尺単品講座をUdemy Course Bundlesと将来の長尺旗艦コースへ接続するための制作方針です。

## Decision

直近の目標は、30〜60分の単品講座を量産すること自体ではなく、バンドル化できる短尺モジュールを作ることです。

制作順序:

1. 単品講座として5レクチャー以上、講義本編30分以上で成立させる
2. 2〜3本単位のUdemyバンドルとして学習パスを作る
3. 売上、レビュー、受講完了率、Q&Aを見て、8〜16時間級の長尺旗艦コースへ再編集する

## Near-Term Bundle

最初の直近目標は `BUNDLE-001 CloudWatch監視入門バンドル` とする。

| Bundle | Course | Course Role | Current Ticket |
| --- | --- | --- | --- |
| `BUNDLE-001` | `aws-cloudwatch-intro-course` | CloudWatch全体像、Metrics、Logs、Alarm、Dashboardの地図 | `TASK-0214` |
| `BUNDLE-001` | `aws-cloudwatch-logs-insights-practical-course` | 障害調査クエリ集、Logs Insightsの実務入口 | `TASK-0213` |
| `BUNDLE-001` | `aws-cloudwatch-alarm-sns-course` | Alarm、SNS、通知設計、CloudFormationハンズオン | `TASK-0215` |

バンドルの約束:

CloudWatchの全体像を理解し、ログ調査と通知設計までを、初学者が順番に学べる状態にする。

## Bundle Portfolio

各コースは原則として、1つのprimary bundleへ所属させる。別バンドルからは関連講座として案内してよいが、同じMP4を大量に重複販売する前提にはしない。

| Bundle | Status | Candidate Courses | Purpose | Owner Ticket |
| --- | --- | --- | --- | --- |
| `BUNDLE-001 CloudWatch監視入門バンドル` | Near-term | `aws-cloudwatch-intro-course`, `aws-cloudwatch-logs-insights-practical-course`, `aws-cloudwatch-alarm-sns-course` | CloudWatchの全体像、ログ調査、通知設計を順番に学ぶ | `TASK-0220` |
| `BUNDLE-002 SRE運用入門バンドル` | Next | `aws-alert-design-practical-course`, `aws-runbook-first-response-course`, `aws-slo-adoption-course` | アラート設計、初動対応、SLO運用レビューをつなげる | `TASK-0221` |
| `BUNDLE-003 発展監視・APMバンドル` | Next | `aws-cloudwatch-application-signals-practical-course`, `aws-sli-slo-metrics-intro-course`, `aws-lambda-error-rate-monitoring-course` | Application Signals、SLI/SLOメトリクス、Lambdaエラー率を実務監視へ接続する | `TASK-0222` |
| `BUNDLE-004 AWS学習安全・トラブルシュートバンドル` | Next | `aws-cost-safety-course`, `aws-cloudformation-rollback-troubleshooting-course`, `aws-iam-accessdenied-troubleshooting-course` | 課金事故、CloudFormation失敗、IAM権限エラーを安全に避ける | `TASK-0223` |

## BUNDLE-002: SRE運用入門バンドル

バンドルの約束:

アラートを鳴らす基準、鳴った後の初動対応、信頼性を数値でレビューする流れを、SRE初学者が一続きで説明できる状態にする。

推奨受講順:

1. `aws-alert-design-practical-course`
2. `aws-runbook-first-response-course`
3. `aws-slo-adoption-course`

役割分担:

| Course | Role | Do Not Overlap |
| --- | --- | --- |
| `aws-alert-design-practical-course` | 良いアラート、悪いアラート、Owner、Severity、Runbookリンクを設計する | Runbook本文の詳細作成やSLOレビュー運用を深掘りしない |
| `aws-runbook-first-response-course` | アラート後の5分、15分、30分の初動対応をRunbook化する | アラート条件設計やSLO計算を主題にしない |
| `aws-slo-adoption-course` | SLI、SLO、エラーバジェット、バーンレート、週次/月次レビューへ発展させる | 初動Runbookの細部や個別アラート文面レビューを主題にしない |

長尺旗艦コースで深掘りする範囲:

- Alert design review workshop
- Incident response simulation
- SLO review meeting scenario
- Postmortemと改善バックログへの接続

## BUNDLE-003: 発展監視・APMバンドル

バンドルの約束:

メトリクス名の暗記ではなく、アプリケーションの状態、依存関係、エラー率、SLI/SLO候補を運用判断へ接続できる状態にする。

推奨受講順:

1. `aws-sli-slo-metrics-intro-course`
2. `aws-lambda-error-rate-monitoring-course`
3. `aws-cloudwatch-application-signals-practical-course`

役割分担:

| Course | Role | Do Not Overlap |
| --- | --- | --- |
| `aws-sli-slo-metrics-intro-course` | ユーザー体験からAWSメトリクス候補へ落とす入口を作る | SLO運用レビューやApplication Signals実ハンズオンを深掘りしない |
| `aws-lambda-error-rate-monitoring-course` | LambdaのErrors、Invocations、エラー率、低トラフィック時の通知判断を扱う | 汎用アラート設計全体やApplication Signalsの画面操作を主題にしない |
| `aws-cloudwatch-application-signals-practical-course` | 実アプリのLatency、Availability、Fault、Error、Service Map、SLOを体験する | CloudWatch全体入門やSLO概念全体を繰り返し説明しない |

長尺旗艦コースで深掘りする範囲:

- サンプルアプリの正常、遅延、エラーシナリオ比較
- Service MapからRunbookへつなぐ演習
- Lambda、API Gateway、ALB、RDSのSLI候補レビュー
- Application SignalsとCloudWatch Alarmの使い分け

## BUNDLE-004: AWS学習安全・トラブルシュートバンドル

バンドルの約束:

AWS学習やハンズオンで詰まりやすい、課金不安、CloudFormation失敗、IAM AccessDeniedを、安全に切り分けて次の行動へ進める状態にする。

推奨受講順:

1. `aws-cost-safety-course`
2. `aws-cloudformation-rollback-troubleshooting-course`
3. `aws-iam-accessdenied-troubleshooting-course`

役割分担:

| Course | Role | Do Not Overlap |
| --- | --- | --- |
| `aws-cost-safety-course` | Budgets、Cost Explorer、異常検知、削除チェックで課金事故への不安を下げる | CloudFormation Events読解やIAM権限設計を主題にしない |
| `aws-cloudformation-rollback-troubleshooting-course` | Stack status、Events、Status Reasonから失敗原因を読む | IAM AccessDenied全般や課金管理全般を深掘りしない |
| `aws-iam-accessdenied-troubleshooting-course` | エラー文、CloudTrail、ポリシー種類から権限エラーを切り分ける | CloudFormation rollback全体やBudgets設定を主題にしない |

長尺旗艦コースで深掘りする範囲:

- ハンズオン前の安全チェック
- 失敗時の証跡保存
- CloudFormation rollback事例演習
- IAM変更のimpact analysisとレビュー

## Future Bundle Candidates

以下は現時点では単品または関連講座として扱い、2〜3本の自然な束が揃った時点でbundle化する。

| Candidate | Needed Before Bundle |
| --- | --- |
| `aws-github-actions-oidc-course` | CI/CD、CodePipeline、CloudFormation deploy safetyなど、OIDCと並べる2本目・3本目が必要 |
| `aws-cloudformation-rollback-troubleshooting-course` の実演版 | rollback読解単品が完成し、実アカウント演習をCEO承認後に分離できた場合 |
| `aws-iam-accessdenied-troubleshooting-course` の実演版 | IAM変更を伴わない安全な読解版が完成した後 |

## Non-Overlap Rules

短尺単品と長尺旗艦コースの両方を作るため、重複は以下の基準で扱う。

- 前提用語の短い復習は許可する
- 同じ図解コンセプトの再利用は許可する
- 同じMP4を複数講座へ大量に入れない
- 単品講座は1テーマ1成果物を守る
- バンドル内の各講座は学習成果を重ねすぎない
- 長尺旗艦コースは短尺講座の連結ではなく、統合演習、章末演習、設計レビュー、運用判断を追加して再編集する

## Course-Level Requirements

各単品講座の `course_spec.md`、`course_curriculum.md`、`course_infomation.md` には、以下を明記する。

- この講座単体で到達する学習成果
- どのバンドルに入るか
- バンドル内での役割
- 他講座と重複させない範囲
- 将来の長尺旗艦コースへ統合するときに深掘りする範囲

## Flagship Course Direction

将来の旗艦候補:

`FLAGSHIP-001 AWS CloudWatch/SRE監視実践マスター`

Course ID:

`aws-cloudwatch-sre-monitoring-master-course`

Owner Ticket:

`TASK-0224`

目標:

- 8〜16時間
- CloudWatch、Logs Insights、Alarm/SNS、Application Signals、SLO、Runbook、Cost Safetyを体系化
- 単品講座の売れ筋テーマを優先して拡張
- CloudFormation教材ハンズオンは初学者がREADME通り再現できる範囲に限定
- 実運用IaCはCDKまたはTerraform推奨として扱う

統合元:

| Source | Role in Flagship |
| --- | --- |
| `BUNDLE-001 CloudWatch監視入門バンドル` | CloudWatch全体像、Logs Insights、Alarm/SNSの基礎導線 |
| `BUNDLE-002 SRE運用入門バンドル` | アラート設計、Runbook、SLO運用レビュー |
| `BUNDLE-003 発展監視・APMバンドル` | Application Signals、SLI/SLO、Lambdaエラー率 |
| `BUNDLE-004 AWS学習安全・トラブルシュートバンドル` | 課金安全、CloudFormation rollback、IAM AccessDenied |

長尺版で追加するもの:

- 章末演習
- 統合CloudFormationハンズオン
- 障害調査シミュレーション
- アラート設計レビュー
- Runbook初動対応シミュレーション
- SLOレビュー会議シナリオ
- 学習安全とトラブルシュートの横断チェック

長尺版で避けるもの:

- 短尺講座MP4の単純連結
- 同じ説明の大量重複
- CloudFormationを実運用IaCの唯一推奨として見せること
- Application Signalsの課金や計装前提を曖昧にしたハンズオン化

## Bundle-Level Definition of Done

- `BUNDLE-001` の3講座がそれぞれ30分以上の単品講座として成立している
- 3講座の学習成果が重複しすぎていない
- 各講座の販売ページ文言に、次に学ぶべき関連講座が示されている
- バンドル全体の受講順、対象者、到達点が説明できる
- 長尺旗艦コースへ統合する時に、どこを深掘りするかが整理されている
- `BUNDLE-002` 以降も、各講座のprimary bundleと重複させない範囲が明記されている
- 同じMP4の大量使い回しを前提にしていない
