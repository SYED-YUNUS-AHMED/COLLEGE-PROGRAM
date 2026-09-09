# 68. Largest and smallest digit in a number
n = input("Enter a number: ")
digits = [int(d) for d in n if d.isdigit()]
print("Largest digit:", max(digits))
print("Smallest digit:", min(digits))