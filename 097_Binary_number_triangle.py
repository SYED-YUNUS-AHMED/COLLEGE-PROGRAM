# 97. Binary number triangle (0 1 0 1 alternating)
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    row = ""
    for j in range(i):
        row += "0 " if j % 2 == 0 else "1 "
    print(row)