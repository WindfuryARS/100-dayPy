from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.write("Score: {}".format(self.score), False, align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.color("white")
        self.write("Game Over", False, align="center", font=("Courier", 24, "normal"))

    def increase_score(self, score):
        self.score += score
        self.clear()
        self.write("Score: {}".format(self.score), False, align="center", font=("Courier", 24, "normal"))


