# 34. Roots of a quadratic equation
import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = b**2 - 4*a*c
if d > 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print("Real and distinct roots:", r1, r2)
elif d == 0:
    r1 = -b / (2*a)
    print("Real and equal root:", r1)
else:
    real = -b / (2*a)
    imag = math.sqrt(-d) / (2*a)
    print(f"Imaginary roots: {real} + {imag}i and {real} - {imag}i")