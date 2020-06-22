import random
import tkinter as tk
from tkinter import *
import pyperclip

root = Tk()
root.title('Password')
root.geometry('300x200')
passstr = StringVar()
passlen = IntVar()
passlen.set(0)

# Generate the password
def generate():
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '^', '&', 
            '*', '>', '?']
    password = ''
    # Creates password
    for i in range(passlen.get()):
        password = password + random.choice(pass1)
    passstr.set(password)
# function to copy password to clipboard 
def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)
    
Label(root,text='Password Generator App',font="calibri 20 bold").pack
Label(root,text='Enter Password Length:').pack(pady=3)
Entry(root,textvariable=passlen).pack(pady=3)
Button(root,text='Generate Password',command=generate).pack(pady=7)
Entry(root,textvariable=passstr).pack(pady=3)
Button(root,text='Copy to Clipboard', command=copytoclipboard).pack(pady=7)
root.mainloop()
