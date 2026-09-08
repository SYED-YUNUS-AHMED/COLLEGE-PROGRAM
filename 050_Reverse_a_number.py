# 50. Reverse a number
n = int(input("Enter a number: "))
neg = n < 0
n = abs(n)
reversed_num = 0
while n > 0:
    digit = n % 10
    reversed_num = reversed_num * 10 + digit
    n = n // 10
if neg:
    reversed_num = -reversed_num
print("Reversed number:", reversed_num)