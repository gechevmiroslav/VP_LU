class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality

    def print(self):
        print(f"Name: {self.name} {self.family}")
        print(f"Nationality: {self.nationality}")

person = Person("Ivan", "Ivanov", 18, "Bulgarian")
person.print()