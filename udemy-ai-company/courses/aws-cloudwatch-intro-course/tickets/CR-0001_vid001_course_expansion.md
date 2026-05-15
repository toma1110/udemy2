# Change Request

## Change Summary

`VID-001`を1本の短尺動画から、CloudWatch入門の複数レクチャーコースへ拡張する。

## Why Change

- 既存の`CloudWatchの地図`動画の品質がコース展開に耐える。
- Logs Insightsは実務需要が高く、単発の概念紹介よりも独立セクションとして扱う価値がある。
- 初学者がCloudWatchの用語、画面、調査手順を一続きで学べる構成にする。

## Scope

- `course_spec.md`をSource of Truthとして更新
- `course_curriculum.md`を追加
- `handson/README.md`へLogs Insights読解を追加
- `s1-l2`、`s1-l3`、`s2-l1`、`s2-l2`、`s3-l1`の台本、GPT-Image2プロンプト、音声、動画を制作
- QAレポートを追加

## Impact

- 既存の`s1-l1`は維持する。
- コースタイトルとREADMEは複数レクチャー前提へ変わる。
- 完成動画数は1本から6本へ増える。

## Risks

- GPT-Image2の日本語文字崩れが発生する可能性がある。
- Logs Insightsクエリは対象ログ形式に依存するため、ハンズオンでは読解中心にする。
- Logs Insights実行にはスキャン料金が発生する可能性がある。

## Approval

- CEO approval: Approved by user request on 2026-05-15
- Approval note: 「コースとして育ててください」「logs insightなんか需要ありそう」「動画作成までやりきって良い」

## Implementation Plan

1. Course spec and curriculum update
2. Hands-on README update
3. New lecture scripts and structured JSON
4. GPT-Image2 prompt creation and source PNG preservation
5. VOICEVOX audio generation
6. MP4 build
7. QA review

## Ownership

- Planner AI: `AI-Strategy-01`
- Worker AI: `AI-Production-01`
- Reviewer AI: `AI-QA-01`
