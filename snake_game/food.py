import turtle
import random

X_MAX_POSITION = 270
X_MIN_POSITION = -270
Y_MAX_POSITION = 270
Y_MIN_POSITION = -270


class Food(turtle.Turtle):
    """The food class is a kind of turtle class with a shape of a circle and randomly placed in the screen"""

    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.penup()
        self.resizemode('user')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.next_position()
        return

    def next_position(self) -> None:
        """Calculates the next position of the food"""
        x_pos = random.randint(X_MIN_POSITION, X_MAX_POSITION)
        y_pos = random.randint(Y_MIN_POSITION, Y_MAX_POSITION)
        self.goto(x_pos, y_pos)
        return
