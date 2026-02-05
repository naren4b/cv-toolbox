import json
import sys
import argparse
import os
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from jsonschema import validate, Draft7Validator
import textwrap

# Version constants
TEMPLATE_VERSION = "v1"
JSON_SCHEMA_VERSION = "v1"

def load_schema():
    schema_path = os.path.join("template", f"schema_{JSON_SCHEMA_VERSION}.json")
    if not os.path.exists(schema_path):
        print(f"Error: Schema {schema_path} not found. Run setup first.")
        sys.exit(1)
    with open(schema_path, 'r') as f:
        return json.load(f)['structure']

def validate_data(data, schema):
    try:
        validate(instance=data['body'], schema=schema['body'])
    except Exception as e:
        print(f"JSON validation error: {e}")
        sys.exit(1)

def format_section_content(section):
    """Format bullets and headings for PDF."""
    content = f"<b>{section['heading']}</b><br/>"
    for bullet in section.get('bullets', []):
        wrapped = textwrap.fill(bullet, width=90).replace('\n', '<br/>')
        content += f"&bull; {wrapped}<br/><br/>"
    return content

def generate_resume(data_path, output_path):
    with open(data_path, 'r') as f:
        data = json.load(f)
    
    schema = load_schema()
    validate_data(data, schema)
    
    doc = SimpleDocTemplate(output_path, pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)
    story = []
    styles = getSampleStyleSheet()
    
    # Custom styles matching ATS-friendly design (your docx: tables, bold headers)
    title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'],
                                 fontSize=24, spaceAfter=30, alignment=TA_CENTER,
                                 fontName='Helvetica-Bold')
    header_style = ParagraphStyle('CustomHeader', parent=styles['Heading2'],
                                  fontSize=14, spaceAfter=12, alignment=TA_LEFT,
                                  fontName='Helvetica-Bold')
    body_style = ParagraphStyle('CustomBody', parent=styles['Normal'],
                                fontSize=10, spaceAfter=6, alignment=TA_JUSTIFY,
                                leading=12)
    
    body_data = data['body']
    
    # Header/Name
    story.append(Paragraph(body_data['profile-name'].upper(), title_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Profile header
    story.append(Paragraph(body_data['profile-header']['title'], header_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Contact info table (like your docx)
    contact_data = [['LinkedIn', body_data['contact-info'][0]['text']],
                    ['Blog', body_data['contact-info'][1]['text']],
                    ['Phone', body_data['contact-info'][2]['text']],
                    ['Email', body_data['contact-info'][3]['text']],
                    ['Location', body_data['contact-info'][4]['text']]]
    contact_table = Table(contact_data, colWidths=[2*inch, 3*inch])
    contact_table.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('GRID', (0,0), (-1,-1), 0.5, 'black')  # Thin grid like docx
    ]))
    story.append(contact_table)
    story.append(Spacer(1, 0.3*inch))
    
    # Professional Summary
    summary_p = Paragraph(f"<b>{body_data['professional-summary']['title']}</b><br/>" +
                          textwrap.fill(body_data['professional-summary']['content'], 90).replace('\n', '<br/>'),
                          body_style)
    story.append(summary_p)
    story.append(Spacer(1, 0.3*inch))
    
    # Core Competencies (multi-column table)
    skills_flat = []
    for cat in body_data['core-competencies']['skills']:
        skills_flat.extend(cat['items'])
    skills_table = Table([skills_flat[i:i+3] for i in range(0, len(skills_flat), 3)],
                         colWidths=[2.2*inch]*3)
    skills_table.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('ALIGN', (0,0), (-1,-1), 'CENTER')
    ]))
    story.append(Paragraph("<b>Core Competencies</b>", header_style))
    story.append(skills_table)
    story.append(Spacer(1, 0.3*inch))
    
    # Professional Experience
    story.append(Paragraph("<b>Professional Experience</b>", header_style))
    for exp in body_data['professional-experience']['experiences']:
        pos_para = Paragraph(f"<b>{exp['position']}</b><br/>" +
                             f"<i>{exp['period']} | {exp['location']}</i>", body_style)
        story.append(pos_para)
        if exp.get('summary'):
            story.append(Paragraph(textwrap.fill(exp['summary'], 90).replace('\n', '<br/>'), body_style))
        for section in exp.get('sections', []):
            story.append(Paragraph(format_section_content(section), body_style))
        story.append(Spacer(1, 0.2*inch))
    
    # Education & Awards (similar structure)
    story.append(Paragraph("<b>Education</b>", header_style))
    for deg in body_data['education']['degrees']:
        story.append(Paragraph(f"&bull; {deg['degree']} | {deg['institution']} ({deg['period']})", body_style))
    
    story.append(Paragraph("<b>Awards & Recognition</b>", header_style))
    for award in body_data['awards-recognition']['awards']:
        story.append(Paragraph(f"&bull; {award['year']}: {award['title']}", body_style))
    
    doc.build(story)
    print(f"Generated: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Generate PDF resumes from template and data.json")
    parser.add_argument('data_files', nargs='+', help="Path(s) to data.json file(s)")
    parser.add_argument('--template-version', default=TEMPLATE_VERSION, help="PDF template version")
    args = parser.parse_args()
    
    template_path = os.path.join("template", f"template_{args.template_version}.pdf")
    if not os.path.exists(template_path):
        print(f"Error: Template {template_path} not found. Run: python src/setup.py")
        sys.exit(1)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    for data_file in args.data_files:
        output = f"resume_{os.path.basename(data_file).replace('.json', '')}_{timestamp}.pdf"
        generate_resume(data_file, output)

if __name__ == "__main__":
    main()
