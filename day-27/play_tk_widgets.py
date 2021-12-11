# Importing external packages.
import tkinter
import random


def do_nothing():
    root_win = tkinter.Toplevel(root)
    another_button = tkinter.Button(root_win)
    another_button.config(text='Another Button')
    return


# Creating a new window and configurations.
root = tkinter.Tk()
root.config(width=500, height=500)
root.title("Widget Examples")
# root.minsize(width=500, height=500)  # minimum size of the root window.
# Create menu.
# Create menu bar.
menu_bar = tkinter.Menu(root)
# Create file menu.
file_menu = tkinter.Menu(menu_bar, tearoff=0)
# file_menu.config(tearoff=False)
file_menu.add_command(label='New', command=do_nothing)
file_menu.add_command(label='Open', command=do_nothing)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)
# Add file menu to menu bar.
menu_bar.add_cascade(menu=file_menu, label='File')
# Create edit menu.
edit_menu = tkinter.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label='Copy', command=do_nothing)
# Add edit menu to menu bar.
menu_bar.add_cascade(menu=edit_menu, label='Edit')
# root.config(menu=menu_bar)


# Label widget.
label = tkinter.Label(text="This is old text")
label.config(text="This is new text")
label.pack()


# Button widget.
def action():
    print("Do something")
    return


# Calls action() when pressed.
button = tkinter.Button()
button_config = dict(text="Click Me", command=action)
button.config(button_config)
button.pack()

# Entry widget.
entry = tkinter.Entry()
entry_config = dict(width=30)
entry.config(entry_config)
# Add some text to begin with.
entry.insert(tkinter.END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
entry.pack()

# Text widget.
text = tkinter.Text()
text.config(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
# text.insert(tkinter.END, "Example of multi-line text entry.")
text.insert('1.0', "Example of multi-line text entry.")
# Gets current value in textbox at line 1, character 0.
print(text.get("1.0", tkinter.END))
text.pack()


# Spinbox widget.
def spinbox_used():
    # Gets the current value in spinbox.
    print(spinbox.get())


spinbox = tkinter.Spinbox()
spinbox.config(from_=0, to=10, increment=0.5, width=3, justify=tkinter.RIGHT, command=spinbox_used)
spinbox.pack()


# Scale widget.
# Called with current scale value.
def scale_used(value):
    print(value)
    scale.set(random.randint(1,100))


scale = tkinter.Scale()
scale.config(from_=0, to=100, bigincrement=5, width=15, command=scale_used)
scale.pack()


# Checkbutton widget.
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# Variable to hold on to checked state, 0 is off, 1 is on.
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton()
checkbutton.config(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
checkbutton.pack()


# Radiobutton widget.
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton()
radiobutton1.config(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton()
radiobutton2.config(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox widget.
def item_selected(event):
    # Gets current selection from listbox
    print(listbox.curselection())  # (#, ) where # is the listbox position starting with 0.
    print(listbox.get(listbox.curselection()))


# Listbox widget use and config.
listbox = tkinter.Listbox()
listbox.config(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
    print(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", item_selected)
listbox.pack()
# Run the event listener.
root.config(menu=menu_bar)
root.mainloop()
