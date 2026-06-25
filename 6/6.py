score = 0
print("Guess the Capital Cities!")


def check_question (guess, answer):
    global score
    guessing = True
    attempt = 1
    while guessing and attempt <4:
        if  guess.lower() == answer.lower(): #paris
            print("Correct Answer!")
            score = score + 1
            guessing = False
        else:
            if attempt < 3:
                guess = input("Wrong answer. Try again. ")
            attempt = attempt + 1
    if attempt == 4:
        print("The correct answer is " + answer)



question1 = input("What is the Capital city of France? \n A)Paris \n B)Prishtina \n")#PARIS
check_question(question1, "a")

question2 = input("What is the Capital city of Kosovo?") 
check_question(question2, "Prishtina")

question3 = input("What is the Capital city of Germany?") 
check_question(question3, "berlin")

question4 = input("What is the Capital city of Italy?") 
check_question(question4, "rome")

question5 = input("What is the Capital city of Polony?") 
check_question(question5, "Warsaw")

print("Your final score is " + str(score) )


