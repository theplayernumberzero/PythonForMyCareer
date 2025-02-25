from tkinter import *
import tkinter.messagebox

root = Tk()

#tkinter.messagebox.showinfo("Title", "This is info message box")
response = tkinter.messagebox.askquestion("Question 1", "Do you like tea?")
if response == "yes":
    tkinter.messagebox.showinfo("Tea Service", "Here is your tea")

root.mainloop()