# Caesar Cipher is just some program that encrypt and decrypt strings.
from random import shuffle


# Two ways to do it
# First one just lists

def encrypt(string):
    result = ''
    for c_s in string:
        for i in range(0, len(alphabet)):
            if c_s == alphabet[i]:
                result += encode_alphabet[i]

    print('This is list encrypt: ' + result)


def decrypt(string):
    result = ''
    for c_s in string:
        for i in range(0, len(alphabet)):
            if c_s == encode_alphabet[i]:
                result += alphabet[i]

    print('This is list decrypt: ' + result)

#Second one with dictionary

def encrypt_dict(string):
    result = ''
    for c_s in string:
        result += alphabet_dict[c_s]
    print('This is dict encrypt: ' + result)


def decrypt_dict(string):
    result = ''
    for c_s in string:
        key = [k for k, v in alphabet_dict.items() if v == c_s][0]
        result += key

    print('This is dict decrypt: '+ result)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    alphabet = 'a b c d e f g h i j l k m n o p q r s t u v w x y z'
    alphabet = alphabet.split()
    alphabet += ' '
    encode_alphabet = alphabet.copy()
    shuffle(encode_alphabet)

    alphabet_dict = {}
    for i in range(0, len(alphabet)):
        alphabet_dict.update({alphabet[i]: encode_alphabet[i]})

    print('Welcome to Caesar Cypher\n')

    while True:
        action = input("Type 'encode' to encrypt or 'decode' to decrypt\n")
        if action != 'encode' and action != 'decode':
            continue

        messenger = input('Type your message:\n').lower()

        if action == 'encode':
            encrypt(messenger)
            encrypt_dict(messenger)
        else:
            decrypt(messenger)
            decrypt_dict(messenger)

        p_again = input("Type 'yes' if you want to play again\n")
        if p_again != ('yes'.lower()):
            break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
