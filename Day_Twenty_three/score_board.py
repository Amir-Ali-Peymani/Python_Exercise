from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score= 1
        self.penup()
        self.hideturtle()
        self.color("brown")
        self.goto(-250, 250)
        self.update_score()
    
    def update_score(self):
        self.write(f"Level: {self.score}", font=("Arial", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
        