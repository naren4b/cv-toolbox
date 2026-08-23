---
description: "Single entry point for a new job application. Create jobs/[company]/ and add job.txt; this workflow creates the organized application package."
agent: "Job Application Manager"
argument-hint: "Provide the company folder name, or place the job description in jobs/[company]/job.txt"
tools: [read, edit, search, web, todo]
---

# New Job Workflow

Use this as the single entry point for every new job application.

## Trigger

The user creates `jobs/[company]/` and adds the job description as:

`jobs/[company]/job.txt`

`job.txt` is the canonical job-description input. Do not create or require a duplicate `jd.txt`.

## Read before writing

1. `data/Master-CV.md` — canonical facts. It wins if other files disagree.
2. `data/current-employer.txt`
3. `data/personal.txt`
4. `data/salary.txt`
5. `create-my-cv/SKILL.md` — tailoring guidance and approved achievement library.
6. `create-my-cv/email-reply/SKILL.md` — only when drafting an email or cover letter.
7. `jobs/[company]/job.txt`

If any required data file or `job.txt` is missing, stop and state exactly what is needed. Never infer, invent, or silently reuse facts from another job folder.

## Workflow

1. Read `job.txt` and identify the company, role, location, seniority, deadline, must-have requirements, preferred requirements, and repeated keywords.
2. Select the closest approved base CV: Engineering, Architect, or Director. Until those three base CVs are available, use `data/Master-CV.md`.
3. Create or update these files in the same job folder:
   - `analysis.md` — JD summary, requirement match, gaps, risk level, and role/CV choice.
   - `cv-DD-MM-YYYY.md` — tailored CV. Use the actual date.
   - `prep.md` — talking points, likely interview questions, questions to ask, and a practical preparation checklist.
   - `cover-letter.md` — concise role-specific cover letter.
   - `company-info.md` — company, product, financial, engineering-culture, and salary research with sources and unknowns clearly labeled.
   - `status.md` — application status, deadline, artifacts created, next action, and submission evidence when available.
4. If `email.txt` exists, create or update `email-reply.md`. If it does not exist, leave it out and note that in `status.md`.
5. Check all output against the source facts. Match the job language, retain only supported claims, and flag genuine gaps rather than hiding them.
6. Do not submit applications, send emails, or claim that an application is submitted. Record a submission only when the user provides confirmation or the workflow has verifiable evidence.

## Status tracking

Every job folder must contain `status.md`. Use one of these stages only:

- `New` — job description saved; package not started.
- `In preparation` — application artifacts are being drafted.
- `Ready to apply` — package is complete and awaiting user review or submission.
- `Submitted` — submission is verified by confirmation, application ID, sent email, or user statement.
- `Recruiter response` — an inbound response has been saved in `email.txt`.
- `Interviewing` — interview details or feedback are saved in the folder.
- `Offer` — a written offer is saved or confirmed by the user.
- `Closed` — rejected, withdrawn, expired, or no longer pursued; state the reason.
- `Needs review` — historical files exist but the current stage is not verified.

`status.md` must show the stage, last confirmed update, deadline when known, evidence, next action, and any submission confirmation. Update `jobs/STATUS.md` whenever a folder status changes.

## Output rules

- Use short, direct, human-sounding language.
- Do not use unsupported metrics or skills.
- Preserve the original `job.txt` unchanged.
- Keep all job-specific outputs inside `jobs/[company]/`.
- Do not alter `data/` unless the user explicitly confirms a factual update.
- Do not move or delete existing files without explicit permission.

## Folder contract

```text
jobs/[company]/
  job.txt              # input: original job description
  email.txt            # optional input: recruiter message
  analysis.md          # output: fit and gap analysis
  cv-DD-MM-YYYY.md     # output: tailored CV
  prep.md              # output: interview preparation
  cover-letter.md      # output: cover letter
  company-info.md      # output: company research
  email-reply.md       # output when email.txt exists
  status.md            # output: current application state and next action
```

## Specialist routing

- CV Tailor: create `analysis.md`, the tailored CV, and `prep.md`.
- Company Intel: create `company-info.md`.
- Email Reply: create `email-reply.md` only when `email.txt` exists; it may also create the cover letter.

The New Job Workflow owns orchestration, filenames, validation, and final status tracking.
