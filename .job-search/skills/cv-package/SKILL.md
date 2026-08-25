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
- Use the candidate's evidenced current or past title in the CV heading. A professional subtitle may be positioned at most one level above the evidenced title only when supported scope demonstrates it; it must not be presented as an official job title.
- The job title may appear only as an explicitly labelled target role, never in the candidate headline, employment history, or summary as a stated fact.
- If a requirement cannot be supported, omit it from the CV and record it as a genuine gap or question in `prep.md`.
- Avoid inflated wording such as “Director”, “Head of”, “owner”, “expert”, or numerical outcomes unless those exact responsibilities or numbers are supported by `AboutMe.md`.
- `thinking.md` must state one clear recommendation: `Apply`, `Apply with caution`, or `Do not apply`; state what the AI recommends the user do next; and include a job-readiness percentage from 0–100. The percentage is an evidence-based requirement-match estimate, not a probability of being hired. List evidenced matches and material gaps. When a material seniority, domain, leadership-scope, or required-experience gap outweighs the matches, recommend `Do not apply`; do not rationalize the gap away.

## Reliability checks

- Before generating, verify that `AboutMe.md` and `job.txt` are present. If either is missing or unclear, stop and ask for it.
- Separate facts from requirements: `AboutMe.md` establishes what the candidate has done; `job.txt` establishes what the role asks for. A job requirement never becomes a candidate claim by itself.
- Do not modify an existing generated output (`cv.md`, `prep.md`, `thinking.md`, `email.md`, or `cover-letter.md`) unless the user explicitly names that file and asks for a change. Create only missing outputs.
- Calculate readiness from evidence against must-have and major requirements. State the percentage as an estimate, list the material gaps that lower it, and never present it as a hiring probability.
- Before finalizing a new CV, check its headline, employer titles, dates, metrics, qualifications, and certifications against `AboutMe.md`. Omit any unsupported item.

## Private tracker

After package artifacts exist, maintain the application-tracker table in root `README.md` in the private workspace:

- Add one row for a previously untracked company with `Prepared — review required`, role brief, current date, and package path.
- Preserve existing user-managed status values; update only package metadata when artifacts change.
- The user alone changes the application status, sends messages, submits applications, and commits files.

## Rules

- Preserve `job.txt` unchanged.
- Do not submit or send external communications.
