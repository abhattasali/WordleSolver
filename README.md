# WordleSolver

## How To Use

Run the below command ONLY to update the processedWords.txt file from the original raw data file: raw_eng_words.txt (Source: https://en.lexipedia.org/).
```
python3 process_words.py
```

Otherwise run
```
python3 predictor.py
```
and follow the steps prompted in the input terminal.

## Summary of Algorithm

This was purely for fun. Wordle relies on guessing a 5-letter word with three outcomes (grey: letter not in the word, yellow: letter in word but not correct position, green: letter is in the right position). You can play it [here](https://www.powerlanguage.co.uk/wordle/).

The algorithm for marking words was done a charDict.json file, which assigns unique prime numbers to each letter; in fact, each letter is assigned 6 unique prime numbers--one for "yellow" and five for "green", indicating the 5 possible positions that a particular letter can be arranged in the answer word. The rest is modulo arithmetic and boolean logic.
