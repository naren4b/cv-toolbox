#!/usr/bin/env python3
"""
Template-based PDF CV Generator using fpdf2
Install: pip install fpdf2
"""

from fpdf import FPDF, XPos, YPos
from pathlib import Path
from datetime import datetime
import json
import re


class PDFTemplateEngine:
    """Renders PDF from data and template"""
    
    def __init__(self, template_path, data_path):
        self.template = self._load_json(template_path)
        self.data = self._load_json(data_path)
        self.pdf = None
        self.styles = self.template.get("styles", {})
        
    def _load_json(self, path):
        """Load JSON file"""
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    
    def _get_nested_value(self, data, path):
        """Get value from nested dict using dot notation path"""
        keys = path.split(".")
        value = data
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return None
        return value
    
    def _sanitize_text(self, text):
        """Sanitize text for PDF latin-1 encoding"""
        if not text:
            return ""
        text = str(text)
        # Replace unicode characters with ASCII equivalents
        text = text.replace("\u2014", "--")  # em dash
        text = text.replace("\u2013", "-")   # en dash
        text = text.replace("\u2019", "'")   # right single quotation mark
        text = text.replace("\u201c", '"')   # left double quotation mark
        text = text.replace("\u201d", '"')   # right double quotation mark
        text = text.replace("\u2022", "-")   # bullet point
        text = text.replace("\u00a0", " ")   # non-breaking space
        # Remove any remaining non-latin1 characters
        text = text.encode("latin-1", errors="replace").decode("latin-1")
        return text
    
    def _apply_template(self, template_str, item):
        """Replace {{placeholder}} with actual values"""
        def replacer(match):
            key = match.group(1)
            return str(item.get(key, ""))
        return re.sub(r"\{\{(\w+(?:-\w+)*)\}\}", replacer, template_str)
    
    def _add_text(self, text, style_name):
        """Add text to PDF using specified style"""
        if not text or not text.strip():
            return
            
        text = self._sanitize_text(text)
        style = self.styles.get(style_name, {})
        
        font_family = style.get("font_family", "Helvetica")
        font_style = style.get("font_style", "")
        font_size = style.get("font_size", 9)
        spacing = style.get("spacing", 4)
        indent = style.get("indent", 0)
        
        self.pdf.set_font(font_family, font_style, font_size)
        self.pdf.set_x(self.template["page"]["margins"]["left"] + indent)
        self.pdf.multi_cell(0, spacing, text.strip(), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    def _render_text(self, section):
        """Render simple text section"""
        data_path = section.get("data_path")
        value = self._get_nested_value(self.data, data_path)
        if value:
            self._add_text(value, section.get("style", "body_text"))
    
    def _render_list(self, section):
        """Render list section"""
        data_path = section.get("data_path")
        items = self._get_nested_value(self.data, data_path)
        if not items:
            return
            
        template_str = section.get("template", "{{text}}")
        style = section.get("style", "body_text")
        
        for item in items:
            if isinstance(item, dict):
                text = self._apply_template(template_str, item)
            else:
                text = str(item)
            self._add_text(text, style)
    
    def _render_experiences(self, data_path):
        """Custom handler for professional experiences"""
        experiences = self._get_nested_value(self.data, data_path)
        if not experiences:
            return
        
        for experience in experiences:
            self.pdf.ln(1)
            
            # Job title, period, location
            header = f"{experience.get('position', '')} | {experience.get('period', '')} | {experience.get('location', '')}"
            self._add_text(header, "subsection_heading")
            
            # Summary if exists
            if "summary" in experience:
                self.pdf.ln(0.5)
                self._add_text(experience["summary"], "body_text")
            
            # Bullets if exists
            if "bullets" in experience:
                for bullet in experience["bullets"]:
                    self._add_text(f"- {bullet}", "bullet_point")
            
            # Sections with subsections (e.g., Nokia role)
            if "sections" in experience:
                for subsection in experience["sections"]:
                    self.pdf.ln(0.5)
                    self._add_text(subsection.get("heading", ""), "subsection_heading_small")
                    for bullet in subsection.get("bullets", []):
                        self._add_text(f"- {bullet}", "bullet_point")
    
    def _render_education(self, data_path):
        """Custom handler for education"""
        degrees = self._get_nested_value(self.data, data_path)
        if not degrees:
            return
        
        for degree in degrees:
            self.pdf.ln(0.5)
            self._add_text(degree.get("degree", ""), "subsection_heading")
            institution_text = f"{degree.get('institution', '')} | {degree.get('period', '')}"
            self._add_text(institution_text, "body_text_indent")
    
    def _render_section(self, section):
        """Render a section based on its type"""
        section_type = section.get("type")
        
        # Line break before
        if "line_break_before" in section:
            self.pdf.ln(section["line_break_before"])
        
        # Render based on type
        if section_type == "text":
            self._render_text(section)
        elif section_type == "list":
            self._render_list(section)
        elif section_type == "section":
            # Nested sections
            for subsection in section.get("sections", []):
                self._render_section(subsection)
        elif section_type == "custom":
            # Custom handlers
            handler_name = section.get("handler")
            data_path = section.get("data_path")
            if handler_name == "render_experiences":
                self._render_experiences(data_path)
            elif handler_name == "render_education":
                self._render_education(data_path)
        
        # Line break after
        if "line_break_after" in section:
            self.pdf.ln(section["line_break_after"])
    
    def generate(self, output_path=None):
        """Generate PDF from template and data"""
        # Initialize PDF
        page_config = self.template.get("page", {})
        pdf_format = page_config.get("format", "Letter")
        margins = page_config.get("margins", {})
        
        class CustomPDF(FPDF):
            def header(self):
                pass
            def footer(self):
                pass
        
        self.pdf = CustomPDF(format=pdf_format)
        self.pdf.set_margins(
            left=margins.get("left", 15),
            top=margins.get("top", 15),
            right=margins.get("right", 15)
        )
        self.pdf.add_page()
        self.pdf.set_auto_page_break(auto=True, margin=margins.get("bottom", 15))
        
        # Render all sections
        for section in self.template.get("sections", []):
            self._render_section(section)
        
        # Generate output filename if not provided
        if not output_path:
            output_config = self.template.get("output", {})
            filename_template = output_config.get("filename_template", "output_{{date}}.pdf")
            
            # Get profile name
            profile_name_path = output_config.get("profile_name_path", "body.profile-name")
            profile_name = self._get_nested_value(self.data, profile_name_path)
            if profile_name:
                profile_name = profile_name.replace(" ", "_").upper()
            else:
                profile_name = "CV"
            
            # Apply template
            date_str = datetime.now().strftime("%Y-%m-%d")
            filename = filename_template.replace("{{profile_name}}", profile_name)
            filename = filename.replace("{{date}}", date_str)
            
            output_path = Path(__file__).parent / filename
        
        # Save PDF
        try:
            self.pdf.output(str(output_path))
            print(f"✓ PDF generated successfully: {output_path}")
            print(f"  File size: {output_path.stat().st_size / 1024:.2f} KB")
            print(f"  Pages: {self.pdf.page_no()}")
            return str(output_path)
        except Exception as e:
            print(f"Error generating PDF: {e}")
            import traceback
            traceback.print_exc()
            raise


def main():
    """Main entry point"""
    # Paths
    script_dir = Path(__file__).parent
    template_path = script_dir / "pdf_template.json"
    data_path = script_dir / "data.json"
    
    # Generate PDF
    engine = PDFTemplateEngine(template_path, data_path)
    engine.generate()


if __name__ == "__main__":
    main()
