import turtle

t = turtle.Turtle()

turtle.delay(10) #delay ke koha qe i vyne per mja fillu egzekutimi i kodit ne milisekonda
t.pensize(15)
t.speed(0.5)

#body
t.penup()
t.setposition(200,-50)
t.setheading(0)
t.pendown()
t.setposition(200,150)
t.setposition(-200,150)
t.setposition(-200,-50)
t.setposition(200,-50)
t.penup()

#neck
t.setposition(-50,150)
t.pendown()
t.setposition(-50,200)

t.penup()
t.setposition(50,150)
t.pendown()
t.setposition(50,200)


#head
t.penup()
t.setposition(-175,200)
t.pendown()
t.setposition(175,200)
t.setposition(175,335)

t.setheading(90)
t.circle(50, 95)

t.setposition(-125,385)

t.setheading(180)
t.circle(50, 95)

t.setposition(-175,200)

#eyes
t.penup()
t.setposition(-35,275)
t.pendown()

t.setheading(90)
t.circle(30,180)

t.penup()
t.setposition(100,275)
t.pendown()

t.setheading(90)
t.circle(30,180)

#left hand
t.penup()
t.setposition(-200,100)
t.pendown()
t.setposition(-250,100)

t.penup()
t.setposition(-250,150)
t.pendown()
t.setposition(-300,150)

t.setheading(180)
t.circle(30,90)

t.setposition(-330,-75)
t.setposition(-250,-75)
t.setposition(-250,150)

t.penup()
t.setposition(-290,-75)
t.pendown()
t.setposition(-290,-110)

t.penup()
t.setposition(-260,-150)
t.pendown()
t.setheading(90)
t.circle(30,180)


#right hand
t.penup()
t.setposition(200,100)
t.pendown()
t.setposition(250,100)

t.penup()
t.setposition(250,150)
t.pendown()

t.setposition(250,-75)
t.setposition(330,-75)
t.setposition(330,120)

t.setheading(90)
t.circle(30,90)

t.setposition(250,150)

t.penup()
t.setposition(290,-75)
t.pendown()
t.setposition(290,-110)

t.penup()
t.setposition(320,-150)
t.pendown()
t.setheading(90)
t.circle(30,180)


#legs
t.penup()
t.setposition(-135,-50)
t.pendown()
t.setposition(-135,-150)

t.penup()
t.setposition(135,-50)
t.pendown()
t.setposition(135,-150)

t.penup()
t.setposition(185,-150)
t.pendown()
t.setposition(-185,-150)

t.setheading(180)
t.circle(50,180)

t.setheading(0)
t.setposition(185,-250)

t.setheading(0)
t.circle(50,180)

t.penup()
t.setposition(-135,-185)
t.pendown()
t.setposition(-135,-215)

t.penup()
t.setposition(-70,-185)
t.pendown()
t.setposition(-70,-215)

t.penup()
t.setposition(0,-185)
t.pendown()
t.setposition(0,-215)

t.penup()
t.setposition(70,-185)
t.pendown()
t.setposition(70,-215)

t.penup()
t.setposition(135,-185)
t.pendown()
t.setposition(135,-215)


