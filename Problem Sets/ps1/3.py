portion_down_payment = 0.25
annual_rate = 0.04
semi_annual_raise = 0.07

total_cost = 1000000
months = 36

down_payment = total_cost * portion_down_payment

annual_salary = float(input("Starting salary: "))



bisection_iterations = 0
guess_a = 0.0
guess_b = 1.0
guess_c = None
while True:

    _current_savings = 0.0
    _annual_salary = annual_salary
    _monthly_salary = _annual_salary / 12.0
    _monthly_rate = annual_rate / 12.0

    guess_c = (guess_a + guess_b)/2.0

    for month in range(months):
        _current_savings += _current_savings * _monthly_rate
        _current_savings += _monthly_salary * guess_c
        if month % 6 == 0:
            _annual_salary += _annual_salary * semi_annual_raise
            _monthly_salary = _annual_salary / 12.0
        
    bisection_iterations += 1
    difference = _current_savings - down_payment
    if abs(difference) <= 100.0:
        break

    if difference < 0:
        guess_a = guess_c
    else:
        guess_b = guess_c

    if abs(guess_a - guess_b) < 0.0001:
        print("It is not possible to pay the down payment in three years.")
        exit()

print("Best savings rate:", guess_c)
print("Steps in bisection search:​", bisection_iterations)
