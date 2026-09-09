# 100. Reverse alphabet triangle: A B C D / A B C / A B / A
n = int(input("Enter number of rows: "))
for i in range(n, 0, -1):
    row = " ".join(chr(65 + j) for j in range(i))
    print(row)