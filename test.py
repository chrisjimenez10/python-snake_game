from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")

test_turtle = Turtle()

def up():
    test_turtle.setheading(90)
    test_turtle.forward(100)


def down():
    test_turtle.setheading(270)
    test_turtle.forward(100)


def left():
    test_turtle.setheading(180)
    test_turtle.forward(100)


def right():
    test_turtle.setheading(0)
    test_turtle.forward(100)

screen.listen()
screen.onkey(fun=up, key="Up")
screen.onkey(fun=down, key="Down")
screen.onkey(fun=left, key="Left")
screen.onkey(fun=right, key="Right")



screen.exitonclick()
