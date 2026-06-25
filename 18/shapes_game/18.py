import random
import time
from tkinter import Tk, Canvas, HIDDEN, NORMAL, Label, Button, Frame

root = Tk()
root.title("Shape Game")
c = Canvas(root, width=400, height=400)

shape = None
score = 0
shapeType = None
scoreString = str(score)

shape_names = ["Circle", "Square", "Triangle"]

shapes = []

circle = c.create_oval(35, 20, 365, 350, outline="black", fill="black", tag = "Circle", state = HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline="red", fill="red", tag = "Circle", state = HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline="green", fill="green", tag = "Circle", state = HIDDEN)
shapes.append(circle)
circle = c.create_oval(35, 20, 365, 350, outline="blue", fill="blue", tag = "Circle", state = HIDDEN)
shapes.append(circle)

square = c.create_rectangle(35, 20, 365, 350, outline="black", fill="black", tag = "Square", state = HIDDEN)
shapes.append(square)
square = c.create_rectangle(35, 20, 365, 350, outline="red", fill="red", tag = "Square", state = HIDDEN)
shapes.append(square)
square = c.create_rectangle(35, 20, 365, 350, outline="green", fill="green", tag = "Square", state = HIDDEN)
shapes.append(square)
square = c.create_rectangle(35, 20, 365, 350, outline="blue", fill="blue", tag = "Square", state = HIDDEN)
shapes.append(square)

points = [200,20, 380,380, 20,380]

triangle = c.create_polygon(points, outline="black", fill="black", tag = "Triangle", state = HIDDEN)
shapes.append(triangle)
triangle = c.create_polygon(points, outline="red", fill="red", tag = "Triangle", state = HIDDEN)
shapes.append(triangle)
triangle = c.create_polygon(points, outline="green", fill="green", tag = "Triangle", state = HIDDEN)
shapes.append(triangle)
triangle = c.create_polygon(points, outline="blue", fill="blue", tag = "Triangle", state = NORMAL)
shapes.append(triangle)

c.pack()




