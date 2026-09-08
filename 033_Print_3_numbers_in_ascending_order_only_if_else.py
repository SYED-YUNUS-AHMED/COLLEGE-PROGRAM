# 33. Print 3 numbers in ascending order (only if-else)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a <= b and a <= c:
    small = a
    mid = b if b <= c else c
    large = c if b <= c else b
elif b <= a and b <= c:
    small = b
    mid = a if a <= c else c
    large = c if a <= c else a
else:
    small = c
    mid = a if a <= b else b
    large = b if a <= b else a
print("Ascending order:", small, mid, large)