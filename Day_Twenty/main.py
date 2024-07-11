import turtle as t
import time
from snake import Snake

screen = t.Screen()
screen.setup(500, 500)
screen.bgcolor("gray")
screen.title("Snake Game")
screen.tracer(0)

positions = [(0,0), (-20,0),(-40,0)]

snakes = []

snake = Snake()

game_is_on= True

screen.listen()
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()    
           

screen.exitonclick()