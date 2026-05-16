# AWS課金事故防止入門 カリキュラム

Source of Truth: `course_spec.md`

## Course Goal

AWS学習者がハンズオンを始める前に、予算アラート、コスト確認、異常検知、削除チェックリスト、月次確認ルーティンを整えられる状態にする。

## Sections

| Section | Lecture | Title | Learning Goal | Hands-on Resource |
| --- | --- | --- | --- | --- |
| 1 | s1-l1 | AWS課金事故防止の地図 | 課金事故の典型パターンと、この講座で作る安全柵を説明できる | `handson/README.md` |
| 1 | s1-l2 | コストデータの遅れと無料枠の誤解 | BudgetsやCost Explorerがリアルタイムではないことを説明できる | `handson/README.md#実行前チェック` |
| 2 | s2-l1 | 月次予算を作る | AWS Budgetsで学習用の月次コスト予算を作る流れを説明できる | `handson/README.md#budgets` |
| 2 | s2-l2 | 実績アラートと予測アラート | Actual通知とForecasted通知の違い、通知確認の必要性を説明できる | `handson/README.md#通知確認` |
| 3 | s3-l1 | サービス別コストを読む | Cost Explorerでサービス別コストを見て、主な費用源を探せる | `handson/README.md#cost-explorer` |
| 3 | s3-l2 | 期間、タグ、フィルターで原因を絞る | 期間比較、タグ、フィルターで原因候補を絞る考え方を説明できる | `handson/README.md#タグ確認` |
| 4 | s4-l1 | 異常コスト検知の考え方 | Cost Anomaly Detectionの役割と限界を説明できる | `handson/README.md#cost-anomaly-detection` |
| 4 | s4-l2 | モニター、サブスクリプション、通知設計 | モニター、通知頻度、しきい値、通知先を設計できる | `handson/README.md#通知設計` |
| 5 | s5-l1 | ハンズオン後の削除チェック | 削除漏れしやすいAWSリソースをチェックリストで確認できる | `handson/README.md#削除チェックリスト` |
| 5 | s5-l2 | タグとスタック名で見失わない | 学習用リソースをタグ、名前、メモで追跡する方法を説明できる | `handson/README.md#タグ確認` |
| 6 | s6-l1 | 毎月15分のコストレビュー | 月次で確認する画面、記録項目、判断基準を説明できる | `handson/README.md#月次レビュー` |
| 6 | s6-l2 | 次に学ぶAWS/SRE講座への接続 | 課金安全策を前提に、CloudWatch/SRE学習へ進む順番を説明できる | `course_spec.md` |

## Section Learning Objectives

### Section 1: 課金事故が起きる理由

- 従量課金、削除漏れ、無料枠誤解、データ反映遅延を説明する
- 本コースで作る安全柵を、Budgets、Cost Explorer、Anomaly Detection、削除チェックリストに分ける

### Section 2: Budgetsで最初の安全柵を作る

- 月次予算、Actual通知、Forecasted通知の違いを扱う
- 通知メールの確認と、Budgetが即時停止ではないことを明確にする

### Section 3: Cost Explorerでコストを見る

- サービス別、期間別、タグ別の見方を扱う
- API利用や日付範囲の扱いは、公式仕様確認後に台本へ反映する

### Section 4: Cost Anomaly Detectionで異常に気づく

- 機械学習による異常検知、モニター、サブスクリプション、通知頻度を扱う
- すべての課金事故を防ぐ保証ではないことを明確にする

### Section 5: タグと削除チェックリスト

- ハンズオン後に残りやすい課金源を確認する
- タグと命名で学習用リソースを追跡する

### Section 6: 月次コスト確認ルーティン

- 毎月短時間で確認する画面と記録項目を決める
- CloudWatch、SRE、FinOps講座への導線を作る
