#!/usr/bin/env bash
set -uo pipefail

usage() {
  echo "Usage: $0 Job-Applications/<company>" >&2
}

if [[ $# -ne 1 ]]; then
  usage
  exit 2
fi

package_dir="${1%/}"
errors=0

fail() {
  printf 'ERROR: %s\n' "$1" >&2
  errors=$((errors + 1))
}

require_file() {
  local path="$1"
  [[ -s "$path" ]] || fail "missing or empty file: $path"
}

require_match() {
  local path="$1"
  local pattern="$2"
  local message="$3"
  grep -Eq "$pattern" "$path" || fail "$message"
}

if [[ ! -d "$package_dir" ]]; then
  fail "package directory does not exist: $package_dir"
else
  for name in job.txt cv.md cv.html prep.md thinking.md; do
    require_file "$package_dir/$name"
  done

  if [[ ! -s "$package_dir/email.md" && ! -s "$package_dir/cover-letter.md" ]]; then
    fail "missing communication file: create email.md or cover-letter.md"
  fi

  if [[ -s "$package_dir/cv.md" ]]; then
    require_match "$package_dir/cv.md" '^## Education & Certifications[[:space:]]*$' \
      "cv.md is missing the Education & Certifications section"
    require_match "$package_dir/cv.md" '^## Awards & Recognition[[:space:]]*$' \
      "cv.md is missing the Awards & Recognition section"
    require_match "$package_dir/cv.md" '^\|.+\|[[:space:]]*$' \
      "cv.md does not contain a Markdown table"
  fi

  if [[ -s "$package_dir/cv.html" ]]; then
    require_match "$package_dir/cv.html" '<!DOCTYPE html>|<!doctype html>' \
      "cv.html is missing an HTML doctype"
    require_match "$package_dir/cv.html" 'fonts\.googleapis\.com/css2\?family=Roboto:wght@400;500;700&display=swap' \
      "cv.html is missing the required Roboto stylesheet"
    require_match "$package_dir/cv.html" "font-family:[[:space:]]*(Roboto|\"Roboto\"|'Roboto')" \
      "cv.html font stack must begin with Roboto"
    require_match "$package_dir/cv.html" '<table([[:space:]>])' \
      "cv.html does not contain an HTML table"
    require_match "$package_dir/cv.html" '@media[[:space:]]+print' \
      "cv.html is missing print CSS"
  fi

  if [[ -s "$package_dir/thinking.md" ]]; then
    first_nonblank="$(grep -m1 -v '^[[:space:]]*$' "$package_dir/thinking.md" || true)"
    [[ "$first_nonblank" == '## Decision' ]] || \
      fail "thinking.md must begin with ## Decision"
    require_match "$package_dir/thinking.md" '^- Recommendation: (Apply|Apply with caution|Do not apply)[[:space:]]*$' \
      "thinking.md has an invalid or missing Recommendation field"
    require_match "$package_dir/thinking.md" '^- Job readiness: ([0-9]|[1-9][0-9]|100)%[[:space:]]*$' \
      "thinking.md has an invalid or missing Job readiness percentage"
    require_match "$package_dir/thinking.md" '^- AI recommendation: .+' \
      "thinking.md is missing a specific AI recommendation"
  fi
fi

if (( errors > 0 )); then
  printf '\nPackage check failed with %d error(s).\n' "$errors" >&2
  exit 1
fi

echo "Package check passed: $package_dir"
