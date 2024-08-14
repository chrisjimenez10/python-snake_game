from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.teleport(y=280)
        self.score = 0
        self.write(F"Score: {self.score}", align="center", font=('Arial', 10, 'bold'))

    def increment_score(self):
        self.score += 1
        self.clear()
        self.write(F"Score: {self.score}", align="center", font=('Arial', 10, 'bold'))

