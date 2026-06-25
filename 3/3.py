5 == 5
5 == 6
type(True)
type(False)


x = 4
y = 7

x == y      # x is equal to y
x != y      # x is not equal to y
x >  y      # x is greater than y
x <  y      # x is smaller than y
x >= y      # x is greater than or equal to y
x <= y      # x is less than or equal to y
x is y      # x is the same as y
x is not y  # x is not the same as y


x = 5
y = "5"
z = 5.0

x == y      #False
x is y      #False
x == z      #True
x is z      #False
z is not x  #True


name = "John"
name == "Elon"  #False
name == "John"  #True


age = 12
age == 18 #False
age != 12 #False


age = 22
age > 20 and age < 30 #True
"""php: ( (age > 20) || (age < 30))"""

age > 20 and age != 22 #False

age > 20 or age != 22  #True

movies = ("F9", "Avatar 2", "Transformers")
"F9" in movies          #True
"Batman" in movies      #False
"Batman" not in movies  #True


# If / else / elif

age = 18
if age < 18:
    print("You can not vote!")


if age < 18:
    print("You can not vote!")
    print("You need to be at least 18 to vote")

if age < 18:
    print("You can not vote!")
    print("You need to be at least 18 to vote")
else:
    print("You can vote now!")



age = 10
if age <= 7:
    print("tickets are free")
elif age < 15:
    print("50% discount on tickets")
elif age < 18:
    print("20% discount on tickets")
else:
    print("pay full price")

    
is_cold = input("A po bje shi? (y/n)")
if is_cold == "y":
    print("Merre qadren")
else:
    print("Ok nuk te vyne qadra")


movies = input("Cili film nuk eshte lancu ne vitin 2003? (Finding Nemo/Spider-Man/School of Rock)")
if movies == "Spider-Man":
    print("Sakte")
elif movies == "Finding Nemo":
    print("Gabim")
else:
    print("Gabim")

username = input("Enter username:")
print("Your username is: "+ username)


