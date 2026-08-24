#!/usr/bin/env bash
set -euo pipefail

payload="$(cat)"
if ! echo "$payload" | grep -qi '"hookEventName"[[:space:]]*:[[:space:]]*"PreToolUse"'; then exit 0; fi
job_path="$(echo "$payload" | grep -Eo '(/[^"[:space:]]*)?Job-Applications/[^"[:space:]]+' | head -n1 || true)"
[[ -n "$job_path" ]] || exit 0
company="$(echo "$job_path" | sed -E 's#.*Job-Applications/([^/]+)/.*#\1#')"
target_file="$(basename "$job_path")"
[[ -n "$company" && "$company" != "$job_path" ]] || exit 0

job_file="Job-Applications/${company}/job.txt"
email_file="Job-Applications/${company}/email.txt"
missing=()
case "$target_file" in
  cv-*.md|prep.md|cover-letter.md|analysis.md|company-info.md|status.md) [[ -f "$job_file" ]] || missing+=("$job_file") ;;
  email-reply.md) [[ -f "$job_file" ]] || missing+=("$job_file"); [[ -f "$email_file" ]] || missing+=("$email_file") ;;
  *) exit 0 ;;
esac
[[ ${#missing[@]} -eq 0 ]] && exit 0
missing_msg="$(IFS=', '; echo "${missing[*]}")"
cat <<EOF
{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"Missing required job input files: ${missing_msg}"},"systemMessage":"Blocked: missing required job input files: ${missing_msg}."}
EOF
exit 2
