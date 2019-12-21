def sentence_maker(phrase):
    interrogatives = ("how", "why", "what", "where", "when", "whose")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

statements = []
while True:
    user_input = input("Enter statement: ")
    if user_input == "\end":
        break
    else:
        statements.append(sentence_maker(user_input))

print(" ".join(statements))   