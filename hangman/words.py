import json
from random import randint


def get_random_word(min_word_length, max_word_length):
    """Get a random word from the wordlist."""
    curr_word = None

    with open("./data/words.json", "r") as words:
        words = [*json.load(words)]
        while curr_word == None:
            word = words[randint(0, len(words))]
            if (len(word) < min_word_length) or (len(word) > max_word_length):
                continue
            else:
                curr_word = word
                return curr_word
