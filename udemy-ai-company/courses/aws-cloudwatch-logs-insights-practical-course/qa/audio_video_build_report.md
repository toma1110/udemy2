# Audio Video Build Report

## Result

- Status: pass
- Voice: local VOICEVOX Engine
- Video build: `udemy-ai-company/tools/build_slide_audio_video.py`
- FFmpeg mode: 1 fps still-image segments, faststart final MP4
- Worker: AI-Production-01
- Reviewer: AI-QA-01

| Lecture | Title | Audio Count | Audio Duration sec | Video Duration sec | Faststart | MP4 Size bytes |
| --- | --- | ---: | ---: | ---: | --- | ---: |
| `s1-l1` | Logs Insights実践の地図 | 6 | 90.432 | 90.452 | True | 4912968 |
| `s1-l2` | ロググループと時間範囲 | 6 | 85.429 | 85.451 | True | 5022723 |
| `s1-l3` | 基本構文: fields/filter/sort/limit | 6 | 87.765 | 87.787 | True | 5021795 |
| `s2-l1` | エラーと例外を探す | 6 | 87.808 | 87.829 | True | 5028673 |
| `s2-l2` | stats/binで傾向を見る | 6 | 88.448 | 88.469 | True | 5025598 |
| `s2-l3` | parseとrequestId追跡 | 6 | 85.76 | 85.782 | True | 5031972 |
| `s3-l1` | pattern/anomalyで未知の変化を見る | 6 | 86.848 | 86.87 | True | 5114233 |
| `s3-l2` | JOIN/subquery/SOURCEの入口 | 6 | 87.701 | 87.723 | True | 5158834 |

## QA Notes

- All lectures have 6 slides and 6 WAV files.
- All MP4 files passed decode validation during build.
- Frame check PNG files were extracted for each lecture.
