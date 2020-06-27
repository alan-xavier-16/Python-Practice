from words import get_random_word


def get_num_attempts():
    """Get number of incorrect attempts allowed"""
    while True:
        num_attempts = input(
            "How many of incorrect attempts do you want? [1-25]: ")
        try:
            num_attempts = int(num_attempts)
            if 1 <= num_attempts <= 25:
                return num_attempts
            else:
                print(f"{num_attempts} must be between 1 and 25!")
        except ValueError:
            print(f"{num_attempts} is not a valid!")
        except Exception as err:
            print(f"Exception Type: {type(err).__name__}")


def get_word():
    '''Get minimim and maximum word length for guess'''
    while True:
        min_word_length = input(
            "What is the minimum word length you want? [>3]: ")
        max_word_length = input(
            "What is the maximum word length you want? [<16]: ")
        try:
            min_word_length = int(min_word_length)
            max_word_length = int(max_word_length)

            if min_word_length > 3 and max_word_length < 16:
                return get_random_word(min_word_length, max_word_length)
            else:
                print(f"Values must be between greater than 3 and less than 16!")
        except ValueError:
            print(f"Values must be between greater than 3 and less than 16!")
        except Exception as err:
            print(
                f"Exception Type: {type(err).__name__}, Arguments: {err.args}")


def get_word_display(word, guesses):
    '''Display for user, word as str & guesses as list'''
    displayed_word = [
        "*" if letter not in guesses else letter for letter in word]
    return "".join(displayed_word)


def get_guesses(guesses, remaining_attempts):
    '''Get user letter, guesses as list, remaining_attempts as int'''
    while remaining_attempts > 0:
        guess = input("Please enter a letter: ")
        try:
            if guess.isalpha() and len(guess) == 1 and guess not in guesses:
                return guess
            elif not guess.isalpha():
                print(f"{guess} must be an alphabetic character!")
            elif guess in guesses:
                print(f"You already tried {guess}!")
            elif len(guess) > 1 or len(guess) < 1:
                print("Only 1 character is allowed!")
        except Exception as err:
            print(
                f"Exception Type: {type(err).__name__}, Arguments: {err.args}")


def play_hangman():
    '''Start game'''
    print("Starting game....")
    print()
    # Setting initial state
    remaining_attempts = get_num_attempts()
    word = get_word()
    guesses = []
    word_solved = False

    while remaining_attempts > 0 and not word_solved:
        print(f"Let's play! WORD: {get_word_display(word, guesses)}")
        print(f"Attempts remaining: {remaining_attempts}")
        print(f"Previous guesses: {''.join(guesses)}")
        print()

        guess = get_guesses(guesses, remaining_attempts)
        if guess in word:
            print(f"---{guess} is correct!---")
        else:
            print(f"---{guess} is NOT correct! Please try again!---")
            remaining_attempts -= 1
        guesses = [*guesses, guess]

        if "*" not in get_word_display(word, guesses):
            word_solved = True
        print()

    # Game over & reveal word
    print(f"The word is: {word}")

    # Win or Lose
    if word_solved:
        print("You won! Congratulations!")
    else:
        print("You lost!")

    # Try again
    try_again = input("Would you like to try again? [Y/y]: ")
    return try_again.lower() == "y"


if(__name__ == '__main__'):
    while play_hangman():
        print()
