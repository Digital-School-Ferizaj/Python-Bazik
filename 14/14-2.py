from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT
from tkinter.ttk import Frame, Label, Entry, Button

root = Tk()
root.geometry('450x500')

frame1 = Frame(root)
frame1.pack(fill=X)

name_label = Label(frame1, text="Name:", width=8)
name_label.pack(side=LEFT, padx=5, pady=5)

name_input = Entry(frame1)
name_input.pack(side=LEFT, padx=5)

email_label = Label(frame1, text="Email:", width=6)
email_label.pack(side=LEFT, padx=5, pady=5)

email_input = Entry(frame1)
email_input.pack(fill=X, padx=5,expand=True)

frame2 = Frame(root)
frame2.pack(fill=BOTH)

message_label = Label(frame2, text="Message:", width=8)
message_label.pack(side=LEFT, anchor=N, padx=5, pady=5)

textarea = Text(frame2)
textarea.pack(fill=BOTH, pady=5, padx=5)

frame3 = Frame(root)
frame3.pack(fill=X, expand=True)

closeBtn = Button(frame3, text="Close")
closeBtn.pack(side=RIGHT, padx=5, pady=5)

sendBtn = Button(frame3, text="Send", command = emriFunksionit)
sendBtn.pack(side=RIGHT, padx=5, pady=5)

root.mainloop()


