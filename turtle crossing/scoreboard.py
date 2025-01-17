from turtle import Turtle

from scipy.stats import scoreatpercentile

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.score=0
        self.goto(x=-270,y=260)
        self.write(f"Level: {self.score}",align="left",font=FONT)

    def increase_score(self):
        self.clear()
        self.score+=1
        self.write(f"Level: {self.score}",align="left",font=FONT)
    def lost(self):
        self.goto(0,0)
        self.write(f"Game Over!!",align="center",font=FONT)





