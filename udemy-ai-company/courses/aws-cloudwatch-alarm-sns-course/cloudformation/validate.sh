#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

aws cloudformation validate-template \
  --template-body "file://${SCRIPT_DIR}/template.yaml"
