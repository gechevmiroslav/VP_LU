def can_fit(width, height, radius):
    diagonal = (width ** 2 + height ** 2) ** 0.5

    if diagonal <= 2 * radius:
        return True
    else:
        return False


width = float(input("Enter rectangle width: "))
height = float(input("Enter rectangle height: "))
radius = float(input("Enter circle radius: "))

if can_fit(width, height, radius):
    print("The rectangle fits in the circle.")
else:
    print("The rectangle does not fit in the circle.")