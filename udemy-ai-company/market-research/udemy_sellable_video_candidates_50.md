# Udemy Sellable Video Candidates 50+

Task ID: TASK-0125
GitHub Issue: https://github.com/toma1110/udemy2/issues/132
Owner AI: AI-Strategy-01
Reviewer AI: AI-QA-01
調査日: 2026-05-13

## 前提

このリストの「売れる」は売上保証ではなく、市場シグナルに基づく制作仮説である。

候補は動画単位または小講座単位であり、CEOが選定した後に別チケットで `course_spec.md` を作成する。

CloudFormationは、教材ハンズオンで受講者の追加準備を減らすための再現手段として扱う。実運用IaCはCDKまたはTerraform推奨として説明する。

ソース略号:

- `Cxx`: `market-research/udemy_competitor_scan.md`
- `Kxx`: `market-research/udemy_keyword_demand_scan.md`
- `Pxx`: `market-research/learner_pain_review_scan.md`

## 50本以上の動画候補

| ID | タイトル案 | カテゴリ | 対象者 | 学習Promise | 市場シグナル | 差別化 | ハンズオン範囲 | 教材CF適性 | 制作難易度 | 優先度 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| VID-001 | AWS CloudWatch入門: Metrics/Logs/Alarm/Dashboardの地図 | CloudWatch | AWS初学者 | CloudWatchの全体像を説明できる | C-03,K-01,P-05 | 日本語・図解・短尺 | 概念図とサンプルメトリクス確認 | medium | low | high |
| VID-002 | CloudFormationで作るCloudWatch Alarm + SNS通知 | CloudWatch | 初学者/SRE志望 | メール通知つきAlarmを再現できる | C-03,C-04,K-02,K-05,P-02 | 作成から削除までREADME化 | SNS Topic、Alarm、削除 | high | low | high |
| VID-003 | CloudWatch Dashboardをコードで管理する | CloudWatch | 運用担当 | Dashboard JSONをIaC化できる | C-03,K-03,P-03 | 手作業クリックを排除 | Dashboard作成、更新、削除 | high | low | high |
| VID-004 | Logs Insightsでエラーを探す10個のクエリ | CloudWatch Logs | 開発者 | 障害時にログ検索できる | C-03,K-04,P-05 | 実務クエリ集 | サンプルログ、クエリ、保存 | medium | medium | high |
| VID-005 | 良いアラートと悪いアラート: Alert Fatigueを防ぐ | SRE | SRE志望者 | ノイズの少ないアラート設計を説明できる | C-01,K-02,P-06 | 実務判断を中心にする | 閾値比較、通知ルール例 | medium | low | high |
| VID-006 | SLI/SLOをAWSメトリクスに落とす入門 | SRE | SRE志望者 | SLOをメトリクスで表現できる | C-01,K-07,P-07 | 抽象論で終わらせない | ALB/Lambda仮想SLI設計 | medium | medium | high |
| VID-007 | エラーバジェットでリリース判断する | SRE | PM/開発者 | 信頼性と開発速度の判断軸を持てる | C-01,K-08,P-07 | ビジネス判断へ接続 | 計算シート例、シナリオ | low | low | medium |
| VID-008 | AWS障害対応Runbookを作る | Incident | 運用担当 | 初動対応手順をテンプレ化できる | C-01,K-09,P-08 | Runbookテンプレート提供 | CloudWatch Alarmから初動確認 | medium | low | high |
| VID-009 | ポストモーテムを書けるようになるAWS障害演習 | Incident | SRE志望者 | 障害振り返りを文書化できる | C-01,K-10,P-08 | 責任追及しない文化を説明 | 模擬障害、テンプレ作成 | low | low | medium |
| VID-010 | CloudFormation超入門: Parameters/Outputsだけで始める | CloudFormation | AWS初学者 | 最小テンプレートを読める | C-02,K-11,P-03 | 初学者向け日本語 | S3/SNSなど低コスト例 | high | low | high |
| VID-011 | CloudFormation validate/update/delete安全手順 | CloudFormation | 実務1年目 | 失敗しにくい更新手順を実行できる | C-02,K-12,P-02 | deleteまでを品質ゲート化 | validate、change set、delete | high | low | high |
| VID-012 | CloudFormation Rollbackの読み方と直し方 | CloudFormation | 実務1年目 | 失敗原因をイベントから追える | C-02,K-13,P-03 | 失敗対応に特化 | 意図的失敗、イベント確認 | high | medium | high |
| VID-013 | IAM AccessDeniedを切り分ける基本 | IAM | 初学者 | 権限エラーの見方がわかる | C-10,K-14,P-04 | AccessDenied一点突破 | IAM Policy Simulator代替、CloudTrail | medium | medium | high |
| VID-014 | IAM最小権限ポリシーの作り方 | IAM | 開発者 | 過剰権限を避けられる | C-10,K-14,P-04 | SRE教材向けに限定 | ReadOnlyから限定権限へ | medium | medium | high |
| VID-015 | CloudTrailで「誰が何をしたか」を追う | Security | 初学者 | 操作ログを追跡できる | C-10,K-15,P-13 | 事故調査シナリオ | Event history、証跡設計 | medium | low | high |
| VID-016 | AWS Configで設定変更を検知する | Security | 運用担当 | 構成変更を検知できる | C-10,K-16,P-13 | ルール1個から開始 | Config Rule、通知 | high | medium | medium |
| VID-017 | Security Hub最小導入と見方 | Security | 実務1年目 | 検出結果を読める | C-10,K-17,P-13 | 網羅でなく初回運用 | Enable、Finding確認 | medium | medium | medium |
| VID-018 | GuardDuty検知をSNSへ通知する | Security | 運用担当 | 脅威検知通知を作れる | C-10,K-18,P-13 | 小さく作るセキュリティ | GuardDuty、EventBridge、SNS | high | medium | medium |
| VID-019 | AWS Budgetsで課金事故を防ぐ | Cost | 初学者 | 予算アラートを設定できる | C-11,C-12,K-19,P-09 | 初学者不安に直撃 | Budget、メール通知 | medium | low | high |
| VID-020 | Cost Explorerで無駄コストを見つける | Cost | 初学者/運用 | サービス別コストを読める | C-11,K-20,P-09 | 画面操作 + 判断軸 | Cost Explorer、タグ | low | low | high |
| VID-021 | FinOps入門: AWSコストをチームで管理する | Cost | PM/開発者 | FinOpsの役割分担がわかる | C-11,C-12,K-21,P-09 | 技術者向け日本語 | タグ方針、予算会議例 | low | low | medium |
| VID-022 | GitHub ActionsからAWSへOIDCで安全に接続 | CI/CD | 開発者 | 長期キーなしでAWS連携できる | C-05,K-22,P-10 | セキュリティ重視 | IAM OIDC、AssumeRole | high | medium | high |
| VID-023 | GitHub ActionsでCloudFormation validateを自動化 | CI/CD | 開発者 | PRでテンプレート検証できる | C-05,K-22,P-03 | 制作パイプラインと相性良い | GitHub Actions、cfn validate | high | medium | high |
| VID-024 | CodePipeline最小構成を30分で理解 | CI/CD | AWS初学者 | CodePipelineの流れを説明できる | C-05,C-06,K-23,P-10 | 総合講座より短尺 | Source/Build/Deploy概念 | medium | medium | medium |
| VID-025 | CodeBuildのログを読んで失敗原因を直す | CI/CD | 開発者 | ビルド失敗を切り分けられる | C-05,K-23,P-10 | トラブル対応に特化 | buildspec、CloudWatch Logs | medium | medium | medium |
| VID-026 | ECS Fargateを低コストで動かす最小構成 | ECS | 開発者 | コンテナをAWSで起動できる | C-05,K-24,P-11 | 低コスト・削除重視 | ECS Service、ALBなし案 | high | high | medium |
| VID-027 | ECSのログとメトリクスをCloudWatchで見る | ECS | 運用担当 | ECS監視の基本がわかる | C-05,K-25,P-05 | 運用に絞る | LogGroup、CPU/Memory Alarm | high | medium | high |
| VID-028 | Lambdaのエラー率を監視する | Lambda | 開発者 | Lambda失敗を検知できる | K-26,P-06 | 低コストで作れる | Lambda、Alarm、SNS | high | low | high |
| VID-029 | Lambda DLQとリトライを図解する | Lambda | 開発者 | 非同期失敗の流れがわかる | K-26,P-05 | 図解向き | DLQ/SQS概念、疑似構成 | medium | medium | medium |
| VID-030 | RDSを止めないための基本メトリクス | RDS | 実務1年目 | DB監視項目を説明できる | C-04,K-27,P-06 | 実務メトリクスに絞る | CPU/Storage/Connections Alarm | high | medium | medium |
| VID-031 | S3の公開事故を防ぐセキュリティ基本 | S3 | 初学者 | Public Access Blockを理解できる | K-28,P-13 | 事故防止訴求 | S3 Block Public Access確認 | medium | low | high |
| VID-032 | S3ライフサイクルでログ保管コストを下げる | S3/Cost | 運用担当 | ログ保管コストを設計できる | K-28,K-20,P-09 | コストと運用を接続 | Lifecycle Rule | high | low | medium |
| VID-033 | OpenTelemetryとCloudWatchの関係を図解 | Observability | 開発者 | メトリクス/ログ/トレースを説明できる | C-01,K-29,P-05 | 図解中心 | ADOT概念、構成図 | low | medium | medium |
| VID-034 | CloudWatch Syntheticsで外形監視する | Observability | 運用担当 | Web監視の考え方がわかる | C-03,K-01,P-06 | Syntheticsに特化 | Canary、Alarm | medium | medium | medium |
| VID-035 | Systems Manager Run Command入門 | Operations | 運用担当 | EC2に安全にコマンド実行できる | K-35,P-08 | SSH不要運用 | SSM Role、Run Command | high | medium | medium |
| VID-036 | SSM AutomationでRunbookを自動化する | Operations | SRE志望者 | 手順を自動化できる | K-35,P-08 | Runbookとの接続 | Automation Document | high | high | medium |
| VID-037 | AWS Well-Architected Reliabilityを初学者向けに読む | Architecture | 初学者 | 信頼性設計の観点を持てる | K-33,P-14 | SRE講座への導線 | チェックリスト化 | low | low | medium |
| VID-038 | AWS Well-Architected Costを実務目線で読む | Architecture/Cost | 初学者 | コスト設計の基本がわかる | K-33,K-21,P-09 | FinOps講座への導線 | 設計レビュー例 | low | low | medium |
| VID-039 | AWS BackupでRDSバックアップを考える | Backup | 運用担当 | バックアップ設計を説明できる | K-34,P-08 | 障害対応と接続 | Backup Plan概念 | medium | medium | low |
| VID-040 | Disaster Recovery入門: RTO/RPOをAWSで考える | Reliability | PM/開発者 | 復旧目標を説明できる | K-33,P-08 | ビジネスと技術を接続 | RTO/RPOワーク | low | low | medium |
| VID-041 | BedrockアプリのCloudWatch監視入門 | AI Ops | AI開発者 | 生成AIアプリの監視観点を持てる | C-13,C-14,K-30,P-12 | 構築でなく運用に特化 | Lambda/API Gateway/Bedrockログ設計 | medium | medium | high |
| VID-042 | Bedrockコストを見える化する | AI Ops/Cost | AI開発者 | 生成AIコストの見方がわかる | C-13,C-14,K-30,P-09 | 高需要 x Cost | Cost Explorer、タグ設計 | low | low | high |
| VID-043 | Bedrock Guardrailsを初学者向けに試す | AI Ops/Security | AI開発者 | 安全性制御の入口がわかる | C-13,C-14,K-31,P-12 | 日本語・安全性に特化 | Guardrails概念、テスト | medium | medium | high |
| VID-044 | RAGアプリの運用チェックリスト | AI Ops | AI開発者 | RAG運用の確認観点を持てる | C-13,C-14,K-32,P-12 | 作る後の運用 | 評価、ログ、コスト、更新 | low | low | high |
| VID-045 | 生成AIアプリのPrompt変更を事故にしない | AI Ops | AI開発者 | Prompt変更管理を説明できる | C-13,C-14,K-30,P-12 | 新規性が強い | 変更管理テンプレート | low | low | medium |
| VID-046 | AWS CLIプロファイルと認証の基本 | Foundation | 初学者 | CLI認証で迷わない | P-03,P-04 | すべての講座の前提解消 | configure、sts get-caller-identity | low | low | high |
| VID-047 | AWSリージョンとリソース名で詰まらない入門 | Foundation | 初学者 | 環境差分を避けられる | P-03 | 初学者の詰まり解消 | region、stack name、name prefix | low | low | medium |
| VID-048 | ハンズオン前に必ず作る削除チェックリスト | Foundation/Cost | 初学者 | 課金事故を避けられる | P-02,P-09 | CEO方針と一致 | 削除手順テンプレート | low | low | high |
| VID-049 | Udemy動画用AWSハンズオンREADMEの作り方 | Production | 制作AI/講師 | 再現性あるREADMEを作れる | P-03,Udemy公式 | 制作ラインの強化 | README構成、検証証跡 | low | low | medium |
| VID-050 | AWS SREロードマップ: 構築から運用へ | SRE | 初学者 | 学習順序がわかる | C-01,K-06,P-14 | 既存講座の入口動画 | ロードマップ図解 | low | low | high |
| VID-051 | CloudWatch Metric Filterでログからメトリクスを作る | CloudWatch Logs | 運用担当 | ログをAlarm化できる | C-01,K-04,P-05 | SLO実装へ接続 | LogGroup、Metric Filter、Alarm | high | medium | high |
| VID-052 | EventBridgeでAWSイベントをSNS通知する | Operations | 運用担当 | イベント駆動通知を作れる | K-18,K-35,P-08 | GuardDuty/Configへ展開可能 | Rule、Target、SNS | high | medium | medium |

## 優先制作方針

最初に作るべき候補は、以下の条件を満たすものに絞る。

- 低コスト
- 教材ハンズオンをCloudFormation化しやすい
- 削除手順を明確にできる
- 1本あたり30〜60分で完結しやすい
- 既存AWS SRE講座と自然につながる

この条件では、`VID-002`、`VID-003`、`VID-006`、`VID-011`、`VID-019`、`VID-022`、`VID-028`、`VID-041`、`VID-042`、`VID-050` が特に強い。
