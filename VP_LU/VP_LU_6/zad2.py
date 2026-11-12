class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality

    def print(self):
        print(f"Name: {self.name} {self.family}")
        print(f"Nationality: {self.nationality}")

class Student(Person):
    def __init__(self, name, family, age, nationality, university, yearofstudy):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.yearofstudy = yearofstudy

    def print(self):
        super().print()
        print(f"University: {self.university}")
        print(f"Year of study: {self.yearofstudy}")

student = Student("Ivan", "Ivanov", 18, "Bulgarian", "TU Sofia", 1)
student.print()