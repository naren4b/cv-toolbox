#!/usr/bin/env python3
"""
PDF Form Generator with fillable fields
Install: pip install reportlab
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfform
from reportlab.lib.colors import black, blue, red, grey
from pathlib import Path
from datetime import datetime
import json


class PDFFormGenerator:
    """Creates fillable PDF forms based on CV structure"""
    
    def __init__(self, template_path, output_path=None):
        self.template = self._load_json(template_path)
        self.width, self.height = letter
        self.margin = 0.75 * inch
        self.y_position = self.height - self.margin
        self.output_path = output_path or self._generate_output_path()
        
    def _load_json(self, path):
        """Load JSON template"""
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f"Template not found: {path}")
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    
    def _generate_output_path(self):
        """Generate output filename"""
        date_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"CV_FORM_{date_str}.pdf"
        return Path(__file__).parent / filename
    
    def _add_label(self, c, text, y, font_size=10, bold=False):
        """Add a label (non-editable text)"""
        c.setFont("Helvetica-Bold" if bold else "Helvetica", font_size)
        c.setFillColor(black)
        c.drawString(self.margin, y, text)
    
    def _add_text_field(self, c, field_name, x, y, width, height=20, multiline=False, tooltip=""):
        """Add a fillable text field"""
        c.setFillColor(grey, alpha=0.1)
        c.rect(x, y - height + 5, width, height, fill=1, stroke=1)
        
        if multiline:
            pdfform.textFieldAbsolute(
                c, field_name,
                x, y - height + 5,
                width, height,
                multiline=True,
                borderColor=blue,
                fillColor=None,
                textColor=black,
                forceBorder=True,
                tooltip=tooltip
            )
        else:
            pdfform.textFieldRelative(
                c, field_name,
                x, y - height + 5,
                width, height,
                borderColor=blue,
                fillColor=None,
                textColor=black,
                forceBorder=True,
                tooltip=tooltip
            )
    
    def create_form(self):
        """Create the PDF form"""
        c = canvas.Canvas(str(self.output_path), pagesize=letter)
        y = self.y_position
        
        # Title
        c.setFont("Helvetica-Bold", 24)
        c.setFillColor(blue)
        c.drawCentredString(self.width / 2, y, "CV / RESUME FORM")
        y -= 40
        
        c.setFont("Helvetica", 10)
        c.setFillColor(black)
        c.drawCentredString(self.width / 2, y, "Fill in the fields below and save the PDF")
        y -= 30
        
        # PERSONAL INFORMATION SECTION
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(red)
        c.drawString(self.margin, y, "PERSONAL INFORMATION")
        y -= 25
        
        # Full Name
        self._add_label(c, "Full Name:", y, bold=True)
        self._add_text_field(c, "profile_name", self.margin + 120, y, 400, tooltip="Enter your full name")
        y -= 35
        
        # Professional Title
        self._add_label(c, "Professional Title:", y, bold=True)
        self._add_text_field(c, "profile_title", self.margin + 120, y, 400, tooltip="e.g., Senior Platform Engineer")
        y -= 40
        
        # CONTACT INFORMATION
        c.setFont("Helvetica-Bold", 12)
        c.drawString(self.margin, y, "Contact Information")
        y -= 25
        
        # Email
        self._add_label(c, "Email:", y)
        self._add_text_field(c, "email", self.margin + 80, y, 200, tooltip="Your email address")
        y -= 30
        
        # Phone
        self._add_label(c, "Phone:", y)
        self._add_text_field(c, "phone", self.margin + 80, y, 200, tooltip="Your phone number")
        y -= 30
        
        # LinkedIn
        self._add_label(c, "LinkedIn:", y)
        self._add_text_field(c, "linkedin", self.margin + 80, y, 300, tooltip="LinkedIn profile URL")
        y -= 30
        
        # Location
        self._add_label(c, "Location:", y)
        self._add_text_field(c, "location", self.margin + 80, y, 200, tooltip="City, Country")
        y -= 30
        
        # Blog/Website
        self._add_label(c, "Website/Blog:", y)
        self._add_text_field(c, "website", self.margin + 80, y, 300, tooltip="Personal website or blog URL")
        y -= 40
        
        # PROFESSIONAL SUMMARY
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(red)
        c.drawString(self.margin, y, "PROFESSIONAL SUMMARY")
        y -= 25
        
        self._add_label(c, "Brief professional summary (2-3 sentences):", y, font_size=9)
        y -= 10
        self._add_text_field(c, "professional_summary", self.margin, y, 
                            self.width - 2 * self.margin, 80, multiline=True,
                            tooltip="Describe your professional background and expertise")
        y -= 100
        
        # Check if we need a new page
        if y < 150:
            c.showPage()
            y = self.height - self.margin
        
        # CORE COMPETENCIES
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(red)
        c.drawString(self.margin, y, "CORE COMPETENCIES / SKILLS")
        y -= 25
        
        skills_categories = [
            "Platform Architecture & Design",
            "Cloud & Container Technologies",
            "DevOps & CI/CD",
            "Observability & Monitoring",
            "Programming Languages",
            "Other Technical Skills"
        ]
        
        for i, category in enumerate(skills_categories):
            self._add_label(c, f"{category}:", y, font_size=9, bold=True)
            y -= 15
            self._add_text_field(c, f"skill_{i}", self.margin + 20, y, 
                               self.width - 2 * self.margin - 20, 25, multiline=True,
                               tooltip=f"List skills in {category}")
            y -= 35
        
        # Check if we need a new page
        if y < 150:
            c.showPage()
            y = self.height - self.margin
        
        # PROFESSIONAL EXPERIENCE
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(red)
        c.drawString(self.margin, y, "PROFESSIONAL EXPERIENCE")
        y -= 25
        
        # Add 3 experience sections
        for i in range(1, 4):
            c.setFont("Helvetica-Bold", 11)
            c.setFillColor(blue)
            c.drawString(self.margin, y, f"Position {i}:")
            y -= 20
            
            # Position Title
            self._add_label(c, "Job Title:", y, font_size=9)
            self._add_text_field(c, f"exp{i}_position", self.margin + 80, y, 250, 
                               tooltip="Your position title")
            y -= 25
            
            # Period
            self._add_label(c, "Period:", y, font_size=9)
            self._add_text_field(c, f"exp{i}_period", self.margin + 80, y, 150, 
                               tooltip="e.g., Jan 2020 - Present")
            
            # Location
            c.drawString(self.margin + 250, y, "Location:")
            self._add_text_field(c, f"exp{i}_location", self.margin + 310, y, 150, 
                               tooltip="City, Country")
            y -= 25
            
            # Summary/Key Achievements
            self._add_label(c, "Summary / Key Achievements:", y, font_size=9)
            y -= 10
            self._add_text_field(c, f"exp{i}_summary", self.margin + 20, y, 
                               self.width - 2 * self.margin - 20, 60, multiline=True,
                               tooltip="Describe your role and achievements")
            y -= 70
            
            # Check if we need a new page
            if y < 150 and i < 3:
                c.showPage()
                y = self.height - self.margin
        
        # Check if we need a new page
        if y < 200:
            c.showPage()
            y = self.height - self.margin
        
        # EDUCATION
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(red)
        c.drawString(self.margin, y, "EDUCATION")
        y -= 25
        
        for i in range(1, 3):
            self._add_label(c, f"Degree {i}:", y, font_size=9, bold=True)
            self._add_text_field(c, f"edu{i}_degree", self.margin + 80, y, 300, 
                               tooltip="e.g., Bachelor of Science in Computer Science")
            y -= 25
            
            self._add_label(c, "Institution:", y, font_size=9)
            self._add_text_field(c, f"edu{i}_institution", self.margin + 80, y, 300, 
                               tooltip="University/College name")
            y -= 25
            
            self._add_label(c, "Period:", y, font_size=9)
            self._add_text_field(c, f"edu{i}_period", self.margin + 80, y, 150, 
                               tooltip="e.g., 2015 - 2019")
            y -= 35
        
        # AWARDS & CERTIFICATIONS
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(red)
        c.drawString(self.margin, y, "AWARDS & CERTIFICATIONS")
        y -= 25
        
        self._add_label(c, "List your awards, certifications, and recognition:", y, font_size=9)
        y -= 10
        self._add_text_field(c, "awards", self.margin, y, 
                           self.width - 2 * self.margin, 60, multiline=True,
                           tooltip="List awards and certifications with years")
        y -= 80
        
        # Footer
        c.setFont("Helvetica", 8)
        c.setFillColor(grey)
        c.drawCentredString(self.width / 2, 30, 
                           f"Generated on {datetime.now().strftime('%Y-%m-%d')} | Save this PDF after filling")
        
        # Save the PDF
        c.save()
        
        print(f"✓ PDF Form generated successfully: {self.output_path}")
        print(f"  File size: {self.output_path.stat().st_size / 1024:.2f} KB")
        print(f"\n📝 Instructions:")
        print("  1. Open the PDF in Adobe Acrobat Reader or a compatible PDF viewer")
        print("  2. Fill in the form fields")
        print("  3. Save the completed form")
        print("  4. Use the filled form data to generate a formatted CV")
        
        return str(self.output_path)


def main():
    """Main entry point"""
    script_dir = Path(__file__).parent
    template_path = script_dir / "pdf_template.json"
    
    generator = PDFFormGenerator(template_path)
    generator.create_form()


if __name__ == "__main__":
    main()
