from tkinter import *

def add():
    number1 = int(input1.get())
    number2 = int(input2.get())
    sum = number1 + number2
    #config hazırda olan widget ın özellilerini değiştirmeye yarar
    answer.config(text= f"{number1} + {number2} = {sum}")

root = Tk()
root.geometry("400x400")

input1 = Entry(root)
input2 = Entry(root)
input1.pack()
input2.pack()

button = Button(root, text= "Add two numbers", command= add)
button.pack()

answer = Label(root)
answer.pack()


root.mainloop()