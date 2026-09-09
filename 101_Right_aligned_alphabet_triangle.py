# 101. Right-aligned alphabet triangle: A / A B / A B C / A B C D
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    row = " ".join(chr(65 + j) for j in range(i))
    print(" " * (2 * (n - i)) + row)