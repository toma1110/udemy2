# S1-L2 Video Build Report

## 対象

- Course: `aws-slo-adoption-course`
- Lecture: Section 1 Lecture 2
- Script: `courses/aws-slo-adoption-course/scripts/s1-l2_script.md`
- Slides: `courses/aws-slo-adoption-course/slides/s1-l2/slide_*.png`
- Audio: `courses/aws-slo-adoption-course/audio/s1-l2/slide_*.wav`
- Output: `courses/aws-slo-adoption-course/video/s1-l2/s1-l2.mp4`

## Build Method

各スライドを対応するWAVと結合してMP4セグメントを作成し、concatで1本の動画に結合した。

- Video: H.264, 1920x1080, 30fps
- Audio: AAC, mono, 44100 Hz
- `-nostdin` を付けてffmpegの標準入力消費を防止
- `-movflags +faststart` 適用済み

## Inputs

| Type | Count |
|---|---:|
| Slide PNG | 9 |
| Audio WAV | 9 |

## Output Validation

| Check | Result |
|---|---|
| MP4 generated | OK |
| Duration | 179.571s |
| Size | 7,890,811 bytes |
| Video stream | H.264, 1920x1080, 30fps |
| Audio stream | AAC, mono, 44100 Hz |
| Decode check | OK |
| Faststart | OK |
| Representative frame check | OK |

## QA Notes

Worker/Reviewer分離のため、AI-Production-01は生成と機械的検証までとする。
AI-QA-01は以下を確認する。

- スライド順と音声順が自然に一致していること
- Slide 1の `さわれる`、Slide 5の `そうしたかたが` が意図通り聞こえること
- 音声の切れ、長すぎる無音、異常なノイズがないこと
- スライド内の表示テキストが講座方針と一致していること
- Google Drive上で再生可能になること
