# AWS課金事故防止入門: Budgets・Cost Explorer・削除チェックリスト

## Course Title

AWS課金事故防止入門: Budgets・Cost Explorer・削除チェックリスト

## Course ID

`aws-cost-safety-course`

## Source Candidate

- Market research ID: `VID-019`
- Original candidate title: `AWS Budgetsで課金事故を防ぐ`
- Related candidates: `VID-020`, `VID-021`, `VID-032`, `VID-042`, `VID-048`
- Market basis: 初学者の課金不安、ハンズオン前提教材、低コストで制作しやすい
- Strategic source: CloudWatch/Alarm/Logs/SLO講座群の前に置ける安全教材
- Priority: high

## Course Positioning

本コースは、AWS初学者がハンズオンや個人検証を安全に進めるための「課金事故防止」入門コースです。

既存のCloudWatch、Alarm/SNS、Logs Insights、SLO教材は、受講者がAWSアカウントを使う前提です。本コースではその前段として、AWS Budgets、Cost Explorer、Cost Anomaly Detection、削除チェックリスト、月次確認ルーティンを扱います。

「コストを必ず何円削減する」と約束するのではなく、「想定外の課金に早く気づき、原因を探し、削除漏れを減らす」ことをCourse Promiseにします。

## Target Audience

- AWS学習を始めたいが、課金事故が怖い人
- Udemyやハンズオン教材でAWSを使う前に、安全策を整えたい人
- AWS BudgetsやCost Explorerを開いたことはあるが、何を見ればよいか分からない人
- 個人開発、小規模チーム、学習用アカウントでAWS費用を管理したい人
- CloudWatch、SRE、FinOpsの入口として、コスト確認の基本習慣を身につけたい人

## Prerequisites

- AWSアカウントを持っている、または作成予定である
- AWSマネジメントコンソールの基本操作ができる
- メールを受信し、通知確認ができる
- Billing and Cost Managementを参照または設定できるIAM権限がある
- AWS CLIとCloudFormationは必須ではない
- 組織アカウントの場合、請求情報にアクセスできないことがある点を理解している

## Learning Objectives

受講後、受講者は以下を説明または実行できる状態になります。

- AWS課金事故が起きる典型パターンを説明できる
- AWSのコストデータやBudgets通知がリアルタイムではないことを説明できる
- AWS Budgetsで月次コスト予算を作成し、実績アラートと予測アラートを設定できる
- 予算通知メール、SNS通知、通知先確認の流れを説明できる
- Cost Explorerでサービス別、期間別、タグ別のコストを確認できる
- Cost Explorer APIや課金確認系APIを使う場合の注意点を説明できる
- Cost Anomaly Detectionの役割、モニター、サブスクリプション、通知しきい値を説明できる
- ハンズオン後に削除すべきリソースをチェックリスト化できる
- タグ、メモ、スタック名で学習用リソースを見失わない管理方法を説明できる
- 月次でコストを確認し、異常時に原因調査へ進むルーティンを作れる

## Course Promise

受講後、AWS学習や小規模検証を始める前に、月次予算アラート、コスト確認画面、異常検知、削除チェックリストを用意し、想定外の課金に早く気づける状態になります。

## Differentiation

- AWSサービス構築講座の前に置ける「安全準備」講座にする
- 料金表の暗記ではなく、課金事故を減らす日々の確認手順に絞る
- Budgets、Cost Explorer、Cost Anomaly Detection、削除チェックリストを一つの流れで扱う
- 「節約できる金額」ではなく「確認できる状態」を成果物にする
- 初学者向けにIAM権限、通知確認、データ反映遅延、削除漏れを丁寧に扱う
- CloudFormationはoptionalな教材再現用に限定し、標準手順はコンソール中心で進められる
- 実運用IaCはCDKまたはTerraform推奨という全社方針を維持する

## Chapter Structure

詳細なセクション別カリキュラムは `course_curriculum.md` を正とします。

1. 課金事故が起きる理由
   - `s1-l1` AWS課金事故防止の地図
   - `s1-l2` コストデータの遅れと無料枠の誤解

2. Budgetsで最初の安全柵を作る
   - `s2-l1` 月次予算を作る
   - `s2-l2` 実績アラートと予測アラート

