# S2-L2 VOICEVOX音声生成レポート

## Ticket

- Task ID: TASK-0033
- Owner AI: AI-Production-01
- Reviewer AI: AI-QA-01
- 実施日: 2026-05-10

## Generation Settings

- Engine: VOICEVOX
- Engine version: `0.25.1`
- Speaker ID: `3`
- Speed scale: `1.1`
- gTTS fallback: 未使用

## Pre-check

```text
python3 udemy-ai-company/tools/narration_checker.py udemy-ai-company/courses/aws-slo-adoption-course/scripts/s2-l2_script.md --warnings-ok
OK: 1 files checked
```

## Generated Files

| Slide | Duration |
| --- | ---: |
| 1 | 19.360 sec |
| 2 | 22.709 sec |
| 3 | 21.760 sec |
| 4 | 21.760 sec |
| 5 | 19.957 sec |
| 6 | 21.248 sec |
| 7 | 21.419 sec |
| 8 | 18.688 sec |
| 9 | 21.867 sec |

Total duration: 188.768 sec

## Validation

- WAV count: 9
- Script slide count: 9
- WAV decode: pass
- Format: PCM 16-bit mono 24000 Hz
- Git tracking: generated WAV files are ignored by `.gitignore`
