from turtle import Turtle

class Score_Board(Turtle):

    def __init__(self, score):
        super().__init__()
        self.score = 0
        self.highscore=score
        self.color("red")
        self.penup()
        self.goto(0, 220)
        self.hideturtle()
        self.penup()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score {self.highscore}", align="center", font=("Arial", 15, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score= 0
        self.update()
        with open("D:\Projects\Python\Python_Exercise\Day_Twenty_four\high_score.txt", mode="w") as file:
                file.write(str(self.highscore))
    #def game_over(self):
    #    self.goto(0,0)
    #    self.write("GAME OVER ", align="center", font=("Arial", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.update()
        