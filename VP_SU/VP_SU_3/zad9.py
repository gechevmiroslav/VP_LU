from collections import namedtuple
Student = namedtuple("Student", ["name", "age", "grade", "city"])
students = (
    Student("Ivan", 20, 5.50, "Sofia"),
    Student("Maria", 21, 5.80, "Plovdiv"),
    Student("Peter", 22, 4.50, "Varna"),
    Student("Anna", 20, 5.20, "Burgas"),
    Student("Georgi", 23, 4.80, "Sofia"),
    Student("Elena", 21, 6.00, "Ruse"),
    Student("Nikolay", 22, 5.00, "Pleven")
)

def good_students(students):
    total = 0

    for student in students:
        total += student.grade
    average = total / len(students)
    names = []

    for student in students:
        if student.grade > average:
            names.append(student.name)
    print("The students", ", ".join(names), "are doing well this semester!")

good_students(students)