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