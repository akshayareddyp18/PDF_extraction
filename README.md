# PDF Outline Extractor – Connecting the Dots Challenge (Round 1A)

This project extracts a structured outline (Title, H1, H2, H3) from a PDF document. It's designed to process PDFs efficiently and offline, forming the foundational step for a futuristic intelligent reading experience.

## Challenge Objective

Given a PDF (up to 50 pages), extract:
- **Document Title**
- **Headings:** H1, H2, H3
- **Output Format:** JSON with heading text, level, and page number

##  Approach

We use [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/en/latest/) to:
- Parse text spans along with font size, style, and location
- Identify the **most frequent and largest font sizes** as structural cues
- Infer heading levels (Title, H1, H2, H3) based on font size hierarchy
- Filter out non-headings based on content heuristics (e.g., short lines, no trailing punctuation)
- Output structured JSON in the required format

##  Example Output

```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "History of AI", "page": 2 },
    { "level": "H3", "text": "Early Research", "page": 3 }
  ]
}
