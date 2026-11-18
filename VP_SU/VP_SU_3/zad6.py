def split_fruits(fruits):
    parts = []

    for fruit in fruits:
        middle = len(fruit) // 2
        first_part = fruit[:middle]
        second_part = fruit[middle:]
        parts.append(first_part)
        parts.append(second_part)
    parts.sort()
    return parts

count = int(input("Enter the number of fruits: "))
fruits = []
for i in range(count):
    fruit = input("Enter a fruit: ")
    fruits.append(fruit)

print("Sorted parts:", split_fruits(fruits))