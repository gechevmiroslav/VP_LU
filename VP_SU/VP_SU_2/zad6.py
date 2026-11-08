count = int(input("Enter the number of cities: "))
cities = []
for i in range(count):
    city = input("Enter a city: ")
    cities.append(city)
print("City list:", cities)

new_city = input("Enter a city to add: ")
cities.append(new_city)
print("List after adding:", cities)

delete_city = input("Enter a city to delete: ")
if delete_city in cities:
    cities.remove(delete_city)
    print("List after deletion:", cities)
else:
    print("City not found.")

print("Current city list:", cities)

cities.sort()
print("Sorted list:", cities)

search_city = input("Enter a city to search: ")
if search_city in cities:
    print("City found.")
else:
    print("City not found.")

number = int(input("Enter the number of new cities: "))
new_cities = []
for i in range(number):
    city = input("Enter a city: ")
    new_cities.append(city)
cities = cities + new_cities
print("Combined city list:", cities)