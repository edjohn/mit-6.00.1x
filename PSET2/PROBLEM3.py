startingBalance = balance
monthlyInterestRate = annualInterestRate/12.0
monthlyPaymentLower = startingBalance/12
monthlyPaymentUpper = (balance*((1+monthlyInterestRate)**12))/12.0
epsilon = 0.01

while abs(balance) > epsilon:
    monthlyPaymentRate = (monthlyPaymentLower + monthlyPaymentUpper)/2
    balance = startingBalance
    for month in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    if balance > epsilon:
        monthlyPaymentLower = monthlyPaymentRate
    else:
        monthlyPaymentUpper = monthlyPaymentRate    

print('Lowest Payment:', round(monthlyPaymentRate, 2))