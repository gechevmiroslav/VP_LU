class Flyer():
    def fly(self):
        print("I am flying in the sky!")

class Swimmer():
    def swimm(self):
        print("I am swimming in the water!")

class Duck(Flyer, Swimmer):
    pass

duck = Duck()
duck.fly
duck.swimm

print(Duck.mro())