class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, faculty_number):
        super().__init__(name, age)
        self.faculty_number = faculty_number

student = Student("Ivan", 18, 12345)
print("Name: ", student.name)
print("Age: ", student.age)
print("Faculty number: ", student.faculty_number)