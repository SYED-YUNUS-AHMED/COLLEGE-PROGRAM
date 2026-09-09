# 71. Convert decimal to binary
n = int(input("Enter a decimal number: "))
if n == 0:
    print("Binary: 0")
else:
    num = abs(n)
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    print("Binary:", ("-" if n < 0 else "") + binary)