# 87. Sandglass / Hourglass
n = int(input("Enter number of rows (odd number): "))
for i in range(n, 0, -2):
    print(" " * ((n - i) // 2) + "*" * i)
for i in range(3, n + 1, 2):
    print(" " * ((n - i) // 2) + "*" * i)