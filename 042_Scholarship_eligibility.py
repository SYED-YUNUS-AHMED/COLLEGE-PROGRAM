# 42. Scholarship eligibility
marks = float(input("Enter marks (%): "))
attendance = float(input("Enter attendance (%): "))
income = float(input("Enter family income: "))
if marks >= 75 and attendance >= 80 and income <= 200000:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")