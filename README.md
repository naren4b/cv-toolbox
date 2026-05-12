# my-cv

Personal career management workspace — CV tailoring, resume generation, job application tracking, and professional profile optimization.

## Quick Start

| Task | How |
|---|---|
| **Tailor a CV** | Place JD in `jobs/[company]/jd.txt`, then use the **CV Tailor** agent or `/apply-to-job` prompt |
| **Research a company** | Use the **Company Intel** agent with the company name and job title |
| **Reply to a recruiter** | Save email to `jobs/[company]/email.txt`, then use `/email-reply` prompt |
| **Prepare for interview** | Use `/interview-prep` prompt with the company name |
| **Generate PDF (Python)** | `cd code/python && pip install -r requirements.txt && python app.py` |
| **Generate PDF (Docker)** | `cd code/resume-generator && docker build -t resume-gen . && docker run -v $(pwd)/data:/app/data resume-gen data.json` |
| **HTML CV** | Open `code/html/index.html` in browser → Print to PDF |

## Agents

Custom AI agents available from the agent picker (`@`) in Copilot Chat.

| Agent | When to Use | What It Produces |
|---|---|---|
| **CV Tailor** | You have a JD and want a tailored CV + gap analysis | `cv.md` + `prep.txt` in `jobs/[company]/` |
| **Company Intel** | Researching a company before interview — financials, culture, salary | `company-intel.txt` in `jobs/[company]/` |

### How to use an Agent
1. Open Copilot Chat
2. Click the agent picker or type `@`
3. Select **CV Tailor** or **Company Intel**
4. Paste the JD or provide the company name

## Prompts

Reusable workflows available via `/` slash commands in Copilot Chat.

| Prompt | When to Use | What It Produces |
|---|---|---|
| `/apply-to-job` | Full application package for a new JD | `cv.md` + `prep.txt` + `cover-letter.txt` + `email-reply.md` |
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
  cv.md               # OUTPUT: Tailored CV
  prep.txt            # OUTPUT: Gap analysis, talking points, interview prep
  cover-letter.txt    # OUTPUT: Cover letter
  email-reply.md     # OUTPUT: Reply to recruiter/HR email
  company-intel.txt   # OUTPUT: Company research, financials, salary benchmarks
```

## Structure

| Directory | Purpose |
|---|---|
| `create-my-cv/` | Master career profile (SKILL.md), LinkedIn guide, email/cover letter templates |
| `jobs/` | Per-company folders: JD, tailored CV, prep, cover letter, email replies |
| `personal/` | Raw personal data (CV, profile, salary, education) |
| `code/python/` | fpdf2-based PDF generator |
| `code/resume-generator/` | Docker + reportlab PDF generator |
| `code/html/` | HTML/CSS CV with print-to-PDF |
| `question-bank/` | Interview prep question banks |
| `.github/agents/` | Custom Copilot agents (CV Tailor, Company Intel) |
| `.github/prompts/` | Copilot prompts (apply-to-job, email-reply, interview-prep) |

See [AGENTS.md](AGENTS.md) for detailed AI agent conventions and workflows.