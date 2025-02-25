from tkinter import *

root = Tk()
root.geometry("300x300")

label1 = Label(root, text= "Email")
label2 = Label(root, text= "Password")

text1 = Entry(root)
text2 = Entry(root)

button = Button(root, text= "Login")

#instead of using pack we use grid
label1.grid(row=0, column=0)
text1.grid(row=0, column=1)
label2.grid(row=1, column=0)
text2.grid(row=1, column=1)
button.grid(row=2, column=1)
root.mainloop()