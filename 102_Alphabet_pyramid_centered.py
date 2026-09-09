# 102. Alphabet pyramid (centered): A / A B A / A B C B A
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    left = [chr(65 + j) for j in range(i)]
    full = left + left[-2::-1]
    print(" " * (n - i) + " ".join(full))