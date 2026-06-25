from tkinter import Tk, Label, Entry, W, E, EW, Button
from tkinter import Listbox, Checkbutton, Frame, SINGLE

root = Tk()
root.geometry("700x500")
root.title("Form")
root.configure(background='#00014e')
root.resizable(0,0)

#Creating the main frames
frame1 = Frame(root, bg="#108bf9", width=700, height=50)
frame2 = Frame(root, bg="#00014e", width=700, height=50)
frame3 = Frame(root, bg="#00014e", width=700, height=100)
frame4 = Frame(root, bg="#00014e", width=700, height=200)
frame5 = Frame(root, bg="#00014e", width=700, height=100)


#positions of frames in grid
frame1.grid(row=0, sticky=W)
frame2.grid(row=1, sticky=W)
frame3.grid(row=2)
frame4.grid(row=3, sticky=W)
frame5.grid(row=4, sticky=W)

#header label
header_label = Label(frame1, text="Summer School registration form", bg="#108bf9", fg="white", font=("Courier", 15))         
header_label.grid(row=0, column=0, pady=15, padx=180)

#child frames of the frame2
frame2_left = Frame(frame2, bg="#00014e", width=350, height=50, padx=56)
frame2_right = Frame(frame2, bg="#00014e", width=350, height=50, padx=20)

frame2_left.grid(row=0, column=0)
frame2_right.grid(row=0, column=1)

#---frame2_left
#name label
name_label = Label(frame2_left, text="Name:", bg="#00014e", fg="white", font=("Arial", 10))
name_label.grid(row=0, column=0, padx=5, pady=30)

#name input
name_input = Entry(frame2_left)
name_input.grid(row=0, column=1, ipadx=30, padx=5, pady=30)

#---frame2_right

#surname label
surname_label = Label(frame2_right, text="Surame:", bg="#00014e", fg="white", font=("Arial", 10))
surname_label.grid(row=0, column=0, padx=5, pady=30)

#suname input
surname_input = Entry(frame2_right)
surname_input.grid(row=0, column=1, ipadx=30, padx=5, pady=30)

#---child frames of the frame3
frame3_left = Frame(frame3, bg="#00014e", width=200, height=100, padx=15, pady=3)
frame3_mid = Frame(frame3, bg="#00014e", width=200, height=100, padx=15, pady=3)
frame3_right = Frame(frame3, bg="#00014e", width=200, height=100, padx=15, pady=3)

frame3_left.grid(row=0,column=0)
frame3_mid.grid(row=0,column=1)
frame3_right.grid(row=0,column=2)


#---Labels and checkboxes

#3d game development label
game_dev_label = Label(frame3_left, text="3D Game Development", bg="#00014e", fg="white", font=("Arial", 10))
game_dev_label.grid(row=0, column=0, pady=30)

#3d checkbox
game_dev_checkbox = Checkbutton(frame3_left, variable="3D Game Development", bg="#00014e")
game_dev_checkbox.grid(row=0, column=1, pady=30)

#Artifical Intelligence Label
ai_label = Label(frame3_mid, text="Artifical Intelligence", bg="#00014e", fg="white", font=("Arial", 10))
ai_label.grid(row=0, column=0, pady=30)

#Artifical Intelligence checkbox
ai_checkbox = Checkbutton(frame3_mid, variable="Artifical Intelligence", bg="#00014e")
ai_checkbox.grid(row=0, column=1, pady=30)

#Web Design label
web_label = Label(frame3_right, text="Web Design (UI/UX)", bg="#00014e", fg="white", font=("Arial", 10))
web_label.grid(row=0, column=0, pady=30)

#Web Design checkbox
web_checkbox = Checkbutton(frame3_right, variable="Web Design (UI/UX)", bg="#00014e")
web_checkbox.grid(row=0, column=1, pady=30)

#--frame4
#students label
student_label = Label(frame4, text="Students:", bg="#00014e", fg="white", font=("Arial", 10))
student_label.grid(row=0, column=0)

#listbox
lb = Listbox(
    frame4,
    width=65,
    height=8,
    borderwidth=0,
    selectmode=SINGLE,
    font=("Arial", 12),
    bd=0,
    fg="#00014e",
    highlightthickness=0,
    selectbackground="#a6a6a6",
    activestyle="none"  
)
lb.grid(row=1, column=0, padx=60, pady=15)

lb.insert(1, "John Doe - 3D Game Development")
lb.insert(2, "Nellie Mcfadden - Web Design (UI/UX)")
lb.insert(3, "Abbey Morley - Artificial Intelligence")
lb.insert(4, "James Whitley - Artificial Intelligence")    

#--frame5
#create childframes for frame5
frame5_left = Frame(frame5, bg='#00014e', width=350, height=50)
frame5_right = Frame(frame5, bg='#00014e', width=350, height=50, padx=65, pady=3)

frame5_left.grid(row=0, column=0)
frame5_right.grid(row=0, column=1)

#submit button
button1 = Button(
    frame5_right,
    text="Submit",
    font=("arial 10"),
    width=10,
    padx=10,
    pady=3,
    bg="#7eb900",
    fg="white"
)
button1.grid(row=0, column=0, sticky=W, pady=15)

#canel button
button2 = Button(
    frame5_right,
    text="Cancel",
    font=("arial 10"),
    width=10,
    padx= 10,
    pady=3,
    bg="#108bf9",
    fg="white"
    )
button2.grid(row=0, column=1, sticky=W, padx=15, pady=15)

root.mainloop()











