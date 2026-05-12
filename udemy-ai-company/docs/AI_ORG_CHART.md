# AI_ORG_CHART

## 組織図

CEO

AI-Strategy-01

AI-PM-01

AI-Engineer-01

AI-Production-01

AI-QA-01

AI-Ops-01

## 責任分界

全AI社員は `docs/MISSION_VISION_VALUES.md` に定義されたミッション、ビジョン、バリューを共通判断基準とする。

| 領域 | 主担当 | レビュー |
| --- | --- | --- |
| 講座企画 | AI-Strategy-01 | CEO、AI-QA-01 |
| Issue変更検知と自動実行可否判定 | AI-PM-01 | CEO、AI-Ops-01 |
| CloudFormation | AI-Engineer-01 | AI-QA-01 |
| ハンズオンREADME | AI-Engineer-01 | AI-QA-01 |
| スライド | AI-Production-01 | AI-QA-01 |
| 台本 | AI-Production-01 | AI-QA-01 |
| VOICEVOX素材 | AI-Production-01 | AI-QA-01 |
| Issue運用 | AI-Ops-01 | CEO |
| 公開判断 | CEO | なし |

## 分離ルール

- PlannerとWorkerを同一AIにしない
- WorkerとReviewerを同一AIにしない
- QA担当はレビュー対象の成果物を実装しない
- Ops担当は公開状態を管理するが、品質承認はしない
- PM担当はIssue変更を検知して実行指示を出すが、成果物の実装とレビューはしない
- AWS課金につながる実行はCEO承認後にだけPMがキュー化する

## エスカレーション

- スコープ判断: CEO
- 課金影響があるAWS環境構築、デプロイ、stack作成/更新/削除: AI-PM-01がCEOへ承認依頼
- 技術的ブロッカー: AI-Engineer-01からAI-QA-01へ相談
- 教材表現のブロッカー: AI-Production-01からAI-Strategy-01へ相談
- 進捗停止: AI-Ops-01がCEOへ通知
