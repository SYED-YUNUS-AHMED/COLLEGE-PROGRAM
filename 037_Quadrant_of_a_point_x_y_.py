# 37. Quadrant of a point (x, y)
x = float(input("Enter x: "))
y = float(input("Enter y: "))
if x == 0 and y == 0:
    print("Origin")
elif x == 0:
    print("Lies on Y-axis")
elif y == 0:
    print("Lies on X-axis")
elif x > 0 and y > 0:
    print("Quadrant I")
elif x < 0 and y > 0:
    print("Quadrant II")
elif x < 0 and y < 0:
    print("Quadrant III")
else:
    print("Quadrant IV")