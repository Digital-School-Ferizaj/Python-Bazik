# FUNCTIONS

def emriFunksionit():
    print("Testing function!")

emriFunksionit()


def pershendete(name):
    print("Pershendetje, " + name)

pershendete("Anes")
pershendete("Flakon")
pershendete("Diart")
pershendete("Butrint")


def hi(name, msg):
    print("Ckemi, " + name + "! " + msg)

hi("Anes", "Si po kalon?")
hi("Flakon", "Mire se vjen!")
hi("Diart", "Mire mengjes!")
hi("Butrint", "A u lodhe?")

def sum_num(num1, num2):
    print(num1 + num2)

sum_num(2, 4)

def add(a, b):
    sum = a + b
    return sum

a = int(input("Enter first number"))
b = int(input("Enter second number"))
result = add(a,b)
print("Result = ", result)

def perserit_emrin(name, num):
    for i in range(0, num):
        print(name, " ")

name = input("give us your name")
n = int(input("sa here me perserit?"))

perserit_emrin(name, n)

min(100, 200, 40, 23, 56, 37)
max(100, 200, 40, 23, 56, 37)

mylist = ["python", "php", "javascript"]
len(mylist)






