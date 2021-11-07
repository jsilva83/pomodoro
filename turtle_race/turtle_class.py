import turtle
import random


class TurtleClass:

    def __init__(self, p_color: str) -> None:
        """Constructs a turtle object"""
        self.turtle_obj = turtle.Turtle()
        self.turtle_obj.shape('turtle')
        self.turtle_obj.color(p_color)
        self.turtle_obj.penup()
        return

    def get_color(self) -> str:
        return self.turtle_obj.color()[0]

    def get_position(self) -> int:
        return self.turtle_obj.pos()[0]

    def reset_pos(self) -> None:
        if self.turtle_obj.color()[0] == 'red':
            self.turtle_obj.goto(x=-230, y=50)
        elif self.turtle_obj.color()[0] == 'green':
            self.turtle_obj.goto(x=-230, y=150)
        elif self.turtle_obj.color()[0] == 'blue':
            self.turtle_obj.goto(x=-230, y=-50)
        else:
            self.turtle_obj.goto(x=-230, y=-150)
        return

    def move_forward_randomly(self) -> bool:
        current_x_pos, current_y_pos = self.turtle_obj.pos()
        current_x_pos += random.randint(0, 10)
        self.turtle_obj.goto(x=current_x_pos, y=current_y_pos)
        return self.get_position() >= 200
