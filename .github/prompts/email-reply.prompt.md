---
description: "Draft recruiter email replies, salary negotiations, follow-ups, and thank-you notes. Use when you receive a recruiter message or need to respond to an HR email."
agent: "agent"
argument-hint: "Paste the recruiter email or describe the scenario (e.g., 'recruiter asking for CTC and notice period')"
tools: [read, search]
---

Draft a professional email reply based on the recruiter message or scenario provided.

## Steps

1. **Read** the approved private Drive `AboutMe.md` master file and the recruiter message before drafting
2. **Read** the approved private Drive `AboutMe.md` master file for runtime candidate details
3. **Identify the scenario** from the user's input and match to the correct template:
   - Template 1: Cold inbound from recruiter
   - Template 2: Applying to a job posting
   - Template 3: Recruiter questionnaire (CTC, notice, etc.)
   - Template 4: Follow-up after no response
   - Template 5: Post-interview thank you
   - Template 6: Declining an opportunity
4. **Personalise** the template using the recruiter's name, company, role title, and candidate details from `data/`
5. If a tailored CV exists in `Job-Applications/[company]/`, reference its key points in the reply
6. **Read** the recruiter email from `Job-Applications/[company]/email.txt` if provided
7. **Write** the reply to `Job-Applications/[company]/email-reply.md`

## Rules

- Keep recruiter replies under **150 words**
- Mirror 2–3 keywords from the recruiter's message or JD
- Read approved compensation, notice-period, and personal details only from private Drive `AboutMe.md`
- **Retention reward** — read the amount and vesting date from private Drive `AboutMe.md`; mention it only when relevant.
- CTC and salary expectations must use a **range**, never a single number
- "Reason for change" must be positive and forward-looking — use one of the 4 ready options from the guide
- For international roles, mention **Canadian PR** status
- Suggest the CV filename as `Candidate_CV_[Company]_[Role].pdf`

## Output Format

Provide:
1. **Subject line** (using the formula from the guide)
2. **Email body** (ready to copy-paste)
3. **Checklist** of items to verify before sending

## Writing Style — Must Sound Human
- The email must read like a real person typed it, not a template engine
- Use natural, conversational English — the way a senior professional actually writes emails
- BANNED phrases: "I'm excited to", "I bring a wealth of", "I'm passionate about", "leverage", "utilize", "endeavour", "it's worth noting", "synergy", "holistic", "delve into"
- Keep sentences short. Don't stack three clauses with commas.
- Start with "Hi [Name]," not "Dear Sir/Madam" or "I hope this email finds you well"
- End with "Best regards" or "Thanks" — not "Warm regards" or "Looking forward to hearing from you at your earliest convenience"
- Don't over-explain. State your point and move on.
- Read the draft aloud. If it sounds like an AI wrote it, rewrite it.
