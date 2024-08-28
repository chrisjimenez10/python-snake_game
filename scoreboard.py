from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "bold")
GAME_OVER_FONT = ("Courier", 15, "bold")
DATA_FILE = "./data.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.teleport(y=280)
        self.highscore = self.display_high_score_data()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(F"Score: {self.score} | Highs Score: {self.display_high_score_data()}", align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.update_high_score_data(new_score=self.score)
        self.score = 0
        self.update_score()

    def display_high_score_data(self):
        with open(DATA_FILE, mode="r") as file:
            content = int(file.read())
            return content

    def update_high_score_data(self, new_score):
        with open(DATA_FILE, mode="w") as file:
            file.write(str(new_score))

    # def game_is_over(self):
    #     self.color("red")
    #     self.home()
    #     self.write(arg="🤦‍ GAME OVER...", align=ALIGNMENT, font=GAME_OVER_FONT)

