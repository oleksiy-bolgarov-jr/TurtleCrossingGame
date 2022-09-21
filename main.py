import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

CAR_GENERATION_CHANCE = 1 / 6

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.go_forward, "Up")

n_iterations = 0
while True:
    time.sleep(0.1)
    screen.update()

    if car_manager.player_hit_by_car(player.position):
        scoreboard.game_over()
        break

    if player.is_at_finish_line():
        player.reset_position()
        scoreboard.increment_level()
        car_manager.speed_up_cars()

    car_manager.move_cars()
    if random.random() < CAR_GENERATION_CHANCE:
        car_manager.generate_car()

screen.exitonclick()
