# 72. Convert binary to decimal
b = input("Enter a binary number: ")
decimal = 0
for digit in b:
    decimal = decimal * 2 + int(digit)
print("Decimal:", decimal)