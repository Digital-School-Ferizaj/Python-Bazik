from tkinter import Tk, Label, Entry, W, E, EW, Button, Listbox, Checkbutton, Frame, SINGLE, Button

root = Tk()
root.geometry("700x500")
root.title('Form')
root.configure(background='#00014e')
root.resizable(0,0)

#Creating the main frames
first_frame = Frame(root, bg='#108bf9', width=700, height=50)
second_frame = Frame(root,bg='#00014e', width=700, height=50)
third_frame = Frame(root, bg='#00014e', width=700, height=100)
fourth_frame = Frame(root, bg='#00014e', width=700, height=200) 
fifth_frame = Frame(root, bg='#00014e', width=700, height=100)

#positioning frames in the grid
first_frame.grid(row=0, sticky=W)
second_frame.grid(row=1, sticky=W)
third_frame.grid(row=2)
fourth_frame.grid(row=3, sticky=W)
fifth_frame.grid(row=4, sticky=W)

#header label
header_label = Label(first_frame, text="Summer School registration form", bg='#108bf9', fg='white', font=("Courier", 15))
header_label.grid(row=0, column=0, pady=15, padx=180)

#creating and positioning child frames of the second frame
second_frame_left = Frame(second_frame, bg='#00014e', width=350, height=50, padx=56)
second_frame_right = Frame(second_frame, bg='#00014e', width=350, height=50, padx=20)

second_frame_left.grid(row=0, column=0)
second_frame_right.grid(row=0, column=1)

#name label
name_label = Label(second_frame_left, text="Name:", bg='#00014e', fg='white', font=("Arial", 10))
name_label.grid(row=0, column=0, padx=5,pady=30)

#name input
name_input = Entry(second_frame_left)
name_input.grid(row=0, column=1, ipadx=30,padx=5, pady=30)

#surname label
surname_label = Label(second_frame_right, text="Surname:", bg='#00014e', fg='white', font=("Arial", 10))
surname_label.grid(row=0, column=0, padx=5,pady=30)

#surname input
surname_input = Entry(second_frame_right)
surname_input.grid(row=0, column=1, ipadx=30, padx=5, pady=30)

#creating and positioning child frames of the third frame
third_frame_left = Frame(third_frame, bg='#00014e', width=200, height=100, padx=15, pady=3)
third_frame_mid = Frame(third_frame,  bg='#00014e',width=200, height=100, padx=15, pady=3)
third_frame_right = Frame(third_frame,  bg='#00014e',width=200, height=100, padx=15, pady=3)

third_frame_left.grid(row=0, column=0)
third_frame_mid.grid(row=0, column=1)
third_frame_right.grid(row=0, column=2)

#3D Game Development Label
game_dev_label = Label(third_frame_left, text="3D Game Development", bg='#00014e', fg='white', font=("Arial", 10))
game_dev_label.grid(row=0, column=0, pady=30)

#3D Game Development Checkbox
game_dev_checkbox = Checkbutton(third_frame_left, variable = '3D Game Development', bg='#00014e')
game_dev_checkbox.grid(row=0, column=1,pady=30)

#Artificial Intelligence Label
ai_label = Label(third_frame_mid, text="Artificial Intelligence", bg='#00014e', fg='white', font=("Arial", 10))
ai_label.grid(row=0, column=0, pady=30)

#Artificial Intelligence Chceckbox
ai_checkbox = Checkbutton(third_frame_mid, variable = 'Artificial Intelligence', bg='#00014e')
ai_checkbox.grid(row=0, column=1, pady=30)

#Web Design (UI/UX) Label
uiux_label = Label(third_frame_right, text="Web Design (UI/UX)", bg='#00014e', fg='white', font=("Arial", 10))
uiux_label.grid(row=0, column=0, pady=30)

#Web Design (UI/UX) Checkbox
uiux_checkbox = Checkbutton(third_frame_right, variable = 'Web Design (UI/UX)',  bg='#00014e')
uiux_checkbox.grid(row=0, column=1, pady=30)

#Students Label
students_label = Label(fourth_frame, text="Students:", bg='#00014e', fg='white', font=("Arial", 10))
students_label.grid(row=0, column=0)

#listbox that contains students that chose a summer school program
lb = Listbox(
    fourth_frame,
    width=65,
    height=8,
    borderwidth=0,
    selectmode=SINGLE,
    font=('Arial', 12),
    bd=0,
    fg='#00014e',
    highlightthickness=0,
    selectbackground='blue',
    activestyle="none"  
)
lb.grid(row=1, column=0,padx=60, pady=15)

lb.insert(1, "John Doe - 3D Game Development")
lb.insert(2, "Nellie Mcfadden - Web Design (UI/UX)")
lb.insert(3, "Abbey Morley - Artificial Intelligence")
lb.insert(4, "James Whitley - Artificial Intelligence")

#creating and positioning child frames of the fifth frame
fifth_frame_left = Frame(fifth_frame, bg='#00014e', width=350, height=50)
fifth_frame_right = Frame(fifth_frame, bg='#00014e', width=350, height=50, padx=65, pady=3)

fifth_frame_left.grid(row=0, column=0)
fifth_frame_right.grid(row=0, column=1)

#Submit Button
button1 = Button(
    fifth_frame_right,
    text='Submit',
    font=('arial 10'),
    width=10,
    padx=10,
    pady=3,
    bg='#7eb900',
    fg='white'
)
button1.grid(row=0, column=0, sticky=W, pady=15)

#Cancel Button
button2 = Button(
    fifth_frame_right,
    text='Cancel',
    font=('arial 10'),
    width=10,
    padx=10,
    pady=3,
    bg='#108bf9',
    fg='white'
)
button2.grid(row=0, column=1, sticky=W, padx=15, pady=15)

root.mainloop()

