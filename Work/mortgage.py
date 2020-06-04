# mortgage.py
#program that simulates a mortgage payment

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

months = 0

extraPaymentStart = 60
extraPaymentEnd = 108
extraPayment = 1000

while principal > 0:
    if months > extraPaymentStart and months < extraPaymentEnd:
        principal = principal * (1 + rate / 12) - (payment + extraPayment)
        total_paid = total_paid + (payment + extraPayment)
        months += 1
    else:
        principal = principal * (1 + rate / 12) - (payment)
        total_paid = total_paid + (payment)
        months += 1

    if principal < 0:
        principal = 0

    print(months, ' ', principal)

print(f'Total paid {round(total_paid, 2)} Total months {months}')
