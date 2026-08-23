#!/usr/bin/env bash
set -euo pipefail

payload="$(cat)"

# This guard only applies to PreToolUse events.
if ! echo "$payload" | grep -qi '"hookEventName"[[:space:]]*:[[:space:]]*"PreToolUse"'; then
  exit 0
fi

# Try to find any jobs/<company>/<file> path from payload.
job_path="$(echo "$payload" | grep -Eo '(/[^"[:space:]]*)?jobs/[^"[:space:]]+' | head -n1 || true)"

if [[ -z "$job_path" ]]; then
  exit 0
fi

company="$(echo "$job_path" | sed -E 's#.*jobs/([^/]+)/.*#\1#')"
target_file="$(basename "$job_path")"

if [[ -z "$company" || "$company" == "$job_path" ]]; then
  exit 0
fi

jd_file="jobs/${company}/jd.txt"
email_file="jobs/${company}/email.txt"

missing=()

case "$target_file" in
  cv-*.md|prep.txt|cover-letter.txt)
    [[ -f "$jd_file" ]] || missing+=("$jd_file")
    ;;
  email-reply.md)
    [[ -f "$jd_file" ]] || missing+=("$jd_file")
    [[ -f "$email_file" ]] || missing+=("$email_file")
    ;;
  *)
    exit 0
    ;;
esac

if [[ ${#missing[@]} -eq 0 ]]; then
  exit 0
fi

missing_msg="$(IFS=', '; echo "${missing[*]}")"

cat <<EOF
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Missing required job input files: ${missing_msg}"
  },
  "systemMessage": "Blocked: missing required job input files: ${missing_msg}. Add the files before generating artifacts for jobs/${company}/."
}
EOF
exit 2
