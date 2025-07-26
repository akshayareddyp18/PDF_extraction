import fitz  # PyMuPDF
from collections import Counter
import json


def extract_text_spans(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    spans = []

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    text = span["text"].strip()
                    if not text or len(text) < 3:
                        continue
                    spans.append({
                        "text": text,
                        "size": round(span["size"], 1),
                        "font": span["font"],
                        "bold": "Bold" in span["font"],
                        "page": page_num,
                        "y": span["origin"][1]
                    })
    return spans


def infer_heading_levels(spans):
    font_sizes = [span["size"] for span in spans]
    size_counter = Counter(font_sizes)
    common_sizes = sorted(size_counter.items(), key=lambda x: (-x[0], -x[1]))

    size_to_level = {}
    if common_sizes:
        size_to_level[common_sizes[0][0]] = "Title"
    if len(common_sizes) > 1:
        size_to_level[common_sizes[1][0]] = "H1"
    if len(common_sizes) > 2:
        size_to_level[common_sizes[2][0]] = "H2"
    if len(common_sizes) > 3:
        size_to_level[common_sizes[3][0]] = "H3"
    return size_to_level


def build_outline(spans, size_to_level):
    title = ""
    outline = []

    for span in spans:
        level = size_to_level.get(span["size"])
        if level == "Title" and not title:
            title = span["text"]
        elif level in ["H1", "H2", "H3"]:
            if len(span["text"]) > 100 or span["text"].endswith("."):
                continue
            outline.append({
                "level": level,
                "text": span["text"],
                "page": span["page"]
            })

    return {
        "title": title,
        "outline": outline
    }


def extract_outline(pdf_file):
    spans = extract_text_spans(pdf_file)
    size_to_level = infer_heading_levels(spans)
    structured_output = build_outline(spans, size_to_level)
    return structured_output
