import pandas

data_fur_colour = pandas.read_csv("Week 4/Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")["Primary Fur Color"].to_list()

number_grey = data_fur_colour.count("Gray")
number_cinnamon = data_fur_colour.count("Cinnamon")
number_black = data_fur_colour.count("Black")

my_dict = {
    "Fur Colour": ["Grey", "Cinnamon", "Black"],
    "Count": [number_grey, number_cinnamon, number_black]
}

print(my_dict)
data = pandas.DataFrame(my_dict)

print(data)