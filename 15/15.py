import tkinter as tk
from tkinter import ttk, Label, Entry, W, E, Button, Tk

#root window
root = tk.Tk()
root.geometry("300x170")
root.title("Sign up")

#columnconfigure() and rowconfigure() methods
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=4)

#grid() method allows us to organize widgets into the grid
#one of the options we can use in grid() are:
"""
column: It is used to specify the column number where we want to position our widget.

columnspan: It is used to specify the number of columns the widget should occupy.
        With this option, we can expand the widget into multiple cells of a row.

row: It is used to specify the row number where we want to position our widget.

rowspan: It is used to specify the number of columns the widget should occupy.
        With this option, we can expand the widget into multiple cells of a column.

padx & pady (External padding): These options are used to specify the external horizontal and vertical paddings.

ipadx & ipady (Internal padding): These options are used to specify the internal horizontal and vertical paddings.

sticky: It is used to specify in which direction we want the widget to be stuck when the cell is larger than the widget.
        Values that we can use are: N,E,S,W,NE,NW,SE & SW.
"""

#username
username_label = Label(root, text="Username:")
username_label.grid(column=0, row=0, sticky=W, padx=15, pady=10)

username_input = Entry(root, width=30)
username_input.grid(column=1, row=0, sticky=W, padx=15, pady=10)

#email
email_label = Label(root, text="Email:")
email_label.grid(column=0, row=1, sticky=W, padx=15, pady=10)

email_input = Entry(root, width=30)
email_input.grid(column=1, row=1, sticky=W, padx=15, pady=10)

#Password
password_label = Label(root, text="Password:")
password_label.grid(column=0, row=2, sticky=W, padx=15, pady=10)

password_input = Entry(root, show="*", width=30)
password_input.grid(column=1, row=2, sticky=W, padx=15, pady=10)

#Sign up button
signup_button = Button(root, text="Sign up")
signup_button.grid(column=1, row=3, sticky=E, padx=15, pady=10)

root.mainloop()




