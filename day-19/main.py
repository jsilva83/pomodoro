import turtle as tu


def move_forward1(shape: tu.Turtle(), x: int) -> None:
    """Moves the turtle x passes forward (East)."""
    shape.forward(x)
    return


def move_forward() -> None:
    tim.forward(10)
    return


def move_backward() -> None:
    tim.backward(10)


def turn_left() -> None:
    tim.setheading(180)
    return


def turn_up() -> None:
    tim.setheading(90)
    return


def turn_right() -> None:
    tim.setheading(0)
    return


def turn_down() -> None:
    tim.setheading(-90)
    return


def clear_screen() -> None:
    tim.clear()
    tim.reset()
    return


def rotate_clock() -> None:
    tim.setheading(tim.heading() + 10)
    return


def rotate_unti_clock() -> None:
    tim.setheading(tim.heading() - 10)
    return


tim = tu.Turtle()
wind = tu.Screen()
wind.listen()
wind.onkey(fun=move_forward, key='space')
wind.onkey(fun=move_backward, key='b')
wind.onkey(fun=turn_right, key='Right')
wind.onkey(fun=turn_up, key='Up')
wind.onkey(fun=turn_left, key='Left')
wind.onkey(fun=turn_down, key='Down')
wind.onkey(fun=clear_screen, key='c')
wind.onkey(fun=rotate_clock, key='plus')
wind.onkey(fun=rotate_unti_clock, key='minus')
wind.exitonclick()
