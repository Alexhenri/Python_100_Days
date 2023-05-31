import pandas

file_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter: row.code for (index, row) in file_csv.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ")
    try:
        result = [alphabet[c.upper()] for c in word]
        print(result)
    except KeyError:
        print("Sorry, only letter in the alphabet please!")
        generate_phonetic()


generate_phonetic()
