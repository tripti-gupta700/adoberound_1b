# Round 1B 

This project is designed to process scanned or image-based PDF files and extract the plain text and tables present in them using OCR (Optical Character Recognition). The final output is a structured JSON that includes all detected text and table data.

## Features

- Converts scanned PDFs into image files (one image per page).
- Performs OCR on each page image to extract text.
- Detects simple table structures based on text alignment.
- Outputs both text and table data in a single JSON file.
- Fully containerized using Docker.
- Works offline, with no internet dependency.

## Folder Structure

round1b/
├── main.py

├── requirements.txt

├── Dockerfile

├── README.md

├── approach_explanation.md

├── input/

│ └── sample.pdf

├── output/

│ └── output.json

├── images/ (generated during execution)

## How to Run

### 1. Build the Docker Image
docker build -t adobe-round1b .

2. Run the Container

docker run --rm -v %cd%/input:/app/input -v %cd%/output:/app/output adobe-round1b
Replace %cd% with the current directory path if not using PowerShell.


3. After execution, output/output.json will contain:

{
  "text": "All extracted plain text...",
  "tables": [
    {
      "page": 3,
      "rows": [
        ["Name", "Age", "City"],
        ["John", "22", "Delhi"]
      ]
    }
  ]
}
4. Requirements (Handled in Dockerfile)
Python 3.10
pytesseract
pdf2image
pillow
poppler-utils
tesseract-ocr

No manual installations are needed outside Docker.

## Notes
This solution works efficiently even on large scanned PDFs (e.g., 300+ pages).
Table detection is based on OCR data grouping by line and may not support complex table formats.

