#!/usr/bin/env python3
"""
Fetch Warren Buffett shareholder letters from Berkshire Hathaway archive.
Downloads letters for 1977-2024 and saves to data/raw/.
Builds metadata.json with year, url, local_path.
"""

import requests
from bs4 import BeautifulSoup
import os
import json
import time
import re

ARCHIVE_URL = "https://www.berkshirehathaway.com/letters/letters.html"
BASE_URL = "https://www.berkshirehathaway.com"
RAW_DIR = "data/raw/"
METADATA_FILE = "data/metadata.json"

def fetch_archive_page():
    """Fetch the archive page HTML."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(ARCHIVE_URL, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching archive page: {e}")
        return None

def parse_letter_links(html):
    """Parse HTML to extract letter links."""
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        # Look for links that match letter patterns: YYYY.html or YYYYltr.pdf
        if re.match(r'\d{4}\.html', href) or re.match(r'\d{4}ltr\.pdf', href):
            full_url = BASE_URL + '/letters/' + href
            # Extract year from href
            year_match = re.search(r'(\d{4})', href)
            if year_match:
                year = int(year_match.group(1))
                if 1977 <= year <= 2024:
                    # Determine filename
                    if href.endswith('.pdf'):
                        filename = f"{year}.pdf"
                    else:
                        filename = f"{year}.html"
                    links.append({
                        'year': year,
                        'url': full_url,
                        'filename': filename
                    })
    # Remove duplicates by year
    seen_years = set()
    unique_links = []
    for link in links:
        if link['year'] not in seen_years:
            seen_years.add(link['year'])
            unique_links.append(link)
    return sorted(unique_links, key=lambda x: x['year'])

def download_letter(letter_info):
    """Download a single letter."""
    url = letter_info['url']
    filename = letter_info['filename']
    filepath = os.path.join(RAW_DIR, filename)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename}")
        return True
    except requests.RequestException as e:
        print(f"Failed to download {filename}: {e}")
        return False

def fetch_all_letters():
    """Main function to fetch all letters."""
    # Ensure raw dir exists
    os.makedirs(RAW_DIR, exist_ok=True)

    # Fetch archive page
    html = fetch_archive_page()
    if not html:
        return

    # Parse links
    letters = parse_letter_links(html)
    print(f"Found {len(letters)} letters to download")

    # Download each letter
    metadata = []
    for letter in letters:
        success = download_letter(letter)
        if success:
            metadata.append({
                'year': letter['year'],
                'url': letter['url'],
                'local_path': os.path.join(RAW_DIR, letter['filename'])
            })
        time.sleep(1)  # Be polite

    # Save metadata
    with open(METADATA_FILE, 'w') as f:
        json.dump(metadata, f, indent=2)
    print(f"Saved metadata for {len(metadata)} letters")

if __name__ == "__main__":
    fetch_all_letters()