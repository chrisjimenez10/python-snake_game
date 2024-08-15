from turtle import Turtle
import random as r

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("gold")
        self.speed("fastest")
        random_x = r.randint(-250, 250)
        random_y = r.randint(-250, 250)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = r.randint(-250, 250)
        random_y = r.randint(-250, 250)
        self.goto(random_x, random_y)
