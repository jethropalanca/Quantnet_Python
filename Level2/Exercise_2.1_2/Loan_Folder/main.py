'''
This program tests the loan class functions.
'''

from Loan_Package.loan import Loan


def main():
    # Instantiate loan
    loan = Loan(30, 0.05, 100000)

    # Test class functionalities

    # Monthly Payment
    print('Monthly Payment:', loan.monthlyPayment())

    # Total Payment
    print('Total Payment:', loan.totalPayments())

    # Total Interest
    print('Total Interest:', loan.totalInterest())

    print('\nTest empty rate:')
    loan = Loan(30, 0, 100000)
    # Monthly Payment
    print('Monthly Payment:', loan.monthlyPayment())

    # Total Payment
    print('Total Payment:', loan.totalPayments())

    # Total Interest
    print('Total Interest:', loan.totalInterest())

    print('\nTest empty term:')
    loan = Loan(0, 1.5, 100000)

    # Monthly Payment
    print('Monthly Payment:', loan.monthlyPayment())

    # Total Payment
    print('Total Payment:', loan.totalPayments())

    # Total Interest
    print('Total Interest:', loan.totalInterest())

    # Monthly Payment
    print('Monthly Payment:', loan.monthlyPayment())

#########################
if __name__ == '__main__':
    main()
