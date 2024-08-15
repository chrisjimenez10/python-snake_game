COLORS = ("coral", "azure3", "DeepPink", "green", "blue", "plum1", "orange", "purple", "pink", "brown", "LightGoldenrod", "cyan", "turquoise", "lightblue", "lime", "lavender", "maroon", "navy", "olive", "orchid")

from turtle import Screen
class BgEffect():
    def __init__(self):
        self.level = 0
        self.screen = Screen()

    def change_bg_color(self):
        if self.level == 19:
            self.level = 0

        self.level += 1
        self.screen.bgcolor(COLORS[self.level])
