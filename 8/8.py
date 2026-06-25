import random
import string

colors = ["yellow", "blue", "green", "black", "grey", "red" ]
shapes = ["circle", "diamond", "square", "hexagon", "rectangle" ]

print("Welcome to Password Generator!")

while True:
    color = random.choice(colors)
    shape = random.choice(shapes)
    number = random.randrange(0,100)
    special_char = random.choice(string.punctuation)

    password = color + shape + str(number) + special_char
    print("Your random password is: %s" % password)

    response = input("Would you like another password? Type y or n: ")

    if response == "n":
        break


shkronjat = [ "a", "b", "c", "d", "e", "f", "g"]

while True:
    shkronja = random.choice(shkronjat)
    numra = random.randrange(0,9)
    char = random.choice(string.punctuation)

    lista = [shkronja, str(numra), char]

    passwordi = random.choice(lista) + random.choice(lista) + random.choice(lista) + random.choice(lista) + random.choice(lista) + random.choice(lista)
    print("Paswordi yt eshte: %s" % passwordi)
    response = input("A pe do nja tjeter? Shkruaje po ose jo: ")

    if response == "jo":
        break

