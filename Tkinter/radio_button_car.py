from tkinter import *

def selected():
    label1.config(text= f"Selected car: {fuel.get()}")

root = Tk()
root.geometry("400x400")

fuel = StringVar(value = "Petrol")  #Initial value for radio buttons, only one variable for grouping

#same variable, different values. Means only 1 of them is selected
r1 = Radiobutton(root, text= "Petrol", variable= fuel, value= "Petrol", command=selected)
r2 = Radiobutton(root, text= "Diesel", variable= fuel, value= "Diesel", command=selected)
r3 = Radiobutton(root, text= "Electric", variable= fuel, value= "Electric", command=selected)

label1 = Label(root)

r1.pack()
r2.pack()
r3.pack()
label1.pack()

root.mainloop()