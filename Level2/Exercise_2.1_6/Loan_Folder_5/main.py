'''
This program tests the asset class functions.
'''

from Loan_Package.loan import Loan
from Loan_Package.Asset import Asset


def main():
    print('\n2.1_6 Test')

    # Initialize Asset
    # asset = Asset(10000), refrain from using variable names similar to function names.
    myAsset = Asset(10000)

    # Returns yearly depreciation rate
    print('Test Annual depreciation function (return 0.1):', myAsset.annualDepr())

    # Returns monthly depreciation rate
    print('Test Monthly depreciation function (return 0.1/12):', myAsset.monthlyDepr())

    # Returns current value of the asset for a given period.
    print('Test asset value function:', myAsset.value(100))

    # Sanity Check - Karandhir @Forum Validation: Returns current value of the asset for a given period.
    print('\nIs this equal to 9044.583741498398?', myAsset.value(12))
    print('Yes.')

    print('\n########################################################')
    print('############ Test Previous Functionalities: ############')
    print('########################################################')

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

    print('\nStill works: at end of term, principal due = final monthly payment')

    print('\nTest with paid periods = 10.')

    # Test class functionalities
    # Functions using math formulas:
    print('Demonstrating loan methods using math formulas:')

    print('t = 15:')

    # Balance Outstanding at t-1
    print('Balance Outstanding:', loan.balance(15))

    # Interest Due at time t:
    print('Interest Due:', loan.interestDue(15))

    # Principal Due at time t:
    print('Principal Due:', loan.principalDue(15))

    # Functions employing recursion:
    print('\nDemonstrating loan methods using recursion:')

    # Balance Outstanding at t-1
    print('Balance Outstanding:', loan.balanceRecursive(15))

    # Interest Due at time t:
    print('Interest Due:', loan.interestDueRecursive(15))

    # Principal Due at time t:
    print('Principal Due:', loan.principalDueRecursive(15))

    print('\n\nTest with paid periods = 20.')
    # Test class functionalities
    # Functions using math formulas:
    print('Demonstrating loan methods using math formulas:')

    # Balance Outstanding at t-1
    print('Balance Outstanding:', loan.balance(20))

    # Interest Due at time t:
    print('Interest Due:', loan.interestDue(20))

    # Principal Due at time t:
    print('Principal Due:', loan.principalDue(20))

    # Functions employing recursion:
    print('\nDemonstrating loan methods using recursion:')

    # Balance Outstanding at t-1
    print('Balance Outstanding:', loan.balanceRecursive(20))

    # Interest Due at time t:
    print('Interest Due:', loan.interestDueRecursive(20))

    # Principal Due at time t:
    print('Principal Due:', loan.principalDueRecursive(20))

    print('\n\n2.1_4 Test')

    # Test class-level methods (Use Class itself without instantiating):
    # Prints Calculated Monthly Payment (Class Method)
    print('Test class-level methods:')
    print('Monthly Payment (Class Method):', Loan.calcMonthlyPmt(30, 0.05, 100000))
    print('Balance at time t (Class Method):', Loan.calcBalance(30, 0.05, 100000, 10))

    # Prints Balance in a given period (Class Function)

    # Test object-level functionalities to see if they still function properly:
    # Instantiate loan
    print('\nCheck rate = 0')
    loan = Loan(30, 0, 100000)  # Sanity check, returns 0.

    # Balance Due at time t:
    print('\nTest if object-level methods still work correctly:')
    print('Monthly Payment:', loan.monthlyPayment())
    print('Balance Outstanding:', loan.balance(5))  # Negative at periods 15+ as loans have now been fully paid. No error-trapping done.

    loan = Loan(30, 0.05, 100000)

    # Balance Due at time t:
    # Functions using math formulas:
    print('\nTest if object-level methods still work correctly:')
    print('Monthly Payment:', loan.monthlyPayment())
    print('Balance Outstanding:', loan.balance(5))

    # Functions using recursion:
    print('\nTest if object-level methods still work correctly:')
    print('Monthly Payment:', loan.monthlyPayment())
    print('Balance Outstanding:', loan.balanceRecursive(5))

    print('Working fine. Recursive and Mathematical - derived Values equal!')

    print('\n2.1_5 Test')

    # Initialize loan
    loan = Loan(30, 0.05, 100000)

    # Test static-level methods:
    print('Test static-level methods:')
    print('Calculated monthly rate:', Loan.monthlyRate(0.05))
    print('Calculated annual rate:', Loan.annualRate(0.004166666666666667))

    print('Checked. Good (Latest re-check: Exercise_2.1_6)')

    # Test if modified functions still work
    print('\nTest if modified functions still work:')

    # Test class functionalities
    # Functions using math formulas:
    print('\nDemonstrating loan methods using math formulas:')

    # Balance Outstanding at t-1
    print('Balance Outstanding:', loan.balance(3))

    # Interest Due at time t:
    print('Interest Due:', loan.interestDue(3))

    # Principal Due at time t:
    print('Principal Due:', loan.principalDue(3))

    # Functions employing recursion:
    print('\nDemonstrating loan methods using recursion:')

    # Balance Outstanding at t-1
    print('Balance Outstanding:', loan.balanceRecursive(3))

    # Interest Due at time t:
    print('Interest Due:', loan.interestDueRecursive(3))

    # Principal Due at time t:
    print('Principal Due:', loan.principalDueRecursive(3))

    print('Checked. Good, still pulling equal values.')

    # Test class-level methods (Use Class itself without instantiating):
    # Prints Calculated Monthly Payment (Class Method)
    print('\nTest class-level methods:')
    print('Monthly Payment (Class Method):', Loan.calcMonthlyPmt(30, 0.05, 100000))
    print('Balance at time t (Class Method):', Loan.calcBalance(30, 0.05, 100000, 10))

    print('Checked. Good, still pulling equal values. (Latest re-check: Exercise_2.1_6)')

    # Prints Balance in a given period (Class Function)

    # Test object-level functionalities to see if they still function properly:
    # Instantiate loan
    loan = Loan(30, 0.05, 100000)

    # Functions using math formulas:
    # Balance Due at time t:
    print('\nTest if object-level methods still work correctly:')
    print('Monthly Payment:', loan.monthlyPayment())
    print('Balance Outstanding:', loan.balance(10))



###########################

if __name__ == '__main__':
    main()
