
def computepay(hours, rate):
    if hours > 40.0:
        bonus = 1.5
        regular_hours = 40.0
        bonus_hours = hours - regular_hours
        hours = regular_hours + bonus_hours * bonus
    return rate * hours

hours = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
print("Pay", computepay(hours, rate))