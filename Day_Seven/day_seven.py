import hang_man

word = "letter"
display = []
for a in range(len(word)):
    display += "_"
condition = True
count = 0
while condition:
    guess = input()
    for a in range(len(word)):
        letter = word[a]
        if letter == guess:
            display[a] = letter
    if guess not in word:
        count += 1
        if count == 6:
            condition = False
            print('you lost')
    for a in display:
        print(a , end="")
    print()
    if "_" not in display:
        condition = False
        print("you won!!!")    
    print(hang_man.hangman[count])