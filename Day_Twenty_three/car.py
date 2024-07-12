from turtle import Turtle
import random

COLORS = ["red", "blue", "black", "green", "orange", "purple", "yellow"]
MOVEMENT = 10

class Car:
    def __init__(self):
        self.cars = []
        self.car_speed = MOVEMENT

    def create_cars(self):
        random_number = random.randint(1, 6)
        if random_number == 1:
            car = Turtle()
            car.color(random.choice(COLORS))
            car.penup()
            car.shape("square")
            car.shapesize(1,2) 
            car_y = random.randint(-240, 240)
            car.goto(300, car_y)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += 10


    