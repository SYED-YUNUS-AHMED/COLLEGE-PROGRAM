# 110. Plus (+) pattern
n = int(input("Enter size (odd number, e.g. 5): "))
mid = n // 2
for i in range(n):
    row = ""
    for j in range(n):
        if i == mid or j == mid:
            row += "* "
        else:
            row += "  "
    print(row)