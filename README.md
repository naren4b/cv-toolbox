<img width="1758" height="836" alt="image" src="https://github.com/user-attachments/assets/9d9a412c-1316-4830-8f70-78ae0bb0bf9f" />


# Job Search Toolbox

**Current version:** `v0.0.11`

**Objective:** provide reusable AI instructions, prompts, agents, and skills for creating tailored job-application packages while keeping all personal data in a private repository.

This public repository is the toolbox. Download a tagged release into your private workspace as `toolbox/`; do not add private files here.

## Setup

1. Create and clone a private workspace repository.
2. Download `cv-toolbox` into the local, ignored `toolbox/` directory using the release steps in [Architecture.md](Architecture.md).
```bash
printf '/toolbox/\n' >> .gitignore
VERSION=v0.0.11 # Choose the release deliberately
mkdir -p toolbox
curl -fsSL https://github.com/naren4b/cv-toolbox/archive/refs/tags/$VERSION.tar.gz \
  | tar -xz --strip-components=1 -C toolbox
```
3. In the private workspace root, add `AboutMe.md` and `Job-Applications/[company]/job.txt`.

## Use

In the private workspace, type:

```text
Read toolbox/AGENTS.md and toolbox/Architecture.md. Generate the job package for Job-Applications/[company] using AboutMe.md and that company’s job.txt. Create cv.md, cv.html, prep.md, thinking.md, and email.md or cover-letter.md. Do not submit or send anything.
```

Commit generated files to the private workspace repository only.

Before reviewing a newly generated package, run its structural quality checks:

```bash
bash toolbox/scripts/check-package.sh Job-Applications/[company]
```

The checker reports all missing files and schema violations in one run. It complements human fact-checking against `AboutMe.md`; it cannot determine whether a claim is true.
