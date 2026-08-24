---
description: "Create a complete job application package in the user's Google Drive workspace."
agent: "Job Application Manager"
argument-hint: "Provide the Google Drive company folder containing job.txt."
tools: [read, edit, search, web, todo]
---

# New Job Workflow

Use this as the single entry point for a new job application.

## Location

All active work happens in Google Drive, not in this GitHub repository. The user creates `Job-Applications/[company]/` in Google Drive and adds `job.txt`, including the job description and its original source link.

Read the approved Drive `data/` files before creating output. Use the reusable skills and templates in this repository only as guidance.

## Create in the Google Drive job folder

- `analysis.md` — role summary, fit, gaps, and recommended CV type.
- `cv-DD-MM-YYYY.md` — tailored CV.
- `prep.md` — talking points, likely questions, and preparation checklist.
- `cover-letter.md` — concise role-specific letter.
- `company-info.md` — sourced company research.
- `status.md` — stage, evidence, deadline, and next action.
- `email-reply.md` — only when `email.txt` is present.

## Required rules

- Keep `job.txt` unchanged.
- Use supported facts only; call out genuine gaps.
- Do not submit applications or send emails.
- Treat drafts as ready to apply only after the package is complete and reviewed.
- Update the Google Drive portfolio status only after the user confirms the relevant change.
