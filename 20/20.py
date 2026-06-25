from tkinter import * 
from tkinter.ttk import *
from PIL import ImageTk,Image
import random
import time

first = True

root = Tk()

foto1 = (Image.open("emri.jpg"))
foto1_rs = foto1.resize((150,150), Image.Resampling.LANCZOS)
new_foto1 = ImageTk.PhotoImage(foto1_rs)

foto2 = (Image.open("emri2.jpg"))
foto2_rs = foto2.resize((150,150), Image.Resampling.LANCZOS)
new_foto2 = ImageTk.PhotoImage(foto2_rs)

foto3 = (Image.open("emri3.jpg"))
foto3_rs = foto3.resize((150,150), Image.Resampling.LANCZOS)
new_foto3 = ImageTk.PhotoImage(foto3_rs)

foto4 = (Image.open("emri4.jpg"))
foto4_rs = foto4.resize((150,150), Image.Resampling.LANCZOS)
new_foto4 = ImageTk.PhotoImage(foto4_rs)

foto5 = (Image.open("emri5.jpg"))
foto5_rs = foto5.resize((150,150), Image.Resampling.LANCZOS)
new_foto5 = ImageTk.PhotoImage(foto5_rs)

foto6 = (Image.open("emri6.jpg"))
foto6_rs = foto6.resize((150,150), Image.Resampling.LANCZOS)
new_foto6 = ImageTk.PhotoImage(foto6_rs)

blank_img = (Image.open("emri7.jpg"))
blank_img_rs = blank_img.resize((150,150), Image.Resampling.LANCZOS)
new_blank_img = ImageTk.PhotoImage(blank_img_rs)

images = [new_foto1, new_foto2, new_foto3,
          new_foto4, new_foto5, new_foto6,
          new_foto1, new_foto2, new_foto3,
          new_foto4, new_foto5, new_foto6]

random.shuffle(images)

buttons = {}

button_images = {}

for x in range(4):
    for y in range(3):
        button = Button(root, image = new_blank_img, command=lambda x=x, y=y: flipImage(x,y))
        button.grid(column=x, row=y)
        buttons[x, y] = button
        button_images[x, y] = images.pop()

def flipImage(x, y):
    global first
    global previousX, previousY
    buttons[x,y]["image"] = button_images[x,y]
    buttons[x,y].update_idletasks()

    if first:
        previousX = x
        previousY = y
        first = False
    elif previousX != x or previousY != y:
        if buttons[previousX, previousY]["image"] != buttons[x, y]['image']:
            time.sleep(0.5)
            buttons[previousX, previousY]["image"] = new_blank_img
            buttons[x, y]['image'] = new_blank_img
        else:
            buttons[previousX, previousY]["command"] = DISABLED
            buttons[x, y]['command'] = DISABLED
        first = True

root.mainloop()








          
