initial_deposit = float(input("Enter the initial deposit: "))
dream_house_cost = 800000
downpayment = 800000 * 0.25
amount_saved = 0
count = 0

low = 0
high = 1
r = (low + high) / 2
while not((downpayment - 100) < amount_saved < (downpayment + 100)):
    amount_saved = initial_deposit * ((1 + (r/12))**36)
    if amount_saved < (downpayment + 100):
        low = r
    else:
        high = r
    r = (low + high) / 2
    count += 1

print(amount_saved)
print(r)
print(count)