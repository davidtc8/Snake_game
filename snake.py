from turtle import Turtle

# variables for the game:
positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
up = 90
down = 270
right = 0
left = 180


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.color('red')
        new_segment.penup()
        new_segment.goto(position)
        self.snake_body.append(new_segment)

    def reset(self):
        for segment in self.snake_body:
            segment.goto(1000, 1000)
        # Basically we're doing kind of the same as in the 'init' function, because we're going to initialize the game again
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for part in range(len(self.snake_body) - 1, 0, -1):
            # this means that the last segment of the snake will follow the following segment
            # and the next segment fill follow the next segment.
            new_x = self.snake_body[part - 1].xcor()
            new_y = self.snake_body[part - 1].ycor()
            self.snake_body[part].goto(new_x, new_y)
        self.head.forward(move_distance)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)
