#!/usr/bin/env bash
set -euo pipefail

AWS_REGION="${AWS_REGION:-us-east-1}"
STACK_NAME="${STACK_NAME:-appsignals-demo-dev}"
PROJECT_NAME="${PROJECT_NAME:-appsignals-demo}"
CREATE_APPLICATION_SIGNALS_SLO="${CREATE_APPLICATION_SIGNALS_SLO:-false}"
STRICT_APPLICATION_SIGNALS="${STRICT_APPLICATION_SIGNALS:-false}"

require_command() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "Required command not found: $1" >&2
    exit 1
  fi
}

output_value() {
  local key="$1"
  aws cloudformation describe-stacks \
    --region "${AWS_REGION}" \
    --stack-name "${STACK_NAME}" \
    --query "Stacks[0].Outputs[?OutputKey=='${key}'].OutputValue | [0]" \
    --output text
}

require_command aws

sample_function="$(output_value SampleApiFunctionName)"
traffic_function="$(output_value TrafficGeneratorFunctionName)"
sample_log_group="$(output_value SampleApiLogGroupName)"
traffic_log_group="$(output_value TrafficGeneratorLogGroupName)"
schedule_name="$(output_value TrafficScheduleName)"
sample_service="${PROJECT_NAME}-sample-api"

echo "Checking CloudFormation stack: ${STACK_NAME}"
aws cloudformation describe-stacks \
  --region "${AWS_REGION}" \
  --stack-name "${STACK_NAME}" \
  --query "Stacks[0].StackStatus" \
  --output text

echo "Checking Lambda functions"
aws lambda get-function \
  --region "${AWS_REGION}" \
  --function-name "${sample_function}" >/dev/null
aws lambda get-function \
  --region "${AWS_REGION}" \
  --function-name "${traffic_function}" >/dev/null

echo "Checking Lambda Application Signals environment"
aws lambda get-function-configuration \
  --region "${AWS_REGION}" \
  --function-name "${sample_function}" \
  --query "Environment.Variables.AWS_LAMBDA_EXEC_WRAPPER" \
  --output text | grep -Fx "/opt/otel-instrument" >/dev/null
aws lambda get-function-configuration \
  --region "${AWS_REGION}" \
  --function-name "${sample_function}" \
  --query "Environment.Variables.OTEL_SERVICE_NAME" \
  --output text | grep -Fx "${sample_service}" >/dev/null

echo "Checking log groups"
aws logs describe-log-groups \
  --region "${AWS_REGION}" \
  --log-group-name-prefix "${sample_log_group}" \
  --query "logGroups[?logGroupName=='${sample_log_group}'].logGroupName | [0]" \
  --output text | grep -Fx "${sample_log_group}" >/dev/null
aws logs describe-log-groups \
  --region "${AWS_REGION}" \
  --log-group-name-prefix "${traffic_log_group}" \
  --query "logGroups[?logGroupName=='${traffic_log_group}'].logGroupName | [0]" \
  --output text | grep -Fx "${traffic_log_group}" >/dev/null

echo "Checking EventBridge Scheduler schedule"
aws scheduler get-schedule \
  --region "${AWS_REGION}" \
  --group-name "${PROJECT_NAME}-traffic" \
  --name "${schedule_name}" \
  --query "{Name:Name,State:State,ScheduleExpression:ScheduleExpression}" \
  --output table

echo "Invoking traffic generator once for smoke test"
aws lambda invoke \
  --region "${AWS_REGION}" \
  --function-name "${traffic_function}" \
  --payload '{"source":"smoke-test"}' \
  --cli-binary-format raw-in-base64-out \
  /tmp/appsignals-smoke-response.json >/dev/null
cat /tmp/appsignals-smoke-response.json
echo

if command -v date >/dev/null 2>&1 && date -u -d "15 minutes ago" +%s >/dev/null 2>&1; then
  start_time="$(date -u -d "15 minutes ago" +%s)"
  end_time="$(date -u +%s)"
  echo "Checking Application Signals service discovery"
  set +e
  service_output="$(aws application-signals get-service \
    --region "${AWS_REGION}" \
    --start-time "${start_time}" \
    --end-time "${end_time}" \
    --key-attributes Environment=lambda:default,Name="${sample_service}",Type=Service 2>&1)"
  service_status=$?
  set -e

  if [[ ${service_status} -eq 0 ]]; then
    echo "${service_output}"
  else
    echo "Application Signals service is not visible yet. It can take several minutes after traffic starts."
    echo "${service_output}"
    if [[ "${STRICT_APPLICATION_SIGNALS}" == "true" ]]; then
      exit "${service_status}"
    fi
  fi
else
  echo "Skipping Application Signals get-service time-window check because GNU date is unavailable."
fi

if [[ "${CREATE_APPLICATION_SIGNALS_SLO}" == "true" ]]; then
  slo_arn="$(output_value ApplicationSignalsSloArn)"
  echo "Checking Application Signals SLO: ${slo_arn}"
  aws application-signals get-service-level-objective \
    --region "${AWS_REGION}" \
    --id "${slo_arn}" \
    --query "Slo.{Name:Name,EvaluationType:EvaluationType}" \
    --output table
fi

echo "Smoke test completed."
