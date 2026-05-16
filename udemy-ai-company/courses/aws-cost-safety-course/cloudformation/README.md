# optional CloudFormation 方針

Source of Truth: `../course_spec.md`

## 位置づけ

本講座の標準ハンズオンはAWSマネジメントコンソール中心です。

CloudFormationは、教材として同じ設定を再現しやすい場合に限りoptionalで扱います。実運用IaCとしては、CDKまたはTerraformを推奨します。

## 対象候補

- `AWS::Budgets::Budget`
- `AWS::CE::AnomalyMonitor`
- `AWS::CE::AnomalySubscription`
- `AWS::SNS::Topic`
- `AWS::SNS::Subscription`

## 初期スコープ外

- `AWS::Budgets::BudgetsAction`
- 自動停止、IAM deny、SCP適用などの強制制御
- Savings PlansやReserved Instancesの購入判断
- Organizations配下のマルチアカウント統制

## 検証ゲート

CloudFormation template作成、validate、stack create、update、deleteは別チケットで行います。

AWSリソース作成、Billing/Cost API実行、CloudFormation stack操作はCEO承認後にだけ実行します。
