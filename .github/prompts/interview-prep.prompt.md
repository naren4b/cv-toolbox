---
description: "Generate targeted interview prep questions and answers from a JD. Use when preparing for an upcoming interview."
agent: "agent"
argument-hint: "Paste the JD or provide the company name"
tools: [read, search]
---

Generate a targeted interview preparation guide for the provided Job Description.

## Steps

1. **Read** the approved private Drive `data/about.md` master file for candidate context
2. **Use** the supported facts and achievement library in the private Drive `data/about.md` master file
3. **Read** the interview question bank at [question-bank/README.md](../../question-bank/README.md)
4. **Analyse the JD** to identify the top 10 technical and behavioural topics likely to be tested
5. If a `prep.txt` already exists in `jobs/[company]/`, read it for gap context

## Output Structure

### Part 1 — Top 10 Interview Questions
For each question:
- The question (phrased as the interviewer would ask it)
- **Why they're asking** (what competency it tests)
- **How to answer** (structured approach using STAR format where applicable)
- **Your evidence** (specific metrics and examples from SKILL.md Section C/D)

### Part 2 — Skill Gap Questions (Prepare Defensive Answers)
For each gap identified in the JD:
- Likely probing question
- Scripted response that acknowledges the gap and pivots to transferable skills

### Part 3 — Questions to Ask Them
5–6 insightful questions that demonstrate domain knowledge and strategic thinking.

### Question Categories to Cover
- Architecture / System Design (at least 2)
- Hands-on Technical Depth (at least 2)
- Incident / RCA / Production Scenarios (at least 2)
- Leadership / Team / Culture (at least 2)
- Domain-Specific (at least 1)
- FinOps / Cost (if relevant to JD)

## Rules
- Pull real metrics from SKILL.md Section C for every answer — never use vague claims
- Match question difficulty to the JD's seniority level
- Include at least one "war story" answer using a real incident/achievement from Section D
- Reference the question-bank for relevant existing questions to adapt

## Writing Style — Must Sound Human
- Write answers the way a real engineer would explain things in an interview — not rehearsed, not robotic
- Use first person naturally: "I set up...", "We ran into...", "What worked was..."
- BANNED phrases: "leverage", "utilize", "spearheaded", "orchestrated", "holistic", "synergy", "it's worth noting", "delve into"
- Keep STAR answers conversational. Don't label sections "Situation:", "Task:" etc. — just tell the story naturally.
- Use plain words: "set up" not "established", "ran" not "managed", "hit" not "achieved"
- Include pauses and transitions a real person would use: "So basically...", "The tricky part was...", "What we ended up doing was..."
- Avoid sounding over-prepared. The answer should feel like you're recalling a real experience, not reading a script.
