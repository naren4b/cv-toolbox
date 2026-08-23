"""
CV Utility Script
-----------------
This script provides utilities for generating, filling, and rendering CVs in PDF and HTML formats.
It supports merging JSON data into PDF forms, rendering HTML from XML, and generating fillable PDF templates.

Main Features:
- Fill PDF forms from JSON data
- Render HTML and export PDF from XML inputs
- Generate fillable PDF templates

Author: [Your Name]
Date: [Update as needed]
"""

# --- Imports ---
import argparse
import json
import re
import html
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

# Third-party dependencies
from pypdf import PdfReader, PdfWriter
from pypdf.errors import EmptyFileError
from pypdf.generic import NameObject
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# --- Project Constants ---
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TEMPLATE = PROJECT_ROOT / "resources" / "cv-template.pdf"
DEFAULT_OUTPUT = PROJECT_ROOT / "build" / "user-cv.pdf"
DEFAULT_DATA_FILES = [
    PROJECT_ROOT / "data" / "user-data-cv-1-data.json",
    PROJECT_ROOT / "data" / "Job-details-data.json",
    PROJECT_ROOT / "data" / "extra-form-data.json",
]
# HTML/CV rendering defaults
DEFAULT_USER_INPUT_DIR = PROJECT_ROOT / "inputs" / "user"
DEFAULT_SYSTEM_INPUT_DIR = PROJECT_ROOT / "inputs" / "system"
DEFAULT_HTML_TEMPLATE = Path("templates") / "cv" / "cv-template-v1.html"
DEFAULT_THEME_CSS = Path("css") / "base.css"
THEMES = {
    "clean": {
        "font": "Arial, sans-serif",
        "accent": "#1f2937",
        "muted": "#4b5563",
    },
    "compact": {
        "font": "Verdana, sans-serif",
        "accent": "#0f172a",
        "muted": "#475569",
    },
    "modern": {
        "font": "'Trebuchet MS', sans-serif",
        "accent": "#0b3b2e",
        "muted": "#365c53",
    },
}


# --- PDF/JSON utilities ---
def load_json_file(file_path: Path) -> dict[str, Any]:
    """
    Load a JSON file and return its contents as a dictionary.
    Returns empty dict if file is empty.
    """
    raw = file_path.read_text(encoding="utf-8").strip()
    if not raw:
        return {}
    payload = json.loads(raw)
    if not isinstance(payload, dict):
        raise ValueError(f"Expected a JSON object in {file_path}")
    return payload


def deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    """
    Recursively merge two dictionaries, with override taking precedence.
    """
    merged = dict(base)
    for key, value in override.items():
        existing = merged.get(key)
        if isinstance(existing, dict) and isinstance(value, dict):
            merged[key] = deep_merge(existing, value)
        else:
            merged[key] = value
    return merged


def merge_json_files(json_files: list[Path]) -> dict[str, Any]:
    """
    Merge a list of JSON files, requiring version 'v1' if present. Later files override earlier ones.
    """
    merged: dict[str, Any] = {}
    for file_path in json_files:
        if not file_path.exists():
            raise FileNotFoundError(f"JSON data file not found: {file_path}")
        data = load_json_file(file_path)
        # If version is present at the top level, require v1
        version = data.get("version")
        if version is not None and version != "v1":
            raise ValueError(
                f"Input JSON file '{file_path}' must have version='v1' (found: {version!r})"
            )
        merged = deep_merge(merged, data)
    return merged


def flatten_data(data: Any, parent_key: str = "") -> dict[str, str]:
    """
    Flatten nested dictionaries/lists into a single-level dict with dot-separated keys.
    """
    flat: dict[str, str] = {}
    if isinstance(data, dict):
        for key, value in data.items():
            key_name = str(key)
            next_key = f"{parent_key}.{key_name}" if parent_key else key_name
            flat.update(flatten_data(value, next_key))
        return flat
    if isinstance(data, list):
        flat[parent_key] = ", ".join(str(item) for item in data)
        return flat
    if parent_key:
        flat[parent_key] = "" if data is None else str(data)
    return flat


def normalize_key(key: str) -> str:
    """
    Normalize a string key: lowercase and remove non-alphanumeric characters.
    """
    return re.sub(r"[^a-z0-9]", "", key.lower())


