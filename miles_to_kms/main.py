# Import external packages.
import tkinter


def convert_miles_to_kms():
    # Method 1.
    # miles = float(miles_input.get())
    # kms_result = round(miles * 1.609344)
    # kms_result_label.config(text=f'{kms_result}')
    # Method 2.
    kms_result = round(in_miles.get() * 1.609344)
    converted_kms.set(f'{kms_result}')
    return


root = tkinter.Tk()
root.title('Mile to Km converter')
root.config(padx=20, pady=20)
in_miles = tkinter.IntVar()
miles_input = tkinter.Entry()
miles_input.config(textvariable=in_miles, justify='right', width=5)
miles_input.grid(row=0, column=1)
miles_label = tkinter.Label()
miles_label.config(text='Miles', justify='left')
miles_label.grid(row=0, column=2)
is_equal_label = tkinter.Label()
is_equal_label.config(text='is equal to', justify='right')
is_equal_label.grid(row=1, column=0)
converted_kms = tkinter.StringVar()
kms_result_label = tkinter.Label()
kms_result_label.config(textvariable=converted_kms, justify='center')
kms_result_label.grid(row=1, column=1)
kms_label = tkinter.Label()
kms_label.config(text='Kms')
kms_label.grid(row=2, column=2)
calculate_button = tkinter.Button()
calculate_button.config(text='Convert', command=convert_miles_to_kms)
calculate_button.grid(row=2, column=1)
root.mainloop()
