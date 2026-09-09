# 63. x^n without using pow/**
x = float(input("Enter x: "))
n = int(input("Enter n: "))
result = 1
for _ in range(abs(n)):
    result *= x
if n < 0:
    result = 1 / result
print("Result:", result)