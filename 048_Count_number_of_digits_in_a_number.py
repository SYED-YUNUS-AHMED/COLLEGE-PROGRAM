# 48. Count number of digits in a number
n = int(input("Enter a number: "))
n = abs(n)
count = 0
if n == 0:
    count = 1
while n > 0:
    n = n // 10
    count += 1
print("Number of digits:", count)