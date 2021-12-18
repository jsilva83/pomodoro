# Import external packages.
import tkinter
import math

# Global constants.
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# WORK_MIN = 25
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# Timer reset.
def reset_timer():
    global my_timer
    global reps
    root_window.after_cancel(my_timer)
    checked_label.config(text='', fg=GREEN, bg=YELLOW, anchor='n')
    timer_txt_label.config(text='Timer', font=(FONT_NAME, 40), fg=GREEN, bg=YELLOW, anchor='s')
    a_canvas.itemconfig(a_text_canvas, text=f'00:00')
    reps = 1
    return


# Timer mechanism.
def start_timer():
    global reps
    working_seconds = int(WORK_MIN * 60)
    short_break_seconds = int(SHORT_BREAK_MIN * 60)
    long_break_seconds = int(LONG_BREAK_MIN * 60)
    # 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21
    #    b     b     b     b       l       b       b       b       b       l
    #
    reps += 1
    if reps % 2 == 0:
        count_down(working_seconds)
        timer_txt_label.config(text='Work', font=(FONT_NAME, 40), fg=GREEN, bg=YELLOW, anchor='s')
        print('working')
    elif reps % 10 == 1:
        count_down(long_break_seconds)
        timer_txt_label.config(text='Break', font=(FONT_NAME, 40), fg=RED, bg=YELLOW, anchor='s')
        print('long break')
    elif reps % 2 != 0:
        count_down(short_break_seconds)
        timer_txt_label.config(text='Break', font=(FONT_NAME, 40), fg=PINK, bg=YELLOW, anchor='s')
        print('short break')
    else:
        count_down(short_break_seconds)
        timer_txt_label.config(text='Break', font=(FONT_NAME, 40), fg=PINK, bg=YELLOW, anchor='s')
    return


# Countdown mechanism.
def count_down(counter):
    global reps
    global my_timer
    # Convert from seconds to minute and seconds.
    count_down_min = math.floor(counter / 60)
    count_down_sec = counter % 60
    if count_down_sec < 10:
        count_down_sec = f'0{count_down_sec}'
    # Changes the attributes of one of the canvas items, in this case the text.
    a_canvas.itemconfig(a_text_canvas, text=f'{count_down_min}:{count_down_sec}')
    if counter > 0:
        # Generates an event every 1 (1000 miliseconds) second and calls a function.
        my_timer = root_window.after(1000, count_down, counter - 1)
    else:
        start_timer()
        if reps % 2 == 1:
            check_marks = ''
            print(math.floor(reps/2))
            for _ in range(math.floor(reps/2)):
                check_marks += '✔︎'
            checked_label.config(text=check_marks, fg=GREEN, bg=YELLOW, anchor='n')
    return


# Global setups.
# reps counts the number of times we have run pomodoros for 5 times
reps = 1
# The variable ht holds the window.after event link.
my_timer = ''
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
a_text_canvas = a_canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
a_canvas.grid(row=1, column=1)
# Create button start.
start_button = tkinter.Button(root_window)
start_button.config(text='Start', font=('Arial', 12), anchor='center', highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)
# Create button reset.
reset_button = tkinter.Button(root_window)
reset_button.config(text='Reset', font=('Arial', 12), anchor='center', highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)
# Create label with number of pomodoros.
checked_label = tkinter.Label(root_window)
# Check mark starts empty.
# checked_label.config(text='✔︎', fg=GREEN, bg=YELLOW, anchor='n')
checked_label.config(text='', fg=GREEN, bg=YELLOW, anchor='n')
checked_label.grid(row=3, column=1)
# Listening events in main window.
root_window.mainloop()
