# Project available at https://hyperskill.org/projects/90

# Test cases to run in the terminal
''' Test Case 1: Calculating differentiated payments
    python3 loan_calculator.py --type=diff --principal=1000000 --periods=10 --interest=10
    
    Test Case 2: Calculate the annuity payment for a 60-month (5-year) loan with a principal
    amount of 1,000,000 at 10% interest
    python3 loan_calculator.py --type=annuity --principal=1000000 --periods=60 --interest=10

    Test Case 3: Fewer than four arguments are given
    python3 loan_calculator.py --type=diff --principal=1000000 --payment=104000

    Test Case 4: Calculate differentiated payments given a principal of 500,000 over 8 months
     at an interest rate of 7.8%
    python3 loan_calculator.py --type=diff --principal=500000 --periods=8 --interest=7.8

    Test Case 5: Calculate the principal for a user paying 8,722 per month for 120 months (10 years)
     at 5.6% interest
    python3 loan_calculator.py --type=annuity --payment=8722 --periods=120 --interest=5.6

    Test Case 6: Calculate how long it will take to repay a loan with 500,000 principal, 
    monthly payment of 23,000, and 7.8% interest
    python3 loan_calculator.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
'''

import math
import argparse

def differentiated_payments(principal, periods, interest):
    interest = float(interest) / (12 * 100)        # Nominal interest over 12 months

    count = 0
    for m in range(1, periods + 1):
        Dm = principal / periods + interest * (principal - (principal * (m - 1) / periods))  # Month differentiated payment
        print("Month", m,": payment is", math.ceil(Dm))
        count += math.ceil(Dm)
    overpayment = 0
    overpayment = count - principal
    print()
    print("Overpayment =", overpayment)

def annuity_payments(principal, periods, interest):
    interest = float(interest) / (12 * 100)

    payment = math.ceil(principal * (interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1))

    print(f'Your annuity payment = {payment}!')
    overpayment = 0
    overpayment = payment * periods - principal
    print()
    print("Overpayment =", overpayment)

def loan_principal(payment, periods, interest):
    interest = float(interest) / (12 * 100)

    principal = round(payment / ((interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1)))
    overpayment = 0
    overpayment = payment * periods - principal

    print(f'Your loan principal = {principal}!')
    print()
    print("Overpayment =", overpayment)

def periods(principal, payment, interest):
    '''Total number of monthly repayments = number of periods =  number of \ payments
    This is usually the number of months in which repayments will be made.'''
    interest = float(interest) / (12 * 100)

    number_of_months = math.log((payment / (payment - interest * principal)), 1 + interest)
    total_months = math.ceil(number_of_months)
    periods = math.floor(total_months / 12)

    overpayment = payment * total_months - principal
    print(f'It will take {periods} years to repay this loan!')
    print()
    print("Overpayment =", overpayment)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This program calculates differentiated payments\
                                                 based on the user's specified interest\
                                                , number of monthly payments, and loan principal")
    # Write parse.add_argument for each parameter
    parser.add_argument("-t", "--type", help="Enter the type of payment: Differentiated or Annuity", required=True, choices=["annuity", "diff"])
    parser.add_argument("-pl", "--principal", type=int, help="Enter the principal amount")
    parser.add_argument("-ps", "--periods", type=int, help="Enter the total number of monthly repayments")
    parser.add_argument("-pt", "--payment", type=int, help="Enter the amount of monthly payment")
    parser.add_argument("-i", "--interest", type=float, help="Enter the interest rate")

    args = parser.parse_args()

    if args.type == "diff" and (args.principal and args.periods and args.interest):    # Calculates the Monthly Differentiated Payment
        differentiated_payments(args.principal, args.periods, args.interest)
    elif args.type == "annuity" and args.payment is None:    # Calculates Annuity Payment
        annuity_payments(args.principal, args.periods, args.interest)
    elif args.type == "annuity" and (args.payment and args.periods and args.interest):    # Calculates Loan Principal
        loan_principal(args.payment, args.periods, args.interest)
    elif args.type == "annuity" and (args.principal and args.payment and args.interest):    # Caculates Total number of monthly repayments
        periods(args.principal, args.payment, args.interest)
    else:
        print("Incorrect parameters.")
