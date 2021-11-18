# Imports.
import turtle

# Constants.
PADDLE_SHAPE = 'square'
PADDLE_COLOR = 'white'
PADDLE_UP = 90
PADDLE_DOWN = -90
PADDLE_DISTANCE_MOVE = 20
WINDOW_MAX_HEIGHT_POSITION = 300
WINDOW_MIN_HEIGHT_POSITION = -280
PROXIMITY_TOLERANCE = 10


class Paddle(turtle.Turtle):
    """This class extends the turtle class"""

    def __init__(self, paddle_initial_positions, obj_window) -> None:
        super().__init__()
        self.segments = []
        for position in paddle_initial_positions:
            self.add_segment(position)
        # Sets heading of the paddle head.
        self.head = self.segments[0]
        self.head.setheading(PADDLE_UP)
        # Sets heading of the paddle tail.
        self.tail = self.segments[-1]
        self.tail.setheading(PADDLE_DOWN)
        self.window = obj_window
        return

    def add_segment(self, position) -> None:
        """Creates de 3 segments of the paddle."""
        new_segment = turtle.Turtle()
        new_segment.shape(PADDLE_SHAPE)
        new_segment.color(PADDLE_COLOR)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move_up(self) -> None:
        """Moves the paddle up until it hits the wall."""
        if (WINDOW_MAX_HEIGHT_POSITION - self.head.ycor()) <= PROXIMITY_TOLERANCE:
            return
        for n in range(len(self.segments) - 1, 0, -1):
            self.segments[n].goto(self.segments[n - 1].position())
        self.head.forward(PADDLE_DISTANCE_MOVE)
        return

    def move_down(self) -> None:
        """Moves the paddle down until it hits the wall."""
        if (self.tail.ycor() - WINDOW_MIN_HEIGHT_POSITION) <= PROXIMITY_TOLERANCE:
            return
        for n in range(0, len(self.segments) - 1):
            self.segments[n].goto(self.segments[n + 1].position())
        self.tail.forward(PADDLE_DISTANCE_MOVE)
        return
