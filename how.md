# Job Application Playbook

> **How to use**: When you get a call/email about a new role, follow this checklist
> end-to-end. Replace `[company]` with the actual company folder name.

---

## Phase 0: Setup — Create the Job Folder

| Step | Action | You do | AI does |
|------|--------|--------|---------|
| 0a | Create folder `jobs/[company]/` | `mkdir jobs/[company]` | — |
| 0b | Paste the JD | Save as `jobs/[company]/jd.txt` | — |
| 0c | Paste the recruiter email (if any) | Save as `jobs/[company]/email.txt` | — |

---

## Phase 1: Analysis — Understand the Role

| Step | Action | Prompt to give | Output file | Source |
|------|--------|----------------|-------------|--------|
| 1a | **Tailor CV** | `@CV Tailor — [company], [job title]` | `jobs/[company]/cv.md` | `create-my-cv/SKILL.md` |
| 1b | **Gap analysis & interview prep** | _(produced automatically with 1a)_ | `jobs/[company]/prep.txt` | JD vs SKILL.md |

> **What happens**: The CV Tailor agent reads your master SKILL.md, analyses the JD,
> generates a tailored CV, flags skill gaps, and creates interview talking points.
> It never fabricates skills — only uses your real experience.

---

## Phase 2: Respond to Recruiter

| Step | Action | Prompt to give | Output file | Source |
|------|--------|----------------|-------------|--------|
| 2a | **Draft email reply** | `Draft the email reply for [company]` | `jobs/[company]/email-reply.md` | `create-my-cv/email-reply/SKILL.md` |
| 2b | **Write cover letter** | `Write a cover letter for [company]` | `jobs/[company]/cover-letter.txt` | `create-my-cv/email-reply/SKILL.md` |

> **What's included in the email reply** (all read from source files, not hardcoded):
> - Total exp, relevant exp
> - CTC / ECTC (from `current-employer.txt`; ECTC calibrated using Company Intel agent salary benchmarks)
> - Notice period (from `current-employer.txt`)
> - Current location (from `current-employer.txt` / `personal.txt`)
> - Canadian PR: Yes
> - Retention reward (from `current-employer.txt` — auto-included if today < vesting date)

---

## Phase 3: Research & Prepare

| Step | Action | Prompt to give | Output file |
|------|--------|----------------|-------------|
| 3a | **Company intel** | `@Company Intel — [company], [job title]` | `jobs/[company]/company-intel.txt` |
| 3b | **Deep interview prep** | `Help me prep for the [company] interview` | Review `prep.txt` + `question-bank/` |

> **Company intel covers**: Revenue, headcount, tech stack, Glassdoor ratings,
> salary benchmarks, recent news, culture signals, and strategic insights.

---

## Phase 4: Generate PDF & Send

| Step | Action | How |
|------|--------|-----|
| 4a | **Generate PDF resume** | Export `cv.md` to PDF using a markdown-to-PDF tool or browser print |
| 4b | **Final review** | Proofread CV PDF + cover letter + email reply |
| 4c | **Send** | Reply to recruiter with: CV (PDF) + cover letter + filled questionnaire |

---

## Phase 5: Post-Send (Optional)

| Step | Action | Prompt to give |
|------|--------|----------------|
| 5a | **LinkedIn optimization** | `Optimize my LinkedIn for the [job title] role` |
| 5b | **Mock interview** | `Run a mock interview for [company]` |
| 5c | **Salary negotiation prep** | `Help me negotiate salary for [company]` |

---

## Quick Reference — File Map

```
jobs/[company]/
  jd.txt              # INPUT   — Original job description
  email.txt           # INPUT   — Recruiter/HR email
  cv.md               # OUTPUT  — Tailored CV (markdown)
  prep.txt            # OUTPUT  — Gap analysis + interview prep
  email-reply.md     # OUTPUT  — Reply to recruiter
  cover-letter.txt    # OUTPUT  — Cover letter
  [company]-info.md   # OUTPUT  — Company research & salary benchmarks
```

## Quick Reference — Key Source Files

| File | Contains |
|------|----------|
| `create-my-cv/SKILL.md` | Master career profile, skills, achievements, CV tailoring rules |
| `create-my-cv/email-reply/SKILL.md` | Email templates, salary data, negotiation scripts |
| `create-my-cv/email-reply/current-employer.txt` | Employer details, CTC breakdown, retention reward |
| `create-my-cv/Linkedin/SKILL.md` | LinkedIn audit & optimization guide |
| `question-bank/` | Interview Q&A banks (K8s, Cloud, Linux, SRE, Leadership) |