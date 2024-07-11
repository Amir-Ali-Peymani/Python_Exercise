from turtle import Turtle

class Score_Board(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("red")
        self.penup()
        self.goto(0, 220)
        self.hideturtle()
        self.penup()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER ", align="center", font=("Arial", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()
        