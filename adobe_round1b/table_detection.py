# This script tries to detect tables using OCR word positions
# It is based on pytesseract image_to_data output

import pytesseract
from PIL import Image
import os
import json

# Setup for Windows (update path if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

images_folder = "images"
tables_output = []

# helper function to group words by y-position (rows)
def group_words_by_line(data):
    rows = {}
    for i, word in enumerate(data['text']):
        if word.strip():
            y = int(data['top'][i])
            text = word.strip()
            row_key = y // 10  # group every 10px vertically
            if row_key not in rows:
                rows[row_key] = []
            rows[row_key].append(text)
    return [rows[key] for key in sorted(rows.keys())]

# process all pages
for file in sorted(os.listdir(images_folder)):
    if file.endswith(".png"):
        image_path = os.path.join(images_folder, file)
        print(" Processing table on", file)

        image = Image.open(image_path)
        data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

        rows = group_words_by_line(data)
        rows = [r for r in rows if len(r) > 1]  # filter out 1-word lines (noise)

        page_number = int(file.split("_")[1].split(".")[0])

        if rows:
            tables_output.append({
                "page": page_number,
                "rows": rows
            })

# Save detected tables to file
with open("tables_only.json", "w", encoding="utf-8") as f:
    json.dump(tables_output, f, indent=2, ensure_ascii=False)

print("Done detecting tables. Output saved to tables_only.json")
