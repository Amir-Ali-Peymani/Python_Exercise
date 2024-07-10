import turtle as t
import random


max = t.Turtle()
t.colormode(255)

def random_colors():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    random_color = (r, b, g)
    return random_color
max.speed(0)

def circle_in_circle():
    for a in range(0, 360):
        max.color(random_colors())
        max.circle(100)
        max.left(1)
def circle(size):
    for a in range(int(360/size)):
        max.color(random_colors())
        max.circle(100)
        max.setheading(max.heading()+ size)
circle(1)

screen = t.Screen()
screen.exitonclick()
    