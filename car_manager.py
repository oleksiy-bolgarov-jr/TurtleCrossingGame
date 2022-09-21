import random
from turtle import Turtle
from typing import List

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
OFFSET_FROM_TOP_AND_BOTTOM = 50
OFFSCREEN_MARGIN = 50

COLLISION_DISTANCE = 20


class CarManager:
    def __init__(self):
        # Since Turtle objects can't be fully deleted, this list is required to recycle them
        self._recycled_turtles: List[Turtle] = []

        self._cars: List[Turtle] = []
        self._move_distance = STARTING_MOVE_DISTANCE

    def generate_car(self):
        if self._recycled_turtles:
            # You can't fully destroy a Turtle, so to prevent memory leaks, recycle existing Turtles where possible
            car = self._recycled_turtles.pop()
        else:
            car = Turtle(shape="square")
        car.penup()
        car.color(random.choice(COLORS))
        car.setheading(180)
        car.shapesize(1, 2)

        y_pos = random.randint(-300 + OFFSET_FROM_TOP_AND_BOTTOM, 300 - OFFSET_FROM_TOP_AND_BOTTOM)
        car.goto(300 + OFFSCREEN_MARGIN, y_pos)

        self._cars.append(car)

    def move_cars(self):
        for car in self._cars.copy():  # Iterate over a copy because elements could be removed
            if car.xcor() < -300 - OFFSCREEN_MARGIN:
                self._cars.remove(car)
                self._recycled_turtles.append(car)
                continue

            car.forward(self._move_distance)

    def speed_up_cars(self):
        self._move_distance += MOVE_INCREMENT

    def player_hit_by_car(self, player_position):
        for car in self._cars:
            if car.distance(player_position) <= COLLISION_DISTANCE:
                return True

        return False
