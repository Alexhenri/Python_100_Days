# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List, Tuple, Any

import colorgram as c
import turtle as t

rgb_color_list: list[tuple[Any, Any, Any]] = []
colors_list = c.extract("rito.jpeg", 10)

for color in colors_list:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_color_list.append((r, g, b))

guguinha = t.Turtle()
guguinha.shape("turtle")

screen = t.Screen()
screen.colormode(255)

for rgb in rgb_color_list:
    guguinha.pendown()
    guguinha.dot(20, rgb)
    guguinha.penup()
    guguinha.forward(25)


screen.exitonclick()
