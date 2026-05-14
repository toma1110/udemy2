# Udemy Market Research Plan

Task ID: TASK-0121
GitHub Issue: https://github.com/toma1110/udemy2/issues/128
Owner AI: AI-Strategy-01
Reviewer AI: AI-QA-01
Created: 2026-05-13

## 目的

Udemyで売れる可能性が高いAWS/SRE関連動画テーマを、推測ではなく市場シグナルに基づいて50本以上リスト化するための調査設計を定義する。

この計画書は後続チケットの作業基準とする。

- TASK-0122: Udemy競合講座調査
- TASK-0123: キーワード需要調査
- TASK-0124: レビュー/Q&A痛点調査
- TASK-0125: 50本以上の動画候補リスト作成
- TASK-0126: スコアリングと上位10本選定
- TASK-0127: CEO判断パック作成
- TASK-0128: QA

## 「売れる」の定義

この調査での「売れる」は、売上保証ではなく市場仮説を意味する。

売れる可能性が高い候補とは、以下を満たす動画テーマである。

- Udemy上で需要シグナルがある
- 競合講座は存在するが、日本語・初学者・実務再現性の差別化余地がある
- 受講者レビューやQ&Aに明確な痛点がある
- AWS/SRE実務で使う場面が説明できる
- README通りに再現できるハンズオンへ落とし込める
- GPT-Image2スライドとVOICEVOX台本で制作可能である
- 教材ハンズオンではCloudFormationで低コストに再現でき、削除手順まで提供できる
- 実運用ではCDKまたはTerraformへ発展させる位置づけを説明できる

## 調査しないこと

- 売上額の断定
- Udemy内部データへの不正アクセス
- 外部有料SEOツールや課金APIの利用
- AWSリソース作成、CloudFormation stack実行、Fargate/Batch/ECR等の課金作業
- 既存講座 `course_spec.md` の変更
- CEO承認前の新講座制作着手

## 調査対象カテゴリ

### Core AWS/SRE

- SLO、SLI、エラーバジェット
- CloudWatch Logs、Metrics、Alarm、Dashboard
- SNS、EventBridge、Systems Manager
- Incident Response、Postmortem、Runbook
- Observability、OpenTelemetry、ログ設計、メトリクス設計

### AWS Hands-on

- CloudFormation入門
- IAM最小権限
- VPC基礎と運用
- Lambda運用
- ECS/Fargate運用
- EKS/Kubernetes運用
- RDS運用、バックアップ、監視
- S3運用、ライフサイクル、セキュリティ
- AWS Config、CloudTrail、Security Hub
- AWS Budgets、Cost Explorer、FinOps

### DevOps / Platform

- GitHub Actions + AWS
- CodePipeline / CodeBuild
- CI/CD失敗対応
- Blue/Green、Canary、Rollback
- Docker基礎とAWSデプロイ
- CDKとTerraformは実運用IaCの推奨選択肢として扱う

### AI / Modern Ops

- Bedrock運用監視
- 生成AIアプリのSRE
- AIエージェント運用のログ、評価、コスト監視
- LLMアプリのCloudWatch設計

## 調査ソース

### 一次ソース

- Udemy検索結果ページ
- Udemyカテゴリページ
- Udemy競合講座ページ
- Udemy講座のレビュー、Q&A、最終更新日、評価、受講者数
- Udemy Instructor Dashboard の Marketplace Insights
- Udemy Business Content Opportunities が利用可能な場合の需要シグナル

### Udemy公式ガイド

- Udemy Course Quality Checklist
  - https://support.udemy.com/hc/en-us/articles/229604988-Udemy-Course-Quality-Checklist
- Udemy Course Title: Quality Standards
  - https://support.udemy.com/hc/en-us/articles/229232467-Course-Title-Quality-Standards
- Udemy Course Description: Quality Standards
  - https://support.udemy.com/hc/en-us/articles/229232407-Course-Description-Quality-Standards
- Udemy Quality Review Process
  - https://support.udemy.com/hc/en-us/articles/229605348-Udemy-s-Quality-Review-Process
- Udemy Teaching Center: Choose your course topic
  - https://teach.udemy.com/course-creation/choose-your-course-topic/
- Udemy Teaching Center: Using your Dashboard
  - https://teach.udemy.com/publishing/using-your-dashboard/
- Official Udemy course creation course
  - https://www.udemy.com/course/official-udemy-create-course/

### 補助ソース

- Google検索結果
- Google Trends
- YouTube検索結果
- AWS公式ドキュメント、AWS What's New
- GitHubのスター数、README、Issue傾向
- Reddit、Hacker News、Qiita、Zennなどの公開投稿

補助ソースは市場シグナルとして扱い、Udemy上の需要や競合確認を優先する。

## 調査手順

### 1. 競合講座スキャン

TASK-0122で実施する。

各カテゴリごとにUdemyで検索し、上位表示・ベストセラー・高レビュー講座を記録する。

記録項目:

- 調査日
- 検索キーワード
- URL
- 講座タイトル
- 言語
- 評価
- レビュー数
- 受講者数
- 最終更新日
- 講座時間
- レクチャー数
- 対象者
- Course Promise
- 章立ての特徴
- ハンズオン有無
- 差別化余地

