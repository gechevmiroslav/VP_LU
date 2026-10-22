print("zad1")
a = float(input("Enter a value for a: "))
h = float(input("Enter a value for h: "))
area = a * h
print(f"Area: {area:.2f}")

print()
print("zad2")
import math
r = float(input("Enter a value for r: "))
h = float(input("Enter a value for h: "))
area = math.pi * (r ** 2) * h
print(f"Area: {area:.3f}")

print()
print("zad3")
km = float(input("Enter the number of kilometers: "))
cost = float(input("Enter the cost per 100 km: "))
fuel = (km / 100) * cost
print(f"Fuel: {fuel:.2f}")