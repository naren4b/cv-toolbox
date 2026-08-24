# Job Search Toolbox

**Objective:** provide a reusable local workflow for producing private, tailored job-application packages without committing personal information to Git.

Create a local checkout of this repository, then open it in Codex, VS Code, or Cursor.

## Setup

1. Create a private `AboutMe.md` in the repository root.
2. Create `Job-Applications/[company]/job.txt` for each role.
3. Keep both local: they are ignored by Git.

## Use

Run this prompt once for a single company, replacing `[company]` with its folder name:

```text
Generate the local job package for Job-Applications/[company]. Read AboutMe.md and job.txt, select the best profile category, and create cv.md, prep.md, thinking.md, and email.md or cover-letter.md. Do not modify the inputs, submit an application, send email, or commit private files.
```

For multiple companies, type:

```text
For every Job-Applications/[company] folder that contains job.txt, generate or refresh the local job package. Read AboutMe.md and each job.txt, select the best profile category for each role, and create cv.md, prep.md, thinking.md, and email.md or cover-letter.md. Do not modify inputs, submit applications, send email, or commit private files.
```

You can also run the **Local Job Package** agent or **Generate Local Job Package** prompt for the company folder.

See [Architecture.md](Architecture.md) for the workflow, privacy rules, profile categories, and internal toolbox layout.
