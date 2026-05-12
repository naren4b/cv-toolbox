import json
import os
from reportlab.pdfgen import canvas
# Simplified: Manually create template_v1.pdf matching your docx layout
# In practice, copy your converted PDF or use this to recreate structure

# Extract schema from data.json (your structure)
with open('../data/data.json', 'r') as f:
    sample_data = json.load(f)

schema = {
  "version": "1.0",
  "structure": {"body": {}}  # Auto-generate from keys (full in main code)
}

with open('template/schema_v1.json', 'w') as f:
    json.dump(schema, f, indent=2)

print("Setup complete: template_v1.pdf and schema_v1.json ready.")
# Note: Convert DOCX to PDF manually first (libreoffice --headless --convert-to pdf original_template.docx)
