from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
import psycopg2

def run_query(query, parameters=()):
    conn = psycopg2.connect(dbname="studentdb", user = "postgres", password = "admin123", host = "localhost", port = 5432)
    cur = conn.cursor()

    query_result = None
    
    try:
        cur.execute(query, parameters)
        if query.lower().startsWith("select"):
            query_result = cur.fetchall
        conn.commit()
    except psycopg2.Error as e:
        messagebox.showerror("Database Error", str(e))
    finally:
        cur.close()
        conn.close()
    return query_result

def refresh_treeview():
    #everytime we call function in tbale there will be dupliacte, with this code we prevent this
    for item in tree.get_children():
        tree.delete(item)

    records = run_query("select * from students;", )
    for record in records:
        tree.insert('', END, values=record)

def insert_data():
    query = "insert into students(name, address, age, number) values (%s, %s, %s, %s);"
    parameters = (name_entry.get(), address_entry.get(), age_entry.get(), number_entry.get())
    run_query(query, parameters)
    messagebox.showinfo("Information", "Data inserted successfully")
    refresh_treeview()

#silme işlemi için önce tree den itemi seç, ardından button a tıkla
def delete_data():
    selected_item = tree.selection()[0] #seçilen item gelir
    student_id = tree.item(selected_item)['values'][0]
    query = "delete from students where student_id = %s;"
    parameters = (student_id)
    run_query(query, student_id)
    messagebox.showinfo("Information", "Data deleted successfully")
    refresh_treeview()

def update_data():
    selected_item = tree.selection()[0] #seçilen item gelir
    student_id = tree.item(selected_item)['values'][0]
    query = "update students set name=%s, address=%s, age=%s, number=%s where student_id=%s;"
    parameters = (name_entry.get(), address_entry.get(), age_entry.get(), number_entry.get(), student_id)
    run_query(query, parameters)
    messagebox.showinfo("Information", f"{student_id} id  updated successfully")
    refresh_treeview()

def create_table():
    query = "create table if not exist students(student_id serial primary key, name text, address text, age int, number text);"
    run_query(query)
    messagebox.showinfo("Information", "Table created successfully")
    refresh_treeview()

root = Tk()
root.title("Student Managment System")

frame = LabelFrame(root, text="Student Data")
frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

Label(frame, text="Name: ").grid(row=0, column=0, padx=2, sticky="w")
name_entry = Entry()
name_entry.grid(row=0, column=1, pady=2, sticky="ew")
Label(frame, text="Address: ").grid(row=1, column=0, padx=2, sticky="w")
address_entry = Entry()
address_entry.grid(row=1, column=1, pady=2, sticky="ew")
Label(frame, text="Age: ").grid(row=2, column=0, padx=2, sticky="w")
age_entry = Entry()
age_entry.grid(row=2, column=1, pady=2, sticky="ew")
Label(frame, text="Number: ").grid(row=3, column=0, padx=2, sticky="w")
number_entry = Entry()
number_entry.grid(row=3, column=1, pady=2, sticky="ew")

button_frame = Frame(root)
button_frame.grid(row=1, column=0, pady=5, sticky="ew")

Button(button_frame, text="Create table", command=create_table).grid(row=0, column=0, padx=5)
Button(button_frame, text="Add data" ,command=insert_data).grid(row=0, column=1, padx=5)
Button(button_frame, text="Update data" ,command=update_data).grid(row=0, column=2, padx=5)
Button(button_frame, text="Delete data", command=delete_data).grid(row=0, column=3, padx=5)

tree_frame = Frame(root)
tree_frame.grid(row=2, column=0, padx=10, sticky="nsew")

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill= Y)

tree = ttk.Treeview(tree_frame, yscrollcommand= tree_scroll.set, selectmode="browse")    #connect scrollbar with table
tree.pack()
tree_scroll.config(command=tree.yview)

tree['columns'] = ("student_id", "name", "address", "age", "number")
tree.column("#0", width=0, stretch=NO)  #for not showing it
tree.column("student_id", width=80, anchor=CENTER)
tree.column("name", width=120, anchor=CENTER)
tree.column("address", width=120, anchor=CENTER)
tree.column("age", width=50, anchor=CENTER)
tree.column("number", width=120, anchor=CENTER)

tree.heading("student_id", text="ID",anchor=CENTER)
tree.heading("name", text="NAME",anchor=CENTER)
tree.heading("address", text="ADDRESS",anchor=CENTER)
tree.heading("age", text="AGE",anchor=CENTER)
tree.heading("number", text="NUMBER",anchor=CENTER)

refresh_treeview()
root.mainloop()