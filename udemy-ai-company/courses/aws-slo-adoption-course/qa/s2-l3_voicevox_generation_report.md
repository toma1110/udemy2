# S2-L3 VOICEVOX音声生成レポート

## Ticket

- Task ID: TASK-0039
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
python3 udemy-ai-company/tools/narration_checker.py udemy-ai-company/courses/aws-slo-adoption-course/scripts/s2-l3_script.md --warnings-ok
OK: 1 files checked
```

## Generated Files

| Slide | Duration |
| --- | ---: |
| 1 | 20.064 sec |
| 2 | 23.115 sec |
| 3 | 21.525 sec |
| 4 | 21.344 sec |
| 5 | 21.323 sec |
| 6 | 20.501 sec |
| 7 | 21.365 sec |
| 8 | 20.811 sec |
| 9 | 19.296 sec |

Total duration: 189.344 sec

## Validation

- WAV count: 9
- Script slide count: 9
- WAV decode: pass
- Format: PCM 16-bit mono 24000 Hz
- Git tracking: generated WAV files are ignored by `.gitignore`