def build_candidate_lookup(flat_data: dict[str, str]) -> dict[str, str]:
    """
    Build a lookup table for flattened data, mapping normalized key variants to values.
    """
    lookup: dict[str, str] = {}
    for key, value in flat_data.items():
        if not key:
            continue
        leaf = key.split(".")[-1]
        variants = {
            key,
            leaf,
            key.replace(".", "_"),
            key.replace(".", " "),
            leaf.replace("_", " "),
        }
        for variant in variants:
            normalized = normalize_key(variant)
            if normalized and normalized not in lookup:
                lookup[normalized] = value
    return lookup


def map_data_to_pdf_fields(
    merged_data: dict[str, Any], pdf_fields: list[str]
) -> dict[str, str]:
    """
    Map merged JSON data to PDF form fields by normalized key matching.
    """
    flat_data = flatten_data(merged_data)
    lookup = build_candidate_lookup(flat_data)
    mapped: dict[str, str] = {}
    for field in pdf_fields:
        matched = lookup.get(normalize_key(field))
        if matched is not None:
            mapped[field] = matched
    return mapped


def read_pdf_field_names(template_path: Path) -> list[str]:
    """
    Read all form field names from a fillable PDF template.
    """
    try:
        reader = PdfReader(str(template_path))
    except EmptyFileError as exc:
        raise ValueError(f"Template PDF is empty: {template_path}") from exc
    fields = reader.get_fields() or {}
    return list(fields.keys())


def fill_pdf_form(
    template_path: Path, output_path: Path, data_dict: dict[str, str]
) -> None:
    """
    Fill a PDF form template with data and save as a non-editable PDF.
    """
    try:
        reader = PdfReader(str(template_path))
    except EmptyFileError as exc:
        raise ValueError(f"Template PDF is empty: {template_path}") from exc

    writer = PdfWriter()
    writer.clone_document_from_reader(reader)

    if hasattr(writer, "set_need_appearances_writer"):
        writer.set_need_appearances_writer(True)

    for page in writer.pages:
        writer.update_page_form_field_values(
            page,
            data_dict,
            auto_regenerate=True,
            flatten=True,
        )

    # Remove interactive form widgets and form dictionary for a non-editable PDF.
    writer.remove_annotations(subtypes=["/Widget"])
    if NameObject("/AcroForm") in writer._root_object:
        del writer._root_object[NameObject("/AcroForm")]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("wb") as output_file:
        writer.write(output_file)


# parse_args is unused and can be removed


# --- PDF Template Generation ---
def draw_section_title(c: canvas.Canvas, title: str, y: int) -> None:
    """
    Draw a section title with underline on the PDF canvas.
    """
    c.setFont("Helvetica-Bold", 14)
    c.drawString(40, y, title)
    c.line(40, y - 4, 570, y - 4)


def add_field(
    c: canvas.Canvas,
    name: str,
    label: str,
    x: int,
    y: int,
    width: int,
    height: int = 20,
    multiline: bool = False,
) -> None:
    """
    Add a text field to the PDF canvas at the specified position.
    """
    c.setFont("Helvetica", 10)
    c.drawString(x, y + height + 4, label)
    flags = 4096 if multiline else 0
    c.acroForm.textfield(
        name=name,
        tooltip=label,
        x=x,
        y=y,
        width=width,
        height=height,
        borderStyle="underlined",
        fieldFlags=flags,
    )


