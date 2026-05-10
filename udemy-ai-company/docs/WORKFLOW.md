# WORKFLOW

AI制作会社 v1 の標準状態遷移は以下です。

`Backlog -> Planning -> Engineering -> Engineering Review -> Production -> Content Review -> Ready for Publish -> Published -> Analytics Review`

## Backlog

- 担当AI: AI-Ops-01
- 入力: CEOの講座案、改善案、Change Request
- 出力: Backlog Issue
- 完了条件: Task ID、概要、優先度、Owner候補が記録されている

## Planning

- 担当AI: AI-Strategy-01
- 入力: Backlog Issue、CEO方針、既存 `course_spec.md`
- 出力: `course_spec.md`、章立て、Task分解、Impact Analysis
- 完了条件: 対象者、学習目標、ハンズオン範囲、Out of Scopeが明記され、CEO承認がある

## Engineering

- 担当AI: AI-Engineer-01
- 入力: 承認済みTask、`course_spec.md`、CloudFormationルール
- 出力: CloudFormationテンプレート、README、検証スクリプト
- 完了条件: validate、create、update、smoke test、deleteの実行結果が記録されている

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
