# Udemy Competitor Course Scan

Task ID: TASK-0122
GitHub Issue: https://github.com/toma1110/udemy2/issues/129
Owner AI: AI-Strategy-01
Reviewer AI: AI-QA-01
調査日: 2026-05-13

## 調査方針

Udemy公開ページとUdemy Teaching Centerの公式ガイドをもとに、AWS/SRE領域で売れる動画候補を作るための競合シグナルを整理する。

制約:

- Udemy Instructor DashboardのMarketplace Insights実画面にはアクセスしていない
- レビュー数、受講者数、評価、更新日は調査時点の公開表示または検索結果スニペットに基づく
- 数値は日々変わるため、制作着手前に再確認する
- 競合講座の内容はコピーせず、差別化仮説の材料として使う

## 公式に確認した市場調査観点

Udemy Teaching Centerは、講座テーマ選定時に「需要」と「競合」を見ること、Marketplace Insightsで検索量、供給、収益可能性、関連トピックを確認することを推奨している。

また、Instructor Dashboardではレビュー、受講者、Engagement、Traffic & Conversions、Q&A Insights、Marketplace Insightsを確認できる。後続調査では、公開ページで見える情報に加えて、CEOがInstructor Dashboardを開ける場合はこれらの指標を追記する。

## 競合講座スキャン

