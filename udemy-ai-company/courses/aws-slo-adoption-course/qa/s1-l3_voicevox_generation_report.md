# S1-L3 VOICEVOX音声生成レポート

## Ticket

- Task ID: TASK-0018
- Owner AI: AI-Production-01
- Reviewer AI: AI-QA-01
- 実施日: 2026-05-10

## Inputs

- 台本: `udemy-ai-company/courses/aws-slo-adoption-course/scripts/s1-l3_script.md`
- 読み上げルール: `udemy-ai-company/docs/VOICEVOX_RULES.md`
- チェッカー: `udemy-ai-company/tools/narration_checker.py`
- 出力先: `udemy-ai-company/courses/aws-slo-adoption-course/audio/s1-l3/`

## Generation Settings

- Engine: VOICEVOX
- Engine version: `0.25.1`
- Speaker ID: `3`
- Speed scale: `1.1`
- gTTS fallback: 未使用
- Text normalization: `src.voice_generator.normalize_for_voicevox()`

## Pre-check

```text
python3 udemy-ai-company/tools/narration_checker.py udemy-ai-company/courses/aws-slo-adoption-course/scripts/s1-l3_script.md --warnings-ok
OK: 1 files checked
```

## Generated Files

| Slide | File | Format | Duration |
| --- | --- | --- | ---: |
| 1 | `slide_001.wav` | PCM 16-bit mono 24000 Hz | 19.499 sec |
| 2 | `slide_002.wav` | PCM 16-bit mono 24000 Hz | 20.149 sec |
| 3 | `slide_003.wav` | PCM 16-bit mono 24000 Hz | 23.797 sec |
| 4 | `slide_004.wav` | PCM 16-bit mono 24000 Hz | 19.499 sec |
| 5 | `slide_005.wav` | PCM 16-bit mono 24000 Hz | 22.965 sec |
| 6 | `slide_006.wav` | PCM 16-bit mono 24000 Hz | 20.384 sec |
| 7 | `slide_007.wav` | PCM 16-bit mono 24000 Hz | 19.787 sec |
| 8 | `slide_008.wav` | PCM 16-bit mono 24000 Hz | 21.365 sec |
| 9 | `slide_009.wav` | PCM 16-bit mono 24000 Hz | 22.517 sec |

Total duration: 189.963 sec

## Validation

- WAV count: 9
- Script slide count: 9
- WAV decode: pass
- `file` check: all files are RIFF/WAVE PCM 16-bit mono 24000 Hz
- Git tracking: generated WAV files are ignored by `.gitignore`

## Notes

- S1-L3のナレーション本文では、既知の誤読リスクが高い `触れる`、`そうした方`、`上で` を使用していない。
- 動画化時は、concatの安定性を優先し、AAC 44100 Hz monoへ変換して結合する。
