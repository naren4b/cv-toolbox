#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
fixture_root="$(mktemp -d)"
trap 'rm -rf "$fixture_root"' EXIT

valid="$fixture_root/valid"
mkdir -p "$valid"
printf 'Role requirements\n' > "$valid/job.txt"
printf '# Candidate\n\n## Education & Certifications\n| Name | Issuer |\n| --- | --- |\n| Example | Example |\n\n## Awards & Recognition\n| Award | Issuer |\n| --- | --- |\n| Example | Example |\n' > "$valid/cv.md"
printf '<!doctype html><html><head><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap"><style>body{font-family:Roboto,sans-serif}@media print{body{margin:0}}</style></head><body><table><tr><td>Example</td></tr></table></body></html>\n' > "$valid/cv.html"
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

echo "check-package tests passed"
