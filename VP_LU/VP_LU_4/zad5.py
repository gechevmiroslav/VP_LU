numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(number) for number in numbers]
new_list = []
for number in numbers:
    if number not in new_list:
        new_list.append(number)
print("Original list:", numbers)
print("List without duplicates:", new_list)