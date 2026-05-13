#!/usr/bin/env bash
set -euo pipefail

REPO="${RULE_AUDITOR_REPO:-toma1110/udemy2}"
LIMIT="${RULE_AUDITOR_LIMIT:-1000}"
AUDIT_TITLE="${RULE_AUDITOR_ISSUE_TITLE:-AI-Ops Rule Audit}"
JSON_OUT="${RULE_AUDITOR_JSON_OUT:-/home/ubuntu/workspace/udemy2/udemy-ai-company/.pm_state/rule_audit_latest.json}"
APPLY="${RULE_AUDITOR_APPLY:-1}"

ARGS=(
  --repo "$REPO"
  --limit "$LIMIT"
  --audit-issue-title "$AUDIT_TITLE"
  --json-out "$JSON_OUT"
)

if [[ "$APPLY" == "1" || "$APPLY" == "true" || "$APPLY" == "yes" ]]; then
  ARGS+=(--apply)
fi

cd /home/ubuntu/workspace/udemy2/udemy-ai-company

exec python3 tools/rule_auditor.py "${ARGS[@]}"
