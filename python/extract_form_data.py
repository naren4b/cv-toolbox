#!/usr/bin/env python3
"""
Extract data from filled PDF forms and save to JSON
Install: pip install pypdf
"""

from pypdf import PdfReader
from pathlib import Path
import json
from datetime import datetime


class PDFFormExtractor:
    """Extracts data from filled PDF forms"""
    
    def __init__(self, pdf_path):
        self.pdf_path = Path(pdf_path)
        if not self.pdf_path.exists():
            raise FileNotFoundError(f"PDF not found: {self.pdf_path}")
    
    def extract_form_data(self):
        """Extract all form field data from PDF"""
        reader = PdfReader(str(self.pdf_path))
        
        if "/AcroForm" not in reader.trailer["/Root"]:
            print("⚠ No form fields found in this PDF")
            return {}
        
        fields = reader.get_form_text_fields()
        
        if not fields:
            print("⚠ No filled form fields found")
            return {}
        
        print(f"✓ Found {len(fields)} form fields")
        return fields
    
    def convert_to_cv_json(self, form_data):
        """Convert form data to CV JSON structure"""
        
        # Build contact info list
        contact_info = []
        if form_data.get("linkedin"):
            contact_info.append({
                "name": "LinkedIn",
                "href": form_data["linkedin"],
                "text": form_data["linkedin"],
                "type": "href"
            })
        if form_data.get("website"):
            contact_info.append({
                "name": "blog",
                "href": form_data["website"],
                "text": form_data["website"],
                "type": "href"
            })
        if form_data.get("phone"):
            contact_info.append({
                "name": "phone",
                "text": form_data["phone"],
                "type": "phone"
            })
        if form_data.get("email"):
            contact_info.append({
                "name": "email",
                "text": form_data["email"],
                "type": "email"
            })
        if form_data.get("location"):
            contact_info.append({
                "name": "location",
                "text": form_data["location"],
                "type": "text"
            })
        
        # Build skills list
        skills = []
        skills_mapping = {
            "skill_0": "Platform Architecture & Design",
            "skill_1": "Cloud & Container Technologies",
            "skill_2": "DevOps & CI/CD",
            "skill_3": "Observability & Monitoring",
            "skill_4": "Programming Languages",
            "skill_5": "Other Technical Skills"
        }
        
        for key, category in skills_mapping.items():
            if form_data.get(key):
                skills.append({
                    "category": category,
                    "items": form_data[key]
                })
        
        # Build experiences list
        experiences = []
        for i in range(1, 4):
            position = form_data.get(f"exp{i}_position")
            if position:
                exp = {
                    "position": position,
                    "period": form_data.get(f"exp{i}_period", ""),
                    "location": form_data.get(f"exp{i}_location", "")
                }
                summary = form_data.get(f"exp{i}_summary")
                if summary:
                    exp["summary"] = summary
                experiences.append(exp)
        
        # Build education list
        degrees = []
        for i in range(1, 3):
            degree = form_data.get(f"edu{i}_degree")
            if degree:
                degrees.append({
                    "degree": degree,
                    "institution": form_data.get(f"edu{i}_institution", ""),
                    "period": form_data.get(f"edu{i}_period", "")
                })
        
        # Build awards list
        awards = []
        awards_text = form_data.get("awards", "")
        if awards_text:
            # Parse awards (each line should be: YYYY - Award Title)
            for line in awards_text.split("\n"):
                line = line.strip()
                if line and " - " in line:
                    year, title = line.split(" - ", 1)
                    awards.append({
                        "year": year.strip(),
                        "title": title.strip()
                    })
        
        # Build complete CV JSON
        cv_data = {
            "head": {
                "title": f"{form_data.get('profile_name', 'CV')} - {form_data.get('profile_title', '')}"
            },
            "body": {
                "profile-name": form_data.get("profile_name", ""),
                "profile-header": {
                    "title": form_data.get("profile_title", ""),
                    "contact-info": contact_info
                },
                "professional-summary": {
                    "title": "Professional Summary",
                    "content": form_data.get("professional_summary", "")
                },
                "core-competencies": {
                    "title": "Core Competencies",
                    "skills": skills
                },
                "professional-experience": {
                    "title": "Professional Experience",
                    "experiences": experiences
                },
                "education": {
                    "title": "Education",
                    "degrees": degrees
                }
            }
        }
        
        # Add awards if any
        if awards:
            cv_data["body"]["awards-recognition"] = {
                "title": "Awards & Recognition",
                "awards": awards
            }
        
        return cv_data
    
    def save_to_json(self, output_path=None):
        """Extract form data and save to JSON"""
        # Extract form data
        form_data = self.extract_form_data()
        
        if not form_data:
            print("No data to save")
            return None
        
        # Convert to CV JSON structure
        cv_data = self.convert_to_cv_json(form_data)
        
        # Generate output path
        if not output_path:
            date_str = datetime.now().strftime("%Y-%m-%d")
            output_path = self.pdf_path.parent / f"cv_data_from_form_{date_str}.json"
        
        # Save to JSON file
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(cv_data, f, indent=4, ensure_ascii=False)
        
        print(f"\n✓ CV data saved to: {output_path}")
        print(f"  Fields extracted: {len(form_data)}")
        
        # Print summary
        print("\n📊 Summary:")
        print(f"  Profile Name: {cv_data['body'].get('profile-name', 'N/A')}")
        print(f"  Contact Info: {len(cv_data['body']['profile-header']['contact-info'])} items")
        print(f"  Skills: {len(cv_data['body']['core-competencies']['skills'])} categories")
        print(f"  Experiences: {len(cv_data['body']['professional-experience']['experiences'])} positions")
        print(f"  Education: {len(cv_data['body']['education']['degrees'])} degrees")
        
        return str(output_path)


def main():
    """Main entry point"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python extract_form_data.py <filled_pdf_form.pdf>")
        print("\nExample:")
        print("  python extract_form_data.py CV_FORM_2026-02-05.pdf")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    
    try:
        extractor = PDFFormExtractor(pdf_path)
        extractor.save_to_json()
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
