# 67. Armstrong number (generalized for any digits)
n = int(input("Enter a number: "))
s = str(n)
power = len(s)
total = sum(int(d) ** power for d in s)
if total == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")