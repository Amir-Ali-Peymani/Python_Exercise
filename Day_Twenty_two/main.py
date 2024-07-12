import turtle as t
import time
from plate import Plate
from ball import Ball
from score_board import Score


screen = t.Screen()
screen.tracer(0)
square_l = Plate(-330)
score_l = Score(-100)

square_r = Plate(330)
score_r = Score(50)
ball = Ball()

screen.listen()
screen.onkeypress(square_l.move_up, "Up")
screen.onkeypress(square_l.move_down, "Down")
screen.onkeypress(square_r.move_up, "w")
screen.onkeypress(square_r.move_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 305 or ball.ycor() < -305:
        ball.bounce_y()
    if ball.distance(square_r) < 50 and ball.xcor() > 310 or ball.distance(square_l) < 50 and ball.xcor() < -310:
        ball.bounve_x()
    if ball.xcor() > 390:
        score_l.increase_score()
        ball.reset_position()
    if ball.xcor() < -390:
        score_r.increase_score()
        ball.reset_position() 


screen.exitonclick()

