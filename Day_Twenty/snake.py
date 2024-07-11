import turtle as t
#const value and written in capital
STARTING_POSITIONS = [(0,0), (-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snakes =[]
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            new_turtle = t.Turtle("square")
            new_turtle.penup()
            new_turtle.speed(3)
            new_turtle.color("black")
            new_turtle.goto(positions)
            self.snakes.append(new_turtle)

    def move(self):
        for snake in range(len(self.snakes)-1, 0, -1):
            x = self.snakes[snake-1].xcor()
            y = self.snakes[snake-1].ycor()
            self.snakes[snake].goto(x, y)
        self.snakes[0].forward(MOVE_DISTANCE) 


    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
