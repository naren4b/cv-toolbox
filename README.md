# Job Search Toolbox

This repository stores reusable agents, prompts, skills, and templates. It supports a local private workspace in a checkout, but private inputs and generated packages are ignored and must never be committed.

## Local private workflow

```text
AboutMe.md                              # private master candidate file
Job-Applications/[company]/
  job.txt                               # required input: original role and source
  cv.md                                 # generated tailored CV
  prep.md                               # generated preparation and gap analysis
  thinking.md                           # generated decision record and output plan
  email.md                              # generated recruiter email, when relevant
  cover-letter.md                       # generated application letter, when relevant
```

Open the checkout in Codex, VS Code, or Cursor. Run the **Local Job Package** agent or the **Generate Local Job Package** prompt from the company directory.

The workflow selects one profile category: **Senior SRE Engineer**, **AWS Solutions Architect**, or **Engineering Manager**. It uses only supported facts from `AboutMe.md`; it never submits applications or sends email.

## Privacy

`AboutMe.md` and `Job-Applications/` are intentionally ignored by Git. A Drive, S3, or other private-storage link may be used only when the local workspace can read it; generated outputs still remain local and ignored.