| ID | 領域 | 競合講座/URL | 公開シグナル | 観察 | 差別化余地 |
| --- | --- | --- | --- | --- | --- |
| C-01 | AWS SRE / CloudWatch / SLO | [AWS SRE実践: CloudWatch・SLO・インシデント対応](https://www.udemy.com/course/aws-sre-cloudwatch/) | 日本語、2026-05更新、約4時間、47講義、少数レビュー | 日本語SRE + CloudWatch + SLOの直接競合。既存ニーズはあるがレビューが少なく、市場がまだ薄い | README再現性、ハンズオンCloudFormation、低コスト、実運用CDK/Terraform補足で差別化 |
| C-02 | CloudFormation | [Hands-On Introduction to CloudFormation](https://www.udemy.com/course/introcloudformation/) | 2024-08更新、英語、約2時間、CloudFormation基礎 | CloudFormation単体の入門需要がある。短時間・ハンズオン訴求が強い | 日本語、SRE用途、validate/create/update/deleteまでの再現性で差別化 |
| C-03 | CloudWatch基礎 | [Amazon CloudWatch in 60 Minutes](https://www.udemy.com/course/aws-monitoring/) | 英語、約56分、28講義、CloudWatch labs | 60分でCloudWatchを学ぶ短尺ニーズあり | 日本語、教材ハンズオンではCloudFormationでAlarm/SNS/Dashboardを作り、実運用ではCDK/Terraformに接続する |
| C-04 | CloudWatch / SNS | [AWS MasterClass: Monitoring and DevOps with AWS CloudWatch](https://www.udemy.com/course/aws-monitoring-alerting-with-aws-cloudwatch-and-aws-sns/) | 英語、2019更新、4時間超、CloudWatch/SNS/Billing | 受講者数の多い古めのCloudWatch競合。古さが痛点になり得る | 2026年画面、削除手順、Slack/Chatbot代替、アラート疲れ設計で差別化 |
| C-05 | AWS DevOps | [AWS DevOps & CI/CD with AWS CodePipeline for Engineers](https://www.udemy.com/course/mastering-aws-devops-for-cloud-engineers/) | 英語、2026-04更新、16時間超、5千人規模 | AWS DevOpsは大規模講座が多く競合が強い | 教材ハンズオンは最小構成、実運用はCDK/Terraformで管理する流れに絞る |
| C-06 | CodePipeline | [AWS CodePipeline: DevOps CI/CD Masterclass](https://www.udemy.com/course/aws-codepipeline-devops/) | 英語、2023更新、CodePipeline/CloudFormation/Beanstalk | CodePipeline単体の需要あり。古めのUI/サービス構成の可能性 | GitHub Actionsとの比較、最小CI/CD、削除まで含める |
| C-07 | CI/CD短尺 | [AWS DevOps CI/CD - CodePipeline, Elastic Beanstalk and Mocha](https://www.udemy.com/course/nodejs-cicd-aws-codepipeline-codebuild-mocha-zero-to-hero/) | 英語、無料/短尺、受講者数が非常に多い | 短尺CI/CDは入口商品として強い | 日本語の「30分でCI/CDの流れだけ理解」動画が狙える |
| C-08 | EKS / Kubernetes | [AWS EKS Kubernetes Masterclass](https://www.udemy.com/course/aws-eks-kubernetes-masterclass-devops-microservices/) | 英語、2026-03更新、7万人規模、EKS大規模講座 | EKSは強い需要があるが競合も強い | 「SRE視点のEKS監視」「EKSに入る前のCloudWatch Container Insights」に絞る |
| C-09 | EKS入門 | [Amazon EKS Starter](https://www.udemy.com/course/amazon-eks-starter-kubernetes-on-aws/) | 英語、3万人規模、CloudFormationでEKS作成を含む | EKS初学者講座は人気だが課金・環境構築が重い | 低コストなECS/CloudWatchから入り、EKSは別講座候補にする |
| C-10 | AWS Security | [Full AWS Security Course](https://www.udemy.com/course/aws-security-course/) | 英語、2025-08更新、IAM/GuardDuty/Security Hub | AWS Securityの実務テーマは新しめ講座が出ている | CloudTrail + Config + Security Hubの検知ハンズオンを日本語で低コスト化 |
| C-11 | FinOps | [AWS - FinOps and Cost Optimization](https://www.udemy.com/course/aws-finops/) | 英語、2024-05更新、Cost Explorer/タグ/Cost Categories | FinOpsは競合が少なめで実務需要がある | 初学者向けに「請求アラートと削除手順」へ絞ると作りやすい |
| C-12 | FinOps日本語外 | [FinOps na AWS](https://www.udemy.com/course/finops-na-aws-economizando-e-gerenciando-custos-na-nuvem/) | ポルトガル語、2026-05更新、Highest Rated表示 | 非英語圏でもFinOps需要あり | 日本語FinOps + AWS Budgets + Cost Anomaly Detectionは候補 |
| C-13 | Bedrock / GenAI | [Generative AI on AWS - Amazon Bedrock, RAG & Langchain](https://www.udemy.com/course/amazon-bedrock-aws-generative-ai-beginner-to-advanced/) | 英語、2026-05更新、3万人規模、Bedrock/RAG/CloudWatch | Bedrockは非常に強い需要。運用監視セクションも含む | 「BedrockアプリのCloudWatch監視・コスト監視」に特化するとSRE差別化 |
| C-14 | Bedrock / Agent | [Complete AWS Bedrock Generative AI Course + Projects](https://www.udemy.com/course/complete-aws-bedrock-generative-ai-course-projects/) | 英語、2026更新、1.5万人規模、AgentCore/Voice Agent | 生成AI x AWSは新規需要が強いが競合も増加 | 日本語の運用・評価・コストに絞る |
| C-15 | AWS DevOps general | [Amazon AWS DevOps](https://www.udemy.com/course/aws-devops/) | スペイン語、2026-03更新、CloudFormation/CloudWatch/イベント対応 | 非英語でもAWS DevOpsの需要がある | 日本語SRE運用、ハンズオンCloudFormation、実運用CDK/Terraform、README再現性で差別化 |

## 競合が強い領域

- AWS認定試験対策
- EKS/Kubernetes大規模講座
- Bedrock/RAG/生成AIアプリ構築
- AWS DevOps総合講座
- CodePipeline/CI/CD総合講座

これらは正面から総合講座で戦うと競合が強い。短尺・実務特化・日本語・ハンズオンCloudFormation・実運用CDK/Terraform補足・README再現性で切り出す。

## 競合が弱い/狙い目の領域

- 日本語のCloudFormation実務入門
- 日本語のCloudWatch Alarm/SNS/Dashboard最小ハンズオン
- SLO/SLIをAWSメトリクスに落とす講座
- インシデント対応、Runbook、PostmortemのAWS実践
- AWS Budgets / Cost Anomaly Detection / Cost Explorerの初学者向け講座
- Bedrockアプリの監視、評価、コスト管理
- CloudTrail / Config / Security Hubの検知ハンズオン
- GitHub ActionsからAWSへ安全にデプロイする最小構成

## 差別化方針

- 日本語で、初学者が詰まる前提知識を短く補う
- 教材ハンズオンではCloudFormationで手作業クリック依存を減らす
- 実運用ではCDKまたはTerraformを推奨する
- README通りに再現できることを合格条件にする
- 作成だけでなく、update、smoke test、deleteまで扱う
- 低コスト構成と削除手順を明記する
- GPT-Image2スライドで構成図を見せ、VOICEVOXで聞きやすい日本語にする
- 「稼げる」ではなく「できること」をタイトルに入れる

## TASK-0125への示唆

50本リストでは、以下のテーマ群を優先的に展開する。

- CloudWatch / SNS / Dashboard / Logs Insights
- CloudFormation validation / update / rollback
- SLO / SLI / Error Budget
- Incident Response / Runbook / Postmortem
- IAM / CloudTrail / Config / Security Hub
- Cost / Budget / FinOps
- GitHub Actions / CodePipeline
- ECS / Lambda / RDS / S3の運用監視
- Bedrock / LLMアプリ運用

## 参照

- Udemy Teaching Center: Choose your course topic: https://teach.udemy.com/course-creation/choose-your-course-topic/
- Udemy Teaching Center: Using your Dashboard: https://teach.udemy.com/publishing/using-your-dashboard/
- Udemy Course Quality Checklist: https://support.udemy.com/hc/en-us/articles/229604988-Udemy-Course-Quality-Checklist
- Udemy Course Title Standards: https://support.udemy.com/hc/en-us/articles/229232467-Course-Title-Quality-Standards
- Udemy競合講座ページ: 上表URL参照
