# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def mod(n1, n2):
    return n1 % n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": mod

}
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print("Welcome do Calculator\n")
    number1 = int(input("What is the first number?\n"))
    while True:
        operator = input("Choose the operator: Add +, Subtract -, Multiply *, Divide /, Mod %\n")
        number2 = int(input("What is the other number?\n"))
        calculation_helper = operations[operator]
        result = calculation_helper(number1, number2)
        print(f"{number1} {operator} {number2} = {result}\n")
        again = input(f"Type y to continue calculating with {result}\n")
        if again != "y" :
            break
        number1 = result




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