def create_fillable_cv(filename: Path) -> None:
    """
    Generate a fillable PDF CV template with standard fields.
    """
    filename.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(filename), pagesize=letter)
    c.setTitle("CV Template")
    # Page 1: Profile and core skills
    c.setFont("Helvetica-Bold", 22)
    c.drawString(40, 750, "CURRICULUM VITAE")
    draw_section_title(c, "Profile", 720)
    add_field(c, "Full Name", "Full Name", 40, 680, 250)
    add_field(c, "Current Title", "Current Title", 310, 680, 250)
    add_field(c, "Phone", "Phone", 40, 640, 170)
    add_field(c, "Email", "Email", 220, 640, 340)
    add_field(c, "Location", "Location", 40, 600, 250)
    add_field(c, "LinkedIn", "LinkedIn", 310, 600, 250)
    add_field(c, "Portfolio", "Portfolio", 40, 560, 520)
    draw_section_title(c, "Professional Summary", 535)
    add_field(c, "Summary", "Summary", 40, 455, 520, height=70, multiline=True)
    draw_section_title(c, "Core Competencies", 435)
    add_field(
        c,
        "Core Competencies",
        "Core Competencies",
        40,
        355,
        520,
        height=70,
        multiline=True,
    )
    draw_section_title(c, "Skills", 335)
    add_field(c, "Primary Skills", "Primary Skills", 40, 295, 520)
    add_field(c, "Secondary Skills", "Secondary Skills", 40, 255, 520)
    add_field(c, "Tech Stack", "Tech Stack", 40, 215, 520)
    c.showPage()
    # Page 2: Experience, education and achievements
    c.setFont("Helvetica-Bold", 22)
    c.drawString(40, 750, "CURRICULUM VITAE")
    draw_section_title(c, "Professional Experience", 720)
    add_field(
        c, "Experience 1", "Experience 1", 40, 640, 520, height=65, multiline=True
    )
    add_field(
        c, "Experience 2", "Experience 2", 40, 560, 520, height=65, multiline=True
    )
    add_field(
        c, "Experience 3", "Experience 3", 40, 480, 520, height=65, multiline=True
    )
    draw_section_title(c, "Job Target", 455)
    add_field(c, "Target Role", "Target Role", 40, 415, 250)
    add_field(c, "Company", "Company", 310, 415, 250)
    add_field(c, "Job Location", "Job Location", 40, 375, 250)
    add_field(c, "Expected CTC", "Expected CTC", 310, 375, 250)
    add_field(c, "Project Highlight", "Project Highlight", 40, 335, 520)
    draw_section_title(c, "Education and Certifications", 315)
    add_field(c, "Education", "Education", 40, 275, 520)
    add_field(c, "Certifications", "Certifications", 40, 235, 520)
    draw_section_title(c, "Awards", 215)
    add_field(c, "Awards", "Awards", 40, 145, 520, height=60, multiline=True)
    add_field(c, "Date", "Date", 40, 95, 170)
    add_field(c, "Signature_Box", "Signature", 390, 95, 170)
    c.save()


# --- HTML/CV Rendering ---
def load_xml(path: Path):
    """
    Load and parse an XML file, returning the root element.
    """
    return ET.parse(path).getroot()


def t(node, default=""):
    """
    Return the text of an XML node, or a default if node is None.
    """
    return (node.text or default).strip() if node is not None else default


def esc(s):
    """
    HTML-escape a string, treating None as empty.
    """
    return html.escape(s or "")


def split_summary(summary):
    """
    Split a summary into lead sentence and the rest.
    """
    parts = summary.split(".", 1)
    if len(parts) == 2:
        return parts[0].strip() + ".", parts[1].strip()
    return summary, ""


def render_skills(root):
    """
    Render skills XML as HTML chunks grouped by category.
    """
    chunks = []
    for cat in root.findall("category"):
        name = esc(cat.attrib.get("name", ""))
        items = " | ".join(esc(t(i)) for i in cat.findall("item"))
        if items.strip():
            chunks.append(
                f'<div class="skill-group"><strong>{name}:</strong> {items}</div>'
            )
    return "\n".join(chunks)


def render_work(root):
    """
    Render work experience XML as HTML.
    """
    out = []
    for company in root.findall("company"):
        out.append(f'<div class="company">{esc(company.attrib.get("name", ""))}</div>')
        for role in company.findall("role"):
            title = esc(role.attrib.get("title", ""))
            start = esc(role.attrib.get("start", ""))
            end = esc(role.attrib.get("end", ""))
            loc = esc(role.attrib.get("location", ""))
            out.append(
                f'<div class="role-line">{title} | {start} – {end} | {loc}</div>'
            )
            for sub in role.findall("subsection"):
                out.append(
                    f'<div class="subhead">{esc(sub.attrib.get("title", ""))}:</div>'
                )
                bullets = [f"<li>{esc(t(b))}</li>" for b in sub.findall("bullet")]
                if bullets:
                    out.append("<ul>" + "".join(bullets) + "</ul>")
            bullets = [f"<li>{esc(t(b))}</li>" for b in role.findall("bullet")]
            if bullets:
                out.append("<ul>" + "".join(bullets) + "</ul>")
    return "\n".join(out)


def render_education(root):
    """
    Render education and certifications XML as HTML.
    """
    out = []
    for item in root.findall("item"):
        if "degree" in item.attrib:
            out.append(
                f'<div class="edu-item">• <strong>{esc(item.attrib.get("degree", ""))}</strong><br>{esc(item.attrib.get("institution", ""))} | {esc(item.attrib.get("year_start", ""))} – {esc(item.attrib.get("year_end", ""))}</div>'
            )
        elif "certification" in item.attrib:
            out.append(
                f'<div class="edu-item">• <strong>{esc(item.attrib.get("certification", ""))}</strong><br>{esc(item.attrib.get("issuer", ""))} | {esc(item.attrib.get("date", ""))}</div>'
            )
    return "\n".join(out)


