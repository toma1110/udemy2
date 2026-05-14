# S4 Feedback Remediation Report

## Target

- GitHub Issue: #91
- Trigger: CEO comments on Issue #90
- Date: 2026-05-11

## Result

Pass. Corrected videos uploaded and ready for CEO spot check.

## Changes

- S4-L1:
  - Narration readings changed to `時系列=じけいれつ`, `1分=いっぷん`.
  - `Application Signals` narration changed to `アプリケーションシグナルズ`.
  - Slide 2 regenerated so ALB metric dimensions no longer imply `Operation`.
- S4-L2:
  - `Application Signals` narration changed to `アプリケーションシグナルズ`.
- S4-L3:
  - Slide 6 title changed from `Availability SLOでの使い分け` to `Availability SLOは成功条件を決める`.
  - Narration readings changed to `1分=いっぷん`, `時間帯=じかんたい`.
  - Slide 8 next label changed to `次: SLO推奨値`.
- S4-L4:
  - Lecture wording changed from `SLO Recommendations` to `SLO推奨値`.
  - Explained as an Application Signals/SLO recommendation capability, not a standalone AWS service.
  - Slide 8 next label changed to `次: SLOハンズオン`.

## Final Drive URLs

| Lecture | Drive URL | Size |
| --- | --- | --- |
| S4-L1 | https://drive.google.com/file/d/1XXBODEV-A9dT5V1JVQQad8CoYiiImFHZ/view?usp=drivesdk | 5,726,060 bytes |
| S4-L2 | https://drive.google.com/file/d/1GY-DoU_Slpi-cEsSzsJrSkyzcbL4JsOe/view?usp=drivesdk | 5,330,892 bytes |
| S4-L3 | https://drive.google.com/file/d/1fA534-pnoeb2CCKxkc-xF1CoihnoFHep/view?usp=drivesdk | 5,466,613 bytes |
| S4-L4 | https://drive.google.com/file/d/1Zvs4Y4hYGDZdg9MUZ6t8cuN2Vwl7EM7Y/view?usp=drivesdk | 5,379,823 bytes |

## Quality Gate

- Change request flow followed: Issue #91
- AWS official docs checked for ALB CloudWatch metrics and CloudWatch SLO/Application Signals
- Scripts updated and converted to JSON
- Narration checker: OK
- GPT-Image2 affected slides regenerated and source evidence saved
- Contact sheets visually checked
- VOICEVOX affected audio regenerated
- MP4 rebuild: faststart true and decode check OK
- Frame check generated
- Drive upload complete
- Drive metadata: `trashed=false`
- Sharing: anyone reader true

## Sources

- https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-cloudwatch-metrics.html
- https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html

