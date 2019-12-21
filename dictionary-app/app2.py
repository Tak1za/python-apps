import json
import os
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        closestMatch = get_close_matches(word, data.keys())[0]
        response = input("Did you mean {} instead? Enter Y if yes, or N if no. : ".format(closestMatch))
        if response.lower() == "y":
            return data[closestMatch]
        elif response.lower() == "n":
            return "Word doesn't exist, please double check!"
        else:
            return "We didn't understand your response."
    else:
        return "Word doesn't exist, please double check!"

word = input("Enter word: ")
print("\n".join(definition(word)))