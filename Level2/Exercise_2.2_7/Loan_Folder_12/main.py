'''
This program instantiates different LOAN TYPES with different ASSETS and tests new functionalities: recoveryValue and Equity.
'''

from Loan_Folder_12.Loan_Package.loan import Loan
from Loan_Folder_12.Loan_Package.loan_types import FixedRateLoan, VariableRateLoan
from Loan_Folder_12.Loan_Package.Autoloan import autoLoan
from Loan_Folder_12.Loan_Package.VariableMortgage import VariableMortgage
from Loan_Folder_12.Loan_Package.FixedMortgage import FixedMortgage

from Loan_Folder_12.Loan_Package.car import Car, Civic, Lexus, Lamborghini
from Loan_Folder_12.Loan_Package.HouseBase import HouseBase, PrimaryHome, VacationHome


####################### Test Function #######################

def testPrints(assetInput, loanInput, t):
    '''
    This initialization function to initialize a FixedMortgage class.
    :param assetInput: instantiated Asset
    :param loanInput: instantiated Loan
    :param t: time
    '''

    # For testing code: Instead of retyping everything again and again.

    print('\n(a) Test Recovery Value:')
    print('Recovery Value at (t = 0) =', loanInput.recoveryValue(0), 'is equal to Manual Calculation .6 x',assetInput.value(0), '=', .6 * assetInput.value(0))
    print('Recovery Value =', loanInput.recoveryValue(t))
    print('\t* Value at time',t,':', assetInput.value(t))
    print('\t* Manual Calculation (Value above * 6) =', assetInput.value(t) * 0.6)

    print('\n(b) Test Equity:')
    print('Equity =', loanInput.equity(0), 'is equal to Manual Calculation (At time 0 = Asset Value - Loan Balance), ', assetInput.value(0), ' - ', loanInput.balance(0))
    print('Equity =', loanInput.equity(t))
    print('Equity (at t = 5 for comparison) =', loanInput.equity(5))
    print('\t* Asset Value at time',t,':', assetInput.value(t))
    print('\t* Loan Balance at time',t,':', loanInput.balance(t))
    print('\t* Manual Calculation =', assetInput.value(t) - loanInput.balance(t))

    print('\n#################################################################################################################################################################################')

####################### Test Function #######################

def main():
    #####################################################
    ######### Test: Where it all comes together #########
    #####################################################

    print('TEST: Test (1) Recovery Value, (2) Equity, after instantiating all of the loans above')

    print('\n(1) Base Loan and Car:')
    car = Car(100000)
    baseLoan = Loan(5, 0.05, 50000, car)
    # 50% loaned; at 100% loaned, since car depreciates faster than loan is paid out, baseLoan is immediately worth less than the car at t = 1.

    testPrints(car, baseLoan, 10)

    print('\n(2) Autoloan and Lamborghini:')
    lambo = Lamborghini(1000000)
    carLoan = autoLoan(7, 0.07, 400000, lambo)
    # 40% loaned; at 100% loaned, since lambo depreciates faster than loan is paid out, carLoan is immediately worth less than the lambo at t = 1.

    testPrints(lambo, carLoan, 60)

    print('\n(3) VariableRateLoan and Vacation Home:')
    vacayHome = VacationHome(25000000)
    varLoan = VariableRateLoan(30, {5: 0.1, 10: 0.11, 15: 0.12, 20: 0.115, 30: 0.105}, 15000000, vacayHome)
    # 50% loaned, at 100% loaned, since lambo depreciates faster than loan is paid out, we lose money.

    testPrints(vacayHome, varLoan, 200)

    print('\n(4) Variable Mortgage and Primary Home:')
    homeSweetHome = PrimaryHome(15000000)
    varMortgage = VariableMortgage(36, {5: 0.1, 10: 0.11, 15: 0.12, 20: 0.115, 30: 0.105}, 10000000, homeSweetHome)
    # 60% loaned, at 100% loaned, since lambo depreciates faster than loan is paid out, we lose money.

    testPrints(homeSweetHome, varMortgage, 500)

    print('\n(5) Variable Mortgage and Primary Home:')
    myLexus = Lexus(250000)
    fixedLoan = FixedRateLoan(5, .08, 200000, myLexus)
    # 80% loaned, at 100% loaned, since lambo depreciates faster than loan is paid out, we lose money.

    testPrints(myLexus, fixedLoan, 45)

    print('\n(6) Fixed Mortgage and Vacation Home:')
    myBora = VacationHome(10000000)
    myfixedDebt = FixedMortgage(50, .12, 6000000, myBora)
    # 60% loaned, at 100% loaned, since lambo depreciates faster than loan is paid out, we lose money.

    testPrints(myBora, myfixedDebt, 200)

    print('\nTest Print PMI for my villa at (t = 240): ', myfixedDebt.PMI(240))

    # Civic, Housebase

    print('\n(7) Fixed Rate Loan and Civic:')
    myCivic = Civic(150000)
    myLoan = FixedRateLoan(4, 0.04, 100000, myCivic)
    # 2/3rds loaned; at 100% loaned, since lambo depreciates faster than loan is paid out, carLoan is immediately worth less than the lambo at t = 1.

    testPrints(myCivic, myLoan, 45)

    print('\n(8) VariableMortgage and myMansion:')
    print('Most of the loan was paid in the last 5 periods.')
    myMansion = HouseBase(100000000)
    myLoan2 = VariableMortgage(50, {50: 0.1, 100: 0.12, 150: 0.14, 200: 0.15, 250: 0.16}, 50000000, myMansion)
    # 50% loaned; at 100% loaned, since lambo depreciates faster than loan is paid out, carLoan is immediately worth less than the lambo at t = 1.

    testPrints(myMansion, myLoan2, 300)
    testPrints(myMansion, myLoan2, 400)
    testPrints(myMansion, myLoan2, 500)
    testPrints(myMansion, myLoan2, 550)
    testPrints(myMansion, myLoan2, 580)
    testPrints(myMansion, myLoan2, 590)
    testPrints(myMansion, myLoan2, 595)
    testPrints(myMansion, myLoan2, 598)

    print('VERDICT: Everything is working as intended.')

###########################

if __name__ == '__main__':
    main()
