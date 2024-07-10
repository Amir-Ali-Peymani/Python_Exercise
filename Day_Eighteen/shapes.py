from turtle import Turtle, Screen

max = Turtle()
max.shape("turtle")
#line
#for a in range(0, 15):
#    max.pendown()
#    max.forward(8)
#    max.penup()
#    max.forward(7)

max.left(180)
max.penup()
max.forward(200)
max.right(90)
max.forward(200)
max.right(90)
max.forward(100)
#triganle
def triangle():
    for a in range(0, 3):
        max.pendown()
        max.forward(100)
        max.right(120)
def square():
    for a in range(0, 4):
        max.color("red")
        max.forward(100)
        max.right(90)
def pentagon():
    for a in range(0, 5):
        max.color("brown")
        max.forward(100)
        max.right(72)
def hexagon():
    for a in range(0, 6):
        max.color("green")
        max.forward(100)
        max.right(60)
def heptagon():#7
    for a in range(0, 7):
        max.color("black")
        max.forward(100)
        max.right(51.43)
def octagon():#8
    for a in range(0, 8):
        max.color("darkblue")
        max.forward(100)
        max.right(45)
def nonagon():#9
    for a in range(0, 9):
        max.color("blue")
        max.forward(100)
        max.right(40)
def decagon():#10
    for a in range(0, 10):
        max.color("darkgreen")
        max.forward(100)
        max.right(36)
triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()

screen = Screen()
screen.exitonclick()

