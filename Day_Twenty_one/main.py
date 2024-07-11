import turtle as t
import time
from food import Food
from snake import Snake
from score_board import Score_Board


screen = t.Screen()

screen.setup(500, 500)
screen.bgcolor("gray")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Score_Board()


screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while(game_is_on):
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 215 or snake.head.xcor() < -215 or snake.head.ycor() >215 or snake.head.ycor() < -215:
        score.game_over()
        game_is_on = False

#    for segment in snake.snakes:
#        if segment == snake.head:
#            pass
#        elif snake.head.distance(segment) < 10:
#            game_is_on = False
#            score.game_over()
# or you can you slicing
    for segment in snake.snakes[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()




screen.exitonclick()


