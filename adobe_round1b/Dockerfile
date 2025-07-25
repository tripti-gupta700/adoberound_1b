# Base image with Python 3.10
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install poppler-utils for pdf2image (Linux dependency)
RUN apt-get update && apt-get install -y poppler-utils tesseract-ocr && apt-get clean

# Run the main script
CMD ["python", "main.py"]
