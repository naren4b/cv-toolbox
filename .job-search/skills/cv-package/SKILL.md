# Private CV Package Skill

## Inputs

- Private workspace `AboutMe.md` — the factual source of truth.
- Private workspace `Job-Applications/[company]/job.txt` — the target-role requirements.

## Profile selection

Choose one: Senior SRE Engineer, AWS Solutions Architect, or Engineering Manager.

## Outputs

- `cv.md`: role-specific CV using supported facts only.
- `prep.md`: requirement mapping, genuine gaps, mitigation, likely questions, and preparation checklist.
- `thinking.md`: concise decision record; no hidden reasoning.
- `email.md` or `cover-letter.md`: role-specific communication when applicable.

## Fact-based CV rules

- Treat `AboutMe.md` as the only factual source of truth for the candidate's titles, employers, dates, achievements, qualifications, certifications, locations, eligibility, compensation, and metrics.
- Every claim in `cv.md` must be directly supported by `AboutMe.md`. Tailoring may reorder, shorten, or select facts, but must not add, upgrade, estimate, or imply facts.
- Use the candidate's evidenced current or past title in the CV heading. Never use the target job title, seniority, or management scope as though the candidate already holds it.
- The job title may appear only as an explicitly labelled target role, never in the candidate headline, employment history, or summary as a stated fact.
- If a requirement cannot be supported, omit it from the CV and record it as a genuine gap or question in `prep.md`.
- Avoid inflated wording such as “Director”, “Head of”, “owner”, “expert”, or numerical outcomes unless those exact responsibilities or numbers are supported by `AboutMe.md`.

## Private tracker

After package artifacts exist, maintain the application-tracker table in root `README.md` in the private workspace:

- Add one row for a previously untracked company with `Prepared — review required`, role brief, current date, and package path.
- Preserve existing user-managed status values; update only package metadata when artifacts change.
- The user alone changes the application status, sends messages, submits applications, and commits files.

## Rules

- Preserve `job.txt` unchanged.
- Do not submit or send external communications.
