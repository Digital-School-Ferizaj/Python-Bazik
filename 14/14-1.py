from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT, BOTTOM
from tkinter.ttk import Frame, Label, Entry, Button

root = Tk()
root.geometry("450x500")

frame1 = Frame(root)

#options that we can use for the Frame widgets:
"""
bd - It is used to set the border width.
bg - It is used to set the background color
cursor - It is used to set the mouse pointer.
        Some of the values that we can use are arrow,
        dot, etc.
height- It is used to set the height of the frame.
width- It is used to set the width of the frame.
"""

frame1.pack(fill=X)

#pack() -- allows us to place widgets in rows or columns
#options to control pack() layout manager:
"""
expand − It is used to set whether the widget should expand to fill any space not used in the widget's parent.
    The values that we can use are: True and False.

fill − It is used to set whether the widget should fill any extra space allocated to it by the packer.
    Values that we can use are NONE, X, Y, and BOTH. Value NONE specifies that the widget will not fill any extra space.
    Value X specifies that the widget will fill the horizontal area.
    Value Y specified that the widget will fill the vertical area.
    Value BOTH specifies that the widget will fill both the horizontal and vertical areas.

side − It is used to set on which side will the widget pack against the parent.
    Values that we can use are TOP (default), BOTTOM, LEFT, or RIGHT.
"""

#
name_label = Label(frame1, text="Name:", width=8)
name_label.pack(side=LEFT, padx=5, pady=5)

name_input = Entry(frame1)
name_input.pack(side=LEFT, padx=5)

#
email_label = Label(frame1, text="Email:", width=6)
email_label.pack(side=LEFT, padx=5, pady=5)

email_input = Entry(frame1)
email_input.pack(side=LEFT, padx=5, expand=True)

###
frame2 = Frame(root)
frame2.pack(fill=BOTH)

#
message_label = Label(frame2, text="Message:", width=8)
message_label.pack(side=LEFT, anchor=N, padx=5, pady=5)

#
textarea = Text(frame2)
textarea.pack(fill=BOTH, pady=5, padx=5)


###
frame3 = Frame(root)
frame3.pack(fill=X, expand=True)

#
closeBtn = Button(frame3, text="Close")
closeBtn.pack(side=RIGHT, padx=5, pady=5)

#
sendBtn = Button(frame3, text="Send")
sendBtn.pack(side=RIGHT, padx=5, pady=5)


root.mainloop()
