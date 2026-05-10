# S1-L1 VOICEVOX Generation Report

## 対象

- Course: `aws-slo-adoption-course`
- Lecture: Section 1 Lecture 1
- Script: `courses/aws-slo-adoption-course/scripts/s1-l1_script.md`
- Output: `courses/aws-slo-adoption-course/audio/s1-l1/slide_*.wav`

## 生成条件

- Engine: VOICEVOX Engine `0.25.1`
- Speaker ID: `3`
- Speed scale: `1.1`
- gTTS fallback: 未使用
- Output format: WAV, PCM 16-bit, mono, 44100 Hz

## 生成結果

| File | Duration |
|---|---:|
| `slide_001.wav` | 20.10s |
| `slide_002.wav` | 21.39s |
| `slide_003.wav` | 19.75s |
| `slide_004.wav` | 17.96s |
| `slide_005.wav` | 20.97s |
| `slide_006.wav` | 21.46s |
| `slide_007.wav` | 21.83s |
| `slide_008.wav` | 25.86s |
| `slide_009.wav` | 20.42s |

Total: 189.74s

## Production Checks

- `tools/narration_checker.py courses/aws-slo-adoption-course/scripts`: OK
- VOICEVOX起動確認: OK
- 生成WAV数: 9
- WAVデコード確認: OK
- `SLO`、`SLI`、`SLA` はナレーション本文で読み上げ表記に変換済み
- `Application Signals`、`CloudWatch`、`error budget`、`burn rate` はナレーション本文で読み上げやすい表記に変換済み

## QA Listening Notes

Worker/Reviewer分離のため、AI-Production-01は制作確認までとする。
AI-QA-01は以下を聴取確認する。

- `エスエルオー`、`エスエルアイ`、`エスエルエー` が自然に聞こえること
- `アプリケーションシグナル`、`クラウドウォッチ`、`エラーバジェット`、`バーンレート` が不自然に途切れないこと
- スライドごとの文末が切れていないこと
- 長すぎる無音や異常なノイズがないこと
