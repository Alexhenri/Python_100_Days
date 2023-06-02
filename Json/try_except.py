import random

# This a scratch just to learn try except structure
mylist = ["apple", "orange", "banana"]

try:
    print("Try print")
    print(mylist[4])
except FileNotFoundError:
    print("File Error")
except KeyError as key_error:
    print(key_error)
except IndexError:
    print("Index Error")
else:  # if error is diff than the expected by except
    print("Index Error Again")
finally:
    print("Always do that")


# Raising a error
# Even or odd
print("Adedaaaaaaa- nha")
player = int(input("Play: "))
if player > 10 or player < 0:
    raise ValueError("Human only have 10 fingers to play. Play something between 0 and 10")

machine = random.randint(0, 11)
