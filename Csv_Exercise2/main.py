# #with open("weather_data.csv") as weather_file:
# #    data = weather_file.read()
# #    print(data)
# #    weather_file.close()
#
# #import csv
# #with open("weather_data.csv") as weather_file:
# #    csv_data = csv.reader(weather_file)
# #    print(csv_data)
# #    temp = []
# #    for row in csv_data:
# #        temp.append(row[1])
# #        print(row)
#
# import pandas
#
# data_panda = pandas.read_csv("weather_data.csv")
# print(data_panda)
# print(data_panda["temp"])
# print(data_panda["temp"].max())
#
# #convert
# temp_list = data_panda["temp"].tolist()
#
# #getting specified objects
# print(data_panda[data_panda["temp"]== data_panda["temp"].max()])
#
# #creating a csv file
# zelda_reviews = dict(games=["Ocarina", "Skyward Sword", "Breath of the Wild"], score=[10, 8, 100])
#
# data = pandas.DataFrame(zelda_reviews)
# data.to_csv("zelda_reviews.csv")
from typing import Dict, Any

import pandas

squirrel_count = {}

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
red = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]
black = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]


squirrel_count["Fur Color"] = ["red", "grey", "black"]
squirrel_count["Count"] = [len(red), len(grey), len(black)]

squirrel_count_csv = pandas.DataFrame(squirrel_count)
squirrel_count_csv.to_csv("squirrel_count.csv")


