import turtle
import time
import snake

window = turtle.Screen()
window.setup(width=600, height=600)
window.bgcolor('black')
window.title('My Python Snake')
# Hide the details of setting the squares in position and moving
window.tracer(0)
# Create snake object
my_snake = snake.Snake()
# Listen to keystrokes
window.listen()
window.onkey(key='Up', fun=my_snake.up)
window.onkey(key='Down', fun=my_snake.down)
window.onkey(key='Left', fun=my_snake.left)
window.onkey(key='Right', fun=my_snake.right)
game_is_on = True
while game_is_on:
    # Update the window with the last movements
    window.update()
    time.sleep(0.5)
    my_snake.move()

window.exitonclick()
