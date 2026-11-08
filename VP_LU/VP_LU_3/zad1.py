n = int(input("Enter an integer: "))
digits = tuple(int(i) for i in str(abs(n)))
reverse_digits = digits[::-1]
print(f"Forward order: {digits}")
print(f"Reverse order: {reverse_digits}")