# Market Research QA Report

Task ID: TASK-0128
GitHub Issue: https://github.com/toma1110/udemy2/issues/135
Owner AI: AI-QA-01
Reviewer AI: AI-Ops-01
作成日: 2026-05-13

## QA対象

- `market-research/udemy_research_plan.md`
- `market-research/udemy_competitor_scan.md`
- `market-research/udemy_keyword_demand_scan.md`
- `market-research/learner_pain_review_scan.md`
- `market-research/udemy_sellable_video_candidates_50.md`
- `market-research/udemy_video_idea_scoring_top10.md`
- `market-research/next_course_decision_pack.md`

## 結論

QA結果: PASS

CEO判断に進められる。

## チェック結果

| 項目 | 結果 | メモ |
| --- | --- | --- |
| 50本以上の動画候補 | PASS | 52件作成済み |
| 各候補にタイトル案がある | PASS | `VID-001`〜`VID-052` |
| 対象者がある | PASS | 候補表の対象者列で確認 |
| 学習Promiseがある | PASS | 候補表の学習Promise列で確認 |
| 市場シグナルがある | PASS | `Cxx`、`Kxx`、`Pxx` を紐付け |
| 差別化がある | PASS | 日本語、ハンズオンCloudFormation、実運用CDK/Terraform補足、README再現性、低コストなど |
| 制作難易度がある | PASS | low/medium/highで分類 |
| 優先度がある | PASS | high/medium/lowで分類 |
| 全候補にスコアがある | PASS | 52件すべて採点済み |
| 上位10本がある | PASS | `udemy_video_idea_scoring_top10.md` に記載 |
| 上位3講座候補がある | PASS | `next_course_decision_pack.md` に記載 |
| 調査日がある | PASS | 各主要ファイルに2026-05-13を記録 |
| 「売れる」と断定していない | PASS | 市場仮説として表現 |
| 外部有料ツール/課金API不使用 | PASS | 調査計画に明記 |
| AWS課金作業不実行 | PASS | 調査のみ、AWS操作なし |
| Worker/Reviewer分離 | PASS | Strategy成果物をQAがレビュー。Opsレビューは本レポート後の運用確認対象 |

## 主要な確認内容

### 調査根拠

Udemy公式ガイドで、講座テーマ選定では需要、競合、Marketplace Insights、レビュー、Q&A、Traffic & Conversionsなどの情報を見るべきことを確認した。

公開競合ページでは、CloudWatch、CloudFormation、AWS DevOps、EKS、FinOps、AWS Security、Bedrock領域の講座を確認した。

### 50本リスト

52件あり、要求された「50本以上」を満たす。

強い候補は以下:

- VID-011 CloudFormation validate/update/delete安全手順
- VID-019 AWS Budgetsで課金事故を防ぐ
- VID-002 CloudFormationで作るCloudWatch Alarm + SNS通知
- VID-006 SLI/SLOをAWSメトリクスに落とす入門
- VID-041 BedrockアプリのCloudWatch監視入門
- VID-042 Bedrockコストを見える化する
- VID-028 Lambdaのエラー率を監視する
- VID-022 GitHub ActionsからAWSへOIDCで安全に接続
- VID-005 良いアラートと悪いアラート
- VID-003 CloudWatch Dashboardをコードで管理する

### CEO判断パック

上位3候補は妥当。

推奨順位:

1. AWS CloudWatch運用監視入門: CloudFormationハンズオン版
2. AWSコスト事故防止とFinOps入門
3. Bedrockアプリ運用監視入門

最初に作るなら、Candidate Aが最も安全。既存AWS SRE路線、教材ハンズオンCloudFormation、実運用CDK/Terraform補足、低コスト、README再現性に合う。

## 残リスク

- Udemy Marketplace Insightsの実データは未確認
- Udemy講座のレビュー/Q&A詳細は公開表示範囲に依存
- 競合講座の評価、受講者数、更新日は変動する
- Bedrock系はAWSサービス更新と料金変更の影響を受けやすい

## 推奨アクション

CEOが次に選ぶべき作業:

1. Candidate Aを採用するか判断する
2. 採用する場合、`course_spec.md` 作成チケットを起票する
3. 制作前にUdemy Marketplace Insightsで `CloudWatch`、`CloudFormation`、`AWS SRE`、`AWS monitoring` を再確認する

## QA判定

PASS。

市場リサーチとしてCEO判断に進めてよい。
