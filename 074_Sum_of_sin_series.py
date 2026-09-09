# 74. Sum of sin series: x - x^3/3! + x^5/5! - x^7/7! ...
x = float(input("Enter x (in radians): "))
n = int(input("Enter number of terms: "))
total = 0
sign = 1
for i in range(n):
    power = 2 * i + 1
    fact = 1
    for j in range(1, power + 1):
        fact *= j
    total += sign * (x ** power) / fact
    sign *= -1
print("Sum:", total)