3. Cost Explorerでコストを見る
   - `s3-l1` サービス別コストを読む
   - `s3-l2` 期間、タグ、フィルターで原因を絞る

4. Cost Anomaly Detectionで異常に気づく
   - `s4-l1` 異常コスト検知の考え方
   - `s4-l2` モニター、サブスクリプション、通知設計

5. タグと削除チェックリスト
   - `s5-l1` ハンズオン後の削除チェック
   - `s5-l2` タグとスタック名でリソースを見失わない

6. 月次コスト確認ルーティン
   - `s6-l1` 毎月15分のコストレビュー
   - `s6-l2` 次に学ぶAWS/SRE講座への接続

## Hands-on Scope

- AWS Budgetsの月次コスト予算をコンソールで作成する
- Actual通知とForecasted通知の違いを説明する
- 通知メールの受信確認を行う
- Cost Explorerで今月のコスト、サービス別コスト、期間比較を見る
- タグがある場合はタグ別コストの見方を確認する
- Cost Anomaly Detectionのモニターとサブスクリプションの役割を確認する
- 削除チェックリストを使い、学習用リソースの削除確認を行う
- 月次コスト確認ルーティンのテンプレートを作る
- optionalとして、CloudFormationでBudgets/Cost Anomaly Detection関連リソースを再現する範囲を検討する

## Hands-on Resources

| Resource Title | Path | Purpose |
| --- | --- | --- |
| 課金事故防止ハンズオン | `handson/README.md` | コンソール操作、確認観点、削除チェックリスト |
| optional CloudFormation方針 | `cloudformation/README.md` | Budgets/Cost Anomaly Detectionを教材用に再現する範囲 |
| 月次レビュー記録テンプレート | `qa/` | 制作時に追加予定。受講者が毎月の確認を記録する |
| 削除チェックリスト | `handson/README.md#削除チェックリスト` | ハンズオン後の課金源確認 |

## Hands-on IaC Scope

標準ハンズオンはAWSマネジメントコンソール中心にします。

CloudFormationは、受講者が追加ツールなしで同じ設定を再現しやすい場合に限り、optional教材として扱います。AWSリソース作成やCloudFormation stack作成/更新/削除は、CEO承認後の検証チケットでのみ実行します。

CloudFormation対象候補:

- `AWS::Budgets::Budget`
- `AWS::CE::AnomalyMonitor`
- `AWS::CE::AnomalySubscription`
- `AWS::SNS::Topic`
- `AWS::SNS::Subscription`

初期スコープ外:

- `AWS::Budgets::BudgetsAction`
- 自動停止、IAM deny、SCP適用などの強制アクション
- Savings PlansやReserved Instancesの購入判断
- Cost and Usage Report、Athena、Organizations配下の高度なFinOps設計

## Production IaC Positioning

本講座のCloudFormationは教材ハンズオン用です。

実運用では、チームの標準に合わせてCDKまたはTerraformで、Budgets、Cost Anomaly Detection、SNS、タグポリシー、運用ドキュメントを管理する前提で説明します。

## Cost Warning

本コースは課金事故を防ぐ講座ですが、AWS Billing and Cost Managementの利用やAPI呼び出し自体にも料金、権限、反映遅延の注意点があります。

必ず説明すること:

- AWS料金、無料枠、Budgets、Cost Explorer、Cost Anomaly Detectionの仕様や料金は変更されるため、公開前に公式情報を再確認する
- BudgetsやCost Explorerのデータはリアルタイムではなく、反映に時間がかかる
- Budgets通知は「即時停止」ではなく、気づくためのアラートである
- Cost Explorer APIはリクエスト課金が発生する場合があるため、講座内では不要なAPI連打を避ける
- Cost Anomaly Detectionは異常に気づく仕組みであり、すべての課金事故を防ぐ保証ではない
- Budget Actionsなど強い制御は初学者向け標準手順に含めない
- CloudFormation検証やAWS実行はCEO承認後にだけ行う

## Production Rules

