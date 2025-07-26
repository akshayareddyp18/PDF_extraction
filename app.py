import os
import json
from pdf_outline_extractor import extract_outline

pdf_path = input("📤 Enter path to your PDF file: ").strip()

if not os.path.isfile(pdf_path):
    print(f"❌ File not found: {pdf_path}")
    exit()

with open(pdf_path, "rb") as f:
    structured_output = extract_outline(f)

output_filename = os.path.splitext(os.path.basename(pdf_path))[0] + "_outline.json"
os.makedirs("output", exist_ok=True)
output_path = os.path.join("output", output_filename)

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(structured_output, f, indent=2, ensure_ascii=False)

print(f"✅ Output saved to: {output_path}")
