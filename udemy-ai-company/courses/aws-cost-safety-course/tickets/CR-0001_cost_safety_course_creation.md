# Change Request

## Change Summary

AWS課金事故防止入門を新規コースとして作成する。

## Why Change

CloudWatch、Alarm/SNS、Logs Insights、SLOの既存コース群はAWSアカウント利用を前提にしている。受講者の課金不安を先に解消する入口講座を作ることで、AWS/SRE講座群への導線と受講完了率を高められるため。

## Scope

- 新規コースディレクトリ作成
- `course_spec.md`、`course_curriculum.md`、`README.md`、`course_infomation.md` 作成
- ハンズオンREADME、optional CloudFormation方針、QA初期レポート作成
- 動画制作チケット作成

## Impact

- 他のAWS講座の前提教材として使える
- 初学者の課金不安に直接対応できる
- 既存のSRE実践コースのコスト管理資産と接続できる
- Billing/Cost関連の説明は公式情報確認とCEO承認ゲートがより重要になる

## Risks

- AWS料金、無料枠、画面UI、Cost Management機能は変更される
- 料金説明を断定すると誤解を招く
- BudgetsやCost Explorerはリアルタイムではないため、受講者が「完全防止」と誤解する可能性がある
- Billing/Cost APIやCloudFormation stack操作には課金、権限、管理上の影響がある

## Approval

- CEO request: 「okです！お願い！」
- Course creation approved
- AWS実行、Billing/Cost API実行、CloudFormation stack作成/更新/削除は別途CEO承認が必要

## Implementation Plan

1. AWS公式ドキュメントでBudgets、Cost Explorer、Cost Anomaly Detection、CloudFormationリソースを確認する
2. 新規コース仕様とカリキュラムを作る
3. ハンズオンREADMEとoptional CloudFormation方針を作る
4. 制作チケットを作る
5. QA、GitHub Issue更新を行う
