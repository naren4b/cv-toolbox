# Project Guidelines — my-cv

## Boot Sequence — Read These First

Before **any** task, load the four input files from `data/`. Full routing rules in [`.github/instructions/data-bootstrap.instructions.md`](.github/instructions/data-bootstrap.instructions.md).

| File | Contains |
|------|----------|
| `data/Master-CV.md` | Canonical approved CV — takes precedence over SKILL.md on any fact |
| `data/current-employer.txt` | Employer, title, notice period, CTC, retention reward, reason for change |
| `data/personal.txt` | DOB, India + Canada addresses, phone numbers |
| `data/salary.txt` | Remuneration breakdown |

## Purpose

This is a personal career management workspace for **Narendranath Panda** — a Senior Platform Engineer / R&D Architect with 19+ years of experience. The workspace is used to:

1. Maintain a master career profile and tailor CVs for specific job applications
2. Generate PDF resumes from JSON data
3. Manage job application workflows (JD analysis, tailored CVs, prep docs, email replies)
4. Optimize LinkedIn and other professional profiles

## Workspace Structure

| Directory | Purpose |
|---|---|
| `data/` | **Central input data** — `Master-CV.md`, `current-employer.txt`, `salary.txt`, `personal.txt`. Read these before any agent or skill runs. |
| `create-my-cv/` | SKILL.md guides for CV tailoring, LinkedIn optimization, and email/cover letter templates |
| `create-my-cv/SKILL.md` | **Master career profile** — single source of truth for all career data, skills, achievements, and CV tailoring instructions |
| `create-my-cv/Linkedin/` | LinkedIn profile optimization guide |
| `create-my-cv/email-reply/` | Email reply templates, cover letter framework, salary negotiation data |
| `jobs/` | Job-specific folders — each contains JD, tailored CV, prep, cover letter, and email replies |
| `personal/` | Raw personal data files (cv.txt, profile.txt, salary.txt, education.txt) |
| `question-bank/` | Interview prep questions (K8s, Cloud, Linux, SRE, Leadership) |
| `devops-qb.md` | DevOps question bank |

## Key Conventions

### CV Tailoring Workflow
When asked to tailor a CV for a job:
1. **Read** `create-my-cv/SKILL.md` — this contains the full tailoring process (Steps 1–4), master skills, quantified achievements, and summary templates
2. **Analyse** the JD from `jobs/[company]/jd.txt`
3. **Create** output files inside `jobs/[company]/`
4. **Never fabricate** skills or achievements — only use content from the master SKILL.md

### Job Folder Structure
Each job application folder under `jobs/` follows this pattern:
```
jobs/[company]/
  jd.txt              # INPUT:  Original job description
  cv.md               # OUTPUT: Tailored CV
  prep.txt            # OUTPUT: Gap analysis, talking points, interview prep
  cover-letter.txt    # OUTPUT: Cover letter
  email.txt           # INPUT:  Recruiter/HR email
  email-reply.md     # OUTPUT: Reply to recruiter/HR email
  [company]-info.md   # OUTPUT: Company research, financials, salary benchmarks
```

### Email & Cover Letter Workflow
When asked to draft emails or cover letters:
1. **Read** `create-my-cv/email-reply/SKILL.md` — contains templates, salary data, negotiation scripts, and the recruiter questionnaire format
2. **Read** `data/current-employer.txt` — employer details, CTC breakdown, retention reward
3. **Read** the recruiter email from `jobs/[company]/email.txt` if available
4. **Run Company Intel agent** for the company + role — saves to `jobs/[company]/[company]-info.md` (skip if file already exists). Use salary benchmarks from the report to set Expected CTC range.
5. **Write** the reply to `jobs/[company]/email-reply.md`
6. **Write** the cover letter to `jobs/[company]/cover-letter.txt`
7. **Retention reward** — read amount and vesting date from `data/current-employer.txt`. Only mention if today's date is before the vesting date.

### LinkedIn Optimization
When asked about LinkedIn:
1. **Read** `create-my-cv/Linkedin/SKILL.md` — contains current vs recommended audit, headline options, about section rewrite, skills strategy
2. Current LinkedIn export is in `create-my-cv/Linkedin/profile.txt`

### Data Files
- `personal/cv.txt` — plain-text master CV
- `personal/profile.txt` — LinkedIn profile export

## Interaction Style

- This workspace is used by a **career counsellor persona** — be interactive, ask clarifying questions when requirements are ambiguous
- When creating tailored CVs, always flag **skill gaps** between the candidate's profile and the JD
- Use quantified metrics from the master SKILL.md (Section C — Impact Library) in every CV and cover letter
- Target role: primarily **DevOps Lead / Manager**, but also Platform Engineer, SRE, Cloud Architect
- Notice period, location, Canadian PR status: Read from `data/current-employer.txt`

## Writing Style — All Outputs Must Sound Human

Every CV, email, cover letter, prep doc, and company report produced by any agent or prompt must sound like a real person wrote it. Zero AI smell.

**BANNED phrases** (instant detection as AI-generated):
"leverage", "utilize", "spearheaded", "orchestrated", "endeavour", "in order to", "it's worth noting", "I bring a wealth of", "I'm passionate about", "cutting-edge", "synergy", "holistic", "delve into", "proven track record", "I'm excited to", "I'm thrilled", "seasoned", "results-driven"

**Rules**:
- Short, direct sentences. Vary length. Fragments are fine.
- Start bullets with plain verbs: Built, Ran, Led, Cut, Shipped, Set up, Moved, Fixed, Rolled out
- Never start with "Successfully..." or "Responsible for..."
- Use contractions naturally (I'm, I've, I'd)
- Prefer plain English: "set up" not "established", "ran" not "managed", "built" not "architected"
- Emails: "Hi [Name]," not "Dear Sir/Madam". End with "Best regards" not "Warm regards".
- Read every sentence aloud — if it sounds like a press release or LinkedIn influencer post, rewrite it
