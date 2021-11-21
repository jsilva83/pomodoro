import turtle

SCOREBOARD_ALIGNMENT = 'center'
SCOREBOARD_FONT = ('courier', 12, 'normal')
SCOREBOARD_X_POS = 0
SCOREBOARD_Y_POS = 280


class Scoreboard(turtle.Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.text = 'Score: '
        self.score = 0
        self.high_score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_X_POS, SCOREBOARD_Y_POS)
        self.update_display()
        return

    def increase_score(self) -> None:
        """Increases the score by one and updates the display"""
        self.score += 1
        self.update_display()
        return

    def update_display(self) -> None:
        """Clears the turtle object and writes the updated scoreboard score"""
        self.clear()
        self.write(f'{self.text}{self.score}  High Score: {self.high_score}', align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)
        return

    def reset(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_display()

    # def display_game_over(self) -> None:
    #     """Turtle object displays Game Over in the center"""
    #     self.goto(0, 0)
    #     self.write('GAME OVER.', align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)
    #     return
