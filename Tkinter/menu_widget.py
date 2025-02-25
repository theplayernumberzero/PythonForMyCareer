from tkinter import *

def function1():
    print("Project submenu clicked")

root = Tk()

my_menu = Menu(root)    #File, edit, selection gibi ekran üsütnde duranlar menü oluyor
root.config(menu=my_menu)

sub_menu = Menu(my_menu)

sub_menu.add_command(label="Project",command=function1)
sub_menu.add_command(label="Save")

my_menu.add_cascade(label="File",menu=sub_menu)

root.mainloop()