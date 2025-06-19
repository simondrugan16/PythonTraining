from turtle import Turtle
import random

class Food():
    def __init__(self, snake_head) -> None:
        self.food = Turtle("square")
        self.food.color("white")
        self.food.penup()
        self.new_food_position(snake_head)

    def new_food_position(self, snake_head: Turtle):
        snake_head_location = snake_head.pos()
        while True:
            random_x = random.randint(-290, 290)
            random_y = random.randint(-290, 290)
            if not ((snake_head_location[0] - 10) < random_x < (snake_head_location[0] + 10) and
                    (snake_head_location[1] - 10) < random_y < (snake_head_location[1] + 10)):
                self.food.teleport(x=random_x, y=random_y)
                break
            print("@@@@@@@@@@")
    
    def make_segment(self, snake_head):
        segments = []
        food = Turtle("square")
        food.color("white")
        food.penup()
        food.goto(self.new_food_position(snake_head))
        segments.append(food)
        return segments