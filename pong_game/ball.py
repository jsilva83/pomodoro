# Importing external packages.
import turtle

# Constants.
BALL_SHAPE = 'circle'
BALL_COLOR = 'white'


class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape(BALL_SHAPE)
        self.color(BALL_COLOR)
        return
