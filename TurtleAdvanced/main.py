from turtle import Turtle, Screen
import random


def move_up():
    guguinha.setheading(90)
    guguinha.forward(10)


def move_right():
    guguinha.setheading(0)
    guguinha.forward(10)


def move_down():
    guguinha.setheading(270)
    guguinha.forward(10)


def move_left():
    guguinha.setheading(180)
    guguinha.forward(10)


def poop():
    guguinha.dot(10, "brown")


def guguinha_mode():
    guguinha.shape("turtle")
    guguinha.speed("fastest")
    guguinha.color("green")
    guguinha.penup()

    s.listen()
    s.onkey(move_up, "w")
    s.onkey(move_left, "a")
    s.onkey(move_right, "d")
    s.onkey(move_down, "s")
    s.onkey(poop, "space")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


def start():
    position = 0
    finish = False
    winner = None

    while finish == False:
        for turtle in turtles:
            speed = random.randint(0, 11)
            turtle.forward(speed)
            turtle_post = turtle.position()
            if turtle.color()[0] == "red":
                speed = 20
            if turtle_post[0] > float(position):
                position = turtle_post[0]

            if turtle_post[0] >= 300.0:
                finish = True
                winner = turtle
                break

    winner.forward(10)
    winner.setheading(90)
    if winner.color()[0] == bet:
        s.textinput("You Win", "")
    else:
        s.textinput("You Loose", "")

    while True:
        turtle.speed("slowest")
        turtle.forward(20)
        turtle.backward(20)


def set_lines_race():
    line = Turtle()
    line.hideturtle()
    line.speed("fastest")
    # start
    line.penup()
    line.setposition(-375, -215)
    line.pendown()
    line.setposition(-375, 265)
    # finish
    line.penup()
    line.setposition(300, -215)
    line.pendown()
    line.setposition(300, 265)


def race_mode():
    set_lines_race()
    position = -200
    for i in range(0, 10):
        t = Turtle()
        t.shape("turtle")
        t.color(color_list[i])

        t.penup()
        t.setposition(-400, position)
        turtles.append(t)
        position += 50

    global bet
    bet = s.textinput("Make your bet", "Choose the turtle who wants to win!! Choose a color: ")

    s.listen()
    s.onkey(start, "space")


# globals
bet = ""
turtles = []
color_list = ["red", "green", "yellow", "black", "blue", "pink", "purple", "grey", "brown", "orange"]

# start Screen
s = Screen()

# race mode
#race_mode()

# guguinha mode
guguinha = Turtle()
guguinha_mode()

s.exitonclick()
