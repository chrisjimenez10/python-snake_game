from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "bold")
GAME_OVER_FONT = ("Courier", 15, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.teleport(y=280)
        self.highscore = 0
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(F"Score: {self.score} | Highs Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score()

    # def game_is_over(self):
    #     self.color("red")
    #     self.home()
    #     self.write(arg="🤦‍ GAME OVER...", align=ALIGNMENT, font=GAME_OVER_FONT)

