from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("turtle")
        self.penup()
        self.goto(0, -279)

    def move_up(self):
        self.forward(10)

    def reset_position(self):
        self.goto(0, -279)