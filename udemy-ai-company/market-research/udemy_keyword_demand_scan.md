# Udemy Keyword Demand Scan

Task ID: TASK-0123
GitHub Issue: https://github.com/toma1110/udemy2/issues/130
Owner AI: AI-Strategy-01
Reviewer AI: AI-QA-01
調査日: 2026-05-13

## 調査方針

Udemy公開検索、競合講座ページ、Udemy Teaching CenterのMarketplace Insights説明、AWS/SRE実務需要をもとに、50本候補へ変換できるキーワードを整理する。

数値の正確な検索量はInstructor DashboardのMarketplace Insightsで再確認する。ここでは公開シグナルから「需要仮説」を作る。

## キーワード一覧

| ID | キーワード | 学習意図 | 競合密度 | 狙い目度 | 動画テーマ化 |
| --- | --- | --- | --- | --- | --- |
| K-01 | AWS CloudWatch | AWS監視を始めたい | high | high | CloudWatch全体像、Metrics/Logs/Alarmの違い |
| K-02 | CloudWatch Alarm | アラートを作りたい | medium | high | SNS通知つきアラームを教材ハンズオンではCloudFormationで作る |
| K-03 | CloudWatch Dashboard | 監視画面を作りたい | medium | high | Dashboard JSONを教材ハンズオンではCloudFormationで管理し、実運用ではCDK/Terraformへ接続 |
| K-04 | CloudWatch Logs Insights | ログ検索を使いたい | medium | high | エラー調査クエリ入門 |
| K-05 | SNS notification | 通知を飛ばしたい | medium | medium | AlarmからSNSへ通知 |
| K-06 | AWS SRE | 構築後の運用を学びたい | low | high | SRE入門、CloudWatch/SLO/Incident |
| K-07 | SLO / SLI | 信頼性指標を理解したい | low | high | AWSメトリクスからSLIを作る |
| K-08 | Error Budget | SREの意思決定を知りたい | low | medium | エラーバジェット入門 |
| K-09 | Incident Response AWS | 障害対応を学びたい | low | high | Runbookと初動対応 |
| K-10 | Postmortem | 障害振り返りを学びたい | low | medium | ポストモーテムテンプレート作成 |
| K-11 | CloudFormation | IaCを始めたい | medium | high | 初学者向けテンプレート作成 |
| K-12 | CloudFormation validate | テンプレート検証したい | low | high | validate/update/deleteの安全手順 |
| K-13 | CloudFormation rollback | 失敗時対応を知りたい | low | high | rollbackとchange set |
| K-14 | IAM least privilege | 権限設計を学びたい | high | medium | 最小権限ポリシーの考え方 |
| K-15 | CloudTrail | 操作ログを見たい | medium | high | 誰が何をしたかを追跡 |
| K-16 | AWS Config | 設定変更を検知したい | medium | high | Config Rule入門 |
| K-17 | Security Hub | セキュリティ検出を集約したい | medium | medium | Security Hub最小導入 |
| K-18 | GuardDuty | 脅威検知を始めたい | medium | medium | GuardDuty検知と通知 |
| K-19 | AWS Budgets | 課金事故を防ぎたい | medium | high | 予算アラートとCost Anomaly Detection |
| K-20 | Cost Explorer | コストを分析したい | medium | high | タグ別コスト分析入門 |
| K-21 | FinOps AWS | クラウドコスト管理を学びたい | low | high | 初学者FinOps入門 |
| K-22 | GitHub Actions AWS | GitHubからAWSへデプロイしたい | high | high | OIDCで安全にAWSへ接続 |
| K-23 | CodePipeline | AWSネイティブCI/CDを学びたい | medium | medium | 最小CodePipeline構成 |
| K-24 | ECS Fargate deploy | コンテナをAWSで動かしたい | high | medium | ECS Fargate最小デプロイ |
| K-25 | ECS monitoring | ECSを監視したい | medium | high | ECSメトリクスとログ |
| K-26 | Lambda monitoring | Lambdaの失敗を追いたい | high | high | エラー率、DLQ、アラーム |
| K-27 | RDS monitoring | DB監視を学びたい | medium | high | CPU/Connections/Storageアラーム |
| K-28 | S3 security | S3事故を防ぎたい | high | medium | Public Access BlockとCloudTrail |
| K-29 | OpenTelemetry AWS | トレースを導入したい | medium | medium | ADOT/CloudWatch入門 |
| K-30 | Amazon Bedrock monitoring | 生成AIアプリを運用したい | medium | high | Bedrockコスト・ログ・評価 |
| K-31 | Bedrock Guardrails | 生成AI安全性を学びたい | medium | high | Guardrails最小ハンズオン |
| K-32 | Bedrock RAG | RAGをAWSで作りたい | high | medium | RAG構築ではなく運用監視に寄せる |
| K-33 | AWS Well-Architected | 設計原則を理解したい | high | medium | Reliability/Security/Costをミニ講座化 |
| K-34 | AWS Backup | バックアップを設計したい | medium | medium | RDS/S3バックアップ入門 |
| K-35 | Systems Manager Runbook | 運用自動化したい | low | high | SSM Automationで運用手順を自動化 |

## 需要仮説

### 高需要だが競合が強い

- AWS DevOps
- EKS / Kubernetes
- Bedrock / RAG
- GitHub Actions + AWS
- ECS/Fargate

これらは総合講座ではなく、運用・監視・失敗対応へ絞る。

### 競合が薄く差別化しやすい

- AWS SRE
- CloudFormation validate/update/delete
- SLO/SLI/Error Budget
- Incident Response / Runbook / Postmortem
- FinOps初学者
- Bedrock運用監視

### 50本リストへ優先投入するキーワード

- CloudWatch Alarm
- CloudWatch Dashboard
- Logs Insights
- CloudFormation validate
- CloudFormation rollback
- SLO/SLI
- Incident Response
- AWS Budgets
- GitHub Actions OIDC
- Bedrock monitoring

## 参照

- `market-research/udemy_research_plan.md`
- `market-research/udemy_competitor_scan.md`
- Udemy Teaching Center: Choose your course topic: https://teach.udemy.com/course-creation/choose-your-course-topic/
- Udemy Teaching Center: Using your Dashboard: https://teach.udemy.com/publishing/using-your-dashboard/
