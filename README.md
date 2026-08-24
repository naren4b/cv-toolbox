# Job Search Toolbox

**Objective:** provide a reusable local workflow for producing private, tailored job-application packages without committing personal information to Git.

Create a local checkout of this repository, then open it in Codex, VS Code, or Cursor.

## Setup

1. Create a private `AboutMe.md` in the repository root.
2. Create `Job-Applications/[company]/job.txt` for each role.
3. Keep both local: they are ignored by Git.

## Use

Run the **Local Job Package** agent or **Generate Local Job Package** prompt for the company folder. It creates local, ignored `cv.md`, `prep.md`, `thinking.md`, plus `email.md` or `cover-letter.md` when relevant.

See [Architecture.md](Architecture.md) for the workflow, privacy rules, profile categories, and internal toolbox layout.
