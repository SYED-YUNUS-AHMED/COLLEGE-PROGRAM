# 93. Number pyramid (centered): 1 / 1 2 3 / 1 2 3 4 5 ...
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    count = 2 * i - 1
    nums = " ".join(str(x) for x in range(1, count + 1))
    print(" " * (n - i) + nums)