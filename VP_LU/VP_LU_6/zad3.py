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

class Lecturer(Person):
    def __init__(self, name, family, age, nationality, university, experience):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.experience = experience

    def print(self):
        super().print()
        print(f"University: {self.university}")
        print(f"Experience: {self.experience}")

lecturer = Lecturer("Ivan", "Ivanov", 30, "Bulgarian", "TU Sofia", 20)
lecturer.print()