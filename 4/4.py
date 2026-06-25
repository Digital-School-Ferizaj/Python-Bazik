# for loop, while loop

prog_lang = ["python", "javascript", "php"]

for x in prog_lang:
    print(x)

for count in range(1,5):
    print(count)

for count in range(1,11):
    print("Digital School is the best!")

for x in range (2, 8):
    print(x)

print("----------")

for x in range(2, 20, 3):
    print(x)

print("----------")

for x in "tomato":
    print(x)

print("----------")

prog_lang = ["python", "javascript", "php"]

for x in prog_lang:
    if x == "javascript":
        break
    print(x)

i=0
while i < 5:
    print(i)
    i = i + 1

print("----------")

i=1
while i < 5:
    print(i)
    if i == 3:
        break
    i = i + 1

print("----------")

i=0
while i < 6:
    i = i + 1
    if i == 3:
        continue
    print(i)

print("----------")

i=1
while i < 6:
    print(i)
    i = i + 1
else:
    print("i is no longer less than 6")

print("----------")

i=1
while i < 6:
    print("Inside WHILE")
    i = i + 1
else:
    print("inside ELSE")

"""---------------------------------------------------------"""
#Program to add natural numbers
#sum = 1+2+3+...+n

#take input from user
n = int(input("Enter number: "))

#initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i + 1 #update counter

print("the sum is", sum)

    
    
