class Person():
    def __int__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hello, I am", self.name, "and I am", self.age, "years old.")

person1 = Person("Ivan", 18)
person2 = Person("Peter", 20)

person1.introduce()
person2.introduce()