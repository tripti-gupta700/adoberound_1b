
## `approach_explanation.md`

# Approach Explanation – Round 1B

The problem required us to extract both plain text and table content from scanned or image-based PDF files. Since such PDFs don't contain embedded text, traditional text extractors wouldn't work. Therefore, I used Optical Character Recognition (OCR) to process the file.

## Step-by-Step Breakdown

### 1. PDF to Image Conversion
Since OCR works on images, I first converted each page of the scanned PDF into a `.png` file using the `pdf2image` library. This step helps in handling scanned pages as image files.

### 2. OCR for Text Extraction
For text detection, I used the `pytesseract` library, which is a Python wrapper for Google's Tesseract OCR engine. It takes each image and extracts text from it page-by-page.

The output from this stage is structured and saved under a single key `"text"` in the final output file.

### 3. Table Detection
To detect tables, I used the `image_to_data()` method from pytesseract, which returns positional information for each detected word.

I applied a simple line-grouping strategy where words with similar vertical positions are grouped into rows. If a line contains multiple words, it's assumed to be part of a table row. These grouped rows are stored under the `"tables"` key.

### 4. Output Format
Both extracted text and table data are combined and saved into a single JSON file (`output.json`). This makes it easier to evaluate and visualize the structure of extracted information.

## Challenges Faced

- Dealing with scanned PDFs means text is not directly accessible, which made it necessary to rely entirely on OCR.
- Some scanned pages had uneven alignment or noise, which made table detection a bit less accurate. To handle this, I filtered out lines with only a single word to reduce false positives.
- Keeping memory usage reasonable with large PDFs (300+ pages) required processing one image at a time instead of loading everything into memory.

## Conclusion

This solution works fully offline and does not rely on any cloud APIs or internet-based OCR tools. It is scalable to hundreds of pages and remains within resource and time constraints. The logic is kept clean and readable so it can be easily extended or integrated into a larger system if needed.
