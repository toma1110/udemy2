# Next Course Decision Pack

Task ID: TASK-0127
GitHub Issue: https://github.com/toma1110/udemy2/issues/134
Owner AI: AI-Strategy-01
Reviewer AI: AI-QA-01
作成日: 2026-05-13

## 目的

50本以上の動画候補とスコアリング結果から、CEOが次に制作する講座を選べるように上位3案へ整理する。

この資料では `course_spec.md` は作成しない。CEOが選定した後、別チケットで正式な `course_spec.md` を作る。

## 推奨順位

| 推奨 | 講座候補 | 根拠 |
| ---: | --- | --- |
| 1 | AWS CloudWatch運用監視入門: CloudFormationハンズオン版 | 既存AWS SRE路線と最も近く、低コストで再現しやすい。実運用ではCDK/Terraform推奨を補足できる |
| 2 | AWSコスト事故防止とFinOps入門 | 初学者の課金不安に直接刺さり、短尺でも価値が出る |
| 3 | Bedrockアプリ運用監視入門 | 生成AI需要が強く鮮度が高いが、更新速度と料金確認が必要 |

## Candidate A: AWS CloudWatch運用監視入門: CloudFormationハンズオン版

### Course Promise

教材ハンズオンではCloudFormationでCloudWatch Alarm、SNS通知、Dashboard、Logs Insightsを作り、README通りに作成・更新・削除できるAWS運用監視の基礎を身につける。実運用ではCDKまたはTerraformで管理する考え方も理解する。

### 対象者

- AWS構築は少しできるが、監視や運用に自信がない人
- CloudWatchを使ったことはあるが、体系的に理解していない人
- SREやクラウド運用に進みたい初学者

### 想定章立て

1. CloudWatchの地図
2. ハンズオン用CloudFormation安全手順
3. Alarm + SNS通知
4. DashboardのIaC管理
5. Logs InsightsとMetric Filter
6. 良いアラート/悪いアラート
7. SLI/SLOへの接続
8. 削除手順と課金確認

### 採用する動画候補

- VID-001
- VID-002
- VID-003
- VID-004
- VID-005
- VID-006
- VID-011
- VID-028
- VID-051
- VID-052

### ハンズオン範囲

- CloudFormation validate/update/delete
- SNS Topic
- CloudWatch Alarm
- CloudWatch Dashboard
- Logs Insightsクエリ
- Metric Filter
- Lambdaまたは低コスト疑似メトリクス

### 低コスト構成案

- 原則無料枠または低コストのCloudWatch/SNS中心
- 長時間稼働リソースは避ける
- Lambdaは最小実行に留める
- 全章に削除手順を入れる

### 差別化

- 日本語
- CloudFormationは教材ハンズオン用
- 実運用IaCはCDK/Terraform推奨
- README再現性
- deleteまで品質ゲート化
- SREの実務判断を含める

### リスク

- CloudWatch画面UI変更
- SNSメール確認の受講者環境差分
- CloudWatch課金の説明不足

### CEO判断ポイント

最短で次講座化するならこの案を推奨する。既存のAWS SRE講座資産ともつながりやすい。

## Candidate B: AWSコスト事故防止とFinOps入門

### Course Promise

AWS Budgets、Cost Explorer、タグ設計、削除チェックリストを使い、初学者が課金事故を避けながらAWSハンズオンを進める方法を学ぶ。

### 対象者

- AWS学習の課金が不安な人
- 個人開発や小規模チームでAWS費用を管理したい人
- 講座ハンズオン前に安全策を知りたい人

### 想定章立て

1. AWS課金で事故が起きる理由
2. AWS Budgetsの設定
3. Cost Explorerの読み方
4. タグでコストを分ける
5. Cost Anomaly Detectionの考え方
6. 削除チェックリスト
7. ハンズオン後の確認ルーティン

### 採用する動画候補

- VID-019
- VID-020
- VID-021
- VID-032
- VID-038
- VID-042
- VID-048

### ハンズオン範囲

- AWS Budgets
- Cost Explorer
- タグ設計
- 削除チェックリスト
- 請求アラート確認

### 低コスト構成案

- 基本は管理画面操作中心
- リソース作成を最小化
- CloudFormation stack作成は原則不要
- AWS課金確認はCEO承認後の検証だけ行う

### 差別化

- AWS初学者の不安に直接刺さる
- 他のAWS講座の前提教材として使える
- 短尺でも販売ページの訴求が明確

### リスク

- Cost Explorer/Budgetsの画面差分
- 料金関連説明は誤解を招かない表現が必要
- 「節約額」をタイトルで約束してはいけない

### CEO判断ポイント

入口商品として強い。AWSハンズオン講座群の前提動画として横展開しやすい。

## Candidate C: Bedrockアプリ運用監視入門

### Course Promise

Amazon Bedrockを使った生成AIアプリで、CloudWatchログ、メトリクス、コスト、Guardrails、変更管理をどう見るかを学ぶ。

### 対象者

- Bedrock/RAGアプリを作り始めた開発者
- 生成AIアプリを本番運用したいクラウド担当者
- AIアプリのコストや安全性に不安がある人

### 想定章立て

1. Bedrockアプリ運用の全体像
2. Lambda/API Gateway/Bedrockのログ設計
3. CloudWatchで見るべき指標
4. Cost ExplorerでBedrockコストを見る
5. Guardrailsの基本
6. Prompt変更管理
7. RAG運用チェックリスト

### 採用する動画候補

- VID-041
- VID-042
- VID-043
- VID-044
- VID-045

### ハンズオン範囲

- Bedrock呼び出しログ設計
- Lambda/API Gatewayログ
- CloudWatch Dashboard
- Cost Explorer確認
- Guardrailsの概念デモ

### 低コスト構成案

- Bedrock呼び出し回数を制限
- サンプルデータは小さくする
- 長時間稼働リソースは置かない
- 料金確認と削除手順を必須化する

### 差別化

- 生成AIアプリ構築講座ではなく、運用監視に特化
- AWS/SRE教材ラインと相性が良い
- 市場鮮度が高い

### リスク

- Bedrock機能と料金の更新が速い
- モデルアクセス設定で受講者差分が出やすい
- 検証にはAWS課金が発生し得るためCEO承認が必要

### CEO判断ポイント

市場性は高いが、更新負荷も高い。先にCandidate Aで制作ラインを安定させてから着手するのが堅い。

## 最終推奨

最初に作るべき講座は Candidate A「AWS CloudWatch運用監視入門: CloudFormationハンズオン版」。

理由:

- 既存のAWS SRE制作方針と最も一致する
- 低コストで検証しやすい
- CloudFormationをハンズオン用途に限定し、実運用CDK/Terraform推奨も伝えられる
- 既存講座との差別化が明確
- 50本候補の上位スコア動画を多く含む
- README再現性、削除手順、品質ゲートを前面に出せる

CEOがこの案を選ぶ場合、次チケットは `course_spec.md` 作成と章立て確定にする。
