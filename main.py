import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Turtles
segments = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for segment_num in range(len(segments) - 1, 0, -1):
        # Here, we are assigning the new coordinate of last two initial segments as the coordinate of the segment in front of it by iterating from the end -> In other words, the preceding segment takes the place of the segment in front of it
        new_x = segments[segment_num - 1].xcor()
        new_y = segments[segment_num - 1].ycor()
        segments[segment_num].goto(new_x, new_y)

    segments[0].forward(20)
    segments[0].left(90)









screen.exitonclick()