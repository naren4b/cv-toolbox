#!/usr/bin/env bash
set -euo pipefail

# Prevent accidental commits of private inputs and generated job packages.
for file in "$@"; do
  case "$file" in
    AboutMe.md|Job-Applications/*/job.txt|Job-Applications/*/cv.md|Job-Applications/*/cv.html|Job-Applications/*/prep.md|Job-Applications/*/thinking.md|Job-Applications/*/email.md|Job-Applications/*/cover-letter.md|Master-CV/cv.md|Master-CV/cv.html)
      echo "Private job-search file must not be committed: $file" >&2
      exit 1
      ;;
  esac
done
