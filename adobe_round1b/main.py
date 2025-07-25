# Final script to process scanned PDF:
# Step 1 - Convert to images
# Step 2 - Extract text using OCR
# Step 3 - Extract tables from OCR layout
# All output saved in output/output.json

import os
import json
import pytesseract
from PIL import Image
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

input_pdf = "input/sample.pdf"
images_folder = "images"
output_folder = "output"


os.makedirs(images_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)


print("Converting PDF to images...")
pages = convert_from_path(input_pdf, dpi=300)

for i, page in enumerate(pages):
    image_path = os.path.join(images_folder, f"page_{i + 1}.png")
    page.save(image_path, "PNG")
    print(f"Saved image: {image_path}")


print("\n🔍 Starting OCR text extraction...")
combined_text = ""
text_by_page = {}

for img_file in sorted(os.listdir(images_folder)):
    if img_file.endswith(".png"):
        img_path = os.path.join(images_folder, img_file)
        img = Image.open(img_path)
        text = pytesseract.image_to_string(img)
        
        page_num = int(img_file.split("_")[1].split(".")[0])
        text_by_page[page_num] = text
        combined_text += f"\n--- Page {page_num} ---\n{text}"

print("\n Extracting table rows...")
tables = []

def group_words_by_line(data):
    rows = {}
    for i, word in enumerate(data['text']):
        if word.strip():
            y = int(data['top'][i])
            text = word.strip()
            row_key = y // 10
            if row_key not in rows:
                rows[row_key] = []
            rows[row_key].append(text)
    return [rows[k] for k in sorted(rows.keys())]

for img_file in sorted(os.listdir(images_folder)):
    if img_file.endswith(".png"):
        img_path = os.path.join(images_folder, img_file)
        img = Image.open(img_path)
        data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
        
        rows = group_words_by_line(data)
        rows = [r for r in rows if len(r) > 1]
        page_num = int(img_file.split("_")[1].split(".")[0])
        
        if rows:
            tables.append({
                "page": page_num,
                "rows": rows
            })


final_output = {
    "text": combined_text,
    "tables": tables
}

with open(os.path.join(output_folder, "output.json"), "w", encoding="utf-8") as f:
    json.dump(final_output, f, indent=2, ensure_ascii=False)

print("\n All done! Output saved to output/output.json")
