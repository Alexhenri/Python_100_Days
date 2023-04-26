from turtle import Screen, Turtle
import ball as b
import scoreboard as sco
import racket as r
import time


def create_div():
    div = Turtle()
    div.color("white")
    div.hideturtle()
    div.penup()
    div.goto(0, 400)
    div.pendown()
    div.setheading(270)
    while div.ycor() > -400:
        div.forward(40)
        div.penup()
        div.forward(20)
        div.pendown()


def create_screen():
    s = Screen()
    s.tracer(0)
    s.setup(width=1200, height=800)
    s.bgcolor("black")
    s.title("Arcade Game - Pong ")

    create_div()
    s.update()

    return s


# create screen
screen = create_screen()

# create score
score_r = sco.Scoreboard(sco.RIGHT)
score_l = sco.Scoreboard(sco.LEFT)

# create racket
racket_r = r.Racket(r.RIGHT)
racket_l = r.Racket(r.LEFT)

# create ball
ball = b.Ball()

game_is_on = True
screen.listen()
screen.onkey(racket_l.move_up, "w")
screen.onkey(racket_l.move_down, "s")
screen.onkey(racket_r.move_up, "Up")
screen.onkey(racket_r.move_down, "Down")

while game_is_on:

    screen.update()
    time.sleep(0.01)
    ball.move()


    # hits racket
    if racket_r.distance(ball) < 30:
        ball.direction_x = b.DIRECTION[b.LEFT]
        if racket_r.heading() == 90:
            ball.direction_y = b.DIRECTION[b.UP]
        else:
            ball.direction_y = b.DIRECTION[b.DOWN]
    elif racket_l.distance(ball) < 30:
        ball.direction_x = b.DIRECTION[b.RIGHT]
        if racket_l.heading() == 90:
            ball.direction_y = b.DIRECTION[b.UP]
        else:
            ball.direction_y = b.DIRECTION[b.DOWN]

    # hits floor
    if ball.ycor() <= -380:
        print(ball.ycor())
        ball.direction_y = b.DIRECTION[b.UP]
    elif ball.ycor() >= 380:
        print(ball.ycor())
        ball.direction_y = b.DIRECTION[b.DOWN]

    # hit goal
    if ball.xcor() < -580:
        score_l.score += 1
        score_l.update_score()
        ball.b_reset()
    elif ball.xcor() > 580:
        score_r.score += 1
        score_r.update_score()
        ball.b_reset()



screen.update()
screen.exitonclick()
