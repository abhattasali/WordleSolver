# Source: https://en.lexipedia.org/
# Program Scrubs Data to Create List containing
# 1. Word, 2. Word Frequency, 3. Unique Prime Combination

import json
from operator import itemgetter
# Each character get's assigned 6 prime numbers, 5 of which in Green
# correspond to the position 0-4 in the 5 letter word.
# Characters sorted by frequency, optimize for smaller primes in more
# popular characters.
DEFAULT_WORD_LENGTH = 5
MIN_FREQUENCY_FILTER = 5

charDict = json.load(open('charDict.json'))

wordData = open('raw_eng_words.txt',
                encoding="utf8").read().splitlines()

# Raw Data: 0. Word, 1. Length, 2. Freq, 3. # of Articles
# Extract only Word & Freq
word_freq_id = {}
wordList = []

for entry in wordData:
    entry = entry.split(' ')
    currWord = entry[0]
    primeID = 1
    addToList = True
    for i in range(DEFAULT_WORD_LENGTH):
        ch = currWord[i]
        if ch not in charDict:
            addToList = False
            break
        primeID *= charDict[ch]["green"][i]*charDict[ch]['yellow']

    if addToList and (int(entry[2]) >= MIN_FREQUENCY_FILTER):
        word_freq_id[currWord] = (int(entry[2]), primeID)
        wordList.append((currWord, int(entry[2]), primeID))

sorted(wordList, key=itemgetter(1))
f = open("processedWords.txt", "w")
for word, freq, num in wordList:
    f.write(str(word) + "," + str(freq) + "," + str(num) + "\n")
f.close()
