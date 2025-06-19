import csv
import pandas

# with open("Week 4/Day 25/weather_data.csv") as weather_data_file:
#     weather_data = csv.reader(weather_data_file)
#     for row in weather_data:
#         print(row)

data = pandas.read_csv("Week 4/Day 25/weather_data.csv")
print(data)
print(data["temp"])