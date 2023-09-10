# mortgage.py
#
# Exercise 1.7

principal = 500000
interest = 0.05 
monthly_payment = 2684.11


extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

total_paid = 0
num_month = 0
while principal > 0: 
    num_month += 1
    principal += 0.05/12 * principal
    principal -= monthly_payment
    total_paid += monthly_payment

    if extra_payment_start_month <= num_month and num_month <= extra_payment_end_month: 
        principal -= extra_payment
        total_paid += extra_payment

    #overpayment on last month 
    if principal < 0: 
        total_paid += principal
        principal = 0 

    print(num_month, round(total_paid, 4), round(principal, 4))



print("total paid", round(total_paid, 2))
print("num month", num_month)