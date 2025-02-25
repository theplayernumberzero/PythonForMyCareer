#allow us to create GUI

from tkinter import *

def display():
    data = entry.get()  #Entryde yazılan ifadeyi alma
    print(data)
    print("Button clicked..")

def selected():
    label1.config(text=check1_value.get())

#create window
root = Tk()
root.geometry("300x400")    #ekran boyutu düzenleme

hello = Label(root, text = "Hello World", fg = "red", bg="white", font = ("Arial", 24))
hello.pack()    #widget ı window a yerleştirme

entry = Entry(root)
entry.pack()

button = Button(root, text= "Click me", command= display)
button.pack()

check1_value = BooleanVar() #It is for controlling is it checked or not
check1 = Checkbutton(root, text= "Accept terms", variable= check1_value, command= selected) #If clicked 1i not clicked 0
check1.pack()

label1 = Label(root)
label1.pack()

#kod execution tamamlandığında kapanmasını önlemek için
root.mainloop() #still running