import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from bgeffect import BgEffect

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
background_effect = BgEffect()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect if snake head collides with food circle
    if snake.head.distance(food) < 15:
        food.refresh()
        background_effect.change_bg_color()
        snake.extend()
        scoreboard.increment_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        # game_is_on = False
        # scoreboard.game_is_over()

    # Detect collision with snake body
    for segment in snake.segments[1:]: # Slicing the segments list to EXCLUDE the head (first segment)
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            # game_is_on = False
            # scoreboard.game_is_over()


screen.exitonclick()