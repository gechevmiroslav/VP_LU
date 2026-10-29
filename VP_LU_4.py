print("zad1")
sentence = input("Enter a sentence: ")
words = sentence.lower().split()
unique_words = set(words)
sorted_unique_words = sorted(unique_words)
print("Number of unique words:", len(unique_words))
print("Unique words:", sorted_unique_words)

print()
print("zad2")
text = input("Enter a text: ")
char_count = {}
for char in text:
    if char != " ":
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
if char_count:
    most_common = max(char_count, key = char_count.get)
    print("Most common character:", most_common)
    print("Number of occurrences:", char_count[most_common])
else:
    print("No characters found.")

print()
print("zad3")
words = input("Enter words separated by spaces: ").split()
k = int(input("Enter k: "))
result = []
for word in words:
    if len(word) >= k:
        result.append(word)
result = tuple(result)
print("Filtered words:", result)

print()
print("zad4")
contacts = {}
for i in range(3):
    name = input("Enter name: ")
    phone = input("Enter phone nuumber: ")
    contacts[name] = phone
search_name = input("Enter name to search: ")
if search_name in contacts:
    print("Phone number: ", contacts[search_name])
else:
    print("Contact not found.")

print()
print("zad5")
numbers = input("Enter numbers separated by spaces: ").split()
numbers = [int(number) for number in numbers]
new_list = []
for number in numbers:
    if number not in new_list:
        new_list.append(number)
print("Original list:", numbers)
print("List without duplicates:", new_list)