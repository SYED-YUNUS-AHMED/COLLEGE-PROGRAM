# 49. Sum of digits of a number
n = int(input("Enter a number: "))
n = abs(n)
total = 0
while n > 0:
    total += n % 10
    n = n // 10
print("Sum of digits:", total)