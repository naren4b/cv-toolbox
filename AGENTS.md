# Job Search Toolbox — Agent Instructions

This repository is a public, generic AI toolbox. Candidate facts and generated job packages live only in a private workspace that downloads a tagged release into an ignored local `toolbox/` directory.

- Humans: `README.md` for setup. Architecture: `Architecture.md`.
- Package generation details: `.job-search/skills/cv-package/SKILL.md`.
- Do not copy private material into this public repository.

## Choose the workspace

**This public repository.** Improve generic docs, skills, agents, prompts, templates, and `scripts/check-package.sh`. Never add `AboutMe.md`, job descriptions, generated CVs, recruiter correspondence, compensation, or application status.

**Private workspace (this repo imported as `toolbox/`).** Follow the [Private workspace contract](#private-workspace-contract). Read `AboutMe.md` and `Job-Applications/[company]/job.txt` from the private workspace root. Write package files into that company folder. Commit only to the private origin.

## Public repo map

| Path | Role |
| --- | --- |
| `AGENTS.md` | Always-on agent contract (this file) |
| `Architecture.md` | Public vs private split, install, upgrade |
| `scripts/check-package.sh` | Structural checker for a company package |
| `tests/check-package.test.sh` | Checker fixtures (valid, invalid, parity) |
| `.job-search/skills/` | `cv-package`, `email-reply`, `linkedin` |
| `.job-search/templates/candidate-data/` | Blank private master (`about.md`); do not fill with real data here |
| `.github/agents/` | Copilot custom agents |
| `.github/prompts/` | Copilot slash prompts |
| `.github/instructions/` | Copilot always-on private-data guard |
| `.github/hooks/` | Block generation without `AboutMe.md`; block committing private paths |
| `.archive/` | Superseded major versions only |

When package rules change, keep this file, `.job-search/skills/cv-package/SKILL.md`, `.github/agents/job-package.agent.md`, `.github/agents/cv-tailor.agent.md`, and `.github/prompts/generate-local-job-package.prompt.md` aligned. Prefer pointing at the skill over duplicating it.

## Commands

There is no package manager, app runtime, or CI workflow. The only automated check is the package checker.

```bash
bash tests/check-package.test.sh
```

From a private workspace root, after generating a package:

```bash
bash toolbox/scripts/check-package.sh Job-Applications/[company]
```

The checker reports missing files and schema violations in one run. It cannot tell whether a claim is true; compare every candidate claim to `AboutMe.md`.

If you change `scripts/check-package.sh`, update `tests/check-package.test.sh` and run it before finishing.

## Conventions

- Markdown for docs, skills, agents, and prompts. Bash for scripts. The checker uses `set -uo pipefail` so it can accumulate errors; tests use `set -euo pipefail`.
- Conventional commits (`feat`, `fix`, `chore`, `docs`, `refactor`, `test`) when the user asks for a commit.
- `.gitignore` already excludes `/AboutMe.md` and `/Job-Applications/`. Do not work around it.
- Do not invent achievements, titles, metrics, compensation, eligibility, or submission status.
- The user alone updates application status, sends messages, submits applications, and commits private files.

## Private workspace contract

When working from a private workspace, read `AboutMe.md` and `Job-Applications/[company]/job.txt` from that workspace root. Follow `toolbox/Architecture.md`, create private package outputs in the company folder, and maintain the application-tracker table in root `README.md`.

When a package is created, add a missing tracker row with status `Prepared — review required`. Never overwrite an existing status.

Reliability contract: treat `AboutMe.md` as the factual source of truth and `job.txt` as requirements, not candidate facts. Do not alter any existing generated package output unless the user explicitly requests that exact file be changed. When evidence is missing, record a gap rather than making a claim. New packages include matching `cv.md` and `cv.html`; the HTML is a printable rendering of the Markdown CV, not an additional source of facts.

### Title integrity

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

### Markdown and HTML parity

When `cv.md` changes, update `cv.html` in the same operation unless the user explicitly excludes `cv.html`. The visible wording, claims, dates, titles, metrics, and section order must remain consistent between both versions. Target a printable CV of 2–3 pages.

Immediately after the headline, include a header contact line with supported phone, email, and a short address (`City, Country` or `City, Region, Country`) from `AboutMe.md`. Never use a street, house number, or postal code. If no location is documented, omit the address and record the gap in `prep.md`. In `cv.html`, render that line in `<div class="contact">`.

Place the same canonical headline marker in both files:

```html
<!-- cv-headline: Evidence-supported headline | Functional keywords -->
```

Before finalizing, audit the current official job title, target job title, headline, short address, leadership level, certifications, years of experience, metrics, employer and product relationships, and Markdown/HTML parity. Then run the package checker and fix structural failures before reporting completion.
