# VID-001 Course Expansion QA Report

## Summary

- Course: `aws-cloudwatch-intro-course`
- Scope: `VID-001` course expansion from 1 lecture to 6 lectures
- QA date: 2026-05-15
- Worker AI: `AI-Production-01`
- Reviewer AI: `AI-QA-01`
- Result: PASS

## Course Structure

| Lecture | Title | Slides | Audio | MP4 | Duration sec | Faststart |
| --- | --- | ---: | ---: | --- | ---: | --- |
| `s1-l1` | CloudWatchの地図 | 10 | 10 | `video/s1-l1/s1-l1.mp4` | 174.878 | true |
| `s1-l2` | Metricsの基本 | 7 | 7 | `video/s1-l2/s1-l2.mp4` | 107.679 | true |
| `s1-l3` | Logsの基本 | 7 | 7 | `video/s1-l3/s1-l3.mp4` | 104.415 | true |
| `s2-l1` | Logs Insights入門 | 8 | 8 | `video/s2-l1/s2-l1.mp4` | 125.055 | true |
| `s2-l2` | Logs Insightsで障害調査 | 7 | 7 | `video/s2-l2/s2-l2.mp4` | 110.398 | true |
| `s3-l1` | Alarm/Dashboardと次の一歩 | 8 | 8 | `video/s3-l1/s3-l1.mp4` | 117.118 | true |

## Source of Truth

| Check | Result | Notes |
| --- | --- | --- |
| `course_spec.md` exists | PASS | Multi-lecture course definition updated |
| `course_curriculum.md` exists | PASS | Section titles, section learning objectives, handson resource titles included |
| `handson/README.md` exists | PASS | Resource-creation-free, Logs Insights read-through added |
| Course is no longer one video only | PASS | 6 lectures defined |
| Logs Insights has independent section | PASS | Section 2 includes `s2-l1` and `s2-l2` |

## Script QA

| Check | Result | Notes |
| --- | --- | --- |
| Structured JSON exists for all lectures | PASS | `s1-l1` through `s3-l1` |
| Markdown scripts exist for all lectures | PASS | New scripts added for 5 lectures |
| Narration checker | PASS | `OK: 12 files checked` |
| VOICEVOX-friendly Japanese | PASS | English service names avoided or read naturally in narration |
| Logs Insights syntax alignment | PASS | `fields`, `filter`, `sort`, `limit`, `stats`, `bin`, `dedup` usage matches official syntax |

## Slide QA

| Check | Result | Notes |
| --- | --- | --- |
| GPT-Image2 source PNGs exist | PASS | Sources saved under `slides/<section>-gpt-image2-sources/<lecture>/` |
| Final PNGs are GPT-Image2-derived | PASS | Local step only resized/fitted to 1920x1080 |
| Local text overlay absent | PASS | `fit_gpt_image_slides.py` does not draw slide title/body text |
| Contact sheets exist | PASS | `slides/<lecture>/contact_sheet.png` exists for all new lectures |
| VID-001 visual baseline | PASS | Tone and density are consistent with `s1-l1` GPT-Image2 version |
| Text quality | PASS with note | Some GPT-generated helper labels appear in diagrams; no local text edits, no visible watermarks |

## Audio QA

| Check | Result | Notes |
| --- | --- | --- |
| VOICEVOX used | PASS | Local VOICEVOX engine, speaker ID 3 |
| gTTS fallback absent | PASS | No fallback used |
| Audio count equals slide count | PASS | Verified for all lectures |
| Audio reports exist | PASS | `audio/<lecture>/voicevox_report.md` and `.json` |

## Video QA

| Check | Result | Notes |
| --- | --- | --- |
| MP4 exists for all lectures | PASS | 6 total including existing `s1-l1` |
| Decode validation | PASS | `build_slide_audio_video.py` validation completed |
| Faststart | PASS | All build reports show `faststart: true` |
| Frame checks | PASS | `frame_check_*s.png` generated for new lectures |
| Slide/audio counts match | PASS | Build reports show matching counts |

## Hands-on QA

| Check | Result | Notes |
| --- | --- | --- |
| Resource creation not required | PASS | README explicitly says not to create resources |
| Logs Insights cost warning | PASS | Scope, time range, query cancellation, dashboard refresh warning included |
| CloudFormation scope | PASS | Not used in this intro course |
| Production IaC recommendation | PASS | CDK or Terraform stated for production |

## Known Notes

- `s3-l1` slide 7 and slide 8 narration was shortened after VOICEVOX repeatedly terminated on the longer text. The learning objective is unchanged.
- `build_slide_audio_video.py` now supports `--reuse-segments` to resume long video builds without discarding already validated segment MP4s.

## Final Decision

PASS. The expanded course has a coherent 6-lecture structure, Logs Insights demand is addressed, and all lectures have GPT-Image2-derived slides, VOICEVOX audio, and MP4 output.
