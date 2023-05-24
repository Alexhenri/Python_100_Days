from turtle import Turtle
import random
import time

RIGHT = 1
LEFT = 0
UP = 1
DOWN = 0

# JUST TO GET MORE EASY TO UNDERSTAND
DIRECTION = [-1, 1]


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.direction_x = DIRECTION[random.randint(0, 1)]
        self.direction_y = DIRECTION[random.randint(0, 1)]

    def move(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x + (self.direction_x * 5), y + (self.direction_y * 5))

    def b_reset(self):
        self.goto(0, 0)
        self.direction_x = DIRECTION[random.randint(0, 1)]
        self.direction_y = DIRECTION[random.randint(0, 1)]
        time.sleep(0.5)
