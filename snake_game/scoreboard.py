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
        self.high_score = self.read_score_from_file()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_X_POS, SCOREBOARD_Y_POS)
        self.update_display()
        return

    def read_score_from_file(self) -> int:
        score_file_obj = open(file='data.txt', mode='r')
        score_file_contents = score_file_obj.read()
        score_file_obj.close()
        return int(score_file_contents)

    def write_score_to_file(self) -> None:
        score_file_obj = open(file='data.txt', mode='w')
        score_file_obj.write(str(self.high_score))
        score_file_obj.close()
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
            self.write_score_to_file()
        self.score = 0
        self.update_display()
        return

    # def display_game_over(self) -> None:
    #     """Turtle object displays Game Over in the center"""
    #     self.goto(0, 0)
    #     self.write('GAME OVER.', align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)
    #     return
