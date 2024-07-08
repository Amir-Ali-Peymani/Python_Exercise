import random

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
              'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1','2','3','4','5', '6', '7', '8', '9','0']
symbols = ['!', '@', '$' , '*', '&', '^', '(',')','+','-']

character = int(input("how much letter? "))
number = int(input("how many numbers? "))
symbol = int(input("how many symbols? "))

password = []

for a in range(character):
    password.append(random.choice(characters))
for a in range(number):
    password.append(random.choice(numbers))
for a in range(symbol):
    password.append(random.choice(symbols))
for a in password:
    print(a, end="")