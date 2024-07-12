from turtle import Turtle

class Score(Turtle):

    def __init__(self, x_cordinate):
        super().__init__()
        self.penup()
        self.goto(x_cordinate, 290)
        self.score = 0
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", font=("Arial", 15, "normal"))

    def increase_score(self):
          self.score += 1
          self.clear()
          self.update()
