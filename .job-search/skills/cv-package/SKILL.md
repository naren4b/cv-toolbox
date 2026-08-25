# Private CV Package Skill

## Inputs

- Private workspace `AboutMe.md` — the factual source of truth.
- Private workspace `Job-Applications/[company]/job.txt` — the target-role requirements.

## Profile selection

Choose one: Senior SRE Engineer, AWS Solutions Architect, or Engineering Manager.

## Outputs

- `cv.md`: role-specific CV using supported facts only.
- `cv.html`: printable HTML rendering of `cv.md`.
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
- Do not modify an existing generated output (`cv.md`, `cv.html`, `prep.md`, `thinking.md`, `email.md`, or `cover-letter.md`) unless the user explicitly names that file and asks for a change. Create only missing outputs.
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


## CV output quality

- Keep the CV focused: select job-relevant evidence with the strongest supported outcomes; omit unrelated detail rather than padding with generic claims.
- Preserve employer names, official job titles, dates, qualifications, and certification names exactly as supported. The target role may be named only in an explicitly labelled target-role context, never as the candidate title.
- Use separate Markdown tables for **Education & Certifications** and **Awards & Recognition**. Every row must be supported by `AboutMe.md`; do not manufacture dates, issuers, rankings, or descriptions.
- Create `cv.html` whenever creating `cv.md`. It must contain the same factual content in the same order, load Roboto from Google Fonts, include responsive and print CSS, and render cleanly on A4 paper. Do not add images, trackers, analytics, JavaScript, or external assets other than the Roboto font stylesheet.
- Before finalizing, verify the Markdown headline, titles, dates, metrics, qualifications, education table, and awards table against `AboutMe.md`; then compare `cv.html` with `cv.md` so their factual content matches.


## Required output schema and acceptance checks

### `cv.md`

- The first line is the candidate name. The next line starts with an exact official title from `AboutMe.md`, followed only by factual specialties. Never use the target title in this headline. If helpful, place the job title later as `Target role: [job title]`; it must be visibly labelled as a target.
- Do not convert technical leadership into people management. When the evidence says technical leadership, mentoring, or roadmap influence, use those words. Do not substitute `direct`, `manage`, `own`, `hire`, or `scale a team` unless `AboutMe.md` explicitly supports that responsibility.
- Include exactly these tabular sections when source evidence exists: `## Education & Certifications` and `## Awards & Recognition`. Use a Markdown pipe table with descriptive columns. Do not omit supported certifications merely because they are less relevant to the target role.

### `cv.html`

- Start with a valid HTML document and include the Google Fonts stylesheet for Roboto: `https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap`. The body font stack must begin with `Roboto`.
- Render the Education & Certifications and Awards & Recognition sections as HTML tables. The HTML must have the same headings, dates, facts, and claim order as `cv.md`.

### `thinking.md`

Begin with this exact decision block before analysis:

```markdown
## Decision
- Recommendation: Apply | Apply with caution | Do not apply
- Job readiness: NN%
- AI recommendation: [specific next action]
```

Do not recommend presenting the candidate with the target title. The readiness percentage is a requirement-match estimate, not a hiring probability.

### Preflight

Do not finalize a package until every item passes: (1) candidate headline uses an official title from `AboutMe.md`, (2) no unsupported people-management verb is used, (3) both required Markdown tables exist, (4) `cv.html` includes Roboto Google Fonts and matching HTML tables, and (5) `thinking.md` contains the exact decision fields. If an input cannot support a required claim, remove the claim and list the gap instead.

After creating all missing artifacts, run `bash toolbox/scripts/check-package.sh Job-Applications/[company]` from the private workspace root. Fix structural failures before reporting completion. The checker does not replace the factual comparison with `AboutMe.md`.
