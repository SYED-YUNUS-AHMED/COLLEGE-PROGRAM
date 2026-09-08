# 40. ATM withdrawal approval
balance = float(input("Enter current balance: "))
amount = float(input("Enter withdrawal amount: "))
min_balance = 500
if amount <= 0:
    print("Invalid amount")
elif amount % 100 != 0:
    print("Amount must be in multiples of 100")
elif balance - amount < min_balance:
    print("Rejected: minimum balance must be maintained")
else:
    print("Approved. New balance:", balance - amount)