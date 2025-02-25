from tkinter import * 

def selected():
    get_check_value1 = check_value1.get()
    get_check_value2 = check_value2.get()
    get_check_value3 = check_value3.get()

    label2.config(text= f"Sugar: {"Yes" if get_check_value1 == 1 else "No"}\nIce: {"Yes" if get_check_value2 == 1 else "No"}\nCream: {"Yes" if get_check_value3 == 1 else "No"}\n")

root = Tk()
root.geometry("400x400")

label1 = Label(root, text= "Please select what do you want on your caffe")
label1.pack()

check_value1 = BooleanVar()
check_value2 = BooleanVar()
check_value3 = BooleanVar()

check1 = Checkbutton(root, text= "Sugar", variable= check_value1, command= selected)
check2 = Checkbutton(root, text= "Ice", variable= check_value2, command= selected)
check3 = Checkbutton(root, text= "Cream", variable= check_value3, command= selected)

check1.pack()
check2.pack()
check3.pack()

label2 = Label(root, fg= "yellow")
label2.pack()

root.mainloop()