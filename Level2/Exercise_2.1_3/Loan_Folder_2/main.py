'''
This program tests the loan class functions.
'''

from Loan_Package.loan import Loan
from Timer_Package.Timer import Timer


def main():
    print('\n2.1_2 Test')

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
    loan = Loan(0, .05, 100000)

    # Monthly Payment
    print('Monthly Payment:', loan.monthlyPayment())

    # Total Payment
    print('Total Payment:', loan.totalPayments())

    # Total Interest
    print('Total Interest:', loan.totalInterest())

    # Monthly Payment
    print('Monthly Payment:', loan.monthlyPayment())

    print('\n\n2.1_3 Test')
    # Instantiate loan
    loan = Loan(30, .05, 100000)

    print('\nInitial Testing:')

    print('\n(a) Error-Trapping / Set Min or Max to prevent non-sensical values at expiry of loan:')
    print('Balance Outstanding:', loan.balance(362))

    # Interest Due at time t:
    print('Interest Due:', loan.interestDue(362))

    # Principal Due at time t:
    print('Principal Due:', loan.principalDue(362))

    t = Timer()

    print('Test with paid periods = 10.')

    # Test class functionalities
    # Functions using math formulas:
    print('Demonstrating loan methods using math formulas:')

    print('t = 15:')
    t.start()
    # Balance Outstanding at t-1
    print('Balance Outstanding:', loan.balance(15))

    # Interest Due at time t:
    print('Interest Due:', loan.interestDue(15))

    # Principal Due at time t:
    print('Principal Due:', loan.principalDue(15))
    t.end()
    print(t.retrieveLastResult())

    # Functions employing recursion:
    print('\nDemonstrating loan methods using recursion:')

    t.start()
    # Balance Outstanding at t-1
    print('Balance Outstanding:', loan.balanceRecursive(15))

    # Interest Due at time t:
    print('Interest Due:', loan.interestDueRecursive(15))

    # Principal Due at time t:
    print('Principal Due:', loan.principalDueRecursive(15))
    t.end()
    print(t.retrieveLastResult())

    print('\nRecursion is slower.')

    print('\n\nTest with paid periods = 20.')
    # Test class functionalities
    # Functions using math formulas:
    print('Demonstrating loan methods using math formulas:')

    t.start()
    # Balance Outstanding at t-1
    print('Balance Outstanding:', loan.balance(20))

    # Interest Due at time t:
    print('Interest Due:', loan.interestDue(20))

    # Principal Due at time t:
    print('Principal Due:', loan.principalDue(20))
    t.end()
    print(t.retrieveLastResult())

    # Functions employing recursion:
    print('\nDemonstrating loan methods using recursion:')

    t.start()
    # Balance Outstanding at t-1
    print('Balance Outstanding:', loan.balanceRecursive(20))

    # Interest Due at time t:
    print('Interest Due:', loan.interestDueRecursive(20))

    # Principal Due at time t:
    print('Principal Due:', loan.principalDueRecursive(20))
    t.end()
    print(t.retrieveLastResult())

    print('\nNote: Testing at more than 30 periods already took more than 5 minutes for recursion. For 25 periods, recursion took 60+ seconds vs. nil for formula-based methods. Recursion is '
          'exponentially slower as periods increase.')


###########################

if __name__ == '__main__':
    main()
