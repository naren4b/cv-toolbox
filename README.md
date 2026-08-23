# my-cv

Personal career management workspace — CV tailoring, resume generation, job application tracking, and professional profile optimization.

## Quick Start

### 0) Initialize candidate input data

The runtime `data/` folder is private and gitignored. Bootstrap it from templates:

```bash
mkdir -p data && cp data-template/* data/
```

Then fill placeholders in:
- `data/Master-CV.md`
- `data/current-employer.txt`
- `data/personal.txt`
- `data/salary.txt`

| Task | How |
|---|---|
| **Tailor a CV** | Place JD in `jobs/[company]/jd.txt`, then use the **CV Tailor** agent or `/apply-to-job` prompt |
| **Research a company** | Use the **Company Intel** agent with the company name and job title |
| **Reply to a recruiter** | Save email to `jobs/[company]/email.txt`, then use `/email-reply` prompt |
| **Prepare for interview** | Use `/interview-prep` prompt with the company name |
| **Generate PDF** | Export `cv-${date}.md` to PDF using a markdown-to-PDF tool or browser print |

## Agents

Custom AI agents available from the agent picker (`@`) in Copilot Chat.

| Agent | When to Use | What It Produces |
|---|---|---|
| **CV Tailor** | You have a JD and want a tailored CV + gap analysis | `cv-${date}.md` + `prep.txt` in `jobs/[company]/` |
| **Email Reply** | You have recruiter mail + JD and need a response draft | `email-reply.md` (and optional `cover-letter.txt`) in `jobs/[company]/` |
| **Company Intel** | Researching a company before interview — financials, culture, salary | `[company]-info.md` in `jobs/[company]/` |

### How to use an Agent
1. Open Copilot Chat
2. Click the agent picker or type `@`
3. Select **CV Tailor**, **Email Reply**, or **Company Intel**
4. Paste the JD or provide the company name

## Prompts

Reusable workflows available via `/` slash commands in Copilot Chat.

| Prompt | When to Use | What It Produces |
|---|---|---|
| `/apply-to-job` | Full application package for a new JD | `cv-${date}.md` + `prep.txt` + `cover-letter.txt` + `email-reply.md` |
| `/email-reply` | Replying to a recruiter email | `email-reply.md` with subject line + body + checklist |
| `/interview-prep` | Preparing for an upcoming interview | Top 10 Q&A, gap defence scripts, questions to ask |

### How to use a Prompt
1. Open Copilot Chat
2. Type `/` and select the prompt
3. Provide the input (JD text, company name, or recruiter email)

## Skills (SKILL.md files)

Master reference guides that agents and prompts read automatically. You can also read them directly.

| Skill | Location | Purpose |
|---|---|---|
| **Master Career Profile** | `create-my-cv/SKILL.md` | Single source of truth — all skills, achievements, experience, summary templates, keyword bank |
| **Email & Cover Letter** | `create-my-cv/email-reply/SKILL.md` | Email templates, salary data, CTC/notice details, negotiation scripts, cover letter framework |
| **LinkedIn Optimization** | `create-my-cv/Linkedin/SKILL.md` | Profile audit, headline options, about section rewrite, skills strategy, posting routine |

## Job Folder Convention

```
jobs/[company]/
  jd.txt              # INPUT:  Original job description
  email.txt           # INPUT:  Recruiter/HR email
  cv-${date}.md       # OUTPUT: Tailored CV (date in DD-MM-YYYY)
  prep.txt            # OUTPUT: Gap analysis, talking points, interview prep
  cover-letter.txt    # OUTPUT: Cover letter
  email-reply.md     # OUTPUT: Reply to recruiter/HR email
  [company]-info.md   # OUTPUT: Company research, financials, salary benchmarks
```

## Structure

| Directory | Purpose |
|---|---|
| `data/` | Canonical runtime input data: CV, personal info, employer info, salary |
| `data-template/` | Generic reusable templates to initialize `data/` for any candidate |
| `create-my-cv/` | Master career profile (SKILL.md), LinkedIn guide, email/cover letter templates |
| `jobs/` | Per-company folders: JD, tailored CV, prep, cover letter, email replies |
| `personal/` | Raw personal data (CV, profile, salary, education) |
| `question-bank/` | Interview prep question banks |
| `.github/agents/` | Custom Copilot agents (CV Tailor, Company Intel) |
| `.github/prompts/` | Copilot prompts (apply-to-job, email-reply, interview-prep) |
| `.github/hooks/` | Runtime guard hooks (blocks generation if required `data/` inputs are missing) |

## Guardrails

- The workspace hook `.github/hooks/data-input-guard.json` enforces required input files in `data/` before prompts/tools run.
- Required files: `data/Master-CV.md`, `data/current-employer.txt`, `data/personal.txt`, `data/salary.txt`.
- The same hook chain enforces job inputs for generation actions:
- `jobs/[company]/cv-${date}.md`, `jobs/[company]/prep.txt`, `jobs/[company]/cover-letter.txt` require `jobs/[company]/jd.txt`.
- `jobs/[company]/email-reply.md` requires `jobs/[company]/jd.txt` and `jobs/[company]/email.txt`.

See [AGENTS.md](AGENTS.md) for detailed AI agent conventions and workflows.