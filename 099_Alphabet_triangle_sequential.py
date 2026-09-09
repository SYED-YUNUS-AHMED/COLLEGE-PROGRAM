# 99. Alphabet triangle (sequential): A / A B / A B C
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    row = " ".join(chr(65 + j) for j in range(i))
    print(row)