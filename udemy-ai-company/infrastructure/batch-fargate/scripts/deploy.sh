#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INFRA_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
TEMPLATE_FILE="${TEMPLATE_FILE:-${INFRA_DIR}/template.yaml}"
STACK_NAME="${STACK_NAME:-udemy-render-batch-dev}"
AWS_REGION="${AWS_REGION:-us-east-1}"
PROJECT_NAME="${PROJECT_NAME:-udemy-render}"
ARTIFACT_BUCKET_NAME="${ARTIFACT_BUCKET_NAME:-}"
JOB_SIZE="${JOB_SIZE:-vcpu4-memory8gb}"
MAX_VCPUS="${MAX_VCPUS:-8}"
EPHEMERAL_STORAGE_GIB="${EPHEMERAL_STORAGE_GIB:-50}"
LOG_RETENTION_DAYS="${LOG_RETENTION_DAYS:-14}"
JOB_TIMEOUT_SECONDS="${JOB_TIMEOUT_SECONDS:-3600}"
ACTION="${1:-deploy}"

log() {
  printf '[%s] %s\n' "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" "$*"
}

require_aws() {
  if ! command -v aws >/dev/null 2>&1; then
    echo "aws CLIが見つかりません。AWS CLI v2をインストールしてください。" >&2
    exit 1
  fi
}

validate_template() {
  log "CloudFormationテンプレートを検証します: ${TEMPLATE_FILE}"
  aws cloudformation validate-template \
    --template-body "file://${TEMPLATE_FILE}" \
    --region "$AWS_REGION" \
    >/dev/null
}

deploy_stack() {
  validate_template
  log "CloudFormationスタックを作成/更新します: ${STACK_NAME}"
  aws cloudformation deploy \
    --stack-name "$STACK_NAME" \
    --template-file "$TEMPLATE_FILE" \
    --region "$AWS_REGION" \
    --capabilities CAPABILITY_NAMED_IAM \
    --parameter-overrides \
      "ProjectName=${PROJECT_NAME}" \
      "ArtifactBucketName=${ARTIFACT_BUCKET_NAME}" \
      "JobSize=${JOB_SIZE}" \
      "MaxvCpus=${MAX_VCPUS}" \
      "EphemeralStorageGiB=${EPHEMERAL_STORAGE_GIB}" \
      "LogRetentionDays=${LOG_RETENTION_DAYS}" \
      "JobTimeoutSeconds=${JOB_TIMEOUT_SECONDS}" \
    --tags \
      "ManagedBy=ai-company-v1" \
      "Purpose=udemy-render-worker" \
    --no-fail-on-empty-changeset
}

delete_stack() {
  log "CloudFormationスタックを削除します: ${STACK_NAME}"
  aws cloudformation delete-stack \
    --stack-name "$STACK_NAME" \
    --region "$AWS_REGION"

  aws cloudformation wait stack-delete-complete \
    --stack-name "$STACK_NAME" \
    --region "$AWS_REGION"
}

show_outputs() {
  aws cloudformation describe-stacks \
    --stack-name "$STACK_NAME" \
    --region "$AWS_REGION" \
    --query 'Stacks[0].Outputs[*].[OutputKey,OutputValue]' \
    --output table
}

usage() {
  cat <<USAGE
Usage: $0 [validate|deploy|outputs|delete]

Environment variables:
  STACK_NAME              Default: udemy-render-batch-dev
  AWS_REGION              Default: us-east-1
  PROJECT_NAME            Default: udemy-render
  ARTIFACT_BUCKET_NAME    Default: empty, CloudFormation generated
  JOB_SIZE                Default: vcpu4-memory8gb
  MAX_VCPUS               Default: 8
  EPHEMERAL_STORAGE_GIB   Default: 50
  LOG_RETENTION_DAYS      Default: 14
  JOB_TIMEOUT_SECONDS     Default: 3600
USAGE
}

require_aws

case "$ACTION" in
  validate)
    validate_template
    ;;
  deploy)
    deploy_stack
    show_outputs
    ;;
  outputs)
    show_outputs
    ;;
  delete)
    delete_stack
    ;;
  -h|--help|help)
    usage
    ;;
  *)
    usage >&2
    exit 1
    ;;
esac

log "完了しました: ${ACTION}"
