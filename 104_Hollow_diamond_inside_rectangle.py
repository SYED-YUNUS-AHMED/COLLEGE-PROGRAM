# 104. Hollow diamond inside rectangle - simplified as hollow diamond
n = int(input("Enter size (odd number, e.g. 5): "))
mid = n // 2
for i in range(n):
    dist = abs(mid - i)
    spaces = dist
    stars = n - 2 * dist
    row = " " * spaces
    for j in range(stars):
        if j == 0 or j == stars - 1 or i == 0 or i == n - 1:
            row += "*"
        else:
            row += " "
    print(row)