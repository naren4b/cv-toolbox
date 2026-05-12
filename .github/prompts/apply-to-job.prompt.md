---
description: "Full job application package — tailored CV, cover letter, and recruiter email reply for a specific JD. Use when applying to a new job."
agent: "CV Tailor"
argument-hint: "Paste the JD or provide company name + job title"
tools: [read, edit, search, todo]
---

Generate a complete job application package for the provided Job Description.

## Steps

1. **Read** `data/Master-CV.md` — canonical approved CV (baseline for all tailoring)
2. **Read** the master career profile at [SKILL.md](../../create-my-cv/SKILL.md) — tailoring process, skills index, quantified achievements
3. **Read** `data/current-employer.txt` — CTC, notice period, retention reward
4. **Read** the email/cover letter guide at [email-reply/SKILL.md](../../create-my-cv/email-reply/SKILL.md)
5. **Analyse the JD** and create the job folder at `jobs/[company]/`
6. **Produce these files**:

### File 1: `jobs/[company]/cv-DD-MM-YYYY.md`
Tailored CV following the Step 1–4 process in the master SKILL.md. Use today's actual date for the filename (e.g. `cv-12-05-2026.md`).

### File 2: `jobs/[company]/prep.txt`
Gap analysis with skill match matrix, talking points, risk assessment, and interviewer questions.

### File 3: `jobs/[company]/cover-letter.txt`
Cover letter using the 4-paragraph framework from the email-reply SKILL.md:
- Paragraph 1: Hook — who you are + why this role
- Paragraph 2: Value — 3 strongest JD matches with metrics
- Paragraph 3: Leadership + culture fit
- Paragraph 4: Call to action

### File 4: `jobs/[company]/email-reply.md`
Ready-to-send recruiter email using Template 2 (Applying to a Job Posting) from the email-reply SKILL.md. Include a pre-filled recruiter questionnaire response.

## Rules
- Mirror the JD's exact terminology in all outputs
- Include at least 2 quantified achievements from SKILL.md Section C
- Flag skill gaps with risk levels and mitigation strategies
- For international roles, mention Canadian PR status
- Ask clarifying questions if the JD is ambiguous

## Writing Style — Must Sound Human
- Write every output like a real person wrote it. No AI smell.
- Use short, direct sentences. Mix in sentence fragments where natural.
- BANNED phrases (instant AI detection): "leverage", "utilize", "spearheaded", "orchestrated", "endeavour", "in order to", "it's worth noting", "I bring a wealth of", "I'm passionate about", "cutting-edge", "synergy", "holistic", "delve into"
- BANNED bullet starters: "Successfully...", "Responsible for..."
- Start bullets with plain verbs: Built, Ran, Led, Cut, Shipped, Set up, Moved, Migrated, Fixed
- Prefer plain English: "set up" not "established", "ran" not "managed", "built" not "architected"
- No exclamation marks in formal docs
- Emails should sound like a senior engineer writing to a peer, not a template
- Cover letters should sound confident and direct — not stiff or overly formal
- Read every sentence aloud. If it sounds like a press release or LinkedIn influencer post, rewrite it.
