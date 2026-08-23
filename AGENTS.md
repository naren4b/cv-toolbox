# Job Search Toolbox — Operating Rules

## Scope

This is a reusable toolbox only. It must not contain active job applications, candidate data, recruiter emails, or application-status records.

## Private working location

Google Drive is the only active workspace. It owns:

- canonical profile information in `data/`;
- leads and packages in `jobs/[company]/`;
- the live portfolio view in `Job Search 2026 — Master Tracker`.

All output is created, reviewed, and tracked in the corresponding Drive job folder.

## Job package contract

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

- Capture the lead source in the Drive job folder.
- Review application packages in Google Drive only.
- Do not submit an application or send a message without the user's direction.
- Mark an application submitted only after the user confirms it or evidence is saved.
- Archive before permanent deletion, which also needs user approval.
- Use Git commit history as the change record for this reusable toolbox.
