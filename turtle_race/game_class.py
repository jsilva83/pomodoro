import turtle_class
import turtle


class TurtleRaceGame:

    def __init__(self) -> None:
        """Constructs a new turtle race game."""
        # Initialize object attributes.
        self.window = turtle.Screen()
        self.turtles =[turtle_class.TurtleClass('red'), turtle_class.TurtleClass('green'),
                       turtle_class.TurtleClass('blue'), turtle_class.TurtleClass('black')]
        # self.turtle1 = turtle_class.TurtleClass('red')
        # self.turtle2 = turtle_class.TurtleClass('green')
        # self.turtle3 = turtle_class.TurtleClass('blue')
        # self.turtle4 = turtle_class.TurtleClass('black')
        self.user_color_bet = ''
        # Call user interface and handle control to game.
        self.user_interface()
        return

    def move_to_begin(self) -> None:
        for item in self.turtles:
            item.reset_pos()
        # self.turtle1.reset_pos()
        # self.turtle2.reset_pos()
        # self.turtle3.reset_pos()
        # self.turtle4.reset_pos()
        return

    def user_interface(self) -> None:
        self.window.setup(width=500, height=400)
        self.move_to_begin()
        self.user_color_bet = self.window.textinput(title='Turtle race', prompt='Chose the color of your turtle: ')
        # make turtle to run in sequence (in the future, randomly).
        is_on_wall = False
        while not is_on_wall:
            for item in self.turtles:
                if item.move_forward_randomly():
                    print(f'{item.get_color()} turtle wins!')
                    if self.user_color_bet.lower() == item.get_color():
                        print('You win!')
                    else:
                        print('You loose!')
                    is_on_wall = True
                    break
            # if self.turtle1.move_forward_randomly():
            #     is_on_wall = True
            #     print(f'{self.turtle1.get_color()} turtle wins!')
            # elif self.turtle2.move_forward_randomly():
            #     is_on_wall = True
            #     print(f'{self.turtle2.get_color()} turtle wins!')
            # elif self.turtle3.move_forward_randomly():
            #     is_on_wall = True
            #     print(f'{self.turtle3.get_color()} turtle wins!')
            # elif self.turtle4.move_forward_randomly():
            #     is_on_wall = True
            #     print(f'{self.turtle4.get_color()} turtle wins!')
        self.window.exitonclick()
        return

