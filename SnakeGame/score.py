from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def finish_game(self):
        self.clear()
        self.color("red")
        self.goto(0, 0)
        self.write(f"Game Over. Your score was: {self.score}", align=ALIGNMENT, font=FONT)
