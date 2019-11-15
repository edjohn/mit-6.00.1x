def calculateBalance(balance, annualInterestRate, monthlyPaymentRate, months = 12):
    unpaidBalance = balance - balance * monthlyPaymentRate 
    if months > 0:
        months -= 1
        return calculateBalance(unpaidBalance + annualInterestRate/12*unpaidBalance, annualInterestRate, monthlyPaymentRate, months)
    else:
        return round(balance, 2)

print("Remaining balance: " + str(calculateBalance(balance, annualInterestRate, monthlyPaymentRate)))