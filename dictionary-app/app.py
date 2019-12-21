import json
import os
import difflib
from difflib import SequenceMatcher

if os.path.exists("data.json"):
    data = json.load(open("data.json"))

def definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        maxSimilarity = 0
        for item in data.keys():
            similarity = SequenceMatcher(None, item, word).ratio()
            if(similarity > maxSimilarity):
                maxSimilarity = similarity
                similarWord = item
        if maxSimilarity > 0.5:
            print ("Did you mean {}? Type Y if Yes, else type N.".format(similarWord))
            userInput = input()
            if userInput.lower() == "y":
                return data[similarWord]
        return "Word doesn't exist, please double check!"

word = input("Enter word: ")
print(definition(word))