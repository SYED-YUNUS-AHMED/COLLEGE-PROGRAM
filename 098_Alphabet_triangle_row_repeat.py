# 98. Alphabet triangle (row repeat): A / B B / C C C
n = int(input("Enter number of rows: "))
for i in range(n):
    letter = chr(65 + i)
    print((letter + " ") * (i + 1))