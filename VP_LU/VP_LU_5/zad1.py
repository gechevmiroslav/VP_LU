def square(a):
    return a * a

def rectangle(a, b):
    return a * b

def triangle(a, b):
    return a * b / 2

choice = int(input("Choose a figure (1-Square, 2-Rectangle, 3-Triangle): "))

if choice == 1:
    a = float(input("Enter side: "))
    print("Area:", square(a))
elif choice == 2:
    a = float(input("Enter side: "))
    b = float(input("Enter side: "))
    print("Area: ", rectangle(a, b))
elif choice == 3:
    a = float(input("Enter side: "))
    b = float(input("Enter side: "))
    print("Area: ", triangle(a, b))
else:
    print("Invalid choice.")