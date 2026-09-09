# 73. Read numbers until -1, print count and average
count = 0
total = 0
while True:
    n = int(input("Enter a number (-1 to stop): "))
    if n == -1:
        break
    count += 1
    total += n
if count > 0:
    print("Count:", count)
    print("Average:", total / count)
else:
    print("No numbers entered")