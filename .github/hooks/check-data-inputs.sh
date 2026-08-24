#!/usr/bin/env bash
set -euo pipefail

payload="$(cat)"
if ! echo "$payload" | grep -qi '"hookEventName"[[:space:]]*:[[:space:]]*"PreToolUse"'; then
  exit 0
fi

required_file="data/about.md"
if [[ -f "$required_file" ]]; then
  exit 0
fi

cat <<EOF
{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"Missing required private master file: ${required_file}"},"systemMessage":"Blocked: add the approved private ${required_file} before generating candidate-specific output."}
EOF
exit 2
