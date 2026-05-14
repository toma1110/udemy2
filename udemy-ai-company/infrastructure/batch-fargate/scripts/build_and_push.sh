#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INFRA_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
STACK_NAME="${STACK_NAME:-udemy-render-batch-dev}"
AWS_REGION="${AWS_REGION:-us-east-1}"
IMAGE_TAG="${IMAGE_TAG:-latest}"
PLATFORM="${PLATFORM:-linux/amd64}"

log() {
  printf '[%s] %s\n' "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" "$*"
}

require_command() {
  local name="$1"
  if ! command -v "$name" >/dev/null 2>&1; then
    echo "${name} が見つかりません。" >&2
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

require_command aws
require_command docker

REPOSITORY_URI="$(stack_output RepositoryUri)"
if [ -z "$REPOSITORY_URI" ] || [ "$REPOSITORY_URI" = "None" ]; then
  echo "RepositoryUriを取得できません。先にscripts/deploy.sh deployを実行してください。" >&2
  exit 1
fi

REGISTRY="${REPOSITORY_URI%/*}"
IMAGE_URI="${REPOSITORY_URI}:${IMAGE_TAG}"

log "ECRへログインします: ${REGISTRY}"
aws ecr get-login-password --region "$AWS_REGION" \
  | docker login --username AWS --password-stdin "$REGISTRY"

log "worker imageをbuildします: ${IMAGE_URI}"
docker build --platform "$PLATFORM" -t "$IMAGE_URI" "${INFRA_DIR}/worker"

log "worker imageをpushします: ${IMAGE_URI}"
docker push "$IMAGE_URI"

log "完了しました: ${IMAGE_URI}"
