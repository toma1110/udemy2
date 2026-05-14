#!/usr/bin/env bash
set -euo pipefail

STACK_NAME="${STACK_NAME:-udemy-render-batch-dev}"
AWS_REGION="${AWS_REGION:-us-east-1}"

log() {
  printf '[%s] %s\n' "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" "$*"
}

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

ARTIFACT_BUCKET="$(stack_output ArtifactBucketName)"
REPOSITORY_URI="$(stack_output RepositoryUri)"
VOICEVOX_REPOSITORY_URI="$(stack_output VoicevoxRepositoryUri)"
JOB_QUEUE="$(stack_output JobQueueName)"
JOB_DEFINITION="$(stack_output JobDefinitionArn)"
VOICEVOX_JOB_DEFINITION="$(stack_output VoicevoxJobDefinitionArn)"
LOG_GROUP="$(stack_output LogGroupName)"
VOICEVOX_LOG_GROUP="$(stack_output VoicevoxLogGroupName)"

log "S3 bucketを確認します: ${ARTIFACT_BUCKET}"
aws s3api head-bucket --bucket "$ARTIFACT_BUCKET" --region "$AWS_REGION"

REPOSITORY_NAME="${REPOSITORY_URI#*/}"
log "ECR repositoryを確認します: ${REPOSITORY_NAME}"
aws ecr describe-repositories \
  --repository-names "$REPOSITORY_NAME" \
  --region "$AWS_REGION" \
  >/dev/null

VOICEVOX_REPOSITORY_NAME="${VOICEVOX_REPOSITORY_URI#*/}"
log "VOICEVOX ECR repositoryを確認します: ${VOICEVOX_REPOSITORY_NAME}"
aws ecr describe-repositories \
  --repository-names "$VOICEVOX_REPOSITORY_NAME" \
  --region "$AWS_REGION" \
  >/dev/null

log "AWS Batch job queueを確認します: ${JOB_QUEUE}"
aws batch describe-job-queues \
  --job-queues "$JOB_QUEUE" \
  --region "$AWS_REGION" \
  --query 'jobQueues[0].[jobQueueName,state,status]' \
  --output table

log "AWS Batch job definitionを確認します: ${JOB_DEFINITION}"
aws batch describe-job-definitions \
  --job-definitions "$JOB_DEFINITION" \
  --region "$AWS_REGION" \
  --query 'jobDefinitions[0].[jobDefinitionName,status,type,platformCapabilities]' \
  --output table

log "AWS Batch VOICEVOX job definitionを確認します: ${VOICEVOX_JOB_DEFINITION}"
aws batch describe-job-definitions \
  --job-definitions "$VOICEVOX_JOB_DEFINITION" \
  --region "$AWS_REGION" \
  --query 'jobDefinitions[0].[jobDefinitionName,status,type,platformCapabilities]' \
  --output table

log "CloudWatch log groupを確認します: ${LOG_GROUP}"
aws logs describe-log-groups \
  --log-group-name-prefix "$LOG_GROUP" \
  --region "$AWS_REGION" \
  --query 'logGroups[0].[logGroupName,retentionInDays]' \
  --output table

log "VOICEVOX CloudWatch log groupを確認します: ${VOICEVOX_LOG_GROUP}"
aws logs describe-log-groups \
  --log-group-name-prefix "$VOICEVOX_LOG_GROUP" \
  --region "$AWS_REGION" \
  --query 'logGroups[0].[logGroupName,retentionInDays]' \
  --output table

log "smoke test完了"
