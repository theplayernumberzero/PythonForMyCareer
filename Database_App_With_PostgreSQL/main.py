import psycopg2

def create_table():
    conn = psycopg2.connect(dbname="studentdb", user = "postgres", password = "admin123", host = "localhost", port = 5432)
    #You can make sql queries with cursor
    cur = conn.cursor()
    cur.execute("create table students(student_id serial primary key, name text, address text, age int, number text);")
    print("Student table created")
    conn.commit()   #commit the changes
    conn.close()

def insert_data():
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    age = int(input("Enter your age: "))
    number = input("Enter your number: ")
    conn = psycopg2.connect(dbname="studentdb", user = "postgres", password = "admin123", host = "localhost", port = 5432)
    #You can make sql queries with cursor
    cur = conn.cursor()
    #passing variables to query
    cur.execute("insert into students(name, address, age, number) values (%s, %s, %s, %s);", (name, address, age, number))
    print("data added in student table")
    conn.commit()   #commit the changes
    conn.close()

def update_data():
    conn = psycopg2.connect(dbname="studentdb", user = "postgres", password = "admin123", host = "localhost", port = 5432)
    #You can make sql queries with cursor
    cur = conn.cursor()
    id = input("Enter id which you want to update: ")
    choice = input("Which field do you want to update\n1)Name\n2)Address\n3)Age\n4)Number\n5)All\n:")
    if choice == "1":
        name = input("Enter your name: ")
        cur.execute("update students set name= %s where student_id=%s;", (name, id))
    elif choice == "2":
        address = input("Enter your address: ")
        cur.execute("update students set address= %s where student_id=%s;", (address, id))
    elif choice == "3":
        age = int(input("Enter your age: "))
        cur.execute("update students set age= %s where student_id=%s;", (age, id))
    elif choice == "4":
        number = input("Enter your number: ")
        cur.execute("update students set number= %s where student_id=%s;", (number, id))
    elif choice == "5":
        name = input("Enter your name: ")
        address = input("Enter your address: ")
        age = int(input("Enter your age: "))
        number = input("Enter your number: ")
        cur.execute("update students set name= %s, address=%s, age=%s, number=%s where student_id=%s;", (name, address, age, number, id))
    else:
        print("Invalid number..")
        return
    print(f"{id} id is updated..")
    conn.commit()   #commit the changes
    conn.close()

def delete_data():
    student_id = input("Enter id number which you want to delete: ")
    conn = psycopg2.connect(dbname="studentdb", user = "postgres", password = "admin123", host = "localhost", port = 5432)
    cur = conn.cursor()
    cur.execute("select * from students where student_id = %s;", (student_id))
    student = cur.fetchone()    #row u verir

    #student[0]:id, student[1]:name...
    if student: #aranan öğrenci varsa
        cur.execute("delete * from students where student_id = %s;", (student_id))
        print(f"Student with id {student_id} deleted..")
    conn.commit()   #commit the changes
    conn.close()

def read_data():
    conn = psycopg2.connect(dbname="studentdb", user = "postgres", password = "admin123", host = "localhost", port = 5432)
    #You can make sql queries with cursor
    cur = conn.cursor()
    cur.execute("select * from studentdb")
    students = cur.fetchall()
    for student in students:
        print(f"id: {students[0]}, name:{student[1]}, address:{student[2]}, age:{student[3]}, number:{student[4]}")
    conn.commit()   #commit the changes
    conn.close()


while True:
    print("\nWelcome to the student DMS")
    print("1. Create data")
    print("2. Insert data")
    print("3. Read data")
    print("4. Update data")
    print("5. Delete data")
    print("6. Exit")
    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        create_table()
    elif choice ==2:
        insert_data()
    elif choice ==3:
        read_data()
    elif choice ==4:
        update_data()
    elif choice ==5:
        delete_data()
    elif choice == 6:
        break
    else:
        print("Invalid number..")