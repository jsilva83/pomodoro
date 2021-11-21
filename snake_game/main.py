import turtle
import time
import snake
import food
import scoreboard

SNAKE_SPEED = 0.1
WALL_COLLISION_TOLERANCE = 15
TAIL_COLLISION_TOLERANCE = 10
UP_WALL_LIMIT = 290
DOWN_WALL_LIMIT = -290
LEFT_WALL_LIMIT = -290
RIGHT_WALL_LIMIT = 290

window = turtle.Screen()
window.setup(width=600, height=600)
window.bgcolor('black')
window.title('My Python Snake')
# Hide the details of setting the squares in position and moving
window.tracer(0)
# Create snake object.
my_snake = snake.Snake()
# Create a food object.
my_food = food.Food()
# Create a scoreboard object.
my_scoreboard = scoreboard.Scoreboard()
# Listen to keystrokes.
window.listen()
window.onkey(key='Up', fun=my_snake.up)
window.onkey(key='Down', fun=my_snake.down)
window.onkey(key='Left', fun=my_snake.left)
window.onkey(key='Right', fun=my_snake.right)
game_is_on = True
while game_is_on:
    # Update the window with the last movements
    window.update()
    time.sleep(SNAKE_SPEED)
    my_snake.move()
    # Detect collision with food
    if my_snake.head.distance(my_food) < WALL_COLLISION_TOLERANCE:
        my_food.next_position()
        my_scoreboard.increase_score()
        my_snake.extend()
    # Detect collision with wall
    if my_snake.head.xcor() > RIGHT_WALL_LIMIT or my_snake.head.xcor() < LEFT_WALL_LIMIT \
            or my_snake.head.ycor() > UP_WALL_LIMIT or my_snake.head.ycor() < DOWN_WALL_LIMIT:
        # Game over
        my_scoreboard.display_game_over()
        game_is_on = False
    # Detect collision with tail
    # If the head collides with any segment in the tail
    for segment in my_snake.snake_segments[1:]:
        if my_snake.head.distance(segment) < TAIL_COLLISION_TOLERANCE:
            # Game over
            my_scoreboard.display_game_over()
            game_is_on = False
window.exitonclick()
