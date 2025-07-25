# This script is for converting PDF pages to images

from pdf2image import convert_from_path
import os

pdf_file = "sample.pdf"  # the scanned PDF file
image_folder = "images"  # folder to save images

# make sure output folder exists
os.makedirs(image_folder, exist_ok=True)


pages = convert_from_path(pdf_file, dpi=300)  # higher dpi gives better clarity

# save each page as PNG
for i, page in enumerate(pages):
    filename = f"page_{i+1}.png"
    page_path = os.path.join(image_folder, filename)
    page.save(page_path, "PNG")
    print(f"Saved {filename} ")
