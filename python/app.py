#!/usr/bin/env python3
"""
Convert JSON CV to PDF using fpdf2
Install: pip install fpdf2
"""

from fpdf import FPDF, XPos, YPos
from pathlib import Path
from datetime import datetime
import json


# Read JSON file
json_file = Path(__file__).parent / "data.json"

if not json_file.exists():
    print(f"Error: JSON file not found at {json_file}")
    exit(1)

# Parse JSON
with open(json_file, "r", encoding="utf-8") as f:
    cv_data = json.load(f)

if not cv_data or "body" not in cv_data:
    print("Error: Could not find CV content in JSON")
    exit(1)

body = cv_data["body"]


# Create PDF
class PDF(FPDF):
    def header(self):
        pass

    def footer(self):
        pass


pdf = PDF(format="Letter")
pdf.set_margins(left=15, top=15, right=15)
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)


# Helper function to safely add text
def add_text(
    text, font_family="Helvetica", font_style="", font_size=9, indent=0, spacing=4
):
    if not text or not text.strip():
        return
    # Sanitize text - replace unicode characters with ASCII equivalents
    text = text.replace("\u2014", "--")  # em dash
    text = text.replace("\u2013", "-")  # en dash
    text = text.replace("\u2019", "'")  # right single quotation mark
    text = text.replace("\u201c", '"')  # left double quotation mark
    text = text.replace("\u201d", '"')  # right double quotation mark
    text = text.replace("\u2022", "-")  # bullet point
    text = text.replace("\u00a0", " ")  # non-breaking space
    # Remove any remaining non-latin1 characters
    text = text.encode("latin-1", errors="replace").decode("latin-1")

    pdf.set_font(font_family, font_style, font_size)
    pdf.set_x(15 + indent)
    pdf.multi_cell(0, spacing, text.strip(), new_x=XPos.LMARGIN, new_y=YPos.NEXT)


# Process content from JSON
# Profile Name
if "profile-name" in body:
    add_text(body["profile-name"], font_style="B", font_size=18, spacing=6)
    pdf.ln(1)

# Profile Header
if "profile-header" in body:
    header = body["profile-header"]
    if "title" in header:
        add_text(header["title"], font_size=10, spacing=4)
        pdf.ln(1)
    if "contact-info" in header:
        for contact in header["contact-info"]:
            if contact.get("type") == "href":
                add_text(contact.get("text", ""), font_size=9, spacing=3)
            else:
                add_text(contact.get("text", ""), font_size=9, spacing=3)
        pdf.ln(1)

# Professional Summary
if "professional-summary" in body:
    section = body["professional-summary"]
    pdf.ln(2)
    add_text(section.get("title"), font_style="B", font_size=12, spacing=5)
    pdf.ln(1)
    add_text(section.get("content"), font_size=9, spacing=4)
    pdf.ln(1)

# Core Competencies
if "core-competencies" in body:
    section = body["core-competencies"]
    pdf.ln(2)
    add_text(section.get("title"), font_style="B", font_size=12, spacing=5)
    pdf.ln(1)
    for skill in section.get("skills", []):
        add_text(f"{skill['category']}: {skill['items']}", font_size=9, spacing=4)
        pdf.ln(0.5)

# Professional Experience
if "professional-experience" in body:
    section = body["professional-experience"]
    pdf.ln(2)
    add_text(section.get("title"), font_style="B", font_size=12, spacing=5)
    pdf.ln(1)
    
    for experience in section.get("experiences", []):
        pdf.ln(1)
        # Job title, period, location
        add_text(
            f"{experience['position']} | {experience['period']} | {experience['location']}",
            font_style="B",
            font_size=10,
            spacing=5,
        )
        
        # Summary if exists
        if "summary" in experience:
            pdf.ln(0.5)
            add_text(experience["summary"], font_size=9, spacing=4)
        
        # Bullets if exists
        if "bullets" in experience:
            for bullet in experience["bullets"]:
                add_text(f"- {bullet}", font_size=9, indent=3, spacing=4)
        
        # Sections with subsections (Nokia role)
        if "sections" in experience:
            for subsection in experience["sections"]:
                pdf.ln(0.5)
                add_text(subsection["heading"], font_style="B", font_size=9, spacing=4)
                for bullet in subsection.get("bullets", []):
                    add_text(f"- {bullet}", font_size=9, indent=3, spacing=4)

# Education
if "education" in body:
    section = body["education"]
    pdf.ln(2)
    add_text(section.get("title"), font_style="B", font_size=12, spacing=5)
    pdf.ln(1)
    
    for degree in section.get("degrees", []):
        pdf.ln(0.5)
        add_text(degree["degree"], font_style="B", font_size=10, spacing=4)
        add_text(
            f"{degree['institution']} | {degree['period']}",
            font_size=9,
            indent=2,
            spacing=4,
        )

# Awards & Recognition
if "awards-recognition" in body:
    section = body["awards-recognition"]
    pdf.ln(2)
    add_text(section.get("title"), font_style="B", font_size=12, spacing=5)
    pdf.ln(1)
    
    for award in section.get("awards", []):
        add_text(
            f"{award['year']} - {award['title']}", font_size=9, spacing=4
        )
        pdf.ln(0.5)

# Generate output filename with date
name = "NARENDRANATH_PANDA"
date_str = datetime.now().strftime("%Y-%m-%d")
output_file = Path(__file__).parent / f"{name}_{date_str}.pdf"

try:
    pdf.output(str(output_file))
    print(f"✓ PDF generated successfully: {output_file}")
    print(f"  File size: {output_file.stat().st_size / 1024:.2f} KB")
    print(f"  Pages: {pdf.page_no()}")
except Exception as e:
    print(f"Error generating PDF: {e}")
    import traceback

    traceback.print_exc()
    exit(1)
