# 38. Armstrong number check (3-digit)
n = int(input("Enter a 3-digit number: "))
s = str(n)
total = sum(int(d) ** len(s) for d in s)
if total == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
    