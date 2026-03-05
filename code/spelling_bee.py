"""NYT Spelling Bee solver with minimal helpers.

The words file lives in the top‑level `data/` folder; this module
computes the path relative to its own location so it will work when
you run it from `code/` or from a notebook.
"""

import os

# data file path constructed once so other functions can use it
DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "words.txt")


def load_wordlist(path=DATA_FILE):
    """Return a list of lowercase words from *path*."""
    with open(path, encoding="utf-8") as f:
        return [line.strip().lower() for line in f if line.strip()]


def uses_only(word, letters):
    """Does *word* consist solely of characters in *letters*?"""
    for letter in word:
        if letter not in letters:
            return False
    return True


def must_use(word, letter):
    """Does *word* use the required *letter*?"""
    for char in word:
        if char == letter:
            return True
    return False


def is_valid(word, letters, required):
    """Is *word* valid for the puzzle defined by *letters* and *required*?"""
    return uses_only(word, letters) and must_use(word, required) and len(word) >= 4


def find_words(letters, required, path=DATA_FILE):
    """Print all valid words using the global word list file."""
    with open(path) as word_file:
        for word in word_file:
            word = word.strip()
            if is_valid(word, letters, required):
                print(word)


def main():
    print("NYT Spelling Bee helper")
    print("Enter seven letters (center first or last).")
    entry = input("letters: ").strip().lower()
    if len(entry) < 7:
        print("please type all seven letters")
        return
    center = entry[0]
    print("valid words:")
    find_words(entry, center)


if __name__ == "__main__":
    main()
