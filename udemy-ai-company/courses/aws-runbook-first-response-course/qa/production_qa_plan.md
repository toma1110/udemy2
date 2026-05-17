# Production QA Plan

Task ID: TASK-0201
Course: `aws-runbook-first-response-course`
Reviewer AI: AI-QA-01
Status: Draft

## Scope

Initial production target:

- `s1-l1`: Runbookに何を書くか

## Content QA

- Runbookの目的が説明されている
- PlaybookとRunbookの違いを混同していない
- Trigger、Owner、Severity、Scope、Goalが含まれている
- First Checksが5分以内の確認に絞られている
- Mitigation、Rollback、Escalationが含まれている
- CommunicationとPostmortem Linkが含まれている
- AWS実行なしで成立している
- 自動化や切り戻しを無条件に推奨していない

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
