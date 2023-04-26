from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
POSITION = (0, 270)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.update_score()
        self.get_high_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.goto(POSITION)
        self.color("white")
        self.write(f"Score: {self.score}   |   HighScore: {self.high_score}" , align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def finish_game(self):
        self.clear()
        self.goto(0, 0)
        if self.high_score < self.score:
            self.color("green")
            self.high_score = self.score
            self.write(f"Nice. You got a NEW score: {self.score}", align=ALIGNMENT, font=FONT)
            self.save_high_score()
        else:
            self.color("red")
            self.write(f"Game Over. Your score was: {self.score}", align=ALIGNMENT, font=FONT)

        self.score = 0
        self.hideturtle()

    def get_high_score(self):
        #here we get the highscore
        try:
            file = open(file="high_score.txt", mode="r")
            data = int(file.read())
            self.high_score = data
            file.close()
        except:
            pass

    def save_high_score(self):
        file = open(file="high_score.txt", mode="w")
        file.write(str(self.high_score))
        file.close()

