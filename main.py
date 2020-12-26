from turtle import Screen, Turtle

# setting up the screen details
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('🐍 Snake Game! 🐍')

# creating the body of the snake
snake_body = Turtle()
x_positions = [0, -20, -40]
snake = []

for snake_parts in range(3):
    snake_body = Turtle(shape = 'square')
    snake_body.color('white')
    snake_body.penup()
    snake_body.goto(x = x_positions[snake_parts], y = 0)
    snake.append(snake_body)

screen.exitonclick()