#!/usr/bin/env bash
set -euo pipefail

STACK_NAME="${STACK_NAME:-sample-aws-sre-dev-monitoring}"
AWS_REGION="${AWS_REGION:-us-east-1}"

log() {
  printf '[%s] %s\n' "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" "$*"
}

require_aws() {
  if ! command -v aws >/dev/null 2>&1; then
    echo "aws CLIが見つかりません。AWS CLI v2をインストールしてください。" >&2
    exit 1
  fi
}

stack_output() {
  local key="$1"
  aws cloudformation describe-stacks \
    --stack-name "$STACK_NAME" \
    --region "$AWS_REGION" \
    --query "Stacks[0].Outputs[?OutputKey=='${key}'].OutputValue | [0]" \
    --output text
}

assert_not_empty() {
  local name="$1"
  local value="$2"

  if [[ -z "$value" || "$value" == "None" ]]; then
    echo "必要なOutputが見つかりません: ${name}" >&2
    exit 1
  fi
}

assert_equals() {
  local expected="$1"
  local actual="$2"
  local message="$3"

  if [[ "$actual" != "$expected" ]]; then
    echo "${message}: expected=${expected}, actual=${actual}" >&2
    exit 1
  fi
}

require_aws

log "CloudFormation Outputsを取得します: ${STACK_NAME}"
ALARM_NAME="$(stack_output SampleAlarmName)"
TOPIC_ARN="$(stack_output AlarmTopicArn)"
DASHBOARD_NAME="$(stack_output DashboardName)"

assert_not_empty "SampleAlarmName" "$ALARM_NAME"
assert_not_empty "AlarmTopicArn" "$TOPIC_ARN"
assert_not_empty "DashboardName" "$DASHBOARD_NAME"

log "CloudWatch Alarmの存在を確認します: ${ALARM_NAME}"
FOUND_ALARM="$(aws cloudwatch describe-alarms \
  --alarm-names "$ALARM_NAME" \
  --region "$AWS_REGION" \
  --query "MetricAlarms[0].AlarmName" \
  --output text)"
assert_equals "$ALARM_NAME" "$FOUND_ALARM" "CloudWatch Alarmが見つかりません"

log "SNS Topicの存在を確認します: ${TOPIC_ARN}"
FOUND_TOPIC="$(aws sns get-topic-attributes \
  --topic-arn "$TOPIC_ARN" \
  --region "$AWS_REGION" \
  --query "Attributes.TopicArn" \
  --output text)"
assert_equals "$TOPIC_ARN" "$FOUND_TOPIC" "SNS Topicが見つかりません"

log "CloudWatch Dashboardの存在を確認します: ${DASHBOARD_NAME}"
FOUND_DASHBOARD="$(aws cloudwatch get-dashboard \
  --dashboard-name "$DASHBOARD_NAME" \
  --region "$AWS_REGION" \
  --query "DashboardName" \
  --output text)"
assert_equals "$DASHBOARD_NAME" "$FOUND_DASHBOARD" "CloudWatch Dashboardが見つかりません"

log "smoke testが成功しました"
