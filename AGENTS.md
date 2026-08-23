# my-cv workspace

## One job workflow

Use `.github/prompts/apply-to-job.prompt.md` as the only entry point for a new job. The user creates `jobs/[company]/` and puts the original posting in `job.txt`. That is the only canonical job-description input.

The workflow reads the approved candidate data first, then creates a complete, organized application package in the same folder. It never requires or creates `jd.txt`.

## Source of truth

Read these before creating job-specific output:

1. `data/Master-CV.md` — approved factual CV baseline; it wins if sources conflict.
2. `data/current-employer.txt`
3. `data/personal.txt`
4. `data/salary.txt`
5. `create-my-cv/SKILL.md` — approved skills and achievement library.

Do not invent a skill, date, title, metric, certification, or submission status. Update `data/` only when the user explicitly provides or approves a factual correction.

## Job-folder contract

```text
jobs/[company]/
  job.txt              # required input: original job description
  email.txt            # optional input: recruiter message
  analysis.md          # fit, gaps, and selected base CV
  cv-DD-MM-YYYY.md     # tailored CV
  prep.md              # interview preparation
  cover-letter.md      # cover letter
  company-info.md      # sourced company research
  email-reply.md       # only when email.txt exists
  status.md            # current state, deadline, and next action
```

Preserve `job.txt`. Keep every job-specific artifact in that job folder. Do not delete or move earlier applications without explicit permission.

## Specialist roles

- **Job Application Manager:** validates inputs, coordinates output, and owns `status.md`.
- **CV Tailor:** produces `analysis.md`, the tailored CV, and `prep.md`.
- **Company Intel:** produces sourced `company-info.md`.
- **Email Reply:** writes `email-reply.md` only if `email.txt` exists and may write `cover-letter.md`.

## Completion checks

Before saying a package is complete, verify that required files exist, facts match `data/Master-CV.md`, gaps are labeled, sources are linked for company research, and `status.md` does not imply a submission without evidence.

## Application status

Every job folder needs `status.md`, and `jobs/STATUS.md` is the live portfolio view. Use only: New, In preparation, Ready to apply, Submitted, Recruiter response, Interviewing, Offer, Closed, or Needs review. Never infer Submitted or Closed from the presence of a CV alone.

## Writing style

Use short, direct human language. Avoid corporate filler and unsupported claims. Keep recruiter email replies concise and role-specific.
