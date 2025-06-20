import csv
import pandas

# with open("Week 4/Day 25/weather_data.csv") as weather_data_file:
#     weather_data = csv.reader(weather_data_file)
#     for row in weather_data:
#         print(row)

data = pandas.read_csv("Week 4/Day 25/weather_data.csv")
print(data)
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

data_list = data["temp"].to_list()
print(data_list)

print(data["temp"].mean())

my_dict = {
    "words": ["the", "brown", "fox"],
    "letters": [3, 5, 3]
}

data = pandas.DataFrame(my_dict)

print(data)

data.to_csv("Week 4/Day 25/new_data.csv")