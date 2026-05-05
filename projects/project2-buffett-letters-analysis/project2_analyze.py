#!/usr/bin/env python3
"""
Analyze text metrics for each year and decade.
"""

import json
import os
from collections import Counter
import project2_clean_text

SIGNAL_WORDS = ['technology', 'moat', 'fear', 'uncertainty', 'opportunity', 'risk', 'inflation', 'insurance', 'capital', 'acquisition']

def analyze_year(year, tokens, filtered_tokens):
    """Analyze text for a single year."""
    total_words = len(tokens)
    unique_words = len(set(tokens))
    vocab_richness = unique_words / total_words if total_words > 0 else 0
    
    # Signal words (normalized per 10,000 words)
    word_counts = Counter(tokens)
    signal_counts = {}
    for word in SIGNAL_WORDS:
        count = word_counts.get(word, 0)
        normalized = (count / total_words) * 10000 if total_words > 0 else 0
        signal_counts[word] = normalized
    
    # Average word length
    avg_word_len = sum(len(word) for word in tokens) / total_words if total_words > 0 else 0
    
    # Most common words (after stopword removal)
    common_words = Counter(filtered_tokens).most_common(10)
    
    return {
        'year': year,
        'total_words': total_words,
        'unique_words': unique_words,
        'vocab_richness': vocab_richness,
        'avg_word_length': avg_word_len,
        'signal_words': signal_counts,
        'top_words': common_words
    }

def analyze_all_years():
    """Analyze all processed text files."""
    results = []
    for filename in os.listdir('data/processed/'):
        if filename.endswith('.txt'):
            year = int(filename.split('.')[0])
            filepath = os.path.join('data/processed/', filename)
            
            # Process text
            processed = project2_clean_text.process_text_file(filepath)
            tokens = processed['tokens']
            filtered = processed['filtered_tokens']
            
            analysis = analyze_year(year, tokens, filtered)
            results.append(analysis)
    
    # Sort by year
    results.sort(key=lambda x: x['year'])
    
    # Save results
    with open('data/analysis.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    return results

def aggregate_by_decade(results):
    """Group results by decade."""
    decades = {}
    for result in results:
        decade = (result['year'] // 10) * 10
        if decade not in decades:
            decades[decade] = []
        decades[decade].append(result)
    
    decade_summary = {}
    for decade, years in decades.items():
        decade_summary[decade] = {
            'years': len(years),
            'avg_vocab_richness': sum(y['vocab_richness'] for y in years) / len(years),
            'total_words': sum(y['total_words'] for y in years),
            'avg_signal_words': {
                word: sum(y['signal_words'][word] for y in years) / len(years)
                for word in SIGNAL_WORDS
            }
        }
    
    with open('data/decade_summary.json', 'w') as f:
        json.dump(decade_summary, f, indent=2)
    
    return decade_summary