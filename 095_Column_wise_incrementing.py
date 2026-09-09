# 95. Column-wise incrementing
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print(" ".join(str(x) for x in range(1, i + 1)))