# 41. Clock angle between hour and minute hands
hour = int(input("Enter hour (1-12): "))
minute = int(input("Enter minute (0-59): "))
hour_angle = (hour % 12) * 30 + minute * 0.5
minute_angle = minute * 6
angle = abs(hour_angle - minute_angle)
angle = min(angle, 360 - angle)
print("Angle between hands:", angle)