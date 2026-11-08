count = int(input("Enter the number of words: "))
dictionary = {}
for i in range(count):
    word = input("Enter an English word: ")
    translation = input("Enter the Bulgarian translation: ")
    dictionary[word] = translation

print("Dictionary:")
for word in dictionary:
    print(word, ":", dictionary[word])

new_word = input("Enter a new English word: ")
new_translation = input("Enter its Bulgarian translation: ")
dictionary[new_word] = new_translation
print("Dictionary after adding:", dictionary)

delete_word = input("Enter a word to delete: ")
if delete_word in dictionary:
    del dictionary[delete_word]
    print("Dictionary after deletion:", dictionary)
else:
    print("Word not found.")

search_word = input("Enter a word to search: ")
if search_word in dictionary:
    print("Translation:", dictionary[search_word])
else:
    print("Word not found.")

sorted_dictionary = dict(sorted(dictionary.items()))
print("Sorted dictionary:")
for word in sorted_dictionary:
    print(word, ":", sorted_dictionary[word])