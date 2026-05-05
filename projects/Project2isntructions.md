# Buffett Letters Text Analysis App Specification

## Project overview

Build a Python project that performs a decade-by-decade text analysis of Warren Buffett's Berkshire Hathaway shareholder letters from 1977 to 2024. Berkshire Hathaway hosts shareholder letters on its official letters page, and the archive spans the years needed for this project. [web:83]

The goal of the project is to answer interesting questions about how Buffett's writing changed over time, not just to count words. The app should analyze language, vocabulary, themes, and sentence complexity across decades, then present the results clearly with tables, charts, and a readable summary. This matches the course goal of using Python to turn a meaningful body of text into structured insight. [web:83]

## Main research question

How has Warren Buffett's writing style changed across six decades of shareholder letters?

Sub-questions:
- Does his vocabulary richness increase or decrease over time?
- Do certain words become more common in specific decades?
- When do investing-related signal words like "technology," "risk," "fear," "opportunity," and "uncertainty" become more visible?
- Does sentence complexity change over time?
- Are there visible shifts in tone or emphasis around major market periods?

## Scope

Analyze Berkshire Hathaway shareholder letters from 1977 through 2024.

Important source notes:
- Berkshire Hathaway provides an official archive page listing the letters. [web:83]
- Recent letters such as 2024 are available as PDF files on the Berkshire Hathaway site. [web:84]
- The project proposal assumes that older letters may exist in HTML and newer ones in PDF, so the code should be flexible enough to handle both formats if needed. [web:83][web:84]

## What to build

Build a Python analysis project with these parts:

1. A data collection pipeline
2. A text cleaning and preprocessing pipeline
3. A metrics and analysis pipeline
4. A visualization pipeline
5. A simple results output, either:
   - a command-line summary plus saved charts, or
   - a small Flask app/dashboard if time allows

For the MVP, prioritize a script-based analysis pipeline and saved charts over a full web app.

## Core features

### 1. Fetch and extract letters
- Automatically fetch all Warren Buffett shareholder letters from 1977 to 2024 from Berkshire Hathaway's official archive page. [web:83]
- Support both HTML and PDF sources where necessary. [web:83][web:84]
- Save the raw files locally in a `data/raw/` folder.
- Extract clean text from each file and save cleaned plain text copies in `data/processed/`.

### 2. Organize letters by year and decade
- Associate each letter with:
  - year
  - decade label, such as 1970s, 1980s, 1990s, 2000s, 2010s, 2020s
- Store metadata in a structured format such as a CSV or JSON file.

### 3. Clean text
- Lowercase text
- Remove punctuation
- Remove extra whitespace
- Tokenize into words
- Optionally remove stop words, but preserve important finance-related signal words
- Remove obvious PDF extraction noise if present, such as page numbers, repeated headers, or artifacts

### 4. Compute analysis metrics
For each individual year and each decade, compute:
- total word count
- unique word count
- vocabulary richness
- average word length
- average sentence length
- most common words
- top words after stop word removal

Define vocabulary richness clearly and implement at least one primary metric:
- type-token ratio (unique words / total words)

Optional advanced richness metrics:
- moving-average type-token ratio
- root type-token ratio

### 5. Track signal words
Track frequency over time for a list of signal words, such as:
- technology
- moat
- fear
- uncertainty
- opportunity
- risk
- inflation
- insurance
- capital
- acquisition

For each signal word:
- count occurrences per year
- normalize counts per 10,000 words so comparisons across years are fair

### 6. Visualize findings
Create charts and save them in an `output/` folder:
- top words by decade, bar chart
- vocabulary richness by year, line chart
- average sentence length by year, line chart
- signal word frequency trends over time, line chart
- optional heatmap of selected word frequency by decade

### 7. Generate a readable summary
Create a final summary report in Markdown that explains:
- what text was analyzed
- what questions were asked
- what methods were used
- what patterns were found
- what limitations exist

## Recommended project structure

```text
buffett-letters-analysis/
├── app.py                     # optional Flask app, only if time allows
├── main.py                    # entry point for analysis pipeline
├── fetch_letters.py           # download/archive logic
├── extract_text.py            # HTML/PDF extraction logic
├── analyze.py                 # metrics and comparisons
├── visualize.py               # charts
├── utils.py                   # helper functions
├── requirements.txt
├── README.md
├── AI_USAGE.md
├── PROPOSAL.md
├── data/
│   ├── raw/
│   ├── processed/
│   └── metadata.csv
└── output/
    ├── charts/
    ├── tables/
    └── summary.md
```

## Preferred implementation approach

Use the course's two-pass approach:
- First pass: implement the core logic using built-in Python where possible, especially for text cleaning, token counting, dictionaries, sets, and file I/O
- Second pass: use libraries like pandas and matplotlib for analysis and visualization

Suggested libraries:
- `requests` for downloading files
- `beautifulsoup4` for HTML parsing
- `pymupdf` or `pdfplumber` for PDF extraction
- `re` for regex cleaning
- `collections.Counter` for word frequencies
- `pandas` for tables and grouped analysis
- `matplotlib` or `seaborn` for charts

## Rules for Copilot

Please follow these coding rules:

- Write clean, beginner-readable Python
- Use small, well-named functions
- Add short comments only where needed
- Do not put all logic in one giant script
- Avoid advanced abstractions unless necessary
- Prefer correctness and readability over cleverness
- Handle errors gracefully, especially failed downloads or bad PDF extraction
- Save intermediate outputs so results can be inspected
- Make the analysis reproducible

## Input and output expectations

### Input
Primary input is Warren Buffett shareholder letters from Berkshire Hathaway's official archive. [web:83]

### Output
The project should produce:
- cleaned text files
- a CSV or JSON file with yearly and decade-level metrics
- several charts in PNG format
- a Markdown summary report

## Minimum viable product

The MVP should do the following:
- fetch or load a subset of letters
- extract text from them
- clean and tokenize the text
- compute word counts and vocabulary richness
- track at least 5 signal words across time
- generate at least 3 charts
- write a summary of findings

## Stretch goals

Only do these after the MVP works:
- build a small Flask dashboard to browse results
- add topic modeling
- add sentiment analysis
- compare Buffett's letters with another investor or CEO
- add interactive filtering by year/decade
- export results to CSV and Markdown automatically

## Suggested development order

1. Build letter metadata and downloader
2. Build HTML/PDF text extraction
3. Build text cleaning functions
4. Build yearly metrics
5. Build decade aggregation
6. Build signal word tracking
7. Build charts
8. Build summary report
9. Add optional Flask interface last

## Example questions the finished project should answer

- Which decade has the richest vocabulary?
- Which words define each decade most strongly?
- When does "technology" begin appearing more often?
- Are Buffett's sentences getting shorter or longer over time?
- Do years around major market events show changes in words like "fear" or "opportunity"?

## README expectations

The README should include:
- project goal
- text source
- questions asked
- methods used
- how to run the project
- main findings
- reflection on built-in Python vs library-based analysis

## AI usage expectations

Document all meaningful AI use in `AI_USAGE.md`:
- what was asked
- what code or explanation was generated
- what was changed or verified
- what was learned

## First coding task

Start by creating:
- `main.py`
- `fetch_letters.py`
- `requirements.txt`
- `README.md`
- folder structure for `data/` and `output/`

Then implement a script that:
1. creates metadata for the years 1977–2024
2. downloads a small test subset of letters
3. saves them locally
4. prints which files were successfully collected