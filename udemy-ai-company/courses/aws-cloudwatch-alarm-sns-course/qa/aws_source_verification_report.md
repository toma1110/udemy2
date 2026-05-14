# AWS Source Verification Report

## Target

- Course: `aws-cloudwatch-alarm-sns-course`
- Video candidate: `VID-002`
- Topic: CloudWatch Alarm + SNS notification with CloudFormation
- Verification date: 2026-05-14

## Ownership

- Owner AI: AI-Engineer-01
- Reviewer AI: AI-QA-01
- Worker != Reviewer: OK

## AWS References Checked

| Area | Source | Result |
| --- | --- | --- |
| CloudWatch Alarm CloudFormation resource | AWS::CloudWatch::Alarm Template Reference | PASS |
| SNS Topic CloudFormation resource | AWS::SNS::Topic Template Reference | PASS |
| SNS Subscription CloudFormation resource | AWS::SNS::Subscription Template Reference | PASS |
| CloudWatch Alarm to encrypted SNS topic caveat | AWS re:Post Knowledge Center | PASS |
| CloudWatch Alarm SNS notification troubleshooting | AWS re:Post Knowledge Center | PASS |

## Confirmed Facts

- `AWS::CloudWatch::Alarm` creates an alarm for a metric or metric math expression.
- A new alarm can start in `INSUFFICIENT_DATA` before CloudWatch evaluates it.
- `AlarmActions` accepts action ARNs and is used when an alarm transitions into `ALARM`.
- `AWS::SNS::Topic` creates a publishable SNS topic.
- `AWS::SNS::Subscription` subscribes an endpoint to a topic, and endpoint owner confirmation is required for email.
- If SNS access policy restricts publishing, CloudWatch must be allowed to publish to the SNS topic.
- If an SNS topic is encrypted with the AWS managed key `alias/aws/sns`, CloudWatch alarm actions can fail because CloudWatch cannot use that key policy.
- A production encrypted SNS design should use a customer managed KMS key with CloudWatch permissions. This is out of scope for the beginner hands-on.

## Course Design Implications

- The beginner template will use SNS Topic, Subscription, Topic Policy, and CloudWatch Alarm.
- Email confirmation is a required human step in the README and video.
- The template will include a Topic Policy allowing `cloudwatch.amazonaws.com` to publish.
- The beginner hands-on will avoid SNS KMS encryption to keep setup reproducible without custom KMS key policy work.
- Production notes will explain that encrypted SNS topics need a customer managed key and explicit permissions.
- Alarm notification testing will use SNS publish as the basic no-metric path, and AWS CLI `set-alarm-state` as an optional AlarmActions test.

## References

- https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-alarm.html
- https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sns-topic.html
- https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sns-subscription.html
- https://repost.aws/knowledge-center/cloudwatch-configure-alarm-sns
- https://repost.aws/knowledge-center/cloudwatch-receive-sns-for-alarm-trigger

## Approval

Status: Ready for CloudFormation template draft

Approved By: AI-QA-01
