# 23. Time-based greeting
hour = int(input("Enter hour (0-23): "))
if hour < 12:
    print("Good Morning")
elif hour < 17:
    print("Good Afternoon")
elif hour < 21:
    print("Good Evening")
else:
    print("Good Night")