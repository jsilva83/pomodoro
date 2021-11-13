import turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """This class creates and manages the object snake in the screen.\n
    attr: snake_segments, represents the snake segments made of squares.
    """

    def __init__(self) -> None:
        self.snake_segments = []
        for pos in STARTING_POSITIONS:
            new_snake_segment = turtle.Turtle()
            new_snake_segment.penup()
            new_snake_segment.shape('square')
            new_snake_segment.color('white')
            new_snake_segment.goto(pos)
            self.snake_segments.append(new_snake_segment)
        self.snake_size = 3
        self.head = self.snake_segments[0]
        return

    def move(self) -> None:
        """Method that moves the snake one square forward"""
        for n in range(self.snake_size - 1, 0, -1):
            next_position = self.snake_segments[n - 1].pos()
            self.snake_segments[n].goto(next_position)
        self.snake_segments[0].forward(MOVE_DISTANCE)
        return

    def up(self) -> None:
        """Turns the heading of the snake up"""
        # Changing the heading of the head of the snake
        # If direction is down it cannot go up (no 180 degrees turns)
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        return

    def down(self) -> None:
        """Turns the heading of the snake down"""
        # Changing the heading of the head of the snake
        # If direction is up it cannot go down (no 180 degrees turns)
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        return

    def left(self) -> None:
        """Turns the heading of the snake left"""
        # Changing the heading of the head of the snake
        # If direction is right it cannot go left (no 180 degrees turns)
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        return

    def right(self) -> None:
        """Turns the heading of the snake right"""
        # Changing the heading of the head of the snake
        # If direction is left it cannot go right (no 180 degrees turns)
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        return