def render_awards(root):
    """
    Render awards section from XML as HTML.
    """
    awards = root.find("awards")
    if awards is None:
        return ""
    return "\n".join(
        f'<div class="award-item">• <strong>{esc(t(item).split(" – ")[0])}</strong>'
        + (
            f' – {esc(" – ".join(t(item).split(" – ")[1:]))}'
            if " – " in t(item)
            else ""
        )
        + "</div>"
        for item in awards.findall("item")
    )


def replace_all(template, mapping):
    """
    Replace all {{key}} in template with values from mapping.
    """
    for k, v in mapping.items():
        template = template.replace("{{" + k + "}}", v)
    return template


def add_theme(template: str, theme_name: str, base_css: str = "") -> str:
    """
    Inject theme CSS and class into HTML template.
    """
    theme = THEMES.get(theme_name, THEMES["clean"])
    theme_css = (
        "<style>\n"
        + (base_css + "\n" if base_css else "")
        + f"body {{ font-family: {theme['font']}; color: {theme['accent']}; }}\n"
        + f".title, .role-line {{ color: {theme['muted']}; }}\n"
        + "</style>"
    )
    if "</head>" in template:
        template = template.replace("</head>", theme_css + "\n</head>", 1)
    body_tag_pattern = re.compile(r"<body(\s[^>]*)?>", re.IGNORECASE)
    match = body_tag_pattern.search(template)
    if match:
        current = match.group(0)
        if "class=" in current:
            updated = re.sub(
                r'class="([^"]*)"', rf'class="\1 theme-{theme_name}"', current, count=1
            )
        else:
            updated = current[:-1] + f' class="theme-{theme_name}">'
        template = template.replace(current, updated, 1)
    return template


def export_pdf_from_html(html_path: Path, pdf_path: Path) -> None:
    """
    Export a PDF from an HTML file using WeasyPrint.
    """
    try:
        from weasyprint import HTML  # type: ignore
    except ImportError as exc:
        raise RuntimeError(
            "PDF export requires weasyprint. Install it with: pip install weasyprint"
        ) from exc
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    HTML(filename=str(html_path)).write_pdf(str(pdf_path))


