# Production QA Plan

Task ID: TASK-0195
Course: `aws-alert-design-practical-course`
Reviewer AI: AI-QA-01
Status: Draft

## Scope

Initial production target:

- `s1-l1`: 深夜3時に動けるアラートとは

## Content QA

- 良いアラートの3条件が説明されている
- 悪い例から良い例への改善が具体的である
- Alert Fatigue、Owner、Runbook、Escalationが含まれている
- CloudWatch AlarmのPeriod、Evaluation Periods、Datapoints to Alarmが正しく説明されている
- missing dataをメトリクス種別で考える説明になっている
- Composite Alarmが通知数削減の選択肢として説明されている
- 「全ワークロードでこの閾値が正解」と断定していない

## Production QA

- GPT-Image2 source PNGが保存されている
- 最終PNGはGPT-Image2由来である
- 表示文字がGPT-Image2生成である
- ローカル文字合成が混ざっていない
- VOICEVOX音声を使っている
- MP4に音声欠落、黒画面、スライド順誤りがない
- Drive upload reportが存在する
- コース画像もGoogle Driveへアップロードされている

## Governance QA

- Worker AI: AI-Production-01
- Reviewer AI: AI-QA-01
- Worker != Reviewer
- AWS実行なし
- 実AWS作業を追加する場合はCEO承認が必要

## Current Status

- Course spec: Draft complete
- Script: Draft complete for `s1-l1`
- GPT-Image2 prompt plan: Draft complete
- Voice/video generation: Not started
- Drive upload: Not started
