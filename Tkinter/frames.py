from tkinter import *

root = Tk()
root.geometry("400x400")

frame1 = Frame(root, highlightthickness=1, highlightbackground="red", padx="20", pady="20")
frame1.pack()

frame2 = Frame(root)
frame2.pack(side= BOTTOM)   #frame and widgets inside will be in bottom

button1 = Button(frame1, text="Frame 1 button") #widget nereye eklenecek ilk parametrede belirtiyoruz
button1.pack()

button2 = Button(frame2, text="Frame 2 button") #widget nereye eklenecek ilk parametrede belirtiyoruz
button2.pack()

root.mainloop()