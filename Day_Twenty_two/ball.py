from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.speed("fastest")
        self.color("blue")
        self.x_move= 10
        self.y_move = 10
        self.move_speed = 0.04

    def move(self):
        x_cordinate = self.xcor() + self.x_move
        y_cordinate = self.ycor() + self.y_move
        self.goto(x_cordinate, y_cordinate)

    def bounce_y(self):
        self.y_move *= -1

    def bounve_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.04
        self.bounve_x()


    