# --- Unified CLI ---
def main() -> int:
    """
    Main entry point for the CV utility CLI.
    Supports subcommands for PDF fill, HTML render, and template generation.
    """
    parser = argparse.ArgumentParser(
        description="CV Utility: PDF fill, HTML render, or template generation."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # PDF fill subcommand
    pdf_parser = subparsers.add_parser("pdf", help="Fill PDF from JSON data")
    pdf_parser.add_argument(
        "--template",
        type=Path,
        default=DEFAULT_TEMPLATE,
        help="Path to source PDF template",
    )
    pdf_parser.add_argument(
        "--output", type=Path, default=DEFAULT_OUTPUT, help="Path for generated PDF"
    )
    pdf_parser.add_argument(
        "--data-files",
        type=Path,
        nargs="+",
        default=DEFAULT_DATA_FILES,
        help="JSON files to merge in order; later files override earlier values",
    )
    pdf_parser.add_argument(
        "--list-fields",
        action="store_true",
        help="List all PDF form field names and exit",
    )
    pdf_parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail if no merged values could be mapped to PDF form fields",
    )

    # HTML render subcommand
    html_parser = subparsers.add_parser(
        "html", help="Render HTML (and optional PDF) from XML inputs"
    )
    html_parser.add_argument(
        "--user-input-dir",
        type=Path,
        default=DEFAULT_USER_INPUT_DIR,
        help="Folder with user XMLs",
    )
    html_parser.add_argument(
        "--system-input-dir",
        type=Path,
        default=DEFAULT_SYSTEM_INPUT_DIR,
        help="Folder with system templates/css",
    )
    html_parser.add_argument(
        "--output-html",
        type=Path,
        default=None,
        help="Output HTML file path (default: ./generated_cv.html)",
    )
    html_parser.add_argument(
        "--template",
        type=Path,
        default=DEFAULT_HTML_TEMPLATE,
        help="HTML template path (relative to system dir unless absolute)",
    )
    html_parser.add_argument(
        "--theme-css",
        type=Path,
        default=DEFAULT_THEME_CSS,
        help="Base CSS path (relative to system dir unless absolute)",
    )
    html_parser.add_argument(
        "--theme", choices=sorted(THEMES.keys()), default="clean", help="Theme preset"
    )
    html_parser.add_argument(
        "--job-xml", type=Path, default=None, help="Optional job-specific work XML file"
    )
    html_parser.add_argument(
        "--output-pdf",
        type=Path,
        default=None,
        help="Optional output PDF path (default: ./generated_cv.pdf)",
    )

    # PDF template generation subcommand
    tmpl_parser = subparsers.add_parser(
        "template", help="Generate fillable PDF template"
    )
    tmpl_parser.add_argument(
        "--output", type=Path, default=DEFAULT_TEMPLATE, help="Output PDF template path"
    )

    args = parser.parse_args()

    if args.command == "pdf":
        if not args.template.exists():
            raise FileNotFoundError(f"Template PDF not found: {args.template}")
        pdf_fields = read_pdf_field_names(args.template)
        if args.list_fields:
            if not pdf_fields:
                print("No PDF form fields found.")
                return 0
            print("PDF form fields:")
            for name in pdf_fields:
                print(f"- {name}")
            return 0
        merged_data = merge_json_files(args.data_files)
        mapped_data = map_data_to_pdf_fields(merged_data, pdf_fields)
        if args.strict and not mapped_data:
            raise ValueError(
                "No JSON values matched any PDF fields; run with --list-fields and adjust input keys"
            )
        fill_pdf_form(args.template, args.output, mapped_data)
        print(f"Generated PDF: {args.output}")
        print(f"Matched fields: {len(mapped_data)}/{len(pdf_fields)}")
        return 0

    elif args.command == "html":
        user_input_dir = args.user_input_dir
        system_input_dir = args.system_input_dir

        def require_version_v1(root, fname):
            """Raise error if XML root does not have version='v1'."""
            v = root.attrib.get("version")
            if v != "v1":
                raise ValueError(
                    f"Input file '{fname}' must have version=\"v1\" in the root element (found: {v!r})"
                )

        personal = load_xml(user_input_dir / "personal-info.xml")
        require_version_v1(personal, "personal-info.xml")
        skills = load_xml(user_input_dir / "skills.xml")
        require_version_v1(skills, "skills.xml")
        work = load_xml(
            args.job_xml if args.job_xml else user_input_dir / "work-exp.xml"
        )
        require_version_v1(
            work, "work-exp.xml" if not args.job_xml else str(args.job_xml)
        )
        education = load_xml(user_input_dir / "education.xml")
        require_version_v1(education, "education.xml")
        template_path = args.template
        if not template_path.is_absolute():
            template_path = system_input_dir / template_path
        theme_css_path = args.theme_css
        if not theme_css_path.is_absolute():
            theme_css_path = system_input_dir / theme_css_path
        base_css = ""
        if theme_css_path.exists():
            base_css = theme_css_path.read_text(encoding="utf-8")
        template = template_path.read_text(encoding="utf-8")
        template = add_theme(template, args.theme, base_css)
        summary = t(personal.find("summary"))
        lead, rest = split_summary(summary)
        mapping = {
            "name": esc(t(personal.find("name"))),
            "title": esc(t(personal.find("title"))),
            "phone": esc(t(personal.find("./contact/phone"))),
            "email": esc(t(personal.find("./contact/email"))),
            "location": esc(t(personal.find("./contact/location"))),
            "linkedin": esc(t(personal.find("./contact/linkedin"))),
            "website": esc(t(personal.find("./contact/website"))),
            "summary_lead": esc(lead),
            "summary_rest": esc(rest),
            "skills_html": render_skills(skills),
            "work_html": render_work(work),
            "education_html": render_education(education),
            "awards_html": render_awards(education),
        }
        # Ask for output directory if not given
        output_html = args.output_html or Path.cwd() / "generated_cv.html"
        output_html.parent.mkdir(parents=True, exist_ok=True)
        output_html.write_text(
            rendered := replace_all(template, mapping), encoding="utf-8"
        )
        print(f"HTML created: {output_html}")
        if args.output_pdf is not None:
            output_pdf = args.output_pdf
        else:
            output_pdf = Path.cwd() / "generated_cv.pdf"
        if args.output_pdf or (
            not args.output_pdf
            and "--output-pdf"
            in [a for a in vars(args) if getattr(args, a) is not None]
        ):
            export_pdf_from_html(output_html, output_pdf)
            print(f"PDF created: {output_pdf}")
        return 0

    elif args.command == "template":
        create_fillable_cv(args.output)
        print(f"Interactive template generated successfully: {args.output}")
        return 0

    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
