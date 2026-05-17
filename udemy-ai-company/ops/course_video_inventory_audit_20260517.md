# Existing Course Video Inventory Audit

Audit date: 2026-05-17

## Basis

Udemy's current course quality checklist requires standard marketplace courses to have:

- 30 minutes or more of video content
- 5 or more separate lectures

Source: https://support.udemy.com/hc/ja/articles/229604988-Udemy%E3%82%B3%E3%83%BC%E3%82%B9%E5%93%81%E8%B3%AA%E3%83%81%E3%82%A7%E3%83%83%E3%82%AF%E3%83%AA%E3%82%B9%E3%83%88

## Method

- Counted lecture IDs in `course_spec.md` using `sN-lN` patterns.
- Counted normal lecture MP4s under `video/<lecture_id>/<lecture_id>.mp4` or equivalent lecture folders.
- Excluded promo videos.
- Excluded segment files under `segments/`.
- Measured MP4 duration with `ffprobe`.
- Compared each publish candidate against 5 lectures and 30 minutes of video content.

## Summary

| Course | Spec Lectures | Lecture MP4s | Video Minutes | Status | Follow-up |
| --- | ---: | ---: | ---: | --- | --- |
| `aws-cloudwatch-logs-insights-practical-course` | 8 | 8 | 11.7 | NG: duration below 30 min | `TASK-0213` / #187 |
| `aws-cloudwatch-intro-course` | 6 | 6 | 12.3 | NG: duration below 30 min | `TASK-0214` / #188 |
| `aws-cloudwatch-alarm-sns-course` | 6 | 6 | 13.3 | NG: duration below 30 min | `TASK-0215` / #189 |
| `aws-cloudwatch-application-signals-practical-course` | 11 | 11 | 13.2 | NG: duration below 30 min | `TASK-0216` / #190 |
| `aws-alert-design-practical-course` | 6 | 1 | 3.1 | NG: missing videos and duration below 30 min | `TASK-0217` / #191 |
| `aws-runbook-first-response-course` | 6 | 1 | 2.8 | NG: missing videos and duration below 30 min | `TASK-0218` / #192 |
| `aws-cost-safety-course` | 12 | 0 | 0.0 | NG: lecture videos not produced | `TASK-0219` / #193 |
| `aws-cloudformation-rollback-troubleshooting-course` | 1 | 0 | 0.0 | Already covered by full-course generation ticket | `TASK-0207` |
| `aws-iam-accessdenied-troubleshooting-course` | 1 | 0 | 0.0 | Already covered by full-course generation ticket | `TASK-0208` |
| `aws-lambda-error-rate-monitoring-course` | 1 | 0 | 0.0 | Already covered by full-course generation ticket | `TASK-0209` |
| `aws-github-actions-oidc-course` | 1 | 0 | 0.0 | Already covered by full-course generation ticket | `TASK-0210` |
| `aws-sli-slo-metrics-intro-course` | 1 | 0 | 0.0 | Already covered by full-course generation ticket | `TASK-0211` |
| `aws-slo-adoption-course` | not machine-counted from spec | 35 | 86.5 | OK by video inventory | none |
| `sample-aws-sre-course` | 0 | 0 | 0.0 | Sample only, not publish candidate | none |

## Logs Insights Detail

`aws-cloudwatch-logs-insights-practical-course` has enough lecture count, but each lecture is too short for the course to reach 30 minutes.

| Lecture | Duration |
| --- | ---: |
| `s1-l1` | 1.51 min |
| `s1-l2` | 1.42 min |
| `s1-l3` | 1.46 min |
| `s2-l1` | 1.46 min |
| `s2-l2` | 1.47 min |
| `s2-l3` | 1.43 min |
| `s3-l1` | 1.45 min |
| `s3-l2` | 1.46 min |
| Total | 11.7 min |

## Remediation Policy

- Do not treat promo videos as lecture minutes.
- For each NG course, update `course_spec.md` and `course_infomation.md` first.
- CEO must review and approve `course_spec.md` and `course_infomation.md` before any script, GPT-Image2 slide, VOICEVOX audio, or MP4 regeneration starts.
- After CEO approval, all lecture videos for a selected course may be regenerated in one batch.
- Do not run AWS, CloudFormation, IAM, Logs Insights, or Google Drive mutations as part of remediation unless a separate ticket and CEO approval exist.

## Recommended Priority

1. `TASK-0213`: Logs Insights runtime remediation, because the course already has 8 lecture videos and is closest to publishable.
2. `TASK-0214` and `TASK-0215`: CloudWatch intro and Alarm/SNS runtime remediation, because they already have 6 lecture videos each.
3. `TASK-0216`: Application Signals runtime remediation, because it has many short lectures but likely needs deeper restructuring.
4. `TASK-0217`, `TASK-0218`, `TASK-0219`: finish missing lecture videos for partially produced or promo-only courses.
