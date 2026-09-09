# 77. Single recursive function: print increasing then decreasing
def increasing_decreasing(n):
    if n == 0:
        return
    print(n)
    increasing_decreasing(n - 1)
    print(n)

n = int(input("Enter N: "))
increasing_decreasing(n)