# This is Number Guessing Game
# We think a number between 1 to 100 and the user tries do guess
# Difficulty:
#   Hard - 5 guesses
#   Medium - 8 guesses
#   Easy - 10 guesses

# Imports
import random

# Global
difficulty_dict = {

    "easy": 10,
    "medium": 8,
    "hard": 5

}


# Functions

def set_difficulty():
    while True:
        level = input("Choose your difficulty. Type 'easy' or 'hard': ")
        if level == "easy" or level == "hard":
            break
        print("Sorry, i don't understand, try again.")

    return level

def make_guess(number):
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it. The answers is {number}")
        return True
    elif guess < number:
        print("Too low.")
    else:
        print("Too high.")

    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Welcome to the Number Guessing Game!!")
    still_playing = True

    while still_playing:
        print("I'm thinking of a number between 1 to 100.")

        difficulty = set_difficulty()

        number = random.randint(1, 100)
        guessed = False
        n_tries = difficulty_dict[difficulty]
        turns = 0

        while not guessed and turns < n_tries:
            guessed = make_guess(number)
            turns += 1

        if not guessed:
            print("You loose.")

        play_again = input("Type 'y' if you want to play again: ")
        if play_again != 'y':
            still_playing = False

    print("Bye.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
