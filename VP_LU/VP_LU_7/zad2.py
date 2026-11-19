class Car():
    def __init__(self, brand, horsepower):
        self.brand = brand
        self.horsepower = horsepower

    def __str__(self):
        return self.brand + "with" + str(self.horsepower) + "horsepower"

car1 = Car("BMW", 100)
print(car1)