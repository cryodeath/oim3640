#!/usr/bin/env python3
"""
Main entry point for Buffett Letters Analysis
"""

import project2_fetch_letters as fetch_letters
import project2_extract_text as extract_text
import project2_analyze as analyze

def main():
    print("Starting Buffett Letters Analysis...")
    
    # Fetch letters
    print("Step 1: Fetching letters...")
    fetch_letters.fetch_all_letters()
    
    # Extract text
    print("Step 2: Extracting text...")
    extract_text.extract_all_texts()
    
    # Analyze
    print("Step 3: Analyzing text...")
    results = analyze.analyze_all_years()
    decade_summary = analyze.aggregate_by_decade(results)
    
    print("Analysis complete!")
    print(f"Processed {len(results)} years")
    print(f"Results saved to data/analysis.json")
    print(f"Decade summary saved to data/decade_summary.json")
    
    # Print some sample results
    if results:
        print(f"\nSample results for {results[0]['year']}:")
        print(f"  Total words: {results[0]['total_words']}")
        print(f"  Vocabulary richness: {results[0]['vocab_richness']:.3f}")
        print(f"  Top words: {[word for word, count in results[0]['top_words'][:5]]}")

if __name__ == "__main__":
    main()