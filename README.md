# Text-Readability
Usage: python readability.py

This program finds out the grade for which a text is appropriate. Longer words and longer sentencess correlate to higher reading levels. Lower reading levels otherwise.

Readability level is often calculated using Coleman-Liau index which involves the formula:  
index = 0.0588 * L - 0.296 * S - 15.8, where L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.

For this program, any sequence of characters separated by spaces is considered a word. Hyphenated words count as one word. Period, exclamation mark, or question mark signify the end of a sentence. Digits and other symbols are not supported though.
