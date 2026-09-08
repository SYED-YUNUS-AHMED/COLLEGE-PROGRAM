# 12. Swap two numbers using XOR
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a = a ^ b
b = a ^ b
a = a ^ b
print("After swap: a =", a, ", b =", b)