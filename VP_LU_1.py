print("zad 1")
a = float(input("Enter a value for a: "))
b = float(input("Enter a value for b: "))
h = float(input("Enter a value for h: "))
area = (a + b) * h / 2
print(f"Area: {area:.2f}")

print()
print("zad 2")
import math
r = float(input("Enter a value for r: "))
d = r**2
area = math.pi * d
perimeter = 2 * math.pi * r
print(f"Area = {area:.3f}; Perimeter = {perimeter:.3f}")

print()
print("zad 3")
hours = float(input("Enter the number of hours: "))
rate = float(input("Enter the hours rate: "))
pay = hours * rate
print(f"{pay:.2f}")