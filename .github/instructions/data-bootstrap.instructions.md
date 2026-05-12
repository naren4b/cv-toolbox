---
applyTo: "**"
---

# Data Bootstrap — Read Before Any Task

Every agent, skill, and prompt in this workspace must load these files **before** producing any output. They are the authoritative source for all personal, employment, and career data.

| File | Read for |
|------|----------|
| [`data/Master-CV.md`](../../data/Master-CV.md) | Canonical approved CV — baseline for all tailoring; takes precedence over SKILL.md on any fact |
| [`data/current-employer.txt`](../../data/current-employer.txt) | Employer, job title, notice period, CTC, retention reward, reason for change |
| [`data/personal.txt`](../../data/personal.txt) | DOB, India address, Canada address, phone numbers |
| [`data/salary.txt`](../../data/salary.txt) | Remuneration breakdown (use `current-employer.txt` for negotiations) |

## Routing Rules

- **Address / phone**: Default India. For Canadian or international roles, use Canada address and +1 phone.
- **Retention reward**: Read amount and vesting date from `data/current-employer.txt`. Mention only if today's date is **before** the vesting date.
- **CTC in emails**: Always give a **range**, never a single number. Calibrate upper end using Company Intel salary benchmarks.
- **Master-CV.md vs SKILL.md conflict**: `data/Master-CV.md` wins — it is the approved baseline.

## Never

- Hardcode salary, address, notice period, or personal details in any output file
- Fabricate skills, achievements, or certifications not in `data/Master-CV.md` or `create-my-cv/SKILL.md`
- Start email replies with "Dear Sir/Madam" — use "Hi [Name],"
