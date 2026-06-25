from tkinter import Tk, simpledialog, messagebox

#this function checks if a number is even or odd
def is_even(number):
    return number % 2 == 0
    
#this function will get to add the leters
#that are in even positions to a list
def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters


#this function will get to add the leters
#that are in odd positions to a list
def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters


#this function get even letters from the encrypted message
#and it is used for decryption
def get_even_letters_dec(message):
    even_letters_dec = []
    for counter in range(0, int(len(message)/2)):
        even_letters_dec.append(message[counter])
    return even_letters_dec


#this function get odd letters from the encrypted message
#and it is used for decryption
def get_odd_letters_dec(message):
    odd_letters_dec = []
    for counter in range(int(len(message)/2), int(len(message))):
        odd_letters_dec.append(message[counter])
    return odd_letters_dec


#this function checks if the letters is vowel
def is_vowel(letter):
    if (letter == "A" or
        letter == "E" or
        letter == "I" or
        letter == "O" or
        letter == "U" or
        letter == "Y" or
        letter == "a" or
        letter == "e" or
        letter == "i" or
        letter == "o" or
        letter == "u" or
        letter == "y"):
        return True

#This function will encrypt the message
def encrypt(message):
    letter_list = []

    if not is_even(len(message)):
        message = message + " "

    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)

    #add the odd letters at the begining
    #also add a dot(.) if the letter is vowel
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        if (is_vowel(odd_letters[counter] == True)):
            letter_list.append(".")

    #add the even letters at the begining
    #also add a dot(.) if the letter is vowel
    for counter in range(0, int(len(message)/2)):
        letter_list.append(even_letters[counter])
        if (is_vowel(even_letters[counter] == True)):
            letter_list.append(".")

    # join the letters to the new message and revers it
    new_message = "".join(letter_list)
    reversed_encrypted_message = "".join(reversed(new_message))

    return reversed_encrypted_message


#This function wil decrypt the message
def decrypt(message):
    letter_list = []

    unreversed_message = "".join(reversed(message))

    if not is_even(len(unreversed_message)):
        unreversed_message = unreversed_message + " "

    #this code removes the dots
    reversed_message = unreversed_message.replace(".", "")

    even_letters = get_even_letters_dec(reversed_message)
    odd_letters = get_odd_letters_dec(reversed_message)

    for counter in range(0, int(len(reversed_message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])

    new_message = "".join(letter_list)

    return new_message


def get_task():
    task = simpledialog.askstring("Task", "Do you wana encrypt or decrypt?")
    return task

def get_message():
    message = simpledialog.askstring("Message", "Enter the message!")
    return message

root = Tk()
root.withdraw()


while True:
    task = get_task()
    if task == "encrypt":
        message = get_message()
        encrypted = encrypt(message)
        messagebox.showinfo("Ciphertex of the secret messsage is:", encrypted)
    elif task == "decrypt":
        message = get_message()
        decrypted = decrypt(message)
        messagebox.showinfo("Plaintext of the secret messsage is:", decrypted)
    else:
        break

root.mainloop()










    
        









    

