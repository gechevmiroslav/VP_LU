data = (["whale", 1, 3], 5)

data[0][0] = "cat"
data[0].remove(1)
data[0][1] = data[0][1] ** 2
print("Modified tuple:", data)

data[1] = data[1] * 2