# 14. Check if Kth bit is set
n = int(input("Enter a number: "))
k = int(input("Enter bit position (0-indexed): "))
if (n & (1 << k)) != 0:
    print(f"Bit {k} is set")
else:
    print(f"Bit {k} is not set")