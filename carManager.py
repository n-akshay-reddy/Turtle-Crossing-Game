#generate all the random cars
COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]
#move distance of each of the cars on each refresh
STARTING_MOVE_DISTANCE = 5
#move distance increases when the user levels up
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_random_number = random.randint(1,6)
        if new_random_number == 2:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLOURS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
