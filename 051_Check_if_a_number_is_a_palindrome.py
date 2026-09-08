# 51. Check if a number is a palindrome
n = int(input("Enter a number: "))
original = n
reversed_num = 0
n = abs(n)
while n > 0:
    reversed_num = reversed_num * 10 + n % 10
    n = n // 10
if abs(original) == reversed_num:
    print("Palindrome")
else:
    print("Not a palindrome")