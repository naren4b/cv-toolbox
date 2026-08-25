---
description: Create a private job-application package and register a new package in the private tracker.
---

# Generate Local Job Package

When this toolbox is imported as `toolbox/`, use the private workspace workflow defined in `toolbox/AGENTS.md`.

1. Read `AboutMe.md` and `Job-Applications/<company>/job.txt` from the private workspace root. Use `AboutMe.md` for facts and `job.txt` for requirements only.
2. If a generated output already exists, do not change it; report it and ask for permission for that exact file.
3. Select Senior SRE Engineer, AWS Solutions Architect, or Engineering Manager.
4. Create only missing `thinking.md`, `cv.md`, `cv.html`, `prep.md`, and `email.md` or `cover-letter.md`. In `cv.md`, use concise, job-relevant evidence only; keep exact employer titles and dates, and use separate Markdown tables for Education & Certifications and Awards & Recognition. `cv.html` must be a fact-for-fact equivalent of `cv.md`, use Roboto from Google Fonts, and print cleanly on A4 paper. Before finalizing, require these acceptance checks: the candidate headline uses an evidence-supported professional identity rather than an unsupported target title; both CV files contain matching `cv-headline` markers; technical leadership is not rewritten as people management; `cv.md` contains Markdown tables titled `Education & Certifications` and `Awards & Recognition`; `cv.html` loads Roboto from Google Fonts, begins its font stack with Roboto, and contains matching HTML tables; and `thinking.md` begins with Recommendation, Job readiness, and AI recommendation fields.
5. Maintain the application-tracker table in root `README.md`: add a missing company as `Prepared — review required`; never overwrite an existing user-managed status.
6. Do not alter inputs, existing outputs, submit an application, send email, or commit private files.
