# Buffett Letters Text Analysis

This project analyzes Warren Buffett's Berkshire Hathaway shareholder letters from 1977 to 2024 to understand how his writing style has changed over time.

## Project Goal
Answer questions about vocabulary richness, signal words, and sentence complexity across six decades.

## Data Source
Official Berkshire Hathaway shareholder letters archive: https://www.berkshirehathaway.com/letters/letters.html

## Quick Start (For Beginners)

Follow these step-by-step instructions to run the analysis on your own computer.

### Step 1: Install Python
If you don't have Python installed:
- Download from https://www.python.org/downloads/
- Choose Python 3.8 or higher
- During installation, check "Add Python to PATH"

### Step 2: Download the Project
- Download this project as a ZIP file from GitHub
- Unzip it to a folder on your computer (e.g., `C:\Users\YourName\Documents\buffett-analysis`)
- Open a terminal/command prompt and navigate to that folder:
  ```
  cd "C:\Users\YourName\Documents\buffett-analysis"
  ```

### Step 3: Install Dependencies
Run this command in your terminal:
```
pip install -r project2_requirements.txt
```
This installs all needed libraries (requests, beautifulsoup4, PyMuPDF, nltk, matplotlib, pandas).

### Step 4: Run the Full Analysis
Execute the main script:
```
python project2_main.py
```
This will:
- Download all shareholder letters (may take 1-2 minutes)
- Extract clean text from HTML/PDF files
- Analyze vocabulary, word frequencies, and signal words
- Save results to JSON files

### Step 5: View the Results
After running, check these files in the `data/` folder:
- `data/analysis.json`: Detailed metrics for each year
- `data/decade_summary.json`: Aggregated results by decade

**Sample output location:**
- Windows: `C:\Users\YourName\Documents\buffett-analysis\data\analysis.json`
- Open with any text editor or web browser

### Step 6: Explore the Data
The analysis includes:
- **Vocabulary richness**: Unique words / total words (higher = more diverse vocabulary)
- **Signal words**: Frequency of words like "risk", "opportunity", "fear" per 10,000 words
- **Top words**: Most common words after removing stop words
- **Word counts**: Total and unique words per letter

### Troubleshooting
- **Permission errors**: Run terminal as administrator
- **Network issues**: The script downloads from Berkshire Hathaway's site; ensure internet connection
- **Encoding errors**: The script handles most encoding issues automatically
- **Missing files**: If download fails for some years, the script continues with available data

## Advanced Usage

### Run Individual Steps
If you want to run parts separately:

1. **Download only**: `python project2_fetch_letters.py`
2. **Extract text only**: `python project2_extract_text.py`
3. **Analyze only**: `python project2_analyze.py`

### Customize Analysis
Edit `project2_analyze.py` to:
- Add new signal words to the `SIGNAL_WORDS` list
- Modify metrics calculations
- Change output formats

### View Raw Data
- `data/raw/`: Original downloaded HTML/PDF files
- `data/processed/`: Clean text files (one per year)

## Project Structure
- `project2_main.py`: Main script to run full pipeline
- `project2_fetch_letters.py`: Downloads letters from web
- `project2_extract_text.py`: Extracts text from HTML/PDF
- `project2_clean_text.py`: Text cleaning utilities
- `project2_analyze.py`: Computes metrics and saves results
- `project2_requirements.txt`: List of Python packages needed
- `data/`: Folder for all data files
  - `raw/`: Downloaded original files
  - `processed/`: Clean text files
  - `analysis.json`: Analysis results
  - `decade_summary.json`: Decade-level summaries
  - `metadata.json`: File information
- `output/`: (Future) Charts and reports

## What the Analysis Tells You
- **Vocabulary richness trends**: Has Buffett's word choice become more or less diverse?
- **Signal word evolution**: When did words like "technology" or "risk" become more prominent?
- **Writing style changes**: Average word length and common themes over decades
- **Comparative insights**: Compare different periods (e.g., 1980s vs 2020s)

## Contributing
This is an educational project. Feel free to modify and experiment!

## License
Educational use only. Berkshire Hathaway shareholder letters are copyrighted.