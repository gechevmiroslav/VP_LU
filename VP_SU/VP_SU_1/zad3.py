km = float(input("Enter the number of kilometers: "))
cost = float(input("Enter the cost per 100 km: "))
fuel = (km / 100) * cost
print(f"Fuel: {fuel:.2f}")