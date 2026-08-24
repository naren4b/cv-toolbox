---
applyTo: "**"
---

# Private workspace rule

This public repository is a reusable AI toolbox only. Do not place candidate information, job descriptions, generated CVs, recruiter messages, or application status here.

For real work, import this repository into a private workspace as `toolbox/` (for example with `git subtree`). The private workspace owns and versions:

- `AboutMe.md`
- `Job-Applications/[company]/job.txt`
- generated `cv.md`, `prep.md`, `thinking.md`, `email.md`, and `cover-letter.md`

When working in that private workspace, read private inputs from its root and read reusable instructions from `toolbox/`. Commit generated files only to the private workspace `origin`, never to this public toolbox repository.

Use supported facts only; never fabricate experience, contact details, compensation, or submission status. The user alone submits applications and sends messages.
