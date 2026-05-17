# AWS Source Verification Report

Task ID: TASK-0195
Course: `aws-alert-design-practical-course`
Reviewer AI: AI-QA-01
Status: Draft source baseline
Checked date: 2026-05-16

## Sources Checked

| Topic | Source | Course Usage |
| --- | --- | --- |
| CloudWatch alarm states and evaluation | Amazon CloudWatch User Guide: Alarm evaluation | Explain OK, ALARM, INSUFFICIENT_DATA, Period, Evaluation Periods, Datapoints to Alarm, M out of N |
| Missing data treatment | Amazon CloudWatch User Guide: Configuring how CloudWatch alarms treat missing data | Explain why missing data handling depends on metric type |
| Recommended alarms | Amazon CloudWatch User Guide: Recommended alarms | Explain that thresholds and evaluation settings should be tuned to workload and acceptable error rates |
| Composite alarms | AWS Cloud Operations Blog: Improve monitoring efficiency using Amazon CloudWatch Composite Alarms | Explain combining alarms to reduce alert fatigue and improve triage |

## Course Design Implications

- The course should teach alarm quality as an operational decision, not only a CloudWatch setting.
- M out of N should be shown as a way to reduce one-off metric spikes and alert noise.
- Missing data must not be taught as a universal fixed setting; the correct choice depends on whether a metric reports continuously or only on events/errors.
- Composite Alarm should be positioned as a way to combine signals and reduce alert storms, not as a replacement for good ownership and runbooks.
- Recommended thresholds from AWS documentation are starting points; learners must tune thresholds to their workload and acceptable error rates.
- Standard course production does not require AWS resource creation.

## Required Follow-up Before Publishing

- Re-check current CloudWatch console labels before recording any console footage.
- If adding real AWS examples, create a separate CEO approval gate before CloudWatch Alarm, SNS, Composite Alarm, or CloudFormation execution.
- Verify that the final script does not imply a single threshold fits every workload.

## References

- https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-evaluation.html
- https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarms-and-missing-data.html
- https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.html
- https://aws.amazon.com/blogs/mt/improve-monitoring-efficiency-using-amazon-cloudwatch-composite-alarms-2/
