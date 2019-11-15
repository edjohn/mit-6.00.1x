monthlyPaymentRate = 0
startingBalance = balance

while balance > 0:
    for month in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * (annualInterestRate/12))
    if balance > 0:
        monthlyPaymentRate += 10
        balance = startingBalance

print('Lowest Payment:', monthlyPaymentRate)