from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCORE_POSITION = (-280, 260)


class Scoreboard:
    def __init__(self):
        self._turtle = Turtle(visible=False)
        self._turtle.penup()
        self._turtle.speed(0)

        self._level = 1

        self._refresh()

    @property
    def level(self):
        return self._level

    def increment_level(self):
        self._level += 1
        self._refresh()

    def game_over(self):
        self._turtle.home()
        self._turtle.write("YOU'RE DEAD", align="center", font=FONT)

    def _refresh(self):
        self._turtle.clear()

        self._turtle.goto(SCORE_POSITION)
        self._turtle.write(f"Level: {self.level}", align="left", font=FONT)
