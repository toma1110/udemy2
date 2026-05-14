#!/usr/bin/env bash
set -euo pipefail

STACK_NAME=${1:-}

if [[ -z "${STACK_NAME}" ]]; then
  echo "Usage: $0 <stack-name>" >&2
  exit 1
fi

ALARM_NAME=$(aws cloudformation describe-stacks \
  --stack-name "${STACK_NAME}" \
  --query "Stacks[0].Outputs[?OutputKey=='AlarmName'].OutputValue" \
  --output text)

TOPIC_ARN=$(aws cloudformation describe-stacks \
  --stack-name "${STACK_NAME}" \
  --query "Stacks[0].Outputs[?OutputKey=='AlarmTopicArn'].OutputValue" \
  --output text)

aws cloudwatch describe-alarms \
  --alarm-names "${ALARM_NAME}" \
  --query "MetricAlarms[0].{AlarmName:AlarmName,ActionsEnabled:ActionsEnabled,AlarmActions:AlarmActions}" \
  --output table

aws sns get-topic-attributes \
  --topic-arn "${TOPIC_ARN}" \
  --query "Attributes.{TopicArn:TopicArn,Policy:Policy}" \
  --output table

aws sns list-subscriptions-by-topic \
  --topic-arn "${TOPIC_ARN}" \
  --query "Subscriptions[].{Protocol:Protocol,Endpoint:Endpoint,SubscriptionArn:SubscriptionArn}" \
  --output table

echo "Smoke test completed for ${STACK_NAME}"
