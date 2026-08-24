---
description: Create a private, local job-application package from AboutMe.md and a company job.txt.
---

# Generate Local Job Package

Use the repository-local workflow defined in `AGENTS.md`.

1. Ask for the company folder only if it cannot be inferred.
2. Read `AboutMe.md` and `Job-Applications/<company>/job.txt`.
3. Select one category: Senior SRE Engineer, AWS Solutions Architect, or Engineering Manager.
4. Create or refresh only these ignored local outputs in that company folder:
   - `thinking.md` — concise decision record; no hidden reasoning.
   - `cv.md` — role-specific CV.
   - `prep.md` — interview preparation and candid profile-vs-job gaps.
   - `email.md` or `cover-letter.md` — a recruiter email or cover letter when appropriate.
5. Do not alter `AboutMe.md` or `job.txt`, submit an application, send email, or commit private files.
