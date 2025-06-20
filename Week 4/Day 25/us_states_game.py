import turtle
import pandas
import time

my_screen = turtle.Screen()
my_screen.title("U.S. States Guessing Game")
image = "Week 4/Day 25/blank_states_img.gif"
my_screen.addshape(image)
turtle.shape(image)

us_state_info = pandas.read_csv("Week 4/Day 25/50_states.csv").set_index("state")[["x", "y"]].to_dict(orient="index")
print(us_state_info)

number_of_states = 50

for i in range(0, number_of_states):
    answer_state = my_screen.textinput(title= "Guess a state!", prompt="What's another state name?").title()
    timmy = turtle.Turtle()
    timmy.hideturtle()
    timmy.penup()
    if answer_state in us_state_info.keys():
        timmy.goto(us_state_info[answer_state]["x"] - 15, us_state_info[answer_state]["y"])
        timmy.pendown()
        timmy.write(answer_state, font=("Arial", 12, "normal"))
        timmy.penup()
    else:
        timmy.goto(-150, 0)
        timmy.write(f"You are wrong! you finished on {i + 1} points!", font=("Arial", 24, "normal"))
        timmy.penup()
        time.sleep(5)
        turtle.bye()
        my_screen.bye()
        break
print(answer_state)