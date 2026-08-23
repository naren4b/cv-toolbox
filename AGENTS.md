# Job Search Toolbox — Operating Rules

## Scope

This repository is a reusable toolbox only. It contains prompts, agents, skills, templates, and process documentation. It must not be used to store active job applications, candidate data, recruiter emails, or application status records.

## Single working location

Google Drive is the only active workspace. The user keeps:

- Canonical profile information in Google Drive `data/`.
- Every lead and application package in Google Drive `jobs/[company]/`.
- The live portfolio view in Google Drive `jobs/STATUS.md`.

The GitHub toolbox may guide generation, but all output is created, reviewed, and tracked in the corresponding Google Drive job folder.

## Job package contract in Google Drive

```text
jobs/[company]/
  job.txt
  email.txt                 # optional
  analysis.md
  cv-DD-MM-YYYY.md
  prep.md
  cover-letter.md
  company-info.md
  email-reply.md            # only when email.txt exists
  status.md
```

`job.txt` is the canonical job-description input. Do not use `jd.txt` for new work.

## Operating rules

- Leads may come from email, phone calls, referrals, LinkedIn, or job portals. Record the source link or contact in the Drive job folder.
- Review all application packages in Google Drive only.
- Do not submit an application or send a message without the user's direction.
- Mark an application `Submitted` only after the user confirms it or evidence is saved.
- Never permanently delete material. Archive first and obtain the user's approval before deletion.
- Commit major changes to this reusable toolbox with a concise changelog entry.
