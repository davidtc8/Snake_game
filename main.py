from turtle import Screen, Turtle
from snake import Snake
import time

# setting up the screen details
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title('🐍 Snake Game! 🐍')

# creating the body of the snake
snake_parts = Turtle()
x_positions = [0, -20, -40]
snake_body = []

# creating a loop to stick together the body of the snake
snake = Snake()

screen.listen()
screen.onkey(snake.up, key= 'Up')
screen.onkey(snake.down, key= 'Down')
screen.onkey(snake.right, key= 'Right')
screen.onkey(snake.left, key= 'Left')

screen.update()
# Getting the game started
game_is_on = True
while game_is_on:
    screen.update ()
    time.sleep (.1)
    # Looping through each of the parts of the body of the snake
    snake.move()

screen.exitonclick()