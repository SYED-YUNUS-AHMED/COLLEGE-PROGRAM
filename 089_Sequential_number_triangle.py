# 89. Sequential number triangle
n = int(input("Enter number of rows: "))
num = 1
for i in range(1, n + 1):
    row = ""
    for j in range(i):
        row += str(num) + " "
        num += 1
    print(row)