# Learner Pain Review Scan

Task ID: TASK-0124
GitHub Issue: https://github.com/toma1110/udemy2/issues/131
Owner AI: AI-Strategy-01
Reviewer AI: AI-QA-01
調査日: 2026-05-13

## 調査方針

Udemyの詳細レビュー/Q&Aはログインや講座購入状態により表示範囲が変わるため、今回は公開講座ページ、講座説明、更新日、カリキュラム、公式Dashboard/Q&A Insights説明から痛点を抽出した。

長文レビュー転載は禁止し、痛点は要約のみ記録する。

## 痛点分類

| ID | 痛点 | 観測シグナル | 動画化すると価値が出る理由 | 候補テーマ |
| --- | --- | --- | --- | --- |
| P-01 | AWS画面や手順が古い | CloudWatch/CodePipeline系に2018-2020更新の古い講座が残る | UI差分で初学者が止まりやすい | 2026年版CloudWatch Alarm/SNS/Dashboard |
| P-02 | 作成だけで削除手順が薄い | 多くの講座は作成ハンズオン中心 | AWS初学者は課金不安が強い | 作る前に削除まで設計するハンズオンIaC |
| P-03 | README通り再現できない | 動画だけの手作業クリックでは環境差分が出る | 再現性が低いと低評価につながる | README再現型ハンズオンIaC入門 |
| P-04 | IAM権限で詰まる | Security/EKS/CodePipeline系でIAMが複雑 | 初学者の最大ブロッカー | IAM最小権限とAccessDenied調査 |
| P-05 | CloudWatchの概念が散らばる | Metrics/Logs/Alarm/Dashboard/Event/Syntheticsが混在 | 全体像なしに手順だけ進めると理解が残らない | CloudWatchの地図を30分で作る |
| P-06 | アラート設計が実務的でない | CloudWatch講座は操作説明に寄りやすい | アラート疲れ、閾値、通知先設計が現場で重要 | 良いアラート/悪いアラート実践 |
| P-07 | SLOが抽象論で終わる | SLO/SLIは実装例が少ない | AWSメトリクスへの落とし込みが価値 | ALB/LambdaのSLI設計 |
| P-08 | 障害対応の型がない | Incident/Runbook/Postmortemは講座数が少ない | 実務で使えるテンプレート需要がある | 初動対応Runbookとポストモーテム |
| P-09 | コスト管理が後回し | 多くの技術講座でCost Explorer/Budgetsは補足扱い | 課金事故防止は初学者の強い不安 | AWS BudgetsとCost Anomaly Detection |
| P-10 | CI/CDが大きすぎる | CodePipeline/EKS講座は長く、構成が重い | 最小構成の成功体験が必要 | GitHub Actions OIDCでS3/Lambdaへデプロイ |
| P-11 | EKSは課金と前提知識が重い | EKS人気講座は長時間・多数サービス | 初学者にはECS/CloudWatchからの段階が必要 | EKS前に学ぶコンテナ監視 |
| P-12 | Bedrock講座は構築寄りで運用が薄い | Bedrock/RAG講座は人気だが、監視・評価・コストは部分扱い | 生成AIアプリは運用論点が売りになる | BedrockアプリのCloudWatch監視 |
| P-13 | セキュリティ講座が網羅的すぎる | Security講座はIAM/GuardDuty/Security Hubなど広い | 初学者は小さな検知パターンから始めたい | CloudTrailで「誰が何をしたか」を追う |
| P-14 | タイトルが広すぎて期待値が曖昧 | 総合講座は内容が広い | 具体タイトルのほうが検索意図と一致する | 1テーマ1成果物の短尺講座 |
| P-15 | 生成AIや新サービスの更新が速い | Bedrock/AgentCore/AI Practitioner関連は2026更新が多い | 旧情報になりやすい | 更新日を前面に出す短期リリース型動画 |

## 受講者の購入動機に変換できる痛点

- 課金事故を避けたい
- README通りに再現したい
- AWSコンソールで迷いたくない
- IAMエラーを自力で切り分けたい
- CloudWatchで何を見るべきか知りたい
- SLOを仕事で説明できるようになりたい
- 障害対応の型を持ちたい
- 生成AIアプリを作った後、運用できるようになりたい

## TASK-0125への変換ルール

50本候補では、1候補につき最低1つの痛点を紐づける。

特に優先する痛点:

- P-02 削除手順不足
- P-03 README再現性
- P-04 IAM権限
- P-06 アラート設計
- P-07 SLO実装
- P-09 コスト管理
- P-12 Bedrock運用

## 参照

- `market-research/udemy_competitor_scan.md`
- Udemy Teaching Center: Using your Dashboard: https://teach.udemy.com/publishing/using-your-dashboard/
- Udemy Course Quality Checklist: https://support.udemy.com/hc/en-us/articles/229604988-Udemy-Course-Quality-Checklist
- Udemy Course Title Standards: https://support.udemy.com/hc/en-us/articles/229232467-Course-Title-Quality-Standards
