# S3 Slide Generation Root Cause Report

## Trigger

- Date: 2026-05-11
- Source: GitHub Issue #77 CEO comment
- Comment: s2に比べ明らかにスライドの質が落ちた。GPT-Image2で作成できているか。できていない場合は原因分析と再発防止を行う。

## Answer

2026-05-10に再アップロードした修正版S3スライドは、GPT-Image2で作成できていません。

修正版S3スライドは、`udemy-ai-company/tools/render_text_rich_s3_slides.py` によるローカルPillow描画で作成されました。これは「スライドはGPT-Image2でPNG生成する」という制作ルールを満たしていません。

## Impact

- S2で承認されたGPT-Image2系スライドに比べ、視覚的な質感、奥行き、教材としてのリッチさが落ちた。
- S3の修正版動画は、ファイル形式、音声、動画結合、Drive共有の技術検証は通っているが、スライド生成元の品質ゲートを満たしていない。
- Issue #77の再確認依頼コメントでは、生成元がローカル描画であることを明示できていなかった。
- 現在の修正版S3動画は、CEO承認済み例外またはGPT-Image2再生成がない限り、最終成果物として扱わない。

## Direct Cause

S3-L1の初回フィードバックで「文字量が少なく、S2と印象が違う」という問題を受けた際、文字量と日本語表示精度を優先し、GPT-Image2再生成ではなくローカルPillow描画でS2風の文字入りスライドへ差し替えました。

## Structural Causes

- 変更要求の品質基準が「S2相当の文字量」に寄り、GPT-Image2由来であることを再確認するゲートが抜けた。
- `*_slide_generation_report.md` に、最終PNGのGeneration Mode、GPT-Image2出力元、プロンプト概要、後処理内容を記録する必須欄がなかった。
- QAが画像サイズ、枚数、contact sheet、動画結合を中心に確認し、最終スライドの生成元証跡をブロッカーとして扱えていなかった。
- ローカル描画スクリプトを、例外承認なしに最終スライド生成手段として使ってしまった。

## What Worked

- 既存VOICEVOX音声は維持され、音声品質の問題は増やしていない。
- S3全5本の動画ファイル自体はH.264、1920x1080、AAC、faststart、ffmpeg decode check、Drive共有まで確認済み。
- CEO確認でS2との差分が早期に検出された。

## Corrective Actions Completed

- `docs/QUALITY_GATE.md` に、最終スライドPNGのGPT-Image2生成元またはCEO承認済み例外を必須化した。
- `docs/QUALITY_GATE.md` に、Generation Mode、GPT-Image2出力元、プロンプト概要、後処理内容、contact sheet比較の記録を必須化した。
- `templates/slide_generation_report_template.md` を追加し、今後のスライド生成レポートに生成元証跡欄を設けた。
- S3のスライド生成レポートとSection 3完了レポートを、現状の修正版S3がGPT-Image2最終成果物ではないことが分かる内容へ更新した。

## Preventive Actions

- AI-Production-01は、最終スライドPNGをGPT-Image2生成物またはCEO承認済み例外として記録するまで動画生成へ進めない。
- AI-QA-01は、スライド枚数、サイズ、contact sheetだけでなく、Generation Modeと生成元証跡を確認する。
- ローカルPillow、HTML Canvas、SVG等の描画は、明示された後処理またはCEO承認済み例外に限定する。
- S2など直近承認済みセクションをリファレンスにする場合は、動画生成前にcontact sheet比較を行い、質感や情報密度が落ちる場合はBlockedにする。
- 例外的にローカル描画を採用する場合は、change requestで理由、影響、リスク、CEO承認を残す。

## Current S3 Status

- Audio: OK
- Video technical validation: OK
- Drive upload: OK
- Slide provenance quality gate: Blocked

S3を最終承認へ進めるには、次のいずれかが必要です。

- GPT-Image2でS3スライドを再生成し、動画を再ビルドする。
- CEOが、現在のローカル描画版を例外として承認する。

## Recommended Next Ticket

- TASK-0084 / GitHub Issue #84: Section 3スライドをGPT-Image2で再生成し、S2承認版の品質に合わせて動画を再作成する。
