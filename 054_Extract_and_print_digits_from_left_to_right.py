# 54. Extract and print digits from left to right
n = input("Enter a number: ")
for ch in n:
    if ch.isdigit():
        print(ch)