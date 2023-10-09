from tkinter import *
import random
import string
password=""


root= Tk()
def generate():

    lengthh=int(e.get())
    global password
    password=""
    for i in range(0, lengthh):
        randomLetter = random.choice(string.ascii_letters)
        password=password+randomLetter
    Label2.config(text=password)
root.title("Password Generator")
Label1= Label(root, text="Enter the number of characters in the password")
Label1.grid(row=0, column=0, columnspan=3)
e=Entry(root, width=50)
e.grid(row=1, column=0, columnspan=3)

button1= Button(root, text="Generate", padx=40, pady=40, command=generate)
button1.grid(row=2, column=0, columnspan=3)

Label2= Label(root, text="")
Label2.grid(row=3, column=0, columnspan=3)


root.mainloop()