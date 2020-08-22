hours = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

bonus = 1.5

if hours > 40.0:
    regular_hours = 40.0
    bonus_hours = hours - regular_hours
    print(rate * (regular_hours + bonus_hours * bonus))
else:
    print(hours * rate)