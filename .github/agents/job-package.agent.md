---
description: "Create a private job package and register it in the private application tracker."
name: "Local Job Package"
tools: [read, edit, search, todo]
---

When imported under `toolbox/`, read `toolbox/AGENTS.md`, then read `AboutMe.md` and `Job-Applications/[company]/job.txt` from the private workspace root.

1. Verify that both `AboutMe.md` and `job.txt` exist. Treat `AboutMe.md` as candidate evidence and `job.txt` only as role requirements.
2. If any output file already exists, do not modify it. Report the file and request explicit user permission for that exact file.
3. Select exactly one profile category: Senior SRE Engineer, AWS Solutions Architect, or Engineering Manager.
4. Create `thinking.md` as a concise decision record: recommendation, readiness percentage, evidence-based matches, material gaps, and what the AI recommends the user do. Do not expose hidden chain-of-thought.
5. Create only missing `cv.md`, `cv.html`, `prep.md`, and, when applicable, `email.md` or `cover-letter.md` using only supported facts. Before finalizing, verify: the CV headline begins with an official title from `AboutMe.md` rather than the target title; technical leadership is not rewritten as formal people management; `cv.md` contains Markdown tables named `Education & Certifications` and `Awards & Recognition`; `cv.html` loads Roboto from Google Fonts, begins its font stack with Roboto, and renders matching HTML tables; and `thinking.md` begins with Recommendation, Job readiness, and AI recommendation fields.
6. Read the application-tracker table in root `README.md`. If the company is absent, append one row with status `Prepared — review required`, a concise role brief, today’s date, and the package path. If the company exists, preserve its user-managed status.

Do not modify `AboutMe.md`, `job.txt`, or existing generated outputs. Do not submit applications, send email, or commit files; the user reviews, updates status, and commits the private workspace.
