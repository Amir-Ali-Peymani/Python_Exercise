import turtle as t

POSITONS = [(0,0), (-10, 0), (-20, 0)]
MOVE = 20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for positon in POSITONS:
            self.add_segment(positon)

    def add_segment(self, position):
        snake = t.Turtle()
        snake.shape("square")
        snake.penup()
        snake.speed(3)
        snake.color("black")
        snake.goto(position)
        self.snakes.append(snake)

    def reposition(self):
        for seg in self.snakes:
            seg.goto(1000,1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]

    def extend(self):
        self.add_segment(self.snakes[-1].position())

    def move(self):
        for move in range(len(self.snakes)-1 , 0, -1):
            x = self.snakes[move-1].xcor()
            y = self.snakes[move-1].ycor()
            self.snakes[move].goto(x, y)
        self.snakes[0].forward(MOVE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)    
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


