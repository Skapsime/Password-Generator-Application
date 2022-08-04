# importing the tkinter module
from tkinter import *

# importing the pyperclip module that is use to copy the generated password to  the clipboard
import pyperclip

# random module will be used for generating the random password
import random

# initializing the tkinter
root = Tk()

# setting the width and height of the GUI
root.geometry("500x500")    # x is small case here

root.title("Password Generator Application")

# declaring a variable of string type and this variable will be
# used to store the password generated
passStr = StringVar()

# declaring a variable of integer type which will be used to
# store the length of the password entered by the user
passlen = IntVar()

# initially the length of the password to be zero 
passlen.set(0)


# function to generate the password
def generate():
    # storing the keys in a list which will be used to generate the password
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
             '*', '(', ')']

    # declaring an empty string
    password = ""

    # This loop will generate the random password of the length entered
    # by the user
    for x in range(passlen.get()):
        password = password + random.choice(pass1)

    # setting the password to the entry widget
    passStr.set(password)

# function to copy the password to the clipboard

def copytoclipboard():
    random_password = passStr.get()
    pyperclip.copy(random_password)


# Creating a text label widget
Label(root, text="Password Generator Application", font="poppins 20 bold").pack()

# Creating a text label widget
Label(root, text="Enter password length" , font="poppins 10 bold").pack(pady=3)

# Creating a entry widget to take password length entered by the user
Entry(root, textvariable=passlen).pack(pady=3)

# button to call the generate function
Button(root, text="Generate Password", command=generate).pack(pady=7)

# entry widget to show the generated password
Entry(root, textvariable=passStr).pack(pady=3)

# button to call the copytoclipboard function
Button(root, text="Copy to clipboard", command=copytoclipboard).pack()

# mainloop() is an infinite loop used to run the application when
# it's in ready state
root.mainloop()
