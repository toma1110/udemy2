#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE_FILE="${TEMPLATE_FILE:-${SCRIPT_DIR}/template.yaml}"
STACK_NAME="${STACK_NAME:-aws-slo-adoption-dev-slo}"
AWS_REGION="${AWS_REGION:-us-east-1}"
PROJECT_NAME="${PROJECT_NAME:-udemy-slo-sample}"
NOTIFICATION_EMAIL="${NOTIFICATION_EMAIL:-}"
DASHBOARD_TITLE="${DASHBOARD_TITLE:-SLO Adoption Dashboard}"
ENABLE_APPLICATION_SIGNALS_SLO="${ENABLE_APPLICATION_SIGNALS_SLO:-false}"
ACTION="${1:-validate}"

log() {
  printf '[%s] %s\n' "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" "$*"
}

require_aws() {
  if ! command -v aws >/dev/null 2>&1; then
    echo "aws CLIが見つかりません。AWS CLI v2をインストールしてください。" >&2
    exit 1
  fi
}

stack_exists() {
  aws cloudformation describe-stacks \
    --stack-name "$STACK_NAME" \
    --region "$AWS_REGION" \
    >/dev/null 2>&1
}

validate_template() {
  log "CloudFormationテンプレートを検証します: ${TEMPLATE_FILE}"
  aws cloudformation validate-template \
    --template-body "file://${TEMPLATE_FILE}" \
    --region "$AWS_REGION" \
    >/dev/null
}

deploy_stack() {
  local mode="$1"

  log "CloudFormationスタックを${mode}します: ${STACK_NAME}"
  aws cloudformation deploy \
    --stack-name "$STACK_NAME" \
    --template-file "$TEMPLATE_FILE" \
    --region "$AWS_REGION" \
    --parameter-overrides \
      "ProjectName=${PROJECT_NAME}" \
      "NotificationEmail=${NOTIFICATION_EMAIL}" \
      "DashboardTitle=${DASHBOARD_TITLE}" \
      "EnableApplicationSignalsSlo=${ENABLE_APPLICATION_SIGNALS_SLO}" \
    --tags \
      "Course=aws-slo-adoption-course" \
      "ManagedBy=ai-company-v1" \
    --no-fail-on-empty-changeset
}

create_stack() {
  if stack_exists; then
    echo "スタックは既に存在します。更新する場合は './validate.sh update' を使ってください: ${STACK_NAME}" >&2
    exit 1
  fi

  deploy_stack "作成"
}

update_stack() {
  if ! stack_exists; then
    echo "スタックが存在しません。先に './validate.sh create' を実行してください: ${STACK_NAME}" >&2
    exit 1
  fi

  deploy_stack "更新"
}

put_metrics() {
  log "サンプルSLIメトリクスを投入します"
  aws cloudwatch put-metric-data \
    --namespace "UdemyAICompany/SLO" \
    --region "$AWS_REGION" \
    --metric-data \
      "MetricName=Availability,Dimensions=[{Name=ProjectName,Value=${PROJECT_NAME}},{Name=Service,Value=sample-api}],Value=99.9,Unit=Percent" \
      "MetricName=Latency,Dimensions=[{Name=ProjectName,Value=${PROJECT_NAME}},{Name=Service,Value=sample-api}],Value=120,Unit=Milliseconds"
}

smoke_test() {
  log "smoke testを実行します"
  STACK_NAME="$STACK_NAME" AWS_REGION="$AWS_REGION" ENABLE_APPLICATION_SIGNALS_SLO="$ENABLE_APPLICATION_SIGNALS_SLO" "${SCRIPT_DIR}/smoke_test.sh"
}

delete_stack() {
  if ! stack_exists; then
    log "スタックは存在しません。削除をスキップします: ${STACK_NAME}"
    return 0
  fi

  log "CloudFormationスタックを削除します: ${STACK_NAME}"
  aws cloudformation delete-stack \
    --stack-name "$STACK_NAME" \
    --region "$AWS_REGION"

  aws cloudformation wait stack-delete-complete \
    --stack-name "$STACK_NAME" \
    --region "$AWS_REGION"
}

full_validation() {
  if stack_exists; then
    echo "fullはcreate/update/deleteを含むため、既存スタックでは実行しません。別のSTACK_NAMEを指定してください: ${STACK_NAME}" >&2
    exit 1
  fi

  validate_template
  create_stack
  put_metrics
  smoke_test
  DASHBOARD_TITLE="${DASHBOARD_TITLE} Updated"
  update_stack
  smoke_test
  delete_stack
}

usage() {
  cat <<USAGE
Usage: $0 [validate|create|update|put-metrics|smoke|delete|full]

Environment variables:
  STACK_NAME                       Default: aws-slo-adoption-dev-slo
  AWS_REGION                       Default: us-east-1
  PROJECT_NAME                     Default: udemy-slo-sample
  NOTIFICATION_EMAIL               Default: empty
  DASHBOARD_TITLE                  Default: SLO Adoption Dashboard
  ENABLE_APPLICATION_SIGNALS_SLO   Default: false
  TEMPLATE_FILE                    Default: ./template.yaml
USAGE
}

require_aws

case "$ACTION" in
  validate)
    validate_template
    ;;
  create)
    validate_template
    create_stack
    ;;
  update)
    validate_template
    update_stack
    ;;
  put-metrics)
    put_metrics
    ;;
  smoke)
    smoke_test
    ;;
  delete)
    delete_stack
    ;;
  full)
    full_validation
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
