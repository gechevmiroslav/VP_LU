text = "ab bc ab bd ab be"
count = text.count("ab")
print("Number of occurrences:", count)

text = text.replace("a", "x")
text = text.replace("b", "a")
text = text.replace("x", "b")
print("Result:", text)