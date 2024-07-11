import turtle as t

max = t.Turtle()

forward_length= 15

screen = t.Screen()

def move_forward():
    max.forward(15)

def move_backward():
    max.backward(15)

#def move_clockwise():
#    max.right(10)
#or can move clock wise
def move_clockwise():
    new_heading = max.heading()+10
    max.setheading(new_heading)

#def move_counterclockwise():
#    max.left(10)
#or you can write like this
def move_counterclockwise():
    new_heading = max.heading()-10
    max.setheading(new_heading)

#def close_window():
#    max.clear()
#    max.penup()
#    max.setheading(0.0)
#    max.goto(0, 0)
def close_window():
 
    max.clear()
    #is the function that put is back to its first place
    max.penup()
    max.home()   
    max.pendown()
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_counterclockwise, "a")
screen.onkey(move_clockwise, "d")
screen.onkey(close_window, "c")
screen.exitonclick()
