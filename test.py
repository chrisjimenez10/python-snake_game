from turtle import Turtle, Screen

score = 1

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")

test_turtle = Turtle()
test_turtle.hideturtle()
test_turtle.color("blue")
test_turtle.teleport(y=280)
test_turtle.write(F"Score: {score}", align="center", font=('Arial', 10, 'bold'))


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
