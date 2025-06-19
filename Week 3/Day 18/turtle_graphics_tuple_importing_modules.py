from turtle import Turtle, Screen

timothy = Turtle()

timothy.shape("turtle")
timothy.color("DarkOrchid1")

def get_poly(num_sides: int):
    angle = 360 - (360/num_sides)
    for _ in range(0, num_sides):
        timothy.forward(50)
        timothy.left(angle)

for i in range(3, 9):
    get_poly(i)

for i in range(1, 200):
    if i % 10 <= 5:
        timothy.pendown()
    else:
        timothy.penup()
    timothy.forward(1)
    


screen = Screen()
screen.exitonclick()