import random
import time
from tkinter import Tk, Canvas, HIDDEN, NORMAL, Label, Button, Frame


root = Tk()
root.title('Shapes Game')
c = Canvas(root, width=400, height=400)

shape = None
score = 0
shapeType = None
scoreString = str(score)

shape_names = ['Circle','Square', 'Triangle']

shapes = []

circle = c.create_oval(35, 20, 365, 350, outline='black', fill='black', tag='Circle', state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline='red', fill='red', tag='Circle',state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline='green', fill='green', tag='Circle',state=HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline='blue', fill='blue',tag='Circle', state=HIDDEN)
shapes.append(circle)

square = c.create_rectangle(35, 20, 365, 350, outline='black', fill='black',tag='Square', state=HIDDEN)
shapes.append(square)
square = c.create_rectangle(35, 20, 365, 350, outline='red', fill='red',tag='Square', state=HIDDEN)
shapes.append(square)
square = c.create_rectangle(35, 20, 365, 350, outline='green', fill='green', tag='Square',state=HIDDEN)
shapes.append(square)
square = c.create_rectangle(35, 20, 365, 350, outline='blue', fill='blue', tag='Square',state=HIDDEN)
shapes.append(square)

points = [200,20, 380,380, 20,380]

triangle = c.create_polygon(points, outline='black', fill='black',tag='Triangle', state=HIDDEN)
shapes.append(triangle)
triangle = c.create_polygon(points, outline='red', fill='red',tag='Triangle', state=HIDDEN)
shapes.append(triangle)
triangle = c.create_polygon(points, outline='green', fill='green',tag='Triangle', state=HIDDEN)
shapes.append(triangle)
triangle = c.create_polygon(points, outline='blue', fill='blue',tag='Triangle', state=HIDDEN)
shapes.append(triangle)

c.pack()

random.shuffle(shapes)
random.shuffle(shape_names)

shapeNameLabel = Label(root, text = "", font = ('Helvetica', 15))
shapeNameLabel.pack()

scoreLabel = Label(root, text = "Score: "+scoreString, font = ('Helvetica', 15))
scoreLabel.pack()


def next_shape():
     global shape
     global shapeType
     random.shuffle(shape_names)
     c.delete(shape)

     if len(shapes) > 0:
         shape = shapes.pop()
         c.itemconfigure(shape, state=NORMAL)
         shapeColor = c.itemcget(shape, 'fill')
         shapeNameLabel.config(fg = shapeColor, text = shape_names[0])
         shapeType = c.itemcget(shape, 'tag')
         root.after(1000, next_shape)
     else:
         scoreString = str(score)
         c.create_text(200, 200, text='Your final score is '+scoreString, font = ('Helvetica', 20))
         c.pack()


def match():
     global score
     valid = False

     c.delete(shape)
     if shapeNameLabel['text'] == shapeType:
         valid = True

     if valid:
          score = score + 1
          scoreString = str(score)
          scoreLabel.config(fg = "Black", text = "Score: " +scoreString)
     else:
          score = score - 1
          scoreString = str(score)
          scoreLabel.config(fg = "Black", text = "Score: " +scoreString)
     c.pack()
     root.update_idletasks()
     time.sleep(1)
     
    
frame= Frame(root)
frame.pack(expand= True, padx= 10, pady=10)

matchButton = Button(frame, text ="Match", command = match, padx=30, pady=5)
matchButton.pack()


root.after(100, next_shape)
root.mainloop()



