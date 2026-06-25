print ("Hello")
print (6*6)
print (5-4)

#Variables can contain letters, underline(_), numbers 
#Symbols such as -, /, #, or @ aren’t allowed.
#Variables cannot start with a number. One variable can be called message1 but not 1message
#No spaces allowed.
#Avoid keywords that are reserved for Python example: “print”

name = 'john'
surname = 'Doe'
print (name, surname)


'''
integer = 1 2 3 4 5                               int
floating-point numbers = 1.2, 0.4, 0.3, 135.8     float
complex number = 1x, -3+2i,                       complex

'''

lunch_money = 25
food = 5
daily = 3

result = (lunch_money - food)/daily
print (result)


#Integer:
x = int(1) # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

print(x+z)

#Float:
x = float(1) # x will be 1.0
y = float(2.8) # y will be 2.8
z = float("3") # z will be 3.0
w = float("4.2") # w will be 4.2

print(y+z)


"hello" == 'hello'
print("hello" == 'hello')

message = "hello"
print(message)

print(len(message))

print (name, surname)
print (name + surname)

name = 'John'
school = "Welcome to Digital School, "
message = school + name
fullname = name + surname

print(message)

message = "Welcome %s to Digital school"
print(message % name)
name = 'Jane'
print(message % name)

score = 100
message = "Your score is %s, try again!"
print(message % score)

school_c = ["code", "scratch", "app inventor"]
print(school_c)
print(school_c[0])




