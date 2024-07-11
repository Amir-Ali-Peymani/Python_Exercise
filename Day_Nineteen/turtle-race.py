import turtle as t
import random
import turtles

screen = t.Screen()
user_bet = screen.textinput("Make you bet: ", "who is going to win? ")

movements = [10, 15, 20, 5]

turtles.leonardo.goto(turtles.x_starting_point, 0)
turtles.donatello.goto(turtles.x_starting_point, 200)
turtles.raphael.goto(turtles.x_starting_point, 100)
turtles.michelangelo.goto(turtles.x_starting_point, -100)

def turtle_movements():
    while(turtles.x_starting_point < 300):
        if(turtles.leonardo.xcor() != 350):
            turtles.leonardo.forward(random.choice(movements))
        else:
            print("leonardo is winner")
            if (turtles.leonardo.pencolor() == user_bet):
                print("you are the winner!!")
            break

        if(turtles.donatello.xcor() != 350):
            turtles.donatello.forward(random.choice(movements))
        else:
            print("donatello is winner")
            if (turtles.donatello.pencolor() == user_bet):
                print("you are the winner!!")
            break

        if(turtles.raphael.xcor() != 350):
            turtles.raphael.forward(random.choice(movements))
        else:
            print("raphael is winner")
            if (turtles.raphael.pencolor() == user_bet):
                print("you are the winner!!")
            break

        if(turtles.michelangelo.xcor() != 350):
            turtles.michelangelo.forward(random.choice(movements))
        else:
            print("michelangelo is winner")
            if (turtles.michelangelo.pencolor() == user_bet):
                print("you are the winner!!")
            break
turtle_movements()

screen.exitonclick()

