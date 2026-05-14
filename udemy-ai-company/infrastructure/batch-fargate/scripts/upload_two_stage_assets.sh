#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
STACK_NAME="${STACK_NAME:-udemy-render-batch-dev}"
AWS_REGION="${AWS_REGION:-us-east-1}"
COURSE_ID="${COURSE_ID:-aws-slo-adoption-course}"
LECTURE_ID="${LECTURE_ID:?LECTURE_IDを指定してください。例: LECTURE_ID=s3-l5}"
COURSE_DIR="${COURSE_DIR:-$(cd "${SCRIPT_DIR}/../../../courses/${COURSE_ID}" && pwd)}"
SLIDES_DIR="${SLIDES_DIR:-${COURSE_DIR}/slides/${LECTURE_ID}}"
SCRIPT_FILE="${SCRIPT_FILE:-${COURSE_DIR}/scripts/${LECTURE_ID}_script.md}"
S3_PREFIX="${S3_PREFIX:-}"
MANIFEST_FILE="${MANIFEST_FILE:-}"
SPEAKER_ID="${SPEAKER_ID:-3}"
SPEED_SCALE="${SPEED_SCALE:-1.1}"

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

if [ ! -d "$SLIDES_DIR" ]; then
  echo "slides directoryが見つかりません: ${SLIDES_DIR}" >&2
  exit 1
fi

if [ ! -f "$SCRIPT_FILE" ]; then
  echo "script fileが見つかりません: ${SCRIPT_FILE}" >&2
  exit 1
fi

ARTIFACT_BUCKET="$(stack_output ArtifactBucketName)"
if [ -z "$ARTIFACT_BUCKET" ] || [ "$ARTIFACT_BUCKET" = "None" ]; then
  echo "ArtifactBucketNameを取得できません。先にscripts/deploy.sh deployを実行してください。" >&2
  exit 1
fi

if [ -z "$S3_PREFIX" ]; then
  S3_PREFIX="s3://${ARTIFACT_BUCKET}/${COURSE_ID}/${LECTURE_ID}-two-stage"
fi

MANIFEST_FILE="${MANIFEST_FILE:-/tmp/${COURSE_ID}-${LECTURE_ID}-two-stage-manifest.json}"
SCRIPT_BASENAME="$(basename "$SCRIPT_FILE")"

log "slidesをアップロードします: ${SLIDES_DIR} -> ${S3_PREFIX}/slides/"
aws s3 sync "$SLIDES_DIR" "${S3_PREFIX}/slides/" \
  --region "$AWS_REGION" \
  --exclude "*" \
  --include "slide_*.png"

log "scriptをアップロードします: ${SCRIPT_FILE} -> ${S3_PREFIX}/script/${SCRIPT_BASENAME}"
aws s3 cp "$SCRIPT_FILE" "${S3_PREFIX}/script/${SCRIPT_BASENAME}" --region "$AWS_REGION"

python3 - "$MANIFEST_FILE" "$COURSE_ID" "$LECTURE_ID" "$S3_PREFIX" "$SCRIPT_BASENAME" "$SPEAKER_ID" "$SPEED_SCALE" <<'PY'
import json
import sys
from pathlib import Path

path, course_id, lecture_id, prefix, script_basename, speaker_id, speed_scale = sys.argv[1:8]
manifest = {
    "course_id": course_id,
    "lecture_id": lecture_id,
    "slides_s3_uri": f"{prefix}/slides/",
    "script_s3_uri": f"{prefix}/script/{script_basename}",
    "audio_s3_uri": f"{prefix}/audio/",
    "output_s3_uri": f"{prefix}/output/",
    "voicevox": {
        "speaker_id": int(speaker_id),
        "speed_scale": float(speed_scale),
    },
    "video": {
        "width": 1920,
        "height": 1080,
        "fps": 30,
        "crf": 23,
        "preset": "veryfast",
        "audio_bitrate": "192k",
        "tail_padding_seconds": 0.2,
    },
}
Path(path).write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
PY

log "manifestをアップロードします: ${MANIFEST_FILE} -> ${S3_PREFIX}/manifest.json"
aws s3 cp "$MANIFEST_FILE" "${S3_PREFIX}/manifest.json" --region "$AWS_REGION"

printf '%s\n' "${S3_PREFIX}/manifest.json"
