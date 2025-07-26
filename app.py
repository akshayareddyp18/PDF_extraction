import os
import json
from pdf_outline_extractor import extract_outline

INPUT_DIR = "input"
OUTPUT_DIR = "output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in os.listdir(INPUT_DIR):
    if filename.endswith(".pdf"):
        input_path = os.path.join(INPUT_DIR, filename)
        output_filename = os.path.splitext(filename)[0] + ".json"
        output_path = os.path.join(OUTPUT_DIR, output_filename)

        with open(input_path, "rb") as f:
            structured_output = extract_outline(f)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(structured_output, f, indent=2, ensure_ascii=False)

        print(f"✅ Processed: {filename} → {output_filename}")
