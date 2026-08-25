# Job Search Toolbox — Agent Entry Contract

This repository is public and generic. Private work happens in a private workspace that downloads a tagged release of this repository into an ignored local `toolbox/` directory.

When working from that private workspace, read `AboutMe.md` and `Job-Applications/[company]/job.txt` from the private workspace root. Follow `toolbox/Architecture.md`, create private package outputs in the company folder, and maintain the application-tracker table in root `README.md`.

When a package is created, add a missing tracker row with status `Prepared — review required`. Never overwrite an existing status; the user alone updates the application status, sends messages, submits applications, and commits files to the private workspace `origin`.

Reliability contract: treat `AboutMe.md` as the factual source of truth and `job.txt` as requirements, not candidate facts. Do not alter any existing generated package output unless the user explicitly requests that exact file be changed. When evidence is missing, record a gap rather than making a claim. New packages include matching `cv.md` and `cv.html`; the HTML is a printable rendering of the Markdown CV, not an additional source of facts.

## Title integrity

- Never present the target job title as the candidate's current or earned title.
- The CV headline must describe the candidate's supported professional identity.
- Use the target title in the headline only when `AboutMe.md` supports that title and seniority.
- Otherwise use a neutral, evidence-supported functional identity such as `DevOps & Platform Engineering Leader` or `Platform Engineering & SRE Leader`.
- Always retain the candidate's official employment title in the experience section.

Before writing the headline:

1. Extract the candidate's official current title from `AboutMe.md`.
2. Extract the target title from `job.txt`.
3. If the titles differ in level or function, do not use the target title as the candidate headline.
4. Use an evidence-supported functional identity instead.
5. Record the target role only in `thinking.md`, `prep.md`, and the communication document.

## Markdown and HTML parity

When `cv.md` changes, update `cv.html` in the same operation unless the user explicitly excludes `cv.html`. The visible wording, claims, dates, titles, metrics, and section order must remain consistent between both versions.

Place the same canonical headline marker in both files:

```html
<!-- cv-headline: Evidence-supported headline | Functional keywords -->
```

Before finalizing, audit the current official job title, target job title, headline, leadership level, certifications, years of experience, metrics, employer and product relationships, and Markdown/HTML parity.
