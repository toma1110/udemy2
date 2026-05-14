# S9-L4 VOICEVOX Generation Report

## Target

- Issue: #124 / TASK-0116
- Lecture: S9-4 このコースで学んだことの総整理
- Script JSON: `scripts/s9-l4_script.json`
- Audio directory: `audio/s9-l4/`
- Worker: AI-Production-01
- Reviewer: AI-QA-01

## Result

Pass.

## Output

- Audio count: 8
- Report slide count: 8
- Total duration seconds: 133.888
- `voicevox_report.json`: recorded

## Audio

| Slide | WAV | Duration sec |
| ---: | --- | ---: |
| 1 | `slide_001.wav` | 16.885 |
| 2 | `slide_002.wav` | 14.165 |
| 3 | `slide_003.wav` | 16.917 |
| 4 | `slide_004.wav` | 16.416 |
| 5 | `slide_005.wav` | 17.163 |
| 6 | `slide_006.wav` | 17.269 |
| 7 | `slide_007.wav` | 15.211 |
| 8 | `slide_008.wav` | 19.861 |

## Notes

- VOICEVOX Engine version checked at runtime: 0.25.1
- Long batch generation was split into one-slide runs for stability; final report was rebuilt from existing WAV durations.
- Worker != Reviewer: pass
