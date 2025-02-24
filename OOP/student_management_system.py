class Student:
    def __init__(self,name,roll_number,age):
        self.name=name
        self.roll_number=roll_number
        self.age=age
        
class School:
    def __init__(self):
        self.students = []
    
    def add_student(self,name,roll_number,age):
        #create a student object
        student=Student(name,roll_number,age)
        self.students.append(student)
        print(f"Student {name} added successfully")
        
    def display_students(self):
        if self.students:
            for student in self.students:
                print(f"Name:{student.name}")
                print(f"Roll number:{student.roll_number}")
                print(f"Age:{student.age}")
                print("...................")
        else:
            print("There is not student yet..")
                
    def edit_student(self,roll_number,new_name,new_age):
        if self.students != []:
            for student in self.students:
                if student.roll_number == roll_number:
                    student.name=new_name
                    student.age= new_age
                    print(f"Student {student.name} successfully updated")
                    return
                else:
                    print("There is no student with that roll number..")
        else:
            print("There is not student yet..")
    
    def delete_student(self,roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                print(f"Student {student.name} deleted successfully.")
                return
            else:
                print("There is no student with that roll number..")
        
#Create a school object first:
school = School()
while True:
    choice = input('\nEnter your choice: \n1)Add student \n2)Display list of students \n3)Edit student data \n4)Remove student\n5)Exit: \n:')
    if choice=="1":
        name = input('Enter name: ')
        roll_number= input('Enter roll number: ')
        age = input('Enter age: ')
        school.add_student(name, roll_number, age)
        
    elif choice =="2":
        school.display_students()
    elif choice =="3":
        roll_number = input("Enter roll number of student you want to edit: ")
        new_name = input("Enter new name for the student: ")
        new_age = input("Enter new age for the student: ")
        school.edit_student(roll_number, new_name, new_age)
    elif choice=="4":
        roll_number= input("Enter roll number you want to delete: ")
        school.delete_student(roll_number)
    elif choice=="5":
        break