import time
from turtle import Screen

import player
from player import Player
from carManager import CarManager
from scoreBoard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreBoard = ScoreBoard()

screen.listen()

screen.onkey(player.move_forward, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    #detect collision with the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreBoard.game_over()

    #Detect successful crossing
    if player.is_at_finish_line():
        player.move_to_starting_position()
        car_manager.level_up()
        scoreBoard.increase_level()

screen.exitonclick()