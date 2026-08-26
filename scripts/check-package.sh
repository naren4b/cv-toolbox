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

headline_marker() {
  local path="$1"
  sed -n 's/.*<!-- cv-headline: \(.*\) -->.*/\1/p' "$path" | head -n 1
}

markdown_visible_headline() {
  local path="$1"
  awk '/<!-- cv-headline: / { found=1; next } found && NF { print; exit }' "$path" |
    sed -E 's/^\*\*(.*)\*\*$/\1/'
}

html_visible_headline() {
  local path="$1"
  sed -n 's/.*<div class="headline">\(.*\)<\/div>.*/\1/p' "$path" |
    head -n 1 |
    sed 's/&amp;/\&/g'
}

markdown_section_has_table() {
  local path="$1"
  local heading="$2"
  awk -v heading="$heading" '
    $0 == heading { in_section=1; next }
    in_section && /^## / { exit }
    in_section && /^\|.*\|[[:space:]]*$/ { found=1; exit }
    END { exit(found ? 0 : 1) }
  ' "$path"
}

html_section_has_table() {
  local path="$1"
  local heading="$2"
  awk -v heading="$heading" '
    index($0, "<h2>" heading "</h2>") { in_section=1; next }
    in_section && /<h2>/ { exit }
    in_section && /<table([[:space:]>])/ { found=1; exit }
    END { exit(found ? 0 : 1) }
  ' "$path"
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
    markdown_section_has_table "$package_dir/cv.md" '## Education & Certifications' || \
      fail "cv.md Education & Certifications section must contain a Markdown table"
    markdown_section_has_table "$package_dir/cv.md" '## Awards & Recognition' || \
      fail "cv.md Awards & Recognition section must contain a Markdown table"
  fi

  if [[ -s "$package_dir/cv.html" ]]; then
    require_match "$package_dir/cv.html" '<!DOCTYPE html>|<!doctype html>' \
      "cv.html is missing an HTML doctype"
    require_match "$package_dir/cv.html" 'fonts\.googleapis\.com/css2\?family=Roboto:wght@400;500;700&display=swap' \
      "cv.html is missing the required Roboto stylesheet"
    require_match "$package_dir/cv.html" "font-family:[[:space:]]*(Roboto|\"Roboto\"|'Roboto')" \
      "cv.html font stack must begin with Roboto"
    html_section_has_table "$package_dir/cv.html" 'Education &amp; Certifications' || \
      fail "cv.html Education & Certifications section must contain an HTML table"
    html_section_has_table "$package_dir/cv.html" 'Awards &amp; Recognition' || \
      fail "cv.html Awards & Recognition section must contain an HTML table"
    require_match "$package_dir/cv.html" '<div class="contact">' \
      "cv.html is missing <div class=\"contact\"> for the header contact line"
  fi

  if [[ -s "$package_dir/cv.md" && -s "$package_dir/cv.html" ]]; then
    markdown_headline="$(headline_marker "$package_dir/cv.md")"
    html_headline="$(headline_marker "$package_dir/cv.html")"
    markdown_visible="$(markdown_visible_headline "$package_dir/cv.md")"
    html_visible="$(html_visible_headline "$package_dir/cv.html")"
    [[ -n "$markdown_headline" ]] || fail "cv.md is missing the cv-headline marker"
    [[ -n "$html_headline" ]] || fail "cv.html is missing the cv-headline marker"
    if [[ -n "$markdown_headline" && -n "$html_headline" && "$markdown_headline" != "$html_headline" ]]; then
      fail "cv.md and cv.html headline markers do not match"
    fi
    [[ -n "$markdown_visible" ]] || fail "cv.md is missing a visible headline after the cv-headline marker"
    [[ -n "$html_visible" ]] || fail "cv.html is missing <div class=\"headline\">"
    if [[ -n "$markdown_headline" && -n "$markdown_visible" && "$markdown_headline" != "$markdown_visible" ]]; then
      fail "cv.md headline marker does not match its visible headline"
    fi
    if [[ -n "$html_headline" && -n "$html_visible" && "$html_headline" != "$html_visible" ]]; then
      fail "cv.html headline marker does not match its visible headline"
    fi
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
