#!/usr/bin/env python3
"""
Clean and tokenize text from processed files.
"""

import re
import nltk
from nltk.corpus import stopwords

# Download stopwords if needed
try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords')

def clean_text(text):
    """Clean text: lowercase, remove punctuation, extra whitespace."""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\s+', ' ', text).strip()  # Normalize whitespace
    return text

def tokenize_text(text):
    """Split text into words."""
    return text.split()

def remove_stopwords(tokens):
    """Remove common stopwords."""
    stop_words = set(stopwords.words('english'))
    return [word for word in tokens if word not in stop_words]

def process_text_file(filepath):
    """Process a single text file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    cleaned = clean_text(text)
    tokens = tokenize_text(cleaned)
    filtered_tokens = remove_stopwords(tokens)
    
    return {
        'original_text': text,
        'cleaned_text': cleaned,
        'tokens': tokens,
        'filtered_tokens': filtered_tokens
    }