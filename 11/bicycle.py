import turtle
turtle.delay(10)
turtle.pensize(10)

#draw the first wheel
turtle.penup()
turtle.setposition(-50,-100)
turtle.setheading(90)
turtle.pendown()
turtle.circle(70.5)

#draw the second wheel
turtle.penup()
turtle.setposition(200,-100)
turtle.pendown()
turtle.circle(70.5)


# Draw the head tube
turtle.penup()
turtle.setposition(125, -100)
turtle.pendown()
turtle.setposition(75, 75)


# Draw the circular part of the handle
turtle.setheading(0)
turtle.circle(15, 180)
turtle.setposition(45, 105)


# Draw the seat tube
turtle.penup()
turtle.setposition(-12.5, -100)
turtle.pendown()
turtle.setposition(-62.5, 50)


# Draw the saddle
turtle.setheading(180)
turtle.setposition(-105, 50)



# Draw the seat
turtle.penup()
turtle.setposition(-52, 35.5)
turtle.pendown()
turtle.setposition(86, 35.5)


# Draw the down tube
turtle.penup()
turtle.setposition(85, 40)
turtle.pendown()
turtle.setposition(-12.5, -100)


# Draw the seat stay
turtle.penup()
turtle.setposition(-50, 36.5)
turtle.pendown()
turtle.setposition(-137.5, -100)


# Draw the chain stay
turtle.penup()
turtle.setposition(-137.5, -100)
turtle.pendown()
turtle.setposition(-12.5, -100)

# Draw the pedals
turtle.penup()
turtle.setposition(-12.5, -80)
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()



