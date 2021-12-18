import tkinter

root = tkinter.Tk()
red = tkinter.Label(root)
red.config(bg='red', width=20, height=5)
red.grid(row=0, column=0)
green = tkinter.Label(root)
green.config(bg='green', width=20, height=5)
green.grid(row=1, column=1)
blue = tkinter.Label(root)
blue.config(bg='blue', width=40, height=5)
blue.grid(row=2, column=0, columnspan=2)
root.mainloop()
