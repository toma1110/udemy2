# AWS Source Verification Report

## Target

- Course: `aws-cloudwatch-logs-insights-practical-course`
- Topic: CloudWatch Logs Insights
- Date: 2026-05-15
- Owner AI: AI-Strategy-01
- Reviewer AI: AI-QA-01

## Sources Checked

| Source | URL | Course Use |
| --- | --- | --- |
| CloudWatch Logs Insights query syntax | https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html | Commands, cost-safety guidance, pipe-based query structure |
| Sample queries | https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-examples.html | General, Lambda, API Gateway, CloudTrail query patterns |
| Supported logs and discovered fields | https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData-discoverable-fields.html | `@timestamp`, `@message`, `@logStream`, `@log`, Lambda fields |
| SOURCE command | https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Source.html | CLI/API log group selection, name prefix, account, class, tag-based selection |
| join command | https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Join.html | Multi-log-group correlation by requestId/transactionId |
| subqueries | https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Subqueries.html | Nested query read-through and limitations |
| pattern command | https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Pattern.html | Log pattern clustering |
| anomaly command | https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Anomaly.html | ML-based unusual pattern detection |

## Verified Course Decisions

| Decision | Verification |
| --- | --- |
| Cost-safety is a first-class lesson | AWS docs recommend selecting only necessary log groups, using narrow time ranges, canceling queries, and avoiding high-frequency dashboard refreshes. |
| Basic query commands are in scope | `fields`, `filter`, `sort`, `limit`, `stats`, `parse`, and `dedup` are Logs Insights QL commands. |
| System fields are valid teaching material | Logs Insights generates fields such as `@timestamp`, `@message`, `@ingestionTime`, `@logStream`, and `@log`. |
| Lambda examples are valid | AWS sample queries include Lambda REPORT log examples using `@type`, `@duration`, `@requestId`, `@memorySize`, and `@maxMemoryUsed`. |
| `SOURCE` is CLI/API-oriented | AWS docs state `SOURCE` is not supported in the CloudWatch console and is used through CLI/API queries. |
| tag-based log group selection is current | `SOURCE logGroupTags(...)` is documented for selecting log groups by tags. |
| `JOIN` and subqueries are valid advanced topics | AWS docs include dedicated command pages with behavior and limitations. |
| `pattern` and `anomaly` are valid advanced topics | AWS docs describe pattern clustering and anomaly detection for log analysis. |

## Constraints for Course Content

- Queries must be framed as examples that may require field-name adaptation.
- Advanced queries can scan more data and must be taught with a short time range.
- `SOURCE` examples must be labeled as CLI/API, not console.
- New AWS log groups or sample log ingestion are not part of the standard hands-on path.

## Result

Status: PASS
