import json
from difflib import get_close_matches

with open("data.json", "r") as JSON_dict:
    data = json.load(JSON_dict)


def findSimilarWord(word, data):
    key_arr = data.keys()
    return get_close_matches(word, key_arr)


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(findSimilarWord(word, data)) > 0:
        similar_word = findSimilarWord(word, data)[0]
        user_confirmation = input(
            f"Did you mean {similar_word}? Enter 'Y' for 'yes' and 'N' for 'no': ")
        if user_confirmation == "Y":
            return data[similar_word]
        elif user_confirmation == "N":
            return f"{word} not found! Please try again."
        else:
            return f"{user_confirmation} is not valid."
    else:
        return f"{word} not found! Please try again."


word = input("Enter a word to search: ")

output = translate(word)

if type(output) == list:
    for definition in output:
        print(definition)
else:
    print(output)
