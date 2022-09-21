from turtle import Turtle
from typing import Tuple

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        self._turtle = Turtle(shape="turtle")
        self._turtle.penup()
        self._turtle.speed(0)
        self._turtle.setheading(90)

        self.reset_position()

    @property
    def position(self) -> Tuple[float, float]:
        return self._turtle.position()

    def reset_position(self):
        self._turtle.goto(STARTING_POSITION)

    def go_forward(self):
        self._turtle.forward(10)

    def is_at_finish_line(self) -> bool:
        return self._turtle.ycor() >= FINISH_LINE_Y
