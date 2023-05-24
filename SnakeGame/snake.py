from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
DISTANCE = 20
START_POSITIONS = [(0.0, 0.0), (-20.0, 0.0), (-40.0, 0.0)]


def create_segment():
    segment = Turtle()
    segment.penup()
    segment.speed("fastest")
    segment.shape("square")
    segment.color("white")

    return segment


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create_snake(self):
        for position in START_POSITIONS:
            s_body = create_segment()
            s_body.goto(position)
            self.segments.append(s_body)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].position())
        self.head.forward(DISTANCE)

    def move_up(self):
        if int(self.head.heading()) != DOWN:
            self.head.setheading(UP)

    def move_right(self):
        if int(self.head.heading()) != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if int(self.head.heading()) != RIGHT:
            self.head.setheading(LEFT)

    def move_down(self):
        if int(self.head.heading()) != UP:
            self.head.setheading(DOWN)

    def grows(self):
        new_tail = create_segment()
        new_tail.goto(self.tail.position())
        self.segments.append(new_tail)
        self.tail = new_tail

    def finish_game(self):
        for segment in self.segments:
            segment.hideturtle()


