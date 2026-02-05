# PDF Template Generator

A flexible, template-based PDF CV generator that separates presentation from data.

## Overview

This system consists of three main components:

1. **`data.json`** - Your CV data (content)
2. **`pdf_template.json`** - PDF layout template with placeholders (presentation)
3. **`app_template.py`** - Template engine that combines data and template to generate PDF

## How It Works

### 1. Data File (`data.json`)
Contains all your CV information in a structured JSON format. The data is organized hierarchically:

```json
{
  "body": {
    "profile-name": "Your Name",
    "professional-summary": {
      "title": "Professional Summary",
      "content": "Your summary..."
    },
    ...
  }
}
```

### 2. Template File (`pdf_template.json`)
Defines the PDF structure, styling, and how data should be presented:

#### Template Structure

```json
{
  "page": {
    "format": "Letter",
    "margins": { "left": 15, "top": 15, "right": 15, "bottom": 15 }
  },
  "styles": {
    "profile_name": {
      "font_family": "Helvetica",
      "font_style": "B",
      "font_size": 18,
      "spacing": 6,
      "indent": 0
    },
    ...
  },
  "sections": [
    {
      "id": "profile_name",
      "type": "text",
      "data_path": "body.profile-name",
      "style": "profile_name"
    },
    ...
  ]
}
```

#### Key Template Concepts

**Styles**: Define how text appears
- `font_family`: Font name (e.g., "Helvetica", "Arial")
- `font_style`: Font style ("B" for bold, "I" for italic, "" for regular)
- `font_size`: Size in points
- `spacing`: Line spacing
- `indent`: Left indentation in mm

**Section Types**:
- `text`: Single text value from data
- `list`: Iterate over array items
- `section`: Group of nested sections
- `custom`: Custom rendering logic

**Data Paths**: Use dot notation to access nested data
- `body.profile-name` → access profile name
- `body.professional-summary.title` → access summary title

**Placeholders in Templates**: Use `{{field_name}}` syntax
```json
{
  "type": "list",
  "template": "{{year}} - {{title}}"
}
```

### 3. Template Engine (`app_template.py`)
Processes the template and data to generate the PDF.

## Usage

### Basic Usage

```bash
python app_template.py
```

This will:
1. Load `data.json` and `pdf_template.json`
2. Generate PDF using the template
3. Save as `NARENDRANATH_PANDA_2026-02-05.pdf` (or similar)

### Customizing Your CV

#### Modify Content
Edit `data.json` to update your information:
- Personal details
- Work experience
- Education
- Skills
- Awards

#### Customize Layout
Edit `pdf_template.json` to change:

**Page Settings**:
```json
"page": {
  "format": "Letter",  // or "A4"
  "margins": { "left": 20, "top": 20, "right": 20, "bottom": 20 }
}
```

**Add New Styles**:
```json
"styles": {
  "my_custom_style": {
    "font_family": "Helvetica",
    "font_style": "B",
    "font_size": 11,
    "spacing": 5,
    "indent": 5
  }
}
```

**Reorder Sections**:
Simply rearrange items in the `sections` array to change the order they appear in the PDF.

**Add New Sections**:
```json
{
  "id": "certifications",
  "type": "section",
  "line_break_before": 2,
  "sections": [
    {
      "type": "text",
      "data_path": "body.certifications.title",
      "style": "section_heading"
    },
    {
      "type": "list",
      "data_path": "body.certifications.items",
      "style": "body_text",
      "template": "{{name}} - {{year}}"
    }
  ]
}
```

## Template Examples

### Example 1: Simple Text Section
```json
{
  "type": "text",
  "data_path": "body.profile-name",
  "style": "profile_name",
  "line_break_after": 1
}
```

### Example 2: List with Template
```json
{
  "type": "list",
  "data_path": "body.awards-recognition.awards",
  "style": "body_text",
  "template": "{{year}} - {{title}}",
  "line_break_after": 0.5
}
```

### Example 3: Nested Section
```json
{
  "id": "professional_summary",
  "type": "section",
  "line_break_before": 2,
  "sections": [
    {
      "type": "text",
      "data_path": "body.professional-summary.title",
      "style": "section_heading"
    },
    {
      "type": "text",
      "data_path": "body.professional-summary.content",
      "style": "body_text"
    }
  ]
}
```

## Advantages

1. **Separation of Concerns**: Content and presentation are independent
2. **Easy Updates**: Change content without touching code
3. **Flexible Styling**: Modify layout without changing data structure
4. **Reusable**: Same template can work with different data files
5. **Version Control**: Track changes to content and template separately

## Advanced Customization

For complex layouts, you can add custom handlers in `app_template.py`:

```python
def _render_custom_section(self, data_path):
    """Custom rendering logic"""
    data = self._get_nested_value(self.data, data_path)
    # Your custom rendering code here
    self._add_text(processed_text, "your_style")
```

Then reference it in the template:
```json
{
  "type": "custom",
  "handler": "render_custom_section",
  "data_path": "body.your.data.path"
}
```

## Requirements

```
fpdf2
```

Install with:
```bash
pip install fpdf2
```
