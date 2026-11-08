count = int(input("Enter the number of elements: "))
set1 = set()
set2 = set()
print("Enter elements for the first set:")
for i in range(count):
    number = int(input("Enter a number: "))
    set1.add(number)
print("Enter elements for the second set:")
for i in range(count):
    number = int(input("Enter a number: "))
    set2.add(number)
print(f"First set: {set1}")
print(f"Second set: {set2}")

print("Size of first set:", len(set1))
print("Size of second set:", len(set2))

print("Union:", set1 | set2)

print("Difference:", set1 - set2)

print("Intersection:", set1 & set2)

number = int(input("Enter a number to remove from the first set: "))
if number in set1:
    set1.remove(number)
    print("First set after removal:", set1)
else:
    print("Element not found.")

set1.clear()
set2.clear()
print("First set after clearing:", set1)
print("Second set after clearing:", set2)