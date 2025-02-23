students = [
    {"name": "Bahadir", "age": 23, "grade": "A"},
    {"name": "Ali", "age": 22, "grade": "B"},
    {"name": "Efe", "age": 21, "grade": "C"},
    {"name": "Arda", "age": 20, "grade": "D"},
    {"name": "Mustafa", "age": 19, "grade": "A"}
]

print(students)

filtered_students = list(filter(lambda student: student["age"] >= 18 and student["grade"] == "A", students))
print(filtered_students)