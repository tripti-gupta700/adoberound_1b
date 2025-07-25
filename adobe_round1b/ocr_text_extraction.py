# This script runs OCR on all the images and extracts plain text

import pytesseract
from PIL import Image
import os
import json

# setting the path to tesseract installed on my Windows system
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image_folder = "images"
all_text = ""
text_by_page = {}

# go through each image and extract text
for file in sorted(os.listdir(image_folder)):
    if file.endswith(".png"):
        img_path = os.path.join(image_folder, file)
        print("Processing:", file)
        
        img = Image.open(img_path)
        extracted_text = pytesseract.image_to_string(img)
        
        page_num = int(file.split("_")[1].split(".")[0])  
        text_by_page[page_num] = extracted_text
        
        all_text += f"\n--- Page {page_num} ---\n" + extracted_text

# preparing final output
output = {
    "text": all_text,
    "tables": []  # will add table data later
}


with open("output.json", "w", encoding="utf-8") as out:
    json.dump(output, out, indent=2, ensure_ascii=False)

print("Text extracted and saved to output.json ")
