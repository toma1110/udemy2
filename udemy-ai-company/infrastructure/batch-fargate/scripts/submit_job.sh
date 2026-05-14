#!/usr/bin/env bash
set -euo pipefail

STACK_NAME="${STACK_NAME:-udemy-render-batch-dev}"
AWS_REGION="${AWS_REGION:-us-east-1}"
MANIFEST_S3_URI="${MANIFEST_S3_URI:?MANIFEST_S3_URIを指定してください。}"
JOB_NAME="${JOB_NAME:-udemy-render-$(date -u '+%Y%m%d%H%M%S')}"
TIMEOUT_SECONDS="${TIMEOUT_SECONDS:-3600}"

stack_output() {
  local key="$1"
  aws cloudformation describe-stacks \
    --stack-name "$STACK_NAME" \
    --region "$AWS_REGION" \
    --query "Stacks[0].Outputs[?OutputKey=='${key}'].OutputValue | [0]" \
    --output text
}

require_aws() {
  if ! command -v aws >/dev/null 2>&1; then
    echo "aws CLIが見つかりません。AWS CLI v2をインストールしてください。" >&2
    exit 1
  fi
}

require_aws

JOB_QUEUE="$(stack_output JobQueueName)"
JOB_DEFINITION="$(stack_output JobDefinitionArn)"

if [ -z "$JOB_QUEUE" ] || [ "$JOB_QUEUE" = "None" ]; then
  echo "JobQueueNameを取得できません。" >&2
  exit 1
fi

if [ -z "$JOB_DEFINITION" ] || [ "$JOB_DEFINITION" = "None" ]; then
  echo "JobDefinitionArnを取得できません。" >&2
  exit 1
fi

aws batch submit-job \
  --region "$AWS_REGION" \
  --job-name "$JOB_NAME" \
  --job-queue "$JOB_QUEUE" \
  --job-definition "$JOB_DEFINITION" \
  --parameters "manifest_s3_uri=${MANIFEST_S3_URI}" \
  --timeout "attemptDurationSeconds=${TIMEOUT_SECONDS}" \
  --tags "ManagedBy=ai-company-v1,Purpose=udemy-render-worker" \
  --query '{jobName:jobName,jobId:jobId}' \
  --output table
