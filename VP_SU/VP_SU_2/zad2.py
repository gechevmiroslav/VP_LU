count = int(input("Enter the number of strings: "))
words = []

for i in range(count):
    word = input("Enter a string: ")
    words.append(word)
print(f"Original list: {words}")

longest_word = max(words, key=len)
print(f"Longest string: {longest_word}")
print(f"Length: {len(longest_word)}")

search_word = input("Enter a string to replace: ")
if search_word in words:
    new_word = input("Enter the new string: ")
    index = words.index(search_word)
    words[index] = new_word
    print(f"List after replacement: {words}")
else:
    print("String not found.")

delete_word = input("Enter a string to delete: ")
if delete_word in words:
    words.remove(delete_word)
    print(f"List after deletion: {words}")
else:
    print("String not found.")

new_word = input("Enter a new string to insert: ")
index = int(input("Enter position to insert: "))
if 0 <= index <= len(words):
    words.insert(index, new_word)
    print(f"List after insertion: {words}")
else:
    print("Invalid index.")