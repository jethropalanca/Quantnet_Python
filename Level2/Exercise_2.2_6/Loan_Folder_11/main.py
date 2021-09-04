'''
This program tests the methods of the newly-created individual Asset derived classes.
'''

from Loan_Folder_11.Loan_Package.car import Car, Civic, Lamborghini, Lexus
from Loan_Folder_11.Loan_Package.HouseBase import HouseBase, PrimaryHome, VacationHome
from Loan_Folder_11.Loan_Package.Autoloan import autoLoan
from Loan_Folder_11.Loan_Package.loan import Loan
from Loan_Folder_11.Loan_Package.loan_types import VariableRateLoan, FixedRateLoan
from Loan_Folder_11.Loan_Package.Asset import Asset
from Loan_Folder_11.Loan_Package.VariableMortgage import VariableMortgage
from Loan_Folder_11.Loan_Package.FixedMortgage import FixedMortgage
from Loan_Folder_11.Loan_Package.LoanPool import LoanPool

# (2) Test formulas
def main():
    print('#######################')
    print('######## CARS: ########')
    print('#######################')
    print('\nTesting out the annualDepr function of each of the cars:')

    print('Initializing Car, Civic, Lamborhgini, and Nexus...')
    car = Car(250000)
    civic = Civic(60000)
    lexus = Lexus(200000)
    lambo = Lamborghini(1000000)

    print('\nDepreciation:')
    print('Car Depreciation:',car.annualDepr())
    print('Civic Depreciation:',civic.annualDepr())
    print('Lexus Depreciation:',lexus.annualDepr())
    print('Lambo Depreciation:',lambo.annualDepr())

    print('\nValue (t = 48 / 4 years:)')
    print('Car: In 4 Years: From 250,000 to', car.value(48))
    print('Civic: In 4 Years: From 600,000 to', civic.value(48))
    print('Lexus: In 4 Years: From 200,000 to', lexus.value(48))
    print('Lambo: In 4 Years: From 1000,000 to', lambo.value(48))

    print('\n\n######################')
    print('######## HOME:########')
    print('######################')
    print('\nTesting out the annualDepr function of each of the cars:')

    print('HouseBase, PrimaryHome, VacationHome...')
    houseBase = HouseBase(750000)
    pHome = PrimaryHome(800000)
    vHome = VacationHome(1000000)

    print('\nDepreciation:')
    print('House Depreciation:',houseBase.annualDepr())
    print('Primary Home Depreciation:',pHome.annualDepr())
    print('Vacation Home Depreciation:',vHome.annualDepr())

    print('\nValue (t = 48 / 4 years:)')
    print('House: In 4 Years: From 750,000 to', houseBase.value(48))
    print('Primary Home: In 4 Years: From 800,000 to', pHome.value(48))
    print('Vacation Home: In 4 Years: From 1,000,000 to', vHome.value(48))


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
    print('Balance Outstanding:', loan.balance(5))

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

    print('\n2.1_6 Test')
    print('Asset Functions no longer work. Will lead to an error as it is now an abstract class.')
    # Initialize Asset
    # asset = Asset(10000), refrain from using variable names similar to function names.
    # myAsset = Asset(10000)

    # Returns yearly depreciation rate
    # print('Test Annual depreciation function (return 0.1):', myAsset.annualDepr())

    # Returns monthly depreciation rate
    # print('Test Monthly depreciation function (return 0.1/12):', myAsset.monthlyDepr())

    # Returns current value of the asset for a given period.
    # print('Test asset value function:', myAsset.value(100))

    # Sanity Check - Karandhir @Forum Validation: Returns current value of the asset for a given period.
    # print('\nIs this equal to 9044.583741498398?', myAsset.value(12))
    # print('Yes.')

    print('\n2.2_1 Test')

    # Initialize loan
    loan = Loan(30, 0.05, 100000)

    # Test getRate function for instantiated Loan base.
    print('\nTest getRate on instantiated Loan Base:', loan.getRate(None))

    # Test getRate function on Variable Rate Loan
    varLoan = VariableRateLoan(30, {1: 0.03, 5: 0.05, 11: 0.07}, 100000)

    print('\nTest getRate Functions all keys and keys in between to test inference')
    print('Print Interest rate for startKey = 0,', varLoan.getRate(0))
    print('Print Interest rate for startKey = 1,', varLoan.getRate(1))
    print('Print Interest rate for startKey = 2,', varLoan.getRate(2))
    print('Print Interest rate for startKey = 3,', varLoan.getRate(3))
    print('Print Interest rate for startKey = 4,', varLoan.getRate(4))
    print('Print Interest rate for startKey = 5,', varLoan.getRate(5))
    print('Print Interest rate for startKey = 6,', varLoan.getRate(6))
    print('Print Interest rate for startKey = 7,', varLoan.getRate(7))
    print('Print Interest rate for startKey = 8,', varLoan.getRate(8))
    print('Print Interest rate for startKey = 9,', varLoan.getRate(9))
    print('Print Interest rate for startKey = 10,', varLoan.getRate(10))
    print('Print Interest rate for startKey = 11,', varLoan.getRate(11))
    print('Print Interest rate for startKey = 12,', varLoan.getRate(12))

    # Test functionalities in previous files if they still work (using a fixed rate loan):

    print('\nTest old functionalities if they still work using Fixed Rate Loan:')
    fLoan = FixedRateLoan(30, 0.05, 100000)

    # Test static-level methods:
    print('Test static-level methods:')
    print('Calculated monthly rate:', fLoan.monthlyRate(0.05))
    print('Calculated annual rate:', fLoan.annualRate(0.004166666666666667))

    # Test if modified functions still work
    print('\nTest if modified functions still work:')

    # Test class functionalities
    # Functions using math formulas:
    print('\nDemonstrating loan methods using math formulas:')

    # Balance Outstanding at t-1
    print('Balance Outstanding:', fLoan.balance(5))

    # Interest Due at time t:
    print('Interest Due:', fLoan.interestDue(5))

    # Principal Due at time t:
    print('Principal Due:', fLoan.principalDue(5))

    # Functions employing recursion:
    print('\nDemonstrating loan methods using recursion:')

    # Balance Outstanding at t-1
    print('Balance Outstanding:', fLoan.balanceRecursive(5))

    # Interest Due at time t:
    print('Interest Due:', fLoan.interestDueRecursive(5))

    # Principal Due at time t:
    print('Principal Due:', fLoan.principalDueRecursive(5))

    # Test class-level methods (Use Class itself without instantiating):
    # Prints Calculated Monthly Payment (Class Method)
    print('\nTest class-level methods:')
    print('Monthly Payment (Class Method):', fLoan.calcMonthlyPmt(30, 0.05, 100000))
    print('Balance at time t (Class Method):', fLoan.calcBalance(30, 0.05, 100000, 10))

    # Prints Balance in a given period (Class Function)

    # Test object-level functionalities to see if they still function properly:

    # Functions using math formulas:
    # Balance Due at time t:
    print('\nTest if object-level methods still work correctly:')
    print('Monthly Payment:', fLoan.monthlyPayment())
    print('Balance Outstanding:', fLoan.balance(10))

    print('\nTest old functionalities if they still work using Variable Rate Loan:')

    # Test static-level methods:
    print('Test static-level methods:')
    print('Calculated monthly rate:', varLoan.monthlyRate(0.05))
    print('Calculated annual rate:', varLoan.annualRate(0.004166666666666667))

    # Test if modified functions still work
    print('\nTest if modified functions still work:')

    # Test class functionalities
    # Functions using math formulas:
    print('\nDemonstrating loan methods using math formulas:')

    # Balance Outstanding at t-1
    print('Balance Outstanding:', varLoan.balance(5))

    # Interest Due at time t:
    print('Interest Due:', varLoan.interestDue(5))

    # Principal Due at time t:
    print('Principal Due:', varLoan.principalDue(5))

    # Functions employing recursion:
    print('\nDemonstrating loan methods using recursion:')

    # Balance Outstanding at t-1
    print('Balance Outstanding:', varLoan.balanceRecursive(5))

    # Interest Due at time t:
    print('Interest Due:', varLoan.interestDueRecursive(5))

    # Principal Due at time t:
    print('Principal Due:', varLoan.principalDueRecursive(5))

    # Test class-level methods (Use Class itself without instantiating):
    # Prints Calculated Monthly Payment (Class Method)
    print('\nTest class-level methods:')
    print('Monthly Payment (Class Method):', varLoan.calcMonthlyPmt(30, 0.05, 100000))
    print('Balance at time t (Class Method):', varLoan.calcBalance(30, 0.05, 100000, 10))

    # Prints Balance in a given period (Class Function)

    # Test object-level functionalities to see if they still function properly:

    # Functions using math formulas:
    # Balance Due at time t:
    print('\nTest if object-level methods still work correctly:')
    print('Monthly Payment:', varLoan.monthlyPayment(5))
    print('Balance Outstanding:', varLoan.balance(10))

    print('\n Does not port over test code from Exercise 2.2_2 as we already test Fixed Mortgage and Variable Mortgage in this exercise.')

    print('\n2.2_3 Test')
    # Test VariableMortgage

    # Be wary of setting rate to rateDict, else error:
    varMort = VariableMortgage(30, {0: 0.03, 5: 0.05, 11: 0.07}, 100000, 100000)
    print('\n##########################################')
    print('Test some VariableMortgage Functionalities')
    print('##########################################')

    # Test Rate Inference
    print('\nTest getRate Functions all keys and keys in between to test inference')
    print('Print Interest rate for startKey = 0,', varMort.getRate(0))
    print('Print Interest rate for startKey = 1,', varMort.getRate(1))
    print('Print Interest rate for startKey = 2,', varMort.getRate(2))
    print('Print Interest rate for startKey = 3,', varMort.getRate(3))
    print('Print Interest rate for startKey = 4,', varMort.getRate(4))
    print('Print Interest rate for startKey = 5,', varMort.getRate(5))
    print('Print Interest rate for startKey = 6,', varMort.getRate(6))
    print('Print Interest rate for startKey = 7,', varMort.getRate(7))
    print('Print Interest rate for startKey = 8,', varMort.getRate(8))
    print('Print Interest rate for startKey = 9,', varMort.getRate(9))
    print('Print Interest rate for startKey = 10,', varMort.getRate(10))
    print('Print Interest rate for startKey = 11,', varMort.getRate(11))
    print('Print Interest rate for startKey = 12,', varMort.getRate(12))

    # Test PMI
    print('\nPMI adjustment is equal to', varMort.PMI(1))
    print('Monthly Payment is equal to', varMort.monthlyPayment(1))
    print('Since the original payment is 536.82, indeed monthlyPayment function has been modified by PMI ( = 536.82 +',
          varMort.PMI(), '=', varMort.monthlyPayment(0), ').')

    print('\nTest Principal Due after removing effects of PMI that crept in the original function as monthlyPayment (a component) is dependent on this:', varMort.principalDue(0))
    print('Since same as in original principalDue (no additional PMI), PASSED!')

    # Test FixedMortgage

    fixMort = FixedMortgage(30, 0.05, 100000, 100000)
    print('\n#######################################')
    print('Test some FixedMortgage Functionalities')
    print('#######################################')

    # Test PMI
    print('\nPMI adjustment is equal to', fixMort.PMI())
    print('Monthly Payment is equal to', fixMort.monthlyPayment(1))
    print('Since the original payment is 536.82, indeed monthlyPayment function has been modified by PMI ( = 536.82 +',
          fixMort.PMI(), '=', fixMort.monthlyPayment(1), ').')

    print('\nTest Principal Due after removing effects of PMI that crept in the original function as monthlyPayment (a component) is dependent on this:', fixMort.principalDue(1))
    print('Since same as in original principalDue (no additional PMI), PASSED!')

    print('\n2.2_4 Test')
    # Test autoLoan

    carLoan = autoLoan(30, 0.05, 100000)
    print('Initialize autoLoan')

    print('\n#######################################')
    print('Test some autoLoan Functionalities')
    print('#######################################')

    print('\nInitial Testing:')

    print('\n(a) Error-Trapping / Set Min or Max to prevent non-sensical values at expiry of loan:')
    print('Balance Outstanding:', carLoan.balance(362))

    # Interest Due at time t:
    print('Interest Due:', carLoan.interestDue(362))

    # Principal Due at time t:
    print('Principal Due:', carLoan.principalDue(362))

    print('\nStill works: at end of term, principal due = final monthly payment')

    print('\nTest with paid periods = 10.')

    # Test class functionalities
    # Functions using math formulas:
    print('Demonstrating loan methods using math formulas:')

    print('t = 15:')

    # Balance Outstanding at t-1
    print('Balance Outstanding:', carLoan.balance(15))

    # Interest Due at time t:
    print('Interest Due:', carLoan.interestDue(15))

    # Principal Due at time t:
    print('Principal Due:', carLoan.principalDue(15))

    # Functions employing recursion:
    print('\nDemonstrating loan methods using recursion:')

    # Balance Outstanding at t-1
    print('Balance Outstanding:', carLoan.balanceRecursive(15))

    # Interest Due at time t:
    print('Interest Due:', carLoan.interestDueRecursive(15))

    # Principal Due at time t:
    print('Principal Due:', carLoan.principalDueRecursive(15))

    print('\n\nTest with paid periods = 20.')
    # Test class functionalities
    # Functions using math formulas:
    print('Demonstrating loan methods using math formulas:')

    # Balance Outstanding at t-1
    print('Balance Outstanding:', carLoan.balance(20))

    # Interest Due at time t:
    print('Interest Due:', carLoan.interestDue(20))

    # Principal Due at time t:
    print('Principal Due:', carLoan.principalDue(20))

    # Functions employing recursion:
    print('\nDemonstrating loan methods using recursion:')

    # Balance Outstanding at t-1
    print('Balance Outstanding:', carLoan.balanceRecursive(20))

    # Interest Due at time t:
    print('Interest Due:', carLoan.interestDueRecursive(20))

    # Principal Due at time t:
    print('Principal Due:', carLoan.principalDueRecursive(20))


    print('\n2.1_5 Test')

    ################################
    ## Instantiate LoanPool Class ##
    ################################

    lP = LoanPool()

    # (1) Set up Loan Collection
    print('\nI. Instantiating Loans...')

    print('\nSetting up collection of Loans...')

    lP.loanCollect(Loan(30, 0.05, 100000))
    lP.loanCollect(Loan(60, 0.03, 200000))

    print('Setting up collection of Variable Rate Loans...')
    lP.loanCollect(VariableRateLoan(30, {0: 0.03, 5: 0.05, 11: 0.07}, 100000))

    print('\nSetting up collection of Fixed Rate Loans...')
    lP.loanCollect(FixedRateLoan(30, 0.05, 100000))

    #########################
    ## Testing the Methods ##
    #########################

    print('\n\nII. Testing the Methods:')
    print('***Testing new list functionalities:')
    lPTest = lP.loanList()
    print('Print Notional of 2nd Loan in List:', lPTest[2].notional)
    print('Print Balance of 2nd Loan in List:', lPTest[2].balance(0))
    print('Print Term of 2nd Loan:', lPTest[2].term)
    print('Test Get rate Function for use in Balance:', lPTest[2].getRate(15))
    print('Is the second loan in our list a Variable Rate Loan?', type(lPTest[2]) == VariableRateLoan)


    # No need to call loanList and assign to variable (can't do list operations here as the class method cannot be used to a list even if it does contain our instantiated loans)
    print('\n(a). Testing the totalPrincipal Method:')
    print('Total Principal:', lP.totalPrincipal())

    print('\n(b). Testing the totalBalance Method:')
    print('Total Balance Remaining at Period 5:', lP.totalBalance(5))
    print('Total Balance Remaining at Period 700 (Demonstrates max of 0 condition):', lP.totalBalance(700)) # demonstrates max of 0 condition in return sum balance
    print('\tExplanation: If all balance due < 0, we get a 0. If some loans are still non-zero, we only get the sum of that loan.')

    print('\n(c). Testing the principalDue Method:')
    print('Total Principal Due at Period 5:', lP.principalDue(5))
    print('Total Principal Due at Period 700:', lP.principalDue(700))

    print('\n(d). Testing the interestDue Method:')
    print('Total Interest Due at Period 5:', lP.interestDue(5))
    print('Total Interest Due Due at Period 700 (Demonstrates max of 0 condition):', lP.interestDue(700)) # demonstrates max of 0 condition in return sum balance

    print('\n(e). Testing the paymentDue Method:')
    print('Total Payment Due at Period 5:', lP.monthlyPayment(5))
    print('Total Payment Due at Period 700:', lP.monthlyPayment(700))
    print('\tExplanation: Monthly Pay remains constant throught the term of the loans.')

    print('\n(f). Testing the activeLoanCount Method:')
    print('Number of Active Loans at Period 5:', lP.activeLoanCount(5))
    print('Number of Active Loans  Period 700:', lP.activeLoanCount(700))

    print('\n\nIII. Testing Ported-over functionalities:')
    print('I. Test WAR:')
    print('WAM = (30*100,000 + 60*200,000 + 30*100,000 + 30*100,000) / 500,000 = 42, CHECK:',lP.waMCalculate())
    print('WAM = (0.05*100,000 + 0.03*200,000 + 0.05*100,000 + 0.05*100,000) / 500,000 = .042, CHECK:', lP.waRCalculate(5))
    print('Another Check: {0: 0.03, 5: 0.05, 11: 0.07}, At period 5, interest rate is 5%, and rate used for third loan is 5%, so good!')




###########################

if __name__ == '__main__':
    main()
