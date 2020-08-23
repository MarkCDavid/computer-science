portion_down_payment = 0.25
annual_rate = 0.04
monthly_rate = annual_rate / 12.0

annual_salary = float(input("Annual salary: "))
semi_annual_raise = float(input("Semi annual raise: "))
portion_saved = float(input("Portion saved: "))
total_cost = float(input("Cost: "))

monthly_salary = annual_salary / 12.0
down_payment = total_cost * portion_down_payment

current_savings = 0.0
months = 0

while current_savings < down_payment:
    current_savings += current_savings * monthly_rate
    current_savings += monthly_salary * portion_saved
    months += 1
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12.0

print(f"It will take {months} months.")