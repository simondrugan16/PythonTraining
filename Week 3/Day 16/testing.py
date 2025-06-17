from turtle import Turtle, Screen
import oop
from prettytable import PrettyTable

print(oop.my_variable)

timmy = Turtle()
print(timmy)
#timmy.shape("turtle")
#timmy.color("DarkOrchid1")
#timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)

#my_screen.exitonclick()

my_table = PrettyTable()
my_table.add_column("Pokemon Name", ["Treecko", "Grovyle", "Sceptile"])
my_table.add_column("Type", ["Grass", "Grass", "Grass"])
print(my_table.align)
print(my_table)