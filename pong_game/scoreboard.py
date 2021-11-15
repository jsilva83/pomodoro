import turtle

SCOREBOARD_ALIGNMENT = 'center'
SCOREBOARD_FONT = ('courier', 12, 'normal')
SCOREBOARD_X_POS = 0
SCOREBOARD_Y_POS = 280


class Scoreboard(turtle.Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.text = f'{self.left_score}               {self.right_score}'
        self.color('white')
        self.draw_middle_line()
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_X_POS, SCOREBOARD_Y_POS)
        self.update_display()
        return

    def draw_middle_line(self) -> None:
        """Draw the dashed middle line."""
        self.goto(x=0, y=280)
        self.setheading(-90)
        self.shape('square')
        pen_is_down = True
        for _ in range(280, -280, -30):
            if pen_is_down:
                self.pendown()
                pen_is_down = False
            else:
                self.penup()
                pen_is_down = True
            self.forward(30)
        return

    def increase_left_score(self) -> None:
        """Increases the score by one and updates the display"""
        self.left_score += 1
        self.update_display()
        return

    def increase_right_score(self) -> None:
        """Increases the score by one and updates the display"""
        self.right_score += 1
        self.update_display()
        return

    def update_display(self) -> None:
        """Clears the turtle object and writes the updated scoreboard score"""
        self.clear()
        self.write(f'{self.text}', align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)
        return

    def display_game_over(self) -> None:
        """Turtle object displays Game Over in the center"""
        self.goto(0, 0)
        self.write('GAME OVER.', align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)
        return
