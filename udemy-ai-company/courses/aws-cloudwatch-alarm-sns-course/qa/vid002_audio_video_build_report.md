# VID-002 Audio and Video Build Report

## Target

- Course: `aws-cloudwatch-alarm-sns-course`
- Video ID: `VID-002`
- Date: 2026-05-17
- Task: `TASK-0215`
- Worker: AI-Production-01
- Reviewer: AI-QA-01

## VOICEVOX

| Lecture | Audio count | Duration sec | Duration min | Report |
| --- | ---: | ---: | ---: | --- |
| `s1-l1` | 11 | 383.328 | 6.39 | `audio/s1-l1/voicevox_report.md` |
| `s1-l2` | 7 | 374.997 | 6.25 | `audio/s1-l2/voicevox_report.md` |
| `s1-l3` | 7 | 308.768 | 5.15 | `audio/s1-l3/voicevox_report.md` |
| `s2-l1` | 8 | 344.064 | 5.73 | `audio/s2-l1/voicevox_report.md` |
| `s2-l2` | 8 | 349.643 | 5.83 | `audio/s2-l2/voicevox_report.md` |
| `s3-l1` | 8 | 354.805 | 5.91 | `audio/s3-l1/voicevox_report.md` |
| **Total** | 49 | 2115.605 | 35.26 |  |

## MP4

| Lecture | Slides | Audios | Duration sec | Duration min | Size bytes | Faststart | Result |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| `s1-l1` | 11 | 11 | 383.345 | 6.39 | 15912591 | true | PASS |
| `s1-l2` | 7 | 7 | 375.018 | 6.25 | 12805540 | true | PASS |
| `s1-l3` | 7 | 7 | 308.789 | 5.15 | 11141666 | true | PASS |
| `s2-l1` | 8 | 8 | 344.084 | 5.73 | 12478741 | true | PASS |
| `s2-l2` | 8 | 8 | 349.663 | 5.83 | 12602727 | true | PASS |
| `s3-l1` | 8 | 8 | 354.826 | 5.91 | 12732591 | true | PASS |
| **Total** | 49 | 49 | 2115.726 | 35.26 | 77673856 | true | PASS |

## Checks

| Check | Result | Notes |
| --- | --- | --- |
| Slide/audio count match | PASS | All six lectures match. |
| Runtime requirement | PASS | Main lecture runtime is 35.26 minutes; promo video is excluded. |
| Faststart | PASS | All build reports have `faststart: true`. |
| Decode validation | PASS | Build tool validated decode for all six MP4 files. |
| Frame check | PASS | Build tool extracted one frame check per lecture. |
| Google Drive upload | NOT RUN | Not requested in this task; separate CEO approval required. |

## Result

Status: PASS for local MP4 production.
