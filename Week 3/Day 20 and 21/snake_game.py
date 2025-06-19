import random
import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("ssS Snake Game Sss")
screen.tracer(0)

snake = Snake()
food = Food(snake.head)
scoreboard = Scoreboard()
_continue = True

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

while _continue:
    screen.update()
    time.sleep(0.04)
    snake.move()
    snake.check_eat(food, scoreboard)
    if (snake.check_collision(scoreboard, screen)):
        break
    
    
screen.exitonclick()