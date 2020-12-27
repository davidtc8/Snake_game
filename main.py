from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

# setting up the screen details
screen = Screen ()
screen.setup (width=600, height=600)
screen.bgcolor ('black')
screen.tracer (0)
screen.title ('🐍 Snake Game! 🐍')

# creating the body of the snake
snake_parts = Turtle ()
x_positions = [0, -20, -40]
snake_body = []

# creating a loop to stick together the body of the snake
snake = Snake ()
food = Food ()
scoreboard = Scoreboard()

screen.listen ()
screen.onkey (snake.up, key='Up')
screen.onkey (snake.down, key='Down')
screen.onkey (snake.right, key='Right')
screen.onkey (snake.left, key='Left')

screen.update ()
# Getting the game started
game_is_on = True
while game_is_on:
    screen.update ()
    time.sleep (.1)
    # Looping through each of the parts of the body of the snake
    snake.move ()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_points()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    # detect collision with head
    for segment in snake.snake_body:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.game_over ()
            game_is_on = False

screen.exitonclick ()
