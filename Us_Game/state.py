import turtle


class State(turtle.Turtle):
    def __init__(self, name, coord, screen):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.shapesize(0.25, 0.25)
        self.color("black")
        self.goto(coord)
        self.name = name
        self.screen = screen

        self.onclick(self.guess_state)

    def guess_state(self, x, y):
        answer_state = self.screen.textinput(f"Guess the State -  0/50", "Write the name of the state:")
        if answer_state == self.name:
            print("Correct")
            self.hideturtle()
            self.write(f"{self.name}")
        else:
            print("Wrong")



