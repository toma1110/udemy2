#!/usr/bin/env bash
set -euo pipefail

REPO="${PM_WATCHER_REPO:-toma1110/udemy2}"
POLL_SECONDS="${PM_WATCHER_POLL_SECONDS:-60}"
EXECUTOR="${PM_WATCHER_EXECUTOR:-codex exec --cd /home/ubuntu/workspace/udemy2 --sandbox danger-full-access -}"
CLOSE_NON_APPROVAL="${PM_WATCHER_CLOSE_NON_APPROVAL:-1}"

EXTRA_ARGS=()
if [[ "$CLOSE_NON_APPROVAL" == "1" || "$CLOSE_NON_APPROVAL" == "true" || "$CLOSE_NON_APPROVAL" == "yes" ]]; then
  EXTRA_ARGS+=(--close-non-approval)
fi

cd /home/ubuntu/workspace/udemy2/udemy-ai-company

exec python3 tools/pm_issue_watcher.py \
  --repo "$REPO" \
  --apply \
  --execute \
  --executor "$EXECUTOR" \
  --poll-seconds "$POLL_SECONDS" \
  "${EXTRA_ARGS[@]}"
