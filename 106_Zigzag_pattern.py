# 106. Zigzag pattern (simplified 3-row zigzag)
n = int(input("Enter width (e.g. 4): "))
for row in range(3):
    line = ""
    for col in range(n):
        if row == 0 and col % 3 == 0:
            line += "* "
        elif row == 1 and col % 3 == 1:
            line += "* "
        elif row == 2 and col % 3 == 2:
            line += "* "
        else:
            line += "  "
    print(line)