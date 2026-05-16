# AWS課金事故防止ハンズオン

Source of Truth: `../course_spec.md`

## 目的

AWS学習前に、予算アラート、コスト確認、異常検知、削除チェックリストを整える。

## 実行前チェック

- Billing and Cost Managementを参照または設定できる権限がある
- 通知を受け取るメールアドレスを用意している
- 組織アカウントの場合、請求情報の表示権限が制限されていないか確認する
- AWS料金や無料枠は変わるため、公開前に公式情報を確認する
- BudgetsやCost Explorerはリアルタイムではなく、反映に時間がかかることを理解する

## Budgets

標準ハンズオンでは、AWSマネジメントコンソールから月次コスト予算を作る。

確認する項目:

- Budget type: Cost budget
- Period: Monthly
- Amount: 受講者自身が許容できる少額にする
- Alert 1: Actual costが予算の一定割合を超えたら通知する
- Alert 2: Forecasted costが予算を超える見込みなら通知する
- Subscriber: 受講者が確認できるメールアドレス

注意:

- Budgets通知は課金を自動停止するものではない
- 通知メールを受け取れることを確認する
- Budget Actionsは本講座の標準手順に含めない

## 通知確認

- Budgetsの通知先メールを確認する
- SNSを使う場合はサブスクリプション確認メールを承認する
- 通知が届かない場合は、メールアドレス、迷惑メール、権限、リージョンを確認する

## Cost Explorer

Cost Explorerでは、以下を確認する。

- 今月の累計コスト
- サービス別コスト
- 日別の変化
- 前月との比較
- タグがある場合はタグ別コスト

注意:

- Cost Explorerのデータは反映に時間がかかる
- APIを使う場合はリクエスト課金が発生する可能性がある
- 講座内の数値計算は、公開前QAでスクリプトまたは表計算により確認する

## タグ確認

学習用リソースには、以下のようなタグや命名を推奨する。

| Key | Value例 |
| --- | --- |
| `Project` | `udemy-handson` |
| `Course` | `aws-cost-safety-course` |
| `Owner` | 自分の名前または識別子 |
| `ExpiresOn` | 削除予定日 |

タグが使えないリソースや請求系設定については、READMEやメモに作成日、目的、削除予定を記録する。

## Cost Anomaly Detection

Cost Anomaly Detectionでは、以下を確認する。

- 何を監視するモニターか
- 通知頻度を個別、日次、週次のどれにするか
- 通知しきい値をどう決めるか
- 通知先をメールまたはSNSにするか

注意:

- 異常検知はすべての課金事故を防ぐ保証ではない
- 誤検知や検知遅れがあり得る
- 異常通知を受けたら、Cost Explorerでサービス別、期間別、タグ別に原因を確認する

## 通知設計

初学者向けの推奨方針:

- まずはメール通知で始める
- チーム運用ではSNS連携を検討する
- 深夜に即対応する通知と、翌営業日に確認する通知を分ける
- しきい値は「自分が調査したい金額」から決める

## 削除チェックリスト

ハンズオン後に確認する項目:

- CloudFormation stackが残っていないか
- EC2、EBS、Elastic IP、NAT Gateway、Load Balancerが残っていないか
- RDS、ElastiCache、OpenSearchなどの継続課金リソースが残っていないか
- CloudWatch Logsのログ保持期間が無期限になっていないか
- CloudWatch Alarms、Dashboards、Custom Metricsが不要になっていないか
- S3 bucketに不要なデータが残っていないか
- SNS Topic、Subscriptionが不要になっていないか
- Cost Explorerで数日後にコストが増え続けていないか

## 月次レビュー

毎月15分で確認する項目:

- 今月の累計コスト
- サービス別の上位5件
- 前月より増えたサービス
- Budget通知の有無
- Anomaly通知の有無
- 削除予定を過ぎた学習用リソース
- 次月に続ける検証と削除する検証

## AWS実行ゲート

このREADMEの内容を実AWSで検証する場合は、CEO承認後に別チケットで実行する。
