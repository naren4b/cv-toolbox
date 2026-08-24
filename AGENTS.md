# Local Job Package Contract

This repository is a generic toolbox. Private candidate material and generated job packages stay local and are ignored by Git.

## Required private inputs

- `AboutMe.md` — the single private source of truth for candidate information.
- `Job-Applications/[company]/job.txt` — the original job description and source reference.

## Required generated outputs

- `cv.md` — customized CV for the selected role.
- `prep.md` — requirements match, genuine gaps, mitigation, likely questions, and preparation plan.
- `thinking.md` — concise decision record: selected profile category, role requirements, source facts selected, gaps, and output plan. Never include hidden chain-of-thought or unsupported claims.
- `email.md` — recruiter email when outreach or reply is needed.
- `cover-letter.md` — application letter when requested or more appropriate than an email.

## Profile categories

Select exactly one: Senior SRE Engineer, AWS Solutions Architect, or Engineering Manager. State the selection and rationale in `thinking.md`.

The user alone submits applications, sends messages, or confirms application status.
