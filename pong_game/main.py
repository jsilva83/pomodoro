# Importing packages.
import time
import turtle
import paddle

# Constants.
GAME_WINDOW_WIDTH = 800
GAME_WINDOW_HEIGHT = 600
GAME_WINDOW_BACKGROUND_COLOR = 'black'
GAME_WINDOW_TITLE = 'My Pong Game'
PADDLE_SPEED = 0.1
R_PADDLE_INITIAL_POSITIONS = [(370, 20), (370, 0), (370, -20)]
L_PADDLE_INITIAL_POSITIONS = [(-380, 20), (-380, 0), (-380, -20)]

# Game initialization.
game_window = turtle.Screen()
game_window.setup(width=GAME_WINDOW_WIDTH, height=GAME_WINDOW_HEIGHT)
game_window.bgcolor(GAME_WINDOW_BACKGROUND_COLOR)
game_window.title(GAME_WINDOW_TITLE)
# Hide the details of setting the squares in position and moving
game_window.tracer(0)
# Create right paddle.
r_paddle = paddle.Paddle(R_PADDLE_INITIAL_POSITIONS, game_window)
l_paddle = paddle.Paddle(L_PADDLE_INITIAL_POSITIONS, game_window)
# Listen to keystrokes
game_window.listen()
game_window.onkeypress(key='q', fun=l_paddle.move_up)
game_window.onkeypress(key='a', fun=l_paddle.move_down)
game_window.onkeypress(key='p', fun=r_paddle.move_up)
game_window.onkeypress(key='l', fun=r_paddle.move_down)
# Start the game
game_is_on = True
while game_is_on:
    # Update the window with the last movements
    game_window.update()
    time.sleep(PADDLE_SPEED)
    pass
# Exit window on click.
game_window.exitonclick()
