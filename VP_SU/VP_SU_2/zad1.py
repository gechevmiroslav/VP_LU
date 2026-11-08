count = int(input("Enter the number of elements: "))
numbers = []

for i in range(count):
    number = int(input("Enter a number: "))
    numbers.append(number)
print(f"Original list: {numbers}")

print(f"Tripled list: {numbers * 3}")

print("List elements:")
for number in numbers:
    print(number)

search_number = int(input("Enter a number to search: "))
if search_number in numbers:
    print("Element found.")
else:
    print("Element not found.")

if numbers:
    numbers.sort()
    print(f"Sorted elements: {numbers}")

    print(f"Maximum element: {max(numbers)}")

    index = int(input("Enter index to delete: "))

    if 0 <= index < len(numbers):
        numbers.pop(index)
        print(f"List after deletion: {numbers}")
    else:
        print("Invalid index.")

    if numbers:
        index = int(input("Enter index to change: "))

        if 0 <= index < len(numbers):
            new_value = int(input("Enter new value: "))
            numbers[index] = new_value
            print(f"List after modification: {numbers}")
        else:
            print("Invalid index.")