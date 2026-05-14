#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INFRA_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
STACK_NAME="${STACK_NAME:-udemy-render-batch-dev}"
AWS_REGION="${AWS_REGION:-us-east-1}"
IMAGE_TAG="${IMAGE_TAG:-latest}"
WORKER_TYPE="${WORKER_TYPE:-render}"
WAIT="${WAIT:-true}"

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

require_command() {
  local name="$1"
  if ! command -v "$name" >/dev/null 2>&1; then
    echo "${name} が見つかりません。" >&2
    exit 1
  fi
}

require_command aws
require_command python3

case "$WORKER_TYPE" in
  render)
    SOURCE_DIR="${INFRA_DIR}/worker"
    SOURCE_KEY="build-source/worker-source.zip"
    SOURCE_ZIP="/tmp/udemy-render-worker-source.zip"
    BUILD_PROJECT_OUTPUT_KEY="BuildProjectName"
    ;;
  voicevox)
    SOURCE_DIR="${INFRA_DIR}/voicevox_worker"
    SOURCE_KEY="build-source/voicevox-source.zip"
    SOURCE_ZIP="/tmp/udemy-voicevox-worker-source.zip"
    BUILD_PROJECT_OUTPUT_KEY="VoicevoxBuildProjectName"
    ;;
  *)
    echo "WORKER_TYPEは render または voicevox を指定してください: ${WORKER_TYPE}" >&2
    exit 1
    ;;
esac

ARTIFACT_BUCKET="$(stack_output ArtifactBucketName)"
BUILD_PROJECT_NAME="$(stack_output "$BUILD_PROJECT_OUTPUT_KEY")"

if [ -z "$ARTIFACT_BUCKET" ] || [ "$ARTIFACT_BUCKET" = "None" ]; then
  echo "ArtifactBucketNameを取得できません。先にscripts/deploy.sh deployを実行してください。" >&2
  exit 1
fi

if [ -z "$BUILD_PROJECT_NAME" ] || [ "$BUILD_PROJECT_NAME" = "None" ]; then
  echo "BuildProjectNameを取得できません。先にscripts/deploy.sh deployを実行してください。" >&2
  exit 1
fi

log "worker sourceをzip化します: ${SOURCE_ZIP}"
python3 - "$SOURCE_DIR" "$SOURCE_ZIP" <<'PY'
import sys
import zipfile
from pathlib import Path

source_dir = Path(sys.argv[1])
zip_path = Path(sys.argv[2])
if zip_path.exists():
    zip_path.unlink()

with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(source_dir.rglob("*")):
        if path.is_file() and "__pycache__" not in path.parts:
            archive.write(path, path.relative_to(source_dir))
PY

log "build sourceをS3へアップロードします"
aws s3 cp "$SOURCE_ZIP" "s3://${ARTIFACT_BUCKET}/${SOURCE_KEY}" \
  --region "$AWS_REGION"

log "CodeBuildを開始します: ${BUILD_PROJECT_NAME}"
BUILD_ID="$(aws codebuild start-build \
  --project-name "$BUILD_PROJECT_NAME" \
  --region "$AWS_REGION" \
  --environment-variables-override "name=IMAGE_TAG,value=${IMAGE_TAG},type=PLAINTEXT" \
  --query 'build.id' \
  --output text)"

printf 'BuildId: %s\n' "$BUILD_ID"

if [ "$WAIT" != "true" ]; then
  exit 0
fi

log "CodeBuild完了を待ちます"
while true; do
  STATUS="$(aws codebuild batch-get-builds \
    --ids "$BUILD_ID" \
    --region "$AWS_REGION" \
    --query 'builds[0].buildStatus' \
    --output text)"
  printf '[%s] build status: %s\n' "$(date -u '+%Y-%m-%dT%H:%M:%SZ')" "$STATUS"
  case "$STATUS" in
    SUCCEEDED)
      exit 0
      ;;
    FAILED|FAULT|STOPPED|TIMED_OUT)
      aws codebuild batch-get-builds \
        --ids "$BUILD_ID" \
        --region "$AWS_REGION" \
        --query 'builds[0].[buildStatus,currentPhase,logs.deepLink]' \
        --output table
      exit 1
      ;;
  esac
  sleep 10
done
