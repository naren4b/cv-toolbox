---
description: Generate or refresh the complete generic CV in Master-CV from AboutMe.md.
---

# Generate Generic CV

When this toolbox is imported as `toolbox/`, follow `toolbox/.job-search/skills/generic-cv/SKILL.md`.

1. Read `AboutMe.md` from the private workspace root. Do not use `job.txt`.
2. Compute 12-character SHA-256 prefixes for `AboutMe.md` (`about`) and `toolbox/.job-search/skills/cv-package/SKILL.md` (`profiles`).
3. If `Master-CV/cv.md` and `Master-CV/cv.html` both exist and both contain `<!-- cv-source: about=<hash> profiles=<hash> -->` matching those values, report that the generic CV is up to date and stop.
4. Otherwise create or replace `Master-CV/cv.md` and `Master-CV/cv.html` in the same operation. Include every supported role, certification, and award; keep 3–5 strongest bullets per role; target 2–3 pages. Use an evidence-supported headline from `AboutMe.md`, never a target job title. After the headline, add `Phone | Email | City, Country` with a short address only. Stamp both files with matching `cv-headline` and `cv-source` markers. `cv.html` must match `cv.md` fact-for-fact, put the contact line in `<div class="contact">`, and use Roboto from Google Fonts with print CSS.
5. Do not create job-package files, update the tracker, submit anything, or commit private files.
