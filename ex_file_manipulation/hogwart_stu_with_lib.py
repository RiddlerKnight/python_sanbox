import csv

students = []
with open("stu.csv") as file:
    for name, house in csv.reader(file):
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

# Sort by student name
for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")

print("===============")

# Another example by using anonymous function (Lambda func)
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
