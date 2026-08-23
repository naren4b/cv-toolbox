# CV Prep App — Job Search 2026

This is the single workspace for job applications, candidate information, and application packages.

## Start a new application

1. Create `jobs/[company]/`.
2. Add the original job description as `job.txt`.
3. Run `.github/prompts/apply-to-job.prompt.md`.
4. Review `analysis.md`, `cv-DD-MM-YYYY.md`, `prep.md`, `cover-letter.md`, `company-info.md`, and `status.md` before applying.
5. Add `email.txt` only when a recruiter has contacted you. The workflow then creates `email-reply.md`.

## Canonical information

Use the files in `data/` as the only factual source for candidate details. Do not copy personal, employer, or compensation information into job folders.

## Versioning

1. Update a canonical file only for verified factual changes.
2. Record every major update in `CHANGELOG.md` with the date, file, reason, and prior version location.
3. Before replacing a major CV or workflow file, keep the prior version in `archive/YYYY-MM-DD/`.
4. Job-specific CVs are dated and remain inside their own company folder.
5. Do not delete old work. Archive it only after review.

## Boundaries

- `data/` holds the candidate facts.
- `jobs/` holds job-specific inputs and generated packages.
- `.github/` holds prompts, specialist agents, and guardrails.
- `create-my-cv/` holds reusable guidance and templates.
- `archive/` holds superseded major versions.

No application is considered submitted unless `status.md` contains verified submission evidence.
