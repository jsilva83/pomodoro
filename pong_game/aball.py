# Importing external packages.
import turtle

BALL_SHAPE = 'circle'
BALL_COLOR = 'white'


class Ball(turtle.Turtle):

    def __int__(self) -> None:
        super().__init__()
        self.shape(BALL_SHAPE)
        self.color(BALL_COLOR)
        self.penup()
        self.goto(0, 0)
        return
