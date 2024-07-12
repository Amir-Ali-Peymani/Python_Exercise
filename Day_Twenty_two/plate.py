from turtle import Turtle

X_CORDINATE = -330

class Plate(Turtle):
    
    def __init__(self, x_cordinate):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.speed(0)
        self.setx(x_cordinate)
        
        

    def moving_position(self, x_cordinate, y_cordinate):
        self.goto(x_cordinate, y_cordinate)
     
    def move_up(self):
        y_new = self.ycor()+20
        self.goto(self.xcor(), y_new)

    def move_down(self):
        y_new = self.ycor()-20
        self.goto(self.xcor(), y_new)