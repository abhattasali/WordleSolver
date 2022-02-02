import json
from xml.etree.ElementInclude import include

processedData = open('processedWords.txt',
                     encoding="utf8").read().splitlines()

# Type: string : (int freq, primeVal)
remaining = {}
for entry in processedData:
    entry = entry.split(",")
    remaining[entry[0]] = (int(entry[1]), int(entry[2]))

charDict = json.load(open('charDict.json'))
query = input("Want to solve the Wordle? (y/n): ")

# Dictionary: (int, str)
validatedChars = {}
# Set: (str)
includedChars = set()

while(query == "y"):
    to_scrub_words = set()

    query = input("Enter GREYS (ex: a,b,g) or '0': ")
    if query != "0":
        greys = query.split(",")
        for ch in greys:
            for word in remaining:
                if remaining[word][1] % charDict[ch]['yellow'] == 0:
                    to_scrub_words.add(word)

    for word in to_scrub_words:
        if not remaining:
            break
        remaining.pop(word)
    to_scrub_words.clear()

    first_five = list(remaining.keys())[:5]
    print("Printing top five recommended from most likely: ")
    print(first_five)

    query = input("Enter GREENS (ex: 1t,3r...) or 'n': ")
    if query != "n":
        currGreens = query.split(',')
        # Scrub All NON GREENS (ex: 2b)
        for val in currGreens:
            index = int(val[0])-1
            ch = val[1].lower()
            if index not in validatedChars:
                # Iterate All Remaining Words
                for word in remaining:
                    if remaining[word][1] % charDict[ch]['green'][index] != 0:
                        to_scrub_words.add(word)
                validatedChars[index] = ch
                print(validatedChars)

    for word in to_scrub_words:
        if not remaining:
            break
        remaining.pop(word)
    to_scrub_words.clear()

    first_five = list(remaining.keys())[:5]
    print("Printing top five recommended from most likely: ")
    print(first_five)

    # Scrub Yellows (appearance of letter)
    # Remove where you guessed AND if not in word at all
    query = input("Enter yellows+position in form (ex: 1x,4z..) or 'n': ")
    if query != "n":
        currYellows = query.split(',')
        for val in currYellows:
            index = int(val[0])-1
            ch = val[1].lower()
            if index not in includedChars:
                # Iterate All Remaining Words
                for word in remaining:
                    # Where You Guessed Letter
                    if (remaining[word][1] % charDict[ch]['green'][index] == 0) or (remaining[word][1] % charDict[ch]['yellow'] != 0):
                        to_scrub_words.add(word)
                includedChars.add(ch)

    for word in to_scrub_words:
        if not remaining:
            break
        remaining.pop(word)

    first_five = list(remaining.keys())[:5]
    print("Printing top five recommended from most likely: ")
    print(first_five)

    if not remaining:
        print("Sorry, couldn't find a word!")
        break

    # Give Best Results
    first_five = list(remaining.keys())[:5]
    print("Printing top five recommended from most likely: ")
    print(first_five)

    query = input("No good? Want to continue? (y/n): ")

print("Done.")
