#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
fixture_root="$(mktemp -d)"
trap 'rm -rf "$fixture_root"' EXIT

valid="$fixture_root/valid"
mkdir -p "$valid"
printf 'Role requirements\n' > "$valid/job.txt"
printf '# Candidate\n<!-- cv-headline: Platform Engineering Leader | SRE -->\n\n**Platform Engineering Leader | SRE**\n\n+1 555 0100 | candidate@example.com | Example City, Example Country\n\n## Education & Certifications\n| Name | Issuer |\n| --- | --- |\n| Example | Example |\n\n## Awards & Recognition\n| Award | Issuer |\n| --- | --- |\n| Example | Example |\n' > "$valid/cv.md"
printf '<!doctype html><html><head><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap"><style>body{font-family:Roboto,sans-serif}@media print{body{margin:0}}</style></head><body>\n<!-- cv-headline: Platform Engineering Leader | SRE -->\n<div class="headline">Platform Engineering Leader | SRE</div>\n<div class="contact">+1 555 0100 | candidate@example.com | Example City, Example Country</div>\n<h2>Education &amp; Certifications</h2>\n<table><tr><td>Example</td></tr></table>\n<h2>Awards &amp; Recognition</h2>\n<table><tr><td>Example</td></tr></table>\n</body></html>\n' > "$valid/cv.html"
printf 'Preparation notes\n' > "$valid/prep.md"
printf '## Decision\n- Recommendation: Apply with caution\n- Job readiness: 75%%\n- AI recommendation: Verify the stated gap before applying.\n' > "$valid/thinking.md"
printf 'Draft email\n' > "$valid/email.md"

"$repo_root/scripts/check-package.sh" "$valid"

invalid="$fixture_root/invalid"
cp -R "$valid" "$invalid"
printf '## Notes\n- Recommendation: Maybe\n- Job readiness: 101%%\n' > "$invalid/thinking.md"

if "$repo_root/scripts/check-package.sh" "$invalid" >/dev/null 2>&1; then
  echo "Expected invalid fixture to fail" >&2
  exit 1
fi

mismatch="$fixture_root/mismatch"
cp -R "$valid" "$mismatch"
sed -i 's/cv-headline: Platform Engineering Leader | SRE/cv-headline: Director | SRE/' "$mismatch/cv.html"

if "$repo_root/scripts/check-package.sh" "$mismatch" >/dev/null 2>&1; then
  echo "Expected mismatched headline markers to fail" >&2
  exit 1
fi

visible_mismatch="$fixture_root/visible-mismatch"
cp -R "$valid" "$visible_mismatch"
sed -i 's/<div class="headline">Platform Engineering Leader | SRE<\//<div class="headline">Director | SRE<\//' "$visible_mismatch/cv.html"

if "$repo_root/scripts/check-package.sh" "$visible_mismatch" >/dev/null 2>&1; then
  echo "Expected a marker/visible-headline mismatch to fail" >&2
  exit 1
fi

missing_table="$fixture_root/missing-table"
cp -R "$valid" "$missing_table"
sed -i '/<h2>Education &amp; Certifications<\/h2>/{n;s#<table><tr><td>Example</td></tr></table>#<p>Example</p>#;}' "$missing_table/cv.html"

if "$repo_root/scripts/check-package.sh" "$missing_table" >/dev/null 2>&1; then
  echo "Expected a missing required section table to fail" >&2
  exit 1
fi

missing_contact="$fixture_root/missing-contact"
cp -R "$valid" "$missing_contact"
sed -i '/<div class="contact">/d' "$missing_contact/cv.html"

if "$repo_root/scripts/check-package.sh" "$missing_contact" >/dev/null 2>&1; then
  echo "Expected a missing contact line to fail" >&2
  exit 1
fi

echo "check-package tests passed"
