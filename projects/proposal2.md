# My Project Proposal

## What I'm building:
A decade-by-decade text analysis of Warren Buffett's annual shareholder 
letters (1977–2024), profiling how his language, vocabulary, and themes 
have shifted across six decades.

## Why I chose this:
As someone interested in venture capital and investing, I've always heard 
that Buffett's letters are some of the best financial writing ever 
produced. I want to go beyond reading them and actually measure how his 
language changed over time — does his tone get more cautious before market 
crashes? When does "technology" actually start appearing? This turns a 
primary source I'd read anyway into a data problem.

## Core features:

- Automatically fetch and extract text from all 48 letters (HTML for 
  1977–2003, PDF for 2004–2024)
- Count word frequencies and compute vocabulary richness per decade
- Track specific "signal words" year-by-year (e.g. technology, moat, 
  fear, uncertainty, opportunity)
- Measure sentence complexity (average sentence length) across decades
- Visualize findings: top words per decade, signal word trends over time, 
  vocabulary richness trend

## What I don't know yet:

- How to reliably extract clean text from PDFs without noise or errors
- How to define and measure vocabulary richness precisely 
  (unique word ratio? type-token ratio?)
- Whether stop word removal will accidentally filter out meaningful 
  signal words
- How to handle inconsistencies in older HTML letters 
  (formatting, tables, footnotes)