### 2. キーワード需要スキャン

TASK-0123で実施する。

Udemy検索候補、検索結果数、関連講座、外部検索の関連語を確認する。

記録項目:

- キーワード
- 日本語/英語
- 学習意図
- Udemy上の競合密度
- 既存講座の強さ
- 日本語講座の不足
- ハンズオン化候補
- 50本リストへの採用可否

### 3. 受講者痛点スキャン

TASK-0124で実施する。

競合講座の低評価レビュー、Q&A、説明文、カリキュラムから、受講者が詰まる点を抽出する。

痛点分類:

- 古いAWS画面や古いCLI手順
- README通り再現できない
- ハンズオンが少ない
- IAMや権限で詰まる
- 課金や削除手順が不明
- 監視や運用の実務文脈が薄い
- 図解が少ない
- 初学者向け説明が浅い
- 本番運用の注意点が不足

### 4. 50本候補リスト作成

TASK-0125で実施する。

候補は「動画単位」または「小講座単位」で作成する。1件ごとに、制作に入れるだけのタイトル案と根拠を持たせる。

### 5. スコアリング

TASK-0126で実施する。

全候補を同じ評価軸で採点し、上位10本と保留候補を分ける。

### 6. CEO判断パック

TASK-0127で実施する。

上位10本から、講座化しやすい3案にまとめる。ここでは `course_spec.md` は作成しない。

## 50本リストの列定義

`market-research/udemy_sellable_video_candidates_50.md` は以下の列を持つ。

| 列 | 内容 |
| --- | --- |
| ID | `VID-001` 形式 |
| タイトル案 | Udemy掲載を意識した仮タイトル |
| カテゴリ | AWS/SRE/DevOps/AI Opsなど |
| 想定形式 | 単発動画、小講座、講座内セクション |
| 対象者 | 初学者、実務1年目、SRE志望者など |
| 学習Promise | 受講後にできること |
| 市場シグナル | Udemy検索、競合、レビュー、外部需要 |
| 参照URL | 調査根拠URL |
| 競合との差別化 | 日本語、低コスト、ハンズオンCloudFormation、README再現性、実運用CDK/Terraform補足など |
| 受講者痛点 | レビュー/Q&Aから抽出した困りごと |
| ハンズオン範囲 | 作るAWS構成、手順、削除手順 |
| ハンズオンIaC適性 | CloudFormationで教材化しやすいか、CDK/Terraform実運用補足が必要か |
| コスト注意 | 無料枠、低コスト、要注意 |
| GPT-Image2適性 | 図解やスライド化のしやすさ |
| VOICEVOX注意 | 読み上げ注意語、専門用語 |
| 制作難易度 | low / medium / high |
| リスク | 古さ、課金、権限、再現性、競合過多 |
| 優先度 | high / medium / low |
| 仮説スコア | 0-100 |
| 備考 | CEO判断用メモ |

## スコアリング基準

合計100点で評価する。

| 評価軸 | 配点 | 見るもの |
| --- | ---: | --- |
| 市場需要 | 25 | Udemy検索結果、受講者数、レビュー数、Marketplace Insights |
| 競合ギャップ | 15 | 日本語不足、古い講座、説明不足、特化不足 |
| 受講者痛点 | 15 | レビュー/Q&Aで繰り返し出る困りごと |
| ハンズオン再現性 | 15 | README通りに再現でき、削除まで可能か |
| 制作容易性 | 10 | GPT-Image2、VOICEVOX、ffmpegで短期制作できるか |
| 戦略適合 | 10 | AWS/SRE教材ラインと相性がよいか |
| 鮮度 | 5 | 最近需要が伸びているか、古い教材が多いか |
| タイトル訴求 | 5 | 具体的で検索意図に合うか |

### 5段階評価の目安

| 点 | 意味 |
| ---: | --- |
| 5 | 強い根拠があり、優先制作候補 |
| 4 | 根拠が複数あり、制作価値が高い |
| 3 | 需要はあるが追加検証が必要 |
| 2 | 根拠が弱い、または競合が強すぎる |
| 1 | 制作する理由が薄い |
| 0 | 対象外またはルール違反 |

## 除外基準

以下に該当する候補は、需要があっても優先度を下げるか除外する。

- AWS/SREの会社ミッションから外れる
- README通りの再現が難しい
- 課金リスクが高い
- 初学者に危険な権限や構成を扱う
- 競合が強く、差別化が説明できない
- Udemyタイトル基準に反する誇大表現になる
- 最新性の維持コストが高すぎる
- AI生成だけで専門性を補えない

## 成果物の品質ゲート

TASK-0121は以下を満たしたら完了とする。

- 「売れる」を市場仮説として定義している
- 調査対象カテゴリが明確である
- 調査ソース一覧がある
- 50本リストの列定義がある
- スコアリング基準がある
- 外部有料ツール、課金API、AWS課金作業を使わないことが明記されている
- Worker/Reviewer分離が明記されている

## Worker / Reviewer分離

- TASK-0121 Owner AI: AI-Strategy-01
- TASK-0121 Reviewer AI: AI-QA-01

AI-Strategy-01は本計画書を作成する。AI-QA-01は、本計画書が後続調査に使えるかをレビューする。作成者が自分で承認してはいけない。
