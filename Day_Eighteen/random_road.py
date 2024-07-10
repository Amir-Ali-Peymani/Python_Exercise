import random
import turtle as t

max = t.Turtle()

colors = ["green", "brown", "black", "blue", "darkblue"]
angles = [0, 90, 180, 270]

#for a in range(0, 40):
#    max.width(10)
#    max.left(random.choice(angles))
#    max.forward(11)
#    max.right(random.choice(angles))
#    max.forward(11)
#    max.color(random.choice(colors))
max.width(5)
#0 ->fastes
#10->fast
#6 ->normal
#3 ->slow
#1 ->slowest
max.speed(0)
#or you can do this way
for a in range(500):
    
    max.color(random.choice(colors))
    max.forward(15)
    max.setheading(random.choice(angles))
    


screen = t.Screen()
screen.exitonclick()

max.forward(100)




