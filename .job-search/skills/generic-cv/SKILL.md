---
name: generic-cv
description: Use when generating or refreshing a complete non-job-specific CV from AboutMe.md, including a master CV, generic CV, or Master-CV folder.
---

# Generic CV Skill

## Inputs

- Private workspace `AboutMe.md` — the only factual source of truth.
- Profile lens definitions in `cv-package` — used only to keep competency coverage complete when those lenses change, not to pick a target title.

Do not read `job.txt`. This CV is not tailored to a vacancy.

## Outputs

Write only:

- `Master-CV/cv.md`
- `Master-CV/cv.html`

Do not create `thinking.md`, `prep.md`, `email.md`, `cover-letter.md`, or a tracker row.

## Source versioning

Stamp both CV files with the same marker:

```html
<!-- cv-source: about=<12-hex> profiles=<12-hex> -->
```

Compute hashes from the private workspace root:

```bash
skill_root="toolbox"
[[ -d toolbox/.job-search/skills ]] || skill_root="."
about=$(sha256sum AboutMe.md | awk '{print substr($1,1,12)}')
profiles=$(sha256sum "$skill_root/.job-search/skills/cv-package/SKILL.md" | awk '{print substr($1,1,12)}')
```

On macOS, use `shasum -a 256` instead of `sha256sum`.

Refresh rules:

1. If `AboutMe.md` is missing, stop and ask for it.
2. Compute current `about` and `profiles` hashes.
3. If `Master-CV/cv.md` and `Master-CV/cv.html` both exist and both markers match the current hashes, report that the generic CV is up to date and do not rewrite.
4. If either file is missing, a marker is absent, or either hash differs, regenerate **both** files in the same operation.
5. Never leave a hash mismatch between `cv.md` and `cv.html`.

A hash change means `AboutMe.md` or the profile-lens skill changed. Treat that as permission to update `Master-CV/` even if those files already exist.

## Processing workflow

1. Read the complete `AboutMe.md`.
2. Compute source hashes.
3. Apply the refresh rules above.
4. When generating, include every supported employer and official title. For each role, keep the strongest 3–5 evidenced bullets; do not drop a role to save space.
5. Include every supported certification and award in the required tables.
6. Use a balanced complete CV: cover SRE, AWS/architecture, and platform-leadership evidence that `AboutMe.md` actually supports. Do not select a single job-package profile lens and do not use a target job title as the headline.
7. Write `cv.md` and `cv.html`, stamp both with the current `cv-source` marker, then run the claim and parity audits.

## CV rules

Reuse the fact, title-integrity, short-address, table, and HTML rules from `.job-search/skills/cv-package/SKILL.md`, with these differences:

- There is no target role. The headline is the candidate’s evidence-supported professional identity from `AboutMe.md`.
- Completeness beats keyword tailoring: do not omit a supported employer, certification, or award because it is less fashionable.
- Keep 3–5 strongest bullets per role. Target a printable CV of 2–3 pages.
- After the headline, include `Phone | Email | City, Country` using a short address from `AboutMe.md`. Never use a street or postal address.
- Place `<!-- cv-headline: [exact visible headline] -->` and the `cv-source` marker in both files.
- In `cv.html`, render the contact line in `<div class="contact">`, load Roboto from Google Fonts, and include print CSS.

## Preflight

Do not finish until: (1) both files exist, (2) `cv-source` hashes match the current `AboutMe.md` and `cv-package` skill, (3) headline markers match, (4) the header has a short address when location is documented, (5) Education & Certifications and Awards & Recognition are tables in both formats, (6) `cv.html` uses Roboto and print CSS, and (7) every claim is supported by `AboutMe.md`.
