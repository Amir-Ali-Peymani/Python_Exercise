
#NAZI TURTLE
from turtle import Turtle , Screen

turtle = Turtle()
print(turtle)
#         -------     |
#               |     |
#         ------|------
#         |     |
#         |     |------

turtle.color("red")
turtle.shape("turtle")
for a in range(0, 3):
    for a in range(0, 3):
        turtle.forward(45)
        turtle.left(90)
        turtle.forward(45)
        turtle.left(180)
        turtle.forward(45)
        turtle.right(90)
        turtle.forward(45)
    turtle.right(90)



my_screen = Screen()

my_screen.exitonclick()