# Import external packages.
import tkinter

# Global constants.
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Timer reset.

# Timer mechanism.

# Countdown mechanism.

# UI Setup.
# Create a root window.
root_window = tkinter.Tk()
root_window.title('Pomodoro Method')
root_window.config(padx=100, pady=50, bg=YELLOW)
# Create label at the top.
timer_txt_label = tkinter.Label(root_window)
timer_txt_label.config(text='Timer', font=(FONT_NAME, 40), fg=GREEN, bg=YELLOW, anchor='s')
timer_txt_label.grid(row=0, column=1)
# Convert an image file to a variable.
bg_image = tkinter.PhotoImage(file='tomato.png')
# Create a canvas.
a_canvas = tkinter.Canvas()
a_canvas.config(width=200, height=224, bg=YELLOW, highlightthickness=0)
a_canvas.create_image(100, 112, image=bg_image, anchor='center')
a_canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
a_canvas.grid(row=1, column=1)
# Create button start.
start_button = tkinter.Button(root_window)
start_button.config(text='Start', font=('Arial', 12), anchor='center', highlightthickness=0)
start_button.grid(row=2, column=0)
# Create button reset.
reset_button = tkinter.Button(root_window)
reset_button.config(text='Reset', font=('Arial', 12), anchor='center', highlightthickness=0)
reset_button.grid(row=2, column=2)
# Create label with number of pomodoros.
checked_label = tkinter.Label(root_window)
checked_label.config(text='✔︎', fg=GREEN, bg=YELLOW, anchor='n')
checked_label.grid(row=3, column=1)
# Listening events in main window.
root_window.mainloop()
