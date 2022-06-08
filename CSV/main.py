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

data = pandas.read_csv("weather_data.csv")
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

monday = data[data.day == "Monday"]
monday_temp = int(monday["temp"])
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)