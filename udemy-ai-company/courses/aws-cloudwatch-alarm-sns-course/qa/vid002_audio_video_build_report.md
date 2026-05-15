# VID-002 Audio and Video Build Report

## Target

- Course: `aws-cloudwatch-alarm-sns-course`
- Video ID: `VID-002`
- Date: 2026-05-15
- Worker: AI-Production-01
- Reviewer: AI-QA-01

## VOICEVOX

| Lecture | Audio count | Duration sec | Report |
| --- | ---: | ---: | --- |
| `s1-l2` | 7 | 118.976 | `audio/s1-l2/voicevox_report.md` |
| `s1-l3` | 7 | 107.605 | `audio/s1-l3/voicevox_report.md` |
| `s2-l1` | 8 | 125.312 | `audio/s2-l1/voicevox_report.md` |
| `s2-l2` | 8 | 127.979 | `audio/s2-l2/voicevox_report.md` |
| `s3-l1` | 8 | 128.043 | `audio/s3-l1/voicevox_report.md` |

## MP4

| Lecture | Slides | Audios | Duration sec | Size bytes | Faststart | Result |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| `s1-l2` | 7 | 7 | 118.996 | 5844636 | true | PASS |
| `s1-l3` | 7 | 7 | 107.625 | 5649791 | true | PASS |
| `s2-l1` | 8 | 8 | 125.332 | 6507702 | true | PASS |
| `s2-l2` | 8 | 8 | 127.998 | 6555266 | true | PASS |
| `s3-l1` | 8 | 8 | 128.063 | 6557141 | true | PASS |

## Checks

| Check | Result | Notes |
| --- | --- | --- |
| Slide/audio count match | PASS | All new lectures match. |
| Faststart | PASS | All build reports have `faststart: true`. |
| Decode validation | PASS | Build tool validated decode for all new MP4 files. |
| Frame check | PASS | Build tool extracted one frame check per lecture. |

## Result

Status: PASS
