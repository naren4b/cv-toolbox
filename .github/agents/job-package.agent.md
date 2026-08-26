---
description: "Create a private job package and register it in the private application tracker."
name: "Local Job Package"
tools: [read, edit, search, todo]
---

When imported under `toolbox/`, read `toolbox/AGENTS.md`, then read `AboutMe.md` and `Job-Applications/[company]/job.txt` from the private workspace root.

1. Verify that both `AboutMe.md` and `job.txt` exist. Treat `AboutMe.md` as candidate evidence and `job.txt` only as role requirements.
2. If any output file already exists, do not modify it. Report the file and request explicit user permission for that exact file.
3. Analyze the role's outcomes, seniority, must-haves, preferred requirements, domain, delivery scope, and leadership expectations. Map each material requirement to explicit evidence or a gap before drafting.
4. Compare and select exactly one stable profile lens: Senior SRE Engineer, SRE / AWS Solution Architect, or DevOps & Platform Engineering Leader. The lens controls emphasis and ordering only; it does not grant a title, seniority, or facts. Record the selection and evidence in `thinking.md`.
5. Create `thinking.md` as a concise decision record: recommendation, readiness percentage, selected profile, evidence-based matches, material gaps, and what the AI recommends the user do. Do not expose hidden chain-of-thought. For leadership targets, keep technical leadership, team direction, mentorship, formal people management, recruiting, budget ownership, and organization design distinct.
6. Create only missing `cv.md`, `cv.html`, `prep.md`, and, when applicable, `email.md` or `cover-letter.md` using only supported facts. Include a supported 90-second introduction, motivation, story bank, and question bank in `prep.md`; add a 30/60/90-day outline only for genuinely leadership-oriented targets. Immediately after the headline, include a header contact line `Phone | Email | City, Country` using a short address from `AboutMe.md` (never a street or postal address); in `cv.html` put that line in `<div class="contact">`. Before finalizing, verify: the CV headline uses an evidence-supported professional identity rather than an unsupported target title; both CV files contain matching `cv-headline` markers; the header includes the supported short address when a location is documented; technical leadership is not rewritten as formal people management; `cv.md` contains Markdown tables named `Education & Certifications` and `Awards & Recognition`; `cv.html` loads Roboto from Google Fonts, begins its font stack with Roboto, and renders matching HTML tables; and `thinking.md` begins with Recommendation, Job readiness, and AI recommendation fields.
7. Read the application-tracker table in root `README.md`. If the company is absent, append one row with status `Prepared — review required`, a concise role brief, today’s date, and the package path. If the company exists, preserve its user-managed status.

Do not modify `AboutMe.md`, `job.txt`, or existing generated outputs. Do not submit applications, send email, or commit files; the user reviews, updates status, and commits the private workspace.
