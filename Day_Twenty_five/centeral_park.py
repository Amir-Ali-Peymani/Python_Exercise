import pandas

data = pandas.read_csv("D:\Projects\Python\Python_Exercise\Day_Twenty_five\\004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrels)
print(red_squirrels)
print(black_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count":[gray_squirrels, red_squirrels, black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrels_count.csv")

