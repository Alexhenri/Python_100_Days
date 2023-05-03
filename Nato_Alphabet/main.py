import pandas

file_csv = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter:row.code for (index, row) in file_csv.iterrows()}

while True:
    word = input("Enter a word: ")
    if word == "exit":
        break
    result = [alphabet[c.upper()] for c in word]
    print(result)

