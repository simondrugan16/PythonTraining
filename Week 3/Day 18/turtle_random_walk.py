import random
from turtle import Turtle, Screen

colours = [
    "red", "blue", "green", "orange", "purple", "yellow",
    "cyan", "magenta", "lime", "pink", "turquoise", "gold",
    "maroon", "navy", "violet", "salmon", "chocolate", "teal",
    "coral", "indigo"
]

angles = [0, 90, 270, 180]

jimmy = Turtle()
jimmy.shape("turtle")
jimmy.pensize(10)
jimmy.speed("fastest")

for i in range(100):
    #jimmy.color(random.choice(colours))
    colour_tuple = (random.randint(0, 255)/255, random.randint(0, 255)/255, random.randint(0, 255)/255)
    jimmy.color(colour_tuple)
    print(colour_tuple[0])
    print(colour_tuple[1])
    print(colour_tuple[2])
    jimmy.forward(20)
    jimmy.right(random.choice(angles))

screen = Screen()
screen.exitonclick()