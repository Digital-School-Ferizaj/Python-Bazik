import turtle
turtle.delay(10)
turtle.pensize(20)

#Draw the horizontal bottom line of the spaceship
turtle.penup()
turtle.setposition(-110,-250)
turtle.setheading(0)
turtle.pendown()
turtle.setposition(110,-250)

turtle.penup()
turtle.setposition(110,-250)
turtle.pendown()
turtle.setposition(125,-25)

#Draw the right arch of spaceship
turtle.setheading(90)
turtle.circle(600, 35)

turtle.penup()
turtle.setposition(0,320)
turtle.setheading(232)
turtle.pendown()
turtle.circle(600, 35)


#Draw the left arch of the spaceship
turtle.penup()
turtle.setposition(-125,-25)
turtle.pendown()
turtle.setposition(-110,-250)

#Draw the vertical bottom line 
turtle.penup()
turtle.setposition(0,-75)
turtle.pendown()
turtle.setposition(0,-350)

#Draw the window
turtle.penup()
turtle.setposition(30,50)
turtle.setheading(90)
turtle.pendown()
turtle.circle(30)

#Draw the left wing
turtle.penup()
turtle.setposition(-125,-75)
turtle.pendown()
turtle.setposition(-250,-150)

turtle.penup()
turtle.setposition(-250,-150)
turtle.pendown()
turtle.setposition(-175,-350)

turtle.penup()
turtle.setposition(-175,-350)
turtle.pendown()
turtle.setposition(-115,-250)


#Draw the right wing
turtle.penup()
turtle.setposition(125,-75)
turtle.pendown()
turtle.setposition(250,-150)

turtle.penup()
turtle.setposition(250,-150)
turtle.pendown()
turtle.setposition(175,-350)

turtle.penup()
turtle.setposition(175,-350)
turtle.pendown()
turtle.setposition(115,-250)


