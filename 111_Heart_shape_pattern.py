n = 6  # controls size
for i in range(n // 2, n + 1, 2):
    row = " " * (n - i) + "* " * (i // 2) + "  " * (n - i) + "* " * (i // 2)
    print(row)
for i in range(n, -1, -1):
    print(" " * (n - i) + "* " * i)