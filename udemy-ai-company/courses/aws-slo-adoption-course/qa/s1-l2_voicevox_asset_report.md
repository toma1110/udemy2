# S1-L2 VOICEVOX Asset Report

## 対象

- Course: `aws-slo-adoption-course`
- Lecture: Section 1 Lecture 2
- Script: `courses/aws-slo-adoption-course/scripts/s1-l2_script.md`
- Audio: `courses/aws-slo-adoption-course/audio/s1-l2/slide_*.wav`

## 検証条件

- WAV files: 9
- Format: WAV, PCM 16-bit, mono, 44100 Hz
- gTTS fallback: 使用痕跡なし
- VOICEVOX Engine起動確認: OK, version `0.25.1`

## 検証結果

| File | Duration |
|---|---:|
| `slide_001.wav` | 20.89s |
| `slide_002.wav` | 21.82s |
| `slide_003.wav` | 18.07s |
| `slide_004.wav` | 16.95s |
| `slide_005.wav` | 21.48s |
| `slide_006.wav` | 20.43s |
| `slide_007.wav` | 19.31s |
| `slide_008.wav` | 20.62s |
| `slide_009.wav` | 19.99s |

Total: 179.55s

## Production Checks

- `tools/narration_checker.py courses/aws-slo-adoption-course/scripts/s1-l2_script.md --warnings-ok`: OK
- WAV数とスライド数の一致: OK
- WAVデコード確認: OK
- 音声形式: OK
- 聴取QA指摘により、Slide 1とSlide 5をVOICEVOXで再生成済み。

## QA Listening Notes

Worker/Reviewer分離のため、AI-Production-01は機械的検証までとする。
AI-QA-01は以下を聴取確認する。

- `エスエルオー`、`エスエルアイ`、`エスアールイー` が自然に聞こえること
- `エーダブリューエス`、`クラウドウォッチ` が不自然に途切れないこと
- Slide 1の `さわれる`、Slide 5の `そうしたかたが` が意図通り聞こえること
- 各スライドの文末が切れていないこと
- 長すぎる無音や異常なノイズがないこと
