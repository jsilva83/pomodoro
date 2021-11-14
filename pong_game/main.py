# Importing packages.
import time
import turtle
import right_paddle

# Constants.
GAME_WINDOW_WIDTH = 800
GAME_WINDOW_HEIGHT = 600
GAME_WINDOW_BACKGROUND_COLOR = 'black'
GAME_WINDOW_TITLE = 'My Pong Game'

# Game initialization.
game_window = turtle.Screen()
game_window.setup(width=GAME_WINDOW_WIDTH, height=GAME_WINDOW_HEIGHT)
game_window.bgcolor(GAME_WINDOW_BACKGROUND_COLOR)
game_window.title(GAME_WINDOW_TITLE)
# Create right paddle.
r_paddle = right_paddle.RightPaddle()
for _ in range(1, 15):
    r_paddle.move_up()
    time.sleep(1)
for _ in range(1, 30):
    r_paddle.move_down()
    time.sleep(1)


# Exit window on click.
game_window.exitonclick()
