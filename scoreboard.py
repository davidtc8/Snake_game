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
        self.write(f"Scoreboard: {self.score}", True, align="center", font=('Courier', 18, 'bold'))

    def score_points(self):
        self.score += 1
        self.clear()
        self.goto (0, 270)
        self.write (f"Scoreboard: {self.score}", True, align="center", font=('Courier', 18, 'bold'))


