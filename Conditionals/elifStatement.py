grade = int(input("Enter your grade 0-100: "))

if grade < 60 and grade > 0:
    print(f"Your grade is {grade}, and your mark is D")
elif grade < 70 and grade > 0:
    print(f"Your grade is {grade}, and your mark is C")
elif grade < 90 and grade > 0:
    print(f"Your grade is {grade}, and your mark is B")
elif grade <= 100 and grade > 0:
    print(f"Your grade is {grade}, and your mark is A")
else:
    print("Enter grade between 0-100") 