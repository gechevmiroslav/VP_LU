class Animal:
    def make_sound(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def make_sound(self):
        print("The dog barks: Woof-woof!")

animal = Animal()
dog = Dog()

animal.make_sound()
dog.make_sound()