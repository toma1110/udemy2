# Change Summary

AWS CloudWatch Application Signalsを主役にした新規講座を作成する。

# Why Change

既存SLO講座ではApplication Signalsを補足扱いにした。Application Signalsは実際の通信とアプリケーション状態を見て初めて価値が伝わるため、独立した実践講座として作る。

# Scope

- Course spec
- Course information
- Course curriculum
- Handson design
- CloudFormation implementation tickets
- Production tickets

# Impact

- 新しいコースディレクトリを追加する
- 将来的にPublicリポジトリとCloudFormationテンプレートを作る
- AWSリソース作成を伴う検証はCEO承認後に実行する

# Risks

- Application Signalsは課金が発生する
- 自動トラフィックの停止漏れが課金事故につながる
- Lambda Application SignalsのLayer ARNや対応リージョンが変わる可能性がある
- SLO Recommendationsなど短時間では確認できない機能を過剰に約束するリスクがある

# Approval

CEO approved course creation in chat on 2026-05-16.

# Implementation Plan

1. Create initial course files.
2. Create CloudFormation implementation task.
3. Create course production tasks.
4. Validate documentation consistency.
5. Do not run AWS create/update/delete in this task.
