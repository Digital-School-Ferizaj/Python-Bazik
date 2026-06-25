import turtle
t=turtle.Turtle()
t.shape("classic")  #square, arrow, circle, turtle, triangle, classic
turtle.bgcolor('black')


# forward, backward, left, right
# fd, bk, lt, rt

"""
t.forward(200)
t.left(90)
t.backward(200)


t.goto(100,100)
t.goto(0,0)
t.goto(100,200)


t.bk(100)
t.lt(90)
t.bk(100)
t.lt(90)
t.bk(100)
t.lt(90)
t.bk(100)

t.circle(60)

t.dot(40)

"""

#trekendesh
t.speed(1)
t.pencolor('yellow')

t.begin_fill()
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.end_fill()

#ylli
t.speed(10)
#t.fillcolor("red")
t.pencolor('light blue')
t.pensize(5)

t.begin_fill()

for i in range(5):
    t.fd(100)
    t.lt(144)

t.end_fill()

#rreth
t.pen(speed=10, pencolor='purple', pensize=5)

t.begin_fill()
t.lt(170)
t.circle(50)
t.end_fill()




#Katror
t.pen(speed=10, pencolor='lime', pensize=5)

t.begin_fill()

t.rt(60)
t.penup()
t.fd(80)
t.pendown()
t.rt(30)

for i in range(4):
    t.fd(80)
    t.rt(90)

t.end_fill()




