# 94. Inverted number triangle
n = int(input("Enter number of rows: "))
for i in range(n, 0, -1):
    print(" ".join(str(x) for x in range(1, i + 1)))