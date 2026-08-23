#!/usr/bin/env bash
set -euo pipefail

payload="$(cat)"

required_files=(
  "data/Master-CV.md"
  "data/current-employer.txt"
  "data/personal.txt"
  "data/salary.txt"
)

missing=()
for file in "${required_files[@]}"; do
  if [[ ! -f "$file" ]]; then
    missing+=("$file")
  fi
done

if [[ ${#missing[@]} -eq 0 ]]; then
  exit 0
fi

missing_msg="$(IFS=', '; echo "${missing[*]}")"

if echo "$payload" | grep -qi '"hookEventName"[[:space:]]*:[[:space:]]*"UserPromptSubmit"'; then
  cat <<EOF
{
  "continue": false,
  "stopReason": "Missing required input files in data/",
  "systemMessage": "Blocked: missing required input files: ${missing_msg}. Initialize with: mkdir -p data && cp data-template/* data/"
}
EOF
  exit 2
fi

if echo "$payload" | grep -qi '"hookEventName"[[:space:]]*:[[:space:]]*"PreToolUse"'; then
  cat <<EOF
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Missing required input files in data/: ${missing_msg}"
  },
  "systemMessage": "Blocked: missing required input files: ${missing_msg}. Initialize with: mkdir -p data && cp data-template/* data/"
}
EOF
  exit 2
fi

exit 0
