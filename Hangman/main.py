# This is the Hangman Game for Python
# This is a basic version of the game, without either classes or more advanced tools

import random
from replit import clear

stages_hang = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()


def print_hang_man(count):
    print(stages_hang[count])


def welcome_player():
    player = input('Welcome to the Hangman Game! What is your name?')
    print('Hello {}, let\'s get it started'.format(player))
    return player


def get_random_word(words):
    n_word = random.randint(0, len(words) - 1)
    return words[n_word]


def get_player_choice():
    while True:
        c = input('Guess the letter: ').lower()
        if (len(c) > 1):
            print('Please guess just one letter\n')
        else:
            return c


def check_if_win_game(word):
    if ('_' not in word):
        return True
    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list_of_all_words = words
    maximum_guess = 6
    player = welcome_player()

    # game loop
    while True:
        word = get_random_word(list_of_all_words)
        empty_word = []
        guess_words = []
        for c in word:
            empty_word.append('_')
        win = False
        total_guess = 0
        # guessing loop
        while not win and total_guess < maximum_guess:
            print_hang_man(total_guess)
            print(empty_word)
            guess = False
            c_choice = get_player_choice()
            clear()
            if c_choice not in guess_words:
                guess_words.append(c_choice)
                for n in range(0, len(word)):
                    if word[n] == c_choice:
                        empty_word[n] = c_choice
                        guess = True
                if not guess:
                    total_guess += 1

                win = check_if_win_game(empty_word)

                if win:
                    print(empty_word)
                    print('\nYou Won!!')
                else:
                    print_hang_man(total_guess)
                    print('You was hanged. You loose')
                    print('The word was: {}'.format(word))
            else:
                print('You already guessed the \'{}\'. Please try another'.format(c_choice))

        play_again = input('Do you want to play again? Y N\n')
        if (play_again == 'N' or play_again == 'n'):
            break

