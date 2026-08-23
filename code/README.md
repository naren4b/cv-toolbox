# CV Generator — Usage Guide

This project automates CV generation in PDF and HTML formats using structured user data and templates.

## Prerequisites
- Python 3.12+
- Make (for automation)
- All dependencies in `src/requirements.txt`

## Quick Start
1. **Install dependencies:**
   ```sh
   make install
   ```
2. **Prepare your data:**
   - Place your XML files in `inputs/user/` (see system templates for structure)
   - Ensure all root elements have `version="v1"`
3. **Render HTML CV:**
   ```sh
   make render-html
   ```
   - Output: `build/generated_cv.html` (or specify your own with `--output-html`)
   - If not given, output will be in the current directory as `generated_cv.html`
4. **Render PDF CV:**
   ```sh
   make render-pdf
   ```
   - Output: `build/generated_cv.pdf` (or specify your own with `--output-pdf`)
   - If not given, output will be in the current directory as `generated_cv.pdf`
5. **Render job-specific CV:**
   ```sh
   make render-job RENDER_JOB_XML=inputs/user/work-exp.xml
   ```

## Command Reference
- **HTML/PDF rendering:**
   - All rendering is handled by `src/app.py` using subcommands:
      - `html` — Render HTML (and optional PDF) from XML
      - `pdf` — Fill PDF from JSON data (legacy)
      - `template` — Generate a fillable PDF template
- **Output location:**
   - If you do not specify `--output-html` or `--output-pdf`, files are created in your current directory as `generated_cv.html` and `generated_cv.pdf`.
- **Example:**
   ```sh
   python src/app.py html --user-input-dir inputs/user --system-input-dir inputs/system --output-html mycv.html --output-pdf mycv.pdf --theme clean
   ```

## Data Structure
- **User XMLs:**
  - `personal-info.xml`, `skills.xml`, `work-exp.xml`, `education.xml`
  - All must have `version="v1"` in the root element
- **System templates:**
  - HTML: `inputs/system/templates/cv/cv-template-v1.html`
  - CSS: `inputs/system/css/base.css`

## Makefile Targets
- `make install` — Set up Python venv and install dependencies
- `make render-html` — Render HTML CV
- `make render-pdf` — Render PDF CV
- `make render-job RENDER_JOB_XML=...` — Render job-specific CV
- `make clean` — Remove build outputs and caches

## Troubleshooting
- If you see a version error, ensure all XML root elements have `version="v1"`.
- For PDF/HTML errors, check your data files and template paths.
- Generated PDF and HTML files are automatically ignored by git (see `.gitignore`).

---

For advanced usage, see comments in `src/app.py` and the Makefile.