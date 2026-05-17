#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE_FILE="${SCRIPT_DIR}/template.yaml"

AWS_REGION="${AWS_REGION:-us-east-1}"
STACK_NAME="${STACK_NAME:-appsignals-demo-dev}"
PROJECT_NAME="${PROJECT_NAME:-appsignals-demo}"
TRAFFIC_ENABLED="${TRAFFIC_ENABLED:-true}"
TRAFFIC_SCHEDULE_EXPRESSION="${TRAFFIC_SCHEDULE_EXPRESSION:-rate(1 minute)}"
SCENARIO="${SCENARIO:-normal}"
REQUEST_COUNT_PER_RUN="${REQUEST_COUNT_PER_RUN:-1}"
SLOW_DELAY_MS="${SLOW_DELAY_MS:-1200}"
ERROR_RATE_PERCENT="${ERROR_RATE_PERCENT:-100}"
CREATE_APPLICATION_SIGNALS_SLO="${CREATE_APPLICATION_SIGNALS_SLO:-false}"
AVAILABILITY_SLO_TARGET="${AVAILABILITY_SLO_TARGET:-95}"

usage() {
  cat <<'USAGE'
Usage: ./validate.sh <command>

Commands:
  validate      Validate the CloudFormation template only.
  create        Create the stack. This creates billable AWS resources.
  update        Update stack parameters, scenario, traffic state, or SLO flag.
  smoke         Run smoke_test.sh against the current stack.
  stop-traffic  Disable scheduled traffic by updating the stack.
  delete        Delete the stack. This removes most billable resources.
  full          Full lifecycle. Requires CONFIRM_FULL_LIFECYCLE=yes.

Common environment variables:
  AWS_REGION=us-east-1
  STACK_NAME=appsignals-demo-dev
  PROJECT_NAME=appsignals-demo
  TRAFFIC_ENABLED=true|false
  TRAFFIC_SCHEDULE_EXPRESSION='rate(1 minute)'
  SCENARIO=normal|slow|error|recovery
  REQUEST_COUNT_PER_RUN=1
  ERROR_RATE_PERCENT=100
  CREATE_APPLICATION_SIGNALS_SLO=false|true

Notes:
  - create/update/delete/full can affect AWS cost.
  - Keep traffic low frequency and delete the stack after the hands-on.
  - Set CREATE_APPLICATION_SIGNALS_SLO=true only after the sample service has
    reported Application Signals metrics.
USAGE
}

PARAMETERS=()

build_parameters() {
  PARAMETERS=(
    "ParameterKey=ProjectName,ParameterValue=${PROJECT_NAME}" \
    "ParameterKey=TrafficEnabled,ParameterValue=${TRAFFIC_ENABLED}" \
    "ParameterKey=TrafficScheduleExpression,ParameterValue=${TRAFFIC_SCHEDULE_EXPRESSION}" \
    "ParameterKey=Scenario,ParameterValue=${SCENARIO}" \
    "ParameterKey=RequestCountPerRun,ParameterValue=${REQUEST_COUNT_PER_RUN}" \
    "ParameterKey=SlowDelayMs,ParameterValue=${SLOW_DELAY_MS}" \
    "ParameterKey=ErrorRatePercent,ParameterValue=${ERROR_RATE_PERCENT}" \
    "ParameterKey=CreateApplicationSignalsSlo,ParameterValue=${CREATE_APPLICATION_SIGNALS_SLO}" \
    "ParameterKey=AvailabilitySloTarget,ParameterValue=${AVAILABILITY_SLO_TARGET}"
  )
}

stack_exists() {
  aws cloudformation describe-stacks \
    --region "${AWS_REGION}" \
    --stack-name "${STACK_NAME}" >/dev/null 2>&1
}

validate_template() {
  aws cloudformation validate-template \
    --region "${AWS_REGION}" \
    --template-body "file://${TEMPLATE_FILE}" >/dev/null
  echo "Template validation succeeded: ${TEMPLATE_FILE}"
}

create_stack() {
  echo "Creating stack ${STACK_NAME} in ${AWS_REGION}"
  build_parameters
  aws cloudformation create-stack \
    --region "${AWS_REGION}" \
    --stack-name "${STACK_NAME}" \
    --template-body "file://${TEMPLATE_FILE}" \
    --capabilities CAPABILITY_IAM \
    --parameters "${PARAMETERS[@]}"

  aws cloudformation wait stack-create-complete \
    --region "${AWS_REGION}" \
    --stack-name "${STACK_NAME}"

  echo "Stack create completed: ${STACK_NAME}"
}

update_stack() {
  echo "Updating stack ${STACK_NAME} in ${AWS_REGION}"
  build_parameters
  set +e
  update_output="$(aws cloudformation update-stack \
    --region "${AWS_REGION}" \
    --stack-name "${STACK_NAME}" \
    --template-body "file://${TEMPLATE_FILE}" \
    --capabilities CAPABILITY_IAM \
    --parameters "${PARAMETERS[@]}" 2>&1)"
  update_status=$?
  set -e

  if [[ ${update_status} -ne 0 ]]; then
    if grep -q "No updates are to be performed" <<<"${update_output}"; then
      echo "No updates are to be performed."
      return 0
    fi
    echo "${update_output}" >&2
    return "${update_status}"
  fi

  aws cloudformation wait stack-update-complete \
    --region "${AWS_REGION}" \
    --stack-name "${STACK_NAME}"

  echo "Stack update completed: ${STACK_NAME}"
}

delete_stack() {
  echo "Deleting stack ${STACK_NAME} in ${AWS_REGION}"
  aws cloudformation delete-stack \
    --region "${AWS_REGION}" \
    --stack-name "${STACK_NAME}"

  aws cloudformation wait stack-delete-complete \
    --region "${AWS_REGION}" \
    --stack-name "${STACK_NAME}"

  echo "Stack delete completed: ${STACK_NAME}"
}

run_smoke() {
  AWS_REGION="${AWS_REGION}" \
  STACK_NAME="${STACK_NAME}" \
  PROJECT_NAME="${PROJECT_NAME}" \
  CREATE_APPLICATION_SIGNALS_SLO="${CREATE_APPLICATION_SIGNALS_SLO}" \
    "${SCRIPT_DIR}/smoke_test.sh"
}

stop_traffic() {
  TRAFFIC_ENABLED=false update_stack
}

full_lifecycle() {
  if [[ "${CONFIRM_FULL_LIFECYCLE:-}" != "yes" ]]; then
    echo "Set CONFIRM_FULL_LIFECYCLE=yes to run create/update/delete lifecycle." >&2
    return 2
  fi

  validate_template
  create_stack
  run_smoke
  SCENARIO=slow update_stack
  run_smoke
  ERROR_RATE_PERCENT=100 SCENARIO=error update_stack
  run_smoke
  TRAFFIC_ENABLED=false SCENARIO=recovery update_stack
  delete_stack
}

command="${1:-}"
case "${command}" in
  validate)
    validate_template
    ;;
  create)
    validate_template
    if stack_exists; then
      echo "Stack already exists: ${STACK_NAME}" >&2
      exit 1
    fi
    create_stack
    ;;
  update)
    validate_template
    update_stack
    ;;
  smoke)
    run_smoke
    ;;
  stop-traffic)
    validate_template
    stop_traffic
    ;;
  delete)
    delete_stack
    ;;
  full)
    full_lifecycle
    ;;
  ""|-h|--help|help)
    usage
    ;;
  *)
    usage >&2
    exit 2
    ;;
esac
