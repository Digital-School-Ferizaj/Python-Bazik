import turtle
turtle.delay(10)
turtle.pensize(20)

#left tye pos
turtle.penup()
turtle.setposition(-87.5, -50)
turtle.setheading(90)


turtle.begin_fill()
turtle.circle(62.5)
turtle.end_fill()

#right tyre
turtle.penup()
turtle.setposition(212.5, -50)
turtle.setheading(90)

turtle.begin_fill()
turtle.circle(62.5)
turtle.end_fill()

# handles
turtle.penup()
turtle.setposition(137.5, 0)
turtle.pendown()
turtle.setposition(75, 150)

# straight_handle
turtle.setheading(0)
turtle.setposition(125, 150)

# curve_handle
turtle.penup()
turtle.setposition(125, 100)
turtle.pendown()
turtle.circle(25, 180)

# seat
turtle.penup()
turtle.setposition(12.5, -50)
turtle.pendown()
turtle.setposition(-62.5, 137.5)

# seat - seat
turtle.setheading(180)
turtle.setposition(-100, 137.5)

# top tube
turtle.penup()
turtle.setposition(100, 75)
turtle.pendown()
turtle.setposition(-37.5, 75)

# down tube
turtle.penup()
turtle.setposition(100, 75)
turtle.pendown()
turtle.setposition(12.5, -50)

# seat stay
turtle.penup()
turtle.setposition(-37.5, 75)
turtle.pendown()
turtle.setposition(-150, -50)

# chain stay
turtle.penup()
turtle.setposition(12.5, -50)
turtle.pendown()
turtle.setposition(-150, -50)
