# WORKFLOW

AI制作会社 v1 の標準状態遷移は以下です。

`Backlog -> Planning -> Engineering -> Engineering Review -> Production -> Content Review -> Ready for Publish -> Published -> Analytics Review`

全フェーズで、AI社員は `docs/MISSION_VISION_VALUES.md` のミッション、ビジョン、バリューと矛盾しない判断を行う。

AI-PM-01は全フェーズ横断でGitHub Issueの変更を検知し、`auto-execute` ラベル付きIssueだけを自動実行キューへ送る。AWS課金につながる環境構築、デプロイ、CloudFormation stack作成/更新/削除、Fargate/Batch/ECR等は、CEO承認がIssueに残るまで自動実行しない。

AI-PM-01はOpen Issueを定期整理し、CEO承認待ちではないIssueを `done` にしてcloseする。Openに残してよいのは、`approval-required` 等でCEO承認待ちであることが明確なIssueだけである。

AI-Ops-01は定期的に仕組みルール監査を行い、Owner/Reviewer分離、CEO承認ゲート、Issue必須項目、Source of Truth参照、PM自動クローズ方針が守られているかを確認する。監査結果は `AI-Ops Rule Audit` Issueへ記録し、軽微なラベル補正以外は報告に留める。

## Backlog

- 担当AI: AI-Ops-01
- 入力: CEOの講座案、改善案、Change Request
- 出力: Backlog Issue
- 完了条件: Task ID、概要、優先度、Owner候補が記録されている

AI-PM-01はBacklog Issueの更新を検知し、Owner AI、Reviewer AI、`Auto Execute`、`Requires CEO Approval` が不足していれば実行対象外にする。

## Planning

- 担当AI: AI-Strategy-01
- 入力: Backlog Issue、CEO方針、既存 `course_spec.md`
- 出力: `course_spec.md`、章立て、Task分解、Impact Analysis
- 完了条件: 対象者、学習目標、ハンズオン範囲、Out of Scopeが明記され、CEO承認がある

AI-PM-01はPlanning完了後のTask Issueを監視し、`auto-execute` があり、Worker/Reviewer分離と承認条件を満たす場合だけ実行キューに入れる。

## Engineering

- 担当AI: AI-Engineer-01
- 入力: 承認済みTask、`course_spec.md`、CloudFormationルール
- 出力: CloudFormationテンプレート、README、検証スクリプト
- 完了条件: validate、create、update、smoke test、deleteの実行結果が記録されている

CloudFormation stack作成/更新/削除、AWS Batch/Fargate、ECR push、その他AWSリソース作成を伴う検証はCEO承認後にだけ実行する。承認前はテンプレート編集、README編集、静的検証準備までに限定する。

## Engineering Review

- 担当AI: AI-QA-01
- 入力: Engineering成果物、検証レポート、`course_spec.md`
- 出力: QAレポート、承認または差戻し
- 完了条件: README再現性、CloudFormation品質、コスト、削除手順が確認済み

## Production

- 担当AI: AI-Production-01
- 入力: レビュー済みハンズオン、`course_spec.md`、STYLE_GUIDE
- 出力: スライドPNG、台本、VOICEVOX素材、動画素材
- 完了条件: READMEと動画手順が一致し、GPT-Image2とVOICEVOX前提で素材が揃い、ナレーションチェックが完了している

## Content Review

- 担当AI: AI-QA-01
- 入力: スライド、台本、音声、動画素材、README
- 出力: 教材QAレポート、承認または差戻し
- 完了条件: 技術的誤り、手順不一致、読み上げ不自然箇所、英字残存、空白による不自然な間が解消されている

## Ready for Publish

- 担当AI: AI-Ops-01
- 入力: QA承認済み成果物、CEO確認依頼
- 出力: 公開候補、Google Driveアップロード準備
- 完了条件: CEOの公開承認待ち状態になっている

## Published

- 担当AI: AI-Ops-01
- 入力: CEO承認、完成動画、関連素材
- 出力: Google Driveアップロード記録、公開完了Issue
- 完了条件: アップロード先、公開状態、対象ファイル名が記録されている

## Analytics Review

- 担当AI: AI-Strategy-01、AI-Ops-01
- 入力: 受講データ、レビュー、質問、完了率
- 出力: 改善Issue、次講座企画
- 完了条件: 改善候補がBacklog Issueとして登録されている
