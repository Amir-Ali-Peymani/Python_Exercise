print("welcome to the calculator !!!")

total = int(input("how much was the bill? \n"))
tip = float(input("how much tip you want to pay? \n"))
count = int(input("how many people are you guys? \n"))

#print((int(total)+int(tip))/int(count))

print((total+(tip*count))/count)