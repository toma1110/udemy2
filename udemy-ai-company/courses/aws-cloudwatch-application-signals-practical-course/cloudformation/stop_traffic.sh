#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Disabling scheduled traffic. This updates the CloudFormation stack."
TRAFFIC_ENABLED=false "${SCRIPT_DIR}/validate.sh" update
