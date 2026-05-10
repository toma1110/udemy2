# AI_ORG_CHART

## 組織図

CEO

AI-Strategy-01

AI-Engineer-01

AI-Production-01

AI-QA-01

AI-Ops-01

## 責任分界

| 領域 | 主担当 | レビュー |
| --- | --- | --- |
| 講座企画 | AI-Strategy-01 | CEO、AI-QA-01 |
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

## エスカレーション

- スコープ判断: CEO
- 技術的ブロッカー: AI-Engineer-01からAI-QA-01へ相談
- 教材表現のブロッカー: AI-Production-01からAI-Strategy-01へ相談
- 進捗停止: AI-Ops-01がCEOへ通知
