from car import Car
from player import Player
from score_board import Score
import turtle as t
import time


screen = t.Screen()
screen.bgcolor("gray")
screen.setup(600, 600)
screen.tracer(0)

car = Car()
turtle = Player()
score = Score()

screen.listen()
screen.onkeypress(turtle.move_up, "Up")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    car.create_cars()
    car.move_cars()
    for car_ in car.cars:
        if car_.distance(turtle)< 20:
            game_is_on = False
    if turtle.ycor() > 270:
        turtle.reset_position()
        score.increase_score()
        car.increase_speed()

screen.exitonclick()