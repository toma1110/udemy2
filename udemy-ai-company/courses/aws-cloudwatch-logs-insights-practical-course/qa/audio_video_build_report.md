# Audio Video Build Report

## Result

- Status: pass
- Remediation task: `TASK-0213`
- Build date: 2026-05-17
- Voice: local VOICEVOX Engine
- Video build: `udemy-ai-company/tools/build_slide_audio_video.py`
- FFmpeg mode: 1 fps still-image segments, faststart final MP4
- Total audio duration: 2058.389 sec (34.31 min)
- Total video duration: 2058.560 sec (34.31 min)
- Worker: AI-Production-01
- Reviewer: AI-QA-01

| Lecture | Title | Audio Count | Audio Duration sec | Video Duration sec | Video mm:ss | Faststart | MP4 Size bytes |
| --- | --- | ---: | ---: | ---: | ---: | --- | ---: |
| `s1-l1` | Logs Insights実践の地図 | 6 | 254.773 | 254.795 | 4:15 | True | 9394533 |
| `s1-l2` | ロググループと時間範囲 | 6 | 265.024 | 265.045 | 4:25 | True | 9927650 |
| `s1-l3` | 基本構文: fields/filter/sort/limit | 6 | 253.547 | 253.567 | 4:14 | True | 9559090 |
| `s2-l1` | エラーと例外を探す | 6 | 271.243 | 271.264 | 4:31 | True | 10042876 |
| `s2-l2` | stats/binで傾向を見る | 6 | 241.707 | 241.728 | 4:02 | True | 9202319 |
| `s2-l3` | parseとrequestId追跡 | 6 | 248.981 | 249.002 | 4:09 | True | 9500425 |
| `s3-l1` | pattern/anomalyで未知の変化を見る | 6 | 254.101 | 254.123 | 4:14 | True | 9677296 |
| `s3-l2` | JOIN/subquery/SOURCEの入口 | 6 | 269.013 | 269.034 | 4:29 | True | 10097383 |

## QA Notes

- All lectures have 6 GPT-Image2-derived slide PNG files and 6 VOICEVOX WAV files.
- All MP4 files passed decode validation during build.
- Faststart is true for all final MP4 files.
- Frame check PNG files were extracted for each lecture.
- Total lecture video duration is over 30 minutes; promo video is not counted.
- No AWS Logs Insights query execution was performed for this remediation.
- Google Drive upload was completed separately in `TASK-0222`; Drive URLs are recorded in `qa/drive_upload_summary.md`.
