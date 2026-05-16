# AWS Source Verification Report

Task ID: TASK-0170
Course: `aws-cost-safety-course`
Reviewer AI: AI-QA-01
Status: Draft source baseline

## Sources Checked

| Topic | Source | Course Usage |
| --- | --- | --- |
| AWS Budgets | AWS Cost Management User Guide: Managing your costs with AWS Budgets | Monthly cost budget, actual/forecasted alerts, update delay caution |
| Cost Explorer | AWS Cost Management User Guide: Analyzing your costs and usage with AWS Cost Explorer | Service breakdown, trend analysis, forecast, API cost caution |
| Cost Anomaly Detection | AWS Cost Anomaly Detection product page | Monitor, alert subscription, ML-based anomaly detection, SNS/email alerts |
| CloudFormation Budgets | AWS CloudFormation Template Reference: AWS Billing and Cost Management Budgets | Optional `AWS::Budgets::Budget` scope |
| CloudFormation Cost Explorer | AWS CloudFormation Template Reference: AWS Cost Explorer | Optional `AWS::CE::AnomalyMonitor` and `AWS::CE::AnomalySubscription` scope |

## Course Design Implications

- Budgets and Cost Explorer are not real-time controls; the course must explain data refresh and alert delay.
- Budget alerts help learners notice spend; they do not automatically stop all billing.
- Cost Explorer API usage can incur request charges; the course should prefer console workflows for beginners.
- Cost Anomaly Detection reduces surprise bills but does not guarantee detection of every issue.
- CloudFormation should be optional for reproducible hands-on only.
- Budget Actions are intentionally out of scope for v1 because automatic guardrails can surprise beginners.

## Required Follow-up Before Publishing

- Re-check current pricing and feature wording immediately before final Udemy upload.
- Confirm console UI labels and navigation paths.
- If CloudFormation templates are added, run static validation first and only run stack create/update/delete after CEO approval.

## References

- https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html
- https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html
- https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/
- https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/AWS_Budgets.html
- https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/AWS_CE.html
