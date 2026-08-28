yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
dream_house_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25
amount_saved = 0
monthly_salary = yearly_salary / 12
r = 0.05
monthly_return = r  /12
downpayment = dream_house_cost * portion_down_payment
months = 0

while amount_saved < downpayment:
    amount_saved += amount_saved * monthly_return
    amount_saved += (monthly_salary * portion_saved)
    months += 1
    if months % 6 == 0:
        monthly_salary += monthly_salary * semi_annual_raise
print(months)