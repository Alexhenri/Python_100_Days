from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("purple")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randrange(-280, 280, 10)
        y = random.randrange(-280, 280, 10)
        self.goto(x , y)