from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 80, "normal")
LEFT = 0
RIGHT = 1
SIDE = [(-100, 270), (100, 270)]


class Scoreboard(Turtle):
    def __init__(self, board):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.goto(SIDE[board])
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
