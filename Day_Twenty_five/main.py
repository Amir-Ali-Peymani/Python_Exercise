#data = []

#with open("D:\Projects\Python\Python_Exercise\Day_Twenty_five\weather_data.csv") as file:
#    data = file.readlines()
#for a in data:
#    print(a)

#import csv 
#
#with open("D:\Projects\Python\Python_Exercise\Day_Twenty_five\weather_data.csv") as file:
#    data = csv.reader(file)
#    tempratures = []
#    for row in data:
#        tempratures.append(row[1])
#    for temp in tempratures:
#        print(temp)

import pandas

data =pandas.read_csv("D:\Projects\Python\Python_Exercise\Day_Twenty_five\weather_data.csv")

data_dic = data.to_dict()

data_temp_list = data["temp"].to_list()
print(data_temp_list)
average = 0

for number in data_temp_list:
    average += number
print(average/len(data_temp_list))
#i love coding with the python than any other language
 
print(data[data.day == "Saturday"])
print(data[data.temp == data.temp.max()])

sunday = data[data.day == "Sunday"]
print(
sunday.temp)



