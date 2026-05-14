# Section 4 Completion Report

## Target

Section 4: AWSでSLOを計測する基礎

## Result

Pass. Ready for CEO spot check.

Section 4 was produced under TASK-0086 to TASK-0090 on 2026-05-11, then remediated under TASK-0091 based on CEO comments. Scripts, GPT-Image2 slides, VOICEVOX audio, MP4 builds, Google Drive upload, and Drive metadata verification are complete.

## Deliverables

| Lecture | Local MP4 | Drive URL | Duration | Size |
| --- | --- | --- | --- | --- |
| S4-L1 CloudWatch MetricsでSLIを表現する | `video/s4-l1/s4-l1.mp4` | https://drive.google.com/file/d/1XXBODEV-A9dT5V1JVQQad8CoYiiImFHZ/view?usp=drivesdk | 151.69s | 5,726,060 bytes |
| S4-L2 Application SignalsでLatencyとAvailabilityを見る | `video/s4-l2/s4-l2.mp4` | https://drive.google.com/file/d/1GY-DoU_Slpi-cEsSzsJrSkyzcbL4JsOe/view?usp=drivesdk | 142.68s | 5,330,892 bytes |
| S4-L3 period-based SLOとrequest-based SLO | `video/s4-l3/s4-l3.mp4` | https://drive.google.com/file/d/1fA534-pnoeb2CCKxkc-xF1CoihnoFHep/view?usp=drivesdk | 150.57s | 5,466,613 bytes |
| S4-L4 SLO推奨値の使いどころ | `video/s4-l4/s4-l4.mp4` | https://drive.google.com/file/d/1Zvs4Y4hYGDZdg9MUZ6t8cuN2Vwl7EM7Y/view?usp=drivesdk | 153.31s | 5,379,823 bytes |

## Quality Gate

- `course_spec.md` and `lectures.md` followed
- Ticket-driven workflow followed: TASK-0086 to TASK-0090
- Worker and Reviewer separated in ticket ownership
- AWS official sources checked for CloudWatch SLO, Application Signals, request-based SLO, and Recommendations
- Narration checker passed for all S4 scripts
- Scripts converted to JSON: 8 slides per lecture
- Slides generated with GPT-Image2: 8 PNG files per lecture
- GPT-Image2 source evidence saved: `slides/s4-gpt-image2-sources/s4-l*/`
- Contact sheets generated and visually checked for all 4 lectures
- VOICEVOX audio generated: 8 WAV files per lecture
- Videos created: H.264, 1920x1080, AAC mono 44100 Hz
- Faststart: true for all 4 MP4s
- ffmpeg decode check: OK for all 4 MP4s
- Google Drive upload: OK for all 4 MP4s
- Drive sharing: anyone reader true for all 4 MP4s
- Drive metadata: `trashed=false` for all 4 new files
- CEO feedback remediation: Done under TASK-0091
- Corrected readings: `時系列=じけいれつ`, `1分=いっぷん`, `時間帯=じかんたい`, `Application Signals=アプリケーションシグナルズ`
- ALB metric dimension slide corrected: no `Operation` dimension in ALB CloudWatch metric example
- SLO Recommendations wording corrected: described as Application Signals/SLO recommendation capability, not a standalone service
- Next labels corrected: S4-L3 `次: SLO推奨値`, S4-L4 `次: SLOハンズオン`

## Sources

- https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html
- https://aws.amazon.com/about-aws/whats-new/2026/03/cloudwatch-application-signals-adds-slo-capabilities/

## Next Gate

- TASK-0090 / Issue #90: CEO spot check and final Section 4 approval.

## Historical Uploads

The first S4 upload remains historical and should not be treated as the final CEO review target:

- S4-L1 old file ID: `1_cWJj1I1FrH7TCfChIYiJMunL1M4mLD3`
- S4-L2 old file ID: `1eFAuIVUnjxN2ETCWrWgk1IhmQ-ykOYHW`
- S4-L3 old file ID: `1JjZ2p8CdfZI6f5bsqsfgJvSCztdQ52Qq`
- S4-L4 old file ID: `1tV42xnI1l1qS1c34xromD_mVL8Y7gOPL`

