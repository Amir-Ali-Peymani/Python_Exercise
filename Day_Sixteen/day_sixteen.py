from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Clone troopers",["rex", "cody", "tup", "thorn"])
table.add_column("Serial id", ["ct-7567", "cc-2224", "ct-5385", "cc-4477"])
table.add_column("Planet Death", ["unkown", "-", "space station", "bank"])

print(table)
