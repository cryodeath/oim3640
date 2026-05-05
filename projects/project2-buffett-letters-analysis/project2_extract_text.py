#!/usr/bin/env python3
"""
Extract clean text from downloaded HTML/PDF files.
Saves processed text to data/processed/.
"""

import os
import json
from bs4 import BeautifulSoup
import fitz  # PyMuPDF

def extract_text_from_html(filepath):
    """Extract text from HTML file."""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        soup = BeautifulSoup(f, 'html.parser')
        # Remove scripts, styles, etc.
        for script in soup(["script", "style"]):
            script.extract()
        text = soup.get_text()
        return text

def extract_text_from_pdf(filepath):
    """Extract text from PDF file."""
    doc = fitz.open(filepath)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_all_texts():
    """Extract text from all raw files and save to data/processed/."""
    raw_dir = 'data/raw/'
    processed_dir = 'data/processed/'
    os.makedirs(processed_dir, exist_ok=True)
    
    for filename in os.listdir(raw_dir):
        if filename.endswith(('.html', '.pdf')):
            year = int(filename.split('.')[0])
            filepath = os.path.join(raw_dir, filename)
            if filepath.endswith('.html'):
                text = extract_text_from_html(filepath)
            elif filepath.endswith('.pdf'):
                text = extract_text_from_pdf(filepath)
            
            # Save cleaned text
            processed_path = os.path.join(processed_dir, f'{year}.txt')
            with open(processed_path, 'w', encoding='utf-8') as f:
                f.write(text)
            
            print(f"Extracted text for {year}")

if __name__ == "__main__":
    extract_all_texts()