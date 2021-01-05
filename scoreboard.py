from turtle import Turtle

import random
# Create our food class which is inherited from the Turtle Class
# Now, this food is like when we create our Turtle but we're customizing it.
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.color('white')
        self.hideturtle()
        self.penup()
        self.score = 0
        self.high_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto (0, 270)
        self.write(f"Scoreboard: {self.score} High Score: {self.high_score}", True, align="center", font=('Courier', 18, 'bold'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def score_points(self):
        self.score += 1
        self.update_scoreboard()


