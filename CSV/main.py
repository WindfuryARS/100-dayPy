# with open("weather_data.csv", "r") as f:
#    weather = f.readlines()
#    print(weather)

# import csv
# with open("weather_data.csv", "r") as f:
#    data = csv.reader(f)
#    temperature = []
#    for row in data:
#        if row[1] != "temp":
#            temperature.append(int(row[1]))
#    print(temperature)

import pandas

#data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
#data_dict = data.to_dict()
#print(data_dict)
#
#temp_list = data["temp"].to_list()
#print(temp_list)
#
##print(round(sum(temp_list)/len(temp_list), 2))
#
#print(data["temp"].mean())
#print(data["temp"].max())
#print(data["temp"])
#print(data.temp)

#print(data[data.day == "Monday"])
#
#print(data[data.temp == data["temp"].max()])

#monday = data[data.day == "Monday"]
#monday_temp = int(monday["temp"])
#monday_temp_F = monday_temp * 9/5 + 32
#print(monday_temp_F)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data["Primary Fur Color"].value_counts())

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

data_dict = {"Fur Color:": ["Gray", "Cinnamon", "Black"],""
             "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_data.csv")