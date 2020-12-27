from turtle import Turtle
import random
# Create our food class which is inherited from the Turtle Class
# Now, this food is like when we create our Turtle but we're customizing it.
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len= .5, stretch_wid= .5)
        self.color('yellow')
        self.speed('fastest')
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        random_x = random.randint (-280, 280)
        random_y = random.randint (-280, 280)
        self.goto (random_x, random_y)