import os

name_list ={}

def runing():
    enlisting = True
    while(enlisting):
        name = input("what is your name: ")
        bet = int(input("how much do you bet: "))
        name_list.update({name: bet})
        ask = input("are there more peopole? ")
        if ask=="no":
            enlisting = False
        if ask=="yes":
            os.system('cls')
def display():
    for name in name_list:
        print(name, end=" ")
        print(name_list[name])
def find_winner():
    large_number = 0
    for person in name_list:
        if name_list[person]> large_number:
            large_number = name_list[person]
    for person in  name_list:
        if large_number == name_list[person]:
            print("this person is the winner: ")
            print(person, end=" ")
    
runing()
print()
display()
print("=====================")
find_winner()