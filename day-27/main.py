# Import external packages.
import tkinter

# Set global constants:
# PACKER = 'pack'
# PACKER = 'place'
PACKER = 'grid'


def button_clicked():
    print("Another click on a button's life.")
    # entry_text = my_input.get()
    # my_label.config(text='Button was clicked.')
    # my_label.config(text=entry_text)


# Create the window.
window = tkinter.Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)   # (0, 0) coordinates start with at left higher corner.
window.config(padx=10, pady=10)
# Create a label.
my_label = tkinter.Label(text='My first label', font=('Arial', 12, 'bold'))
# Layout the label. Pack displays and centers the label in the window on the top.
if PACKER == 'pack':
    # my_label.pack(side='left')  # If to pack on the left.
    my_label.pack()
elif PACKER == 'place':
    my_label.place(x=10, y=5)
elif PACKER == 'grid':
    my_label.grid(row=0, column=0)
another_button = tkinter.Button()
another_button.config(text='Click me, also!', command=button_clicked)
if PACKER == 'pack':
    another_button.pack()
elif PACKER == 'place':
    another_button.place(x=100, y=215)
elif PACKER == 'grid':
    another_button.grid(row=0, column=2)
# Input something.
my_input = tkinter.Entry()
my_input.config(width=20)
if PACKER == 'pack':
    my_input.pack()
elif PACKER == 'place':
    my_input.place(x=100, y=0)
elif PACKER == 'grid':
    my_input.grid(row=1, column=1)
# Create a button.
my_button = tkinter.Button()
my_button.config(text='Click me!', command=button_clicked)
if PACKER == 'pack':
    my_button.pack()
elif PACKER == 'place':
    my_button.place(x=100, y=25)
elif PACKER == 'grid':
    my_button.grid(row=2, column=4)
# Listening for events in the window.
window.mainloop()
