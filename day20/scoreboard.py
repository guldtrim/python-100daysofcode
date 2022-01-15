from tkinter import CURRENT
from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.ht() #hides the turtle creating the scoreboard
        self.goto(x=0, y=250)
        self.color("white")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align="center", font=('Arial', 20, 'normal'))


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=('Arial', 20, 'normal'))
