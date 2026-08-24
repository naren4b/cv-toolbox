# Job Search Toolbox Architecture

## Purpose

This is a reusable public-safe toolbox. Private candidate information and application packages exist only in the local checkout (or an accessible private store), never in Git.

## Private local contract

```text
AboutMe.md                              # single private candidate source of truth
Job-Applications/[company]/
  job.txt                               # input: role description and source
  cv.md                                 # generated tailored CV
  prep.md                               # generated preparation and gap analysis
  thinking.md                           # generated concise decision record
  email.md                              # generated recruiter email, when relevant
  cover-letter.md                       # generated application letter, when relevant
```

`AboutMe.md` and `Job-Applications/` are ignored by Git. A Drive, S3, or other private-store link can be used only if the local agent can read it; outputs remain local and ignored.

## Job-package process

1. Read `AboutMe.md` and the company’s `job.txt`.
2. Select exactly one profile category: Senior SRE Engineer, AWS Solutions Architect, or Engineering Manager.
3. Create or refresh the package files in the company folder.
4. Use supported facts only and state genuine gaps in `prep.md`.
5. Keep `thinking.md` as a short decision record—not hidden chain-of-thought.
6. The user alone sends messages, submits applications, and confirms status.

## Toolbox layout

```text
.github/       agents, prompts, instructions, and safety hooks
.job-search/   reusable skills, templates, and portal research
.archive/      preserved historical generic material
AGENTS.md      compact agent entry contract
Architecture.md detailed operating design
README.md      quick setup and use
```

## Agent safeguards

- Never change `AboutMe.md` or `job.txt` while generating a package.
- Never invent achievements, qualifications, compensation, or submission status.
- Never commit private inputs or generated packages.
- Never submit an application or send a message without the user.
