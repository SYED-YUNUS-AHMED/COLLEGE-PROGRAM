# 29. Check if a valid triangle can be formed
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))
if a + b > c and b + c > a and a + c > b:
    print("Valid triangle")
else:
    print("Not a valid triangle")