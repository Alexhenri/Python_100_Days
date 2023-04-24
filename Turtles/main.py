# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from turtle import Turtle, Screen
import random

polygons = {
    "triangle": 3,
    "square": 4,
    "pentagon": 5,
    "hexagon": 6,
    "heptagon": 7,
    "octagon": 8,
    "nonagon": 9,
    "decagon": 10,
    "circle": 0
}


def draw_any_polygon(my_turtle, sides):
    if sides == 0:
        my_turtle.penup()
        my_turtle.fd(50)
        my_turtle.setheading(90)
        my_turtle.fd(10)
        my_turtle.setheading(0)
        my_turtle.pendown()
        my_turtle.circle(radius=-165)
    else:
        ang = 360 / sides
        for i in range(0, sides):
            my_turtle.fd(100)
            my_turtle.rt(ang)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)

    return color


def draw_dashed(my_turtle):
    for _ in range(5):
        my_turtle.penup()
        my_turtle.fd(10)
        my_turtle.pendown()
        my_turtle.fd(10)


guguinha = Turtle()
guguinha.shape("turtle")
guguinha.color("green")
guguinha.speed("fast")
guguinha.width(5)
my_screen = Screen()
my_screen.colormode(255)

# draw_square(guguinha)
# polygon = input("What polygon do U want to draw? circle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon")
# draw_any_polygon(guguinha, polygons[polygon])

for polygon in polygons:
    draw_any_polygon(guguinha, polygons[polygon])
    guguinha.color(random_color())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

my_screen.exitonclick()