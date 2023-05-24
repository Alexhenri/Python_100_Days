from turtle import Turtle

LEFT = 0
RIGHT = 1
SIDE = [(-550, 0), (550, 0)]


class Racket(Turtle):
    def __init__(self, side):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=4)
        self.setheading(90)
        self.penup()
        self.goto(SIDE[side])

    def move_up(self):
        self.setheading(90)
        self.forward(10 * self.tork)

    def move_down(self):
        self.setheading(270)
        self.forward(10 * self.tork)

    def move(self):
        self.forward(10)