- 完成動画のスライドPNGは必ずGPT-Image2由来にする
- 完成動画に表示するタイトル、短いラベル、図解内テキストもGPT-Image2に生成させる
- ローカル描画のみのスライドは下書き・検証用に限る
- ローカル文字合成したスライドを完成動画に使わない
- 音声はVOICEVOXを使う
- 料金や節約額を断定しない
- 古い料金情報、古いUI、無料枠の過剰な約束を避ける
- WorkerとReviewerを分離する

## Promotion Video Scope

公開前に、講座全体を紹介するプロモーション動画を通常レクチャーとは別に作成する。

- 目的: AWS学習前に課金事故への不安を減らしたい受講者へ、Budgets、Cost Explorer、異常検知、削除チェックを学べる講座だと伝える
- 主な訴求: 節約額を保証せず、想定外の課金に早く気づき、原因を探し、削除漏れを減らす習慣を作る
- 必須素材: `scripts/promo_video_script.md`、GPT-Image2 source PNG、GPT-Image2由来最終PNG、VOICEVOX音声、MP4、Drive upload report
- 制作ルール: `docs/PROMOTION_VIDEO_RULES.md`、`docs/GPT_IMAGE_RULES.md`、`docs/VIDEO_QUALITY_BASELINE.md` に従う
- 禁止: 通常レクチャー `s1-l1` をプロモーション動画の代用にしない
- 禁止: 特定の節約額、無料枠、料金の恒久性を保証しない

## Definition of Done

- `course_spec.md` がSource of Truthとして成立している
- AWS公式ドキュメントに基づく仕様確認レポートが存在する
- `course_curriculum.md` にセクションタイトル、セクション学習目標、ハンズオンリソースタイトルがある
- `README.md` と `handson/README.md` が存在し、標準手順が低リスクで再現できる
- AWS実行、Billing API実行、CloudFormation stack作成/更新/削除はCEO承認ゲートが明記されている
- optional CloudFormation範囲と標準コンソール手順の違いが明記されている
- 料金、無料枠、反映遅延、API課金の注意が明記されている
- 全レクチャーの `scripts/*_script.md` と `scripts/*_script.json` が存在する
- 全レクチャーのGPT-Image2プロンプトが存在する
- GPT-Image2 source PNG、最終PNG、contact sheetが各レクチャーに存在する
- VOICEVOX音声、MP4、QAレポート、Drive URLが各レクチャーに存在する
- プロモーション動画の台本、GPT-Image2素材、VOICEVOX音声、MP4、Drive URL、QAレポートが存在する
- WorkerとReviewerが別AIである

## Out of Scope

- AWS料金を法務、税務、会計観点で保証する
- 特定の節約額を約束する
- Savings Plans、Reserved Instances、Enterprise Discount Programの購入判断
- Organizations、Control Tower、SCPを含むマルチアカウント統制
- Cost and Usage Report、Athena、QuickSightを使う高度なFinOps分析
- 本番環境のコスト削減代行
- 自動停止LambdaやBudget Actionsによる強制停止
- Bedrockコスト最適化の詳細。生成AIコストは別講座候補として扱う

## Voice and Terminology Rules

ナレーションでは以下の読みを優先する。

| 表記 | ナレーション |
| --- | --- |
| AWS | エーダブリューエス |
| Billing | ビリング |
| Cost Management | コストマネジメント |
| AWS Budgets | エーダブリューエスバジェッツ |
| Budgets | バジェッツ |
| Cost Explorer | コストエクスプローラー |
| Cost Anomaly Detection | コストアノマリーディテクション |
| SNS | エスエヌエス |
| IAM | アイアム |
| CloudFormation | クラウドフォーメーション |
| CDK | シーディーケー |
| Terraform | テラフォーム |
| FinOps | フィンオプス |
| API | エーピーアイ |
| CSV | シーエスブイ |
| tag | タグ |
| forecasted | フォーキャステッド |
| actual | アクチュアル |

## References

- AWS Cost Management User Guide: Managing your costs with AWS Budgets
  - https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html
- AWS Cost Management User Guide: Analyzing your costs and usage with AWS Cost Explorer
  - https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html
- AWS Cost Anomaly Detection
  - https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/
- AWS CloudFormation Template Reference: AWS Billing and Cost Management Budgets
  - https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/AWS_Budgets.html
- AWS CloudFormation Template Reference: AWS Cost Explorer
  - https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/AWS_CE.html
