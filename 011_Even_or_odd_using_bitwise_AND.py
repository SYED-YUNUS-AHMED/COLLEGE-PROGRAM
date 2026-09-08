# 11. Even or odd using bitwise AND
n = int(input("Enter a number: "))
if n & 1 == 0:
    print("Even")
else:
    print("Odd")