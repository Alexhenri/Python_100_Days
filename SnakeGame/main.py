from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake = Snake()
food = Food()
score = Score()

s.listen()
s.onkey(snake.move_up, "w")
s.onkey(snake.move_down, "s")
s.onkey(snake.move_left, "a")
s.onkey(snake.move_right, "d")

game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.05)
    snake.move()

    #food colision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grows()
        score.increase_score()

    #wall colision
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() < -280:
        score.finish_game()
        game_is_on = False

    #tail colision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.finish_game()
            game_is_on = False




s.exitonclick()
