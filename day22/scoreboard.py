from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.ht() #hides the turtle creating the scoreboard
        self.goto(x=0, y=250)
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"{self.l_score} | {self.r_score}", align="center", font=('Arial', 20, 'normal'))


    def left_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def right_score(self):
        self.r_score += 1
        self.update_scoreboard()