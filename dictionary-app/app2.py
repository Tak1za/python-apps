# import json
# import os
import difflib
from difflib import get_close_matches
import mysql.connector

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()

word = input("Enter word: ")

query = cursor.execute("select * from Dictionary where Expression = '{}'".format(word))
results = cursor.fetchall()

query = cursor.execute("select Expression from Dictionary")
resultsExpressions = cursor.fetchall()

possibilities = [i for r in resultsExpressions for i in r]

if results:
    for result in results:
        print (result[1])
elif word.title() in possibilities:
    query = cursor.execute("select Definition from Dictionary where Expression = '{}'".format(word.title()))
    response = cursor.fetchall()
    for res in response:
        print (res[0])
elif word.upper() in possibilities:
    query = cursor.execute("select Definition from Dictionary where Expression = '{}'".format(word.upper()))
    response = cursor.fetchall()
    for res in response:
        print (res[0])
elif len(get_close_matches(word, possibilities)) > 0:
    closestMatch = get_close_matches(word, possibilities)[0]
    response = input("Did you mean {} instead? Enter Y if yes, or N if no. : ".format(closestMatch))
    if response.lower() == "y":
        query = cursor.execute("select Definition from Dictionary where Expression = '{}'".format(closestMatch))
        results = cursor.fetchall()
        for result in results:
            print (result[0])
    elif response.lower() == "n":
        print ("No word found")
    else:
        print ("We didn't understand your response")
else:
    print ("No word found")

# data = json.load(open("data.json"))

# def definition(word):
#     word = word.lower()
#     if word in data:
#         return data[word]
#     elif word.title() in data:
#         return data[word.title()]
#     elif word.upper() in data:
#         return data[word.upper()]
#     elif len(get_close_matches(word, data.keys())) > 0:
#         test = data.keys()
#         closestMatch = get_close_matches(word, data.keys())[0]
#         response = input("Did you mean {} instead? Enter Y if yes, or N if no. : ".format(closestMatch))
#         if response.lower() == "y":
#             return data[closestMatch]
#         elif response.lower() == "n":
#             return "Word doesn't exist, please double check!"
#         else:
#             return "We didn't understand your response."
#     else:
#         return "Word doesn't exist, please double check!"

# word = input("Enter word: ")
# print("\n".join(definition(word)))