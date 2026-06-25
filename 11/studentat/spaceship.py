import turtle
turtle.delay(10)
turtle.pensize(15)
turtle.speed(5)

#window
turtle.penup()
turtle.setposition(20,100)
turtle.setheading(90)
turtle.pendown()
turtle.circle(30)

#left wing
turtle.penup()
turtle.setposition(-125,-75)
turtle.pendown()
turtle.setposition(-175,-110)
turtle.setposition(-135,-200)
turtle.setposition(-115,-180)
turtle.setposition(-115,-75)

#b
turtle.penup()
turtle.setposition(-115,-75)
turtle.pendown()
turtle.setposition(115,-75)

#right wing
turtle.penup()
turtle.setposition(115,-75)
turtle.pendown()
turtle.setposition(150,-110)
turtle.setposition(120,-200)
turtle.setposition(100,-180)
turtle.setposition(100,-75)

#l
turtle.penup()
turtle.setposition(-10,-150)
turtle.pendown()
turtle.setposition(-10,0)

#right arch
turtle.penup()
turtle.setposition(100,-75)
turtle.pendown()
turtle.setposition(100,200)
turtle.setposition(-115,200)
turtle.setposition(-115,-75)

#t
turtle.penup()
turtle.setposition(100,200)
turtle.pendown()
turtle.setheading(15)
turtle.setposition(-10,250)
turtle.setposition(-115,200)


