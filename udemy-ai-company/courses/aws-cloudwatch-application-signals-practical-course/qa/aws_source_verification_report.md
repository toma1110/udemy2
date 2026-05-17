# AWS Source Verification Report

## Target

- Course: `aws-cloudwatch-application-signals-practical-course`
- Topic: CloudWatch Application Signals for Lambda, Application Signals SLO, CloudFormation
- Date: 2026-05-16
- Owner AI: AI-Strategy-01 / AI-Engineer-01
- Reviewer AI: AI-QA-01

## Sources Checked

| Source | URL | Course Use |
| --- | --- | --- |
| CloudWatch Application Signals overview | https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html | Services, Application Map, metrics, traces, cost caution |
| Enable Application Signals on Lambda | https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable-LambdaMain.html | Lambda layer, ADOT, execution role policy, environment variables |
| Lambda console Application Signals help | https://docs.aws.amazon.com/help-panel/lambda/latest/console/configuration-appsignals.html | `AWS_LAMBDA_EXEC_WRAPPER=/opt/otel-instrument`, role policy, service discovery setup |
| Application Signals CLI examples | https://docs.aws.amazon.com/cli/latest/userguide/cli_application-signals_code_examples.html | `get-service`, `list-services`, SLO CLI confirmation examples |
| `AWS::ApplicationSignals::Discovery` | https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-applicationsignals-discovery.html | CloudFormation account discovery resource |
| `AWS::ApplicationSignals::ServiceLevelObjective` | https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-applicationsignals-servicelevelobjective.md | SLO resource design and creation constraints |
| Service level objectives | https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html | SLO concepts, latency, availability, error budget, burn rate |
| Application Signals SLO capabilities announcement | https://aws.amazon.com/about-aws/whats-new/2026/03/cloudwatch-application-signals-adds-slo-capabilities/ | Recommendations, Service-Level SLO, Performance Report positioning |
| Amazon CloudWatch pricing | https://aws.amazon.com/cloudwatch/pricing/ | Pricing caution for Application Signals and SLO |
| ADOT Lambda layer ARNs | https://aws-otel.github.io/docs/getting-started/lambda/ | Region-specific Lambda layer ARN mapping |

## Verified Course Decisions

| Decision | Verification |
| --- | --- |
| Lambda-first MVP is appropriate | AWS docs support Application Signals for Lambda through ADOT Lambda Layer and console/manual/CDK methods. |
| Lambda functions require Application Signals instrumentation settings | AWS docs identify the Lambda OpenTelemetry layer, `AWS_LAMBDA_EXEC_WRAPPER=/opt/otel-instrument`, and `CloudWatchLambdaApplicationSignalsExecutionRolePolicy`. |
| Discovery is included in CloudFormation | `AWS::ApplicationSignals::Discovery` is documented as the CloudFormation resource for Application Signals discovery setup. |
| SLO creation is delayed until after metrics arrive | AWS CloudFormation docs state that an SLO for an Application Signals service operation cannot be created until that operation has reported standard metrics. |
| Request-based availability SLO is a suitable first SLO | Application Signals docs identify availability and latency as standard application metrics and explain request-based SLOs. |
| SLO Recommendations and Performance Report should not be a short hands-on completion condition | AWS announcement and SLO docs position these as data-driven capabilities. The course treats them as operational features requiring enough real metrics. |
| Low-frequency traffic and cleanup are mandatory | Pricing docs show Application Signals and SLO can incur charges. Course design includes stop traffic, stack delete, and cost confirmation. |
| Function URL is not required for MVP | Lambda Invoke between two functions avoids public HTTP exposure while still giving a simple service interaction for the learning lab. |

## Constraints for Course Content

- Do not promise that Application Signals is free.
- Do not present SLO Recommendations as guaranteed to work in a short hands-on window.
- Do not create or delete AWS resources in production work without CEO approval.
- Explain that Application Signals console data can take several minutes to appear.
- Explain that service-linked roles or historical telemetry may remain visible after stack deletion.
- If AWS updates Lambda layer ARNs, verify the ADOT layer mapping before publishing.

## Result

Status: PASS for planning and template validation sources.

Full AWS lifecycle QA remains pending until CEO-approved stack create/update/smoke/delete validation is performed.

## 2026-05-17 Runtime Remediation Source Recheck

| Source | URL | Course Use |
| --- | --- | --- |
| Monitor the operational health of your applications with Application Signals | https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Services.html | Services, Service detail, Application Map, SLIs, delayed discovery/evaluation notes |
| Application Signals SLO capabilities announcement | https://aws.amazon.com/about-aws/whats-new/2026/03/cloudwatch-application-signals-adds-slo-capabilities/ | SLO Recommendations, Service-Level SLO, SLO Performance Report, 30-day metrics premise |
| Application Performance Monitoring of AWS Lambda apps with Application Signals | https://aws.amazon.com/blogs/mt/announcing-amazon-cloudwatch-application-signals-support-for-lambda/ | Lambda Application Signals support and automatic instrumentation positioning |
| Application map generally available announcement | https://aws.amazon.com/about-aws/whats-new/2025/10/application-map-generally-available-amazon-cloudwatch/ | Application Map dependency and topology positioning |

Result: PASS for narration/runtime remediation wording. No AWS API or CloudFormation lifecycle action was executed during video production.
