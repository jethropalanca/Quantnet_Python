'''
This now tests the new term method.
PORTED OVER FROM 3_1_2 This program tests the loan pool functions.
'''

from Exercise_5_1.Exercise_5_1_6.Loan_Package.loan_types import VariableRateLoan, FixedRateLoan
from Exercise_5_1.Exercise_5_1_6.Loan_Package.loan import Loan
from Exercise_5_1.Exercise_5_1_6.Loan_Package.auto_loan import autoLoan
from Exercise_5_1.Exercise_5_1_6.Loan_Package.house_base import HouseBase
from Exercise_5_1.Exercise_5_1_6.Loan_Package.loan_pool import LoanPool
from Exercise_5_1.Exercise_5_1_6.Loan_Package.variable_mortgage import VariableMortgage
from Exercise_5_1.Exercise_5_1_6.Loan_Package.car import Car

import logging
import datetime


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
    # print('Equity (at t = 5 for comparison) =', loanInput.equity(5)) Removed as it is not useful.
    print('\t* Asset Value at time',t,':', assetInput.value(t))
    print('\t* Loan Balance at time',t,':', loanInput.balance(t))
    print('\t* Manual Calculation =', assetInput.value(t) - loanInput.balance(t))

    print('\n#################################################################################################################################################################################')

####################### Test Function #######################



def main():

    ########################################################
    ######### Test: Where it all comes together v2 #########
    ########################################################
    print('ERROR-HANDLING VERSION:')
    print('This program: Tests (1) Recovery Value, (2) Equity, after instantiating all of the loans above.')

    ##############################
    print('\n####################')
    print('Test 1: Ordinary Run')
    print('####################')

    print('\n(1) Base Loan and Car:')

    # 1 Asset Spec
    car = Car(100000)

    #2 Loan Spec
    try:
        logging.info('DATES entered in the following format: YYYY mmmm dd (e.g. 2021 July 13).')
        dateTime1 = '2021 July 13'
        dateTime2 = '2026 July 13'

        format = ('%Y %B %d')

        logging.debug('\nProcessing BASE DATE...')
        dateTime1 = datetime.datetime.strptime(dateTime1, format)
        logging.debug(f'Value of generated datetime object: {dateTime1}')

        logging.debug('\nProcessing COMPARISON DATE...')
        dateTime2 = datetime.datetime.strptime(dateTime2, format)
        logging.debug(f'Value of generated datetime object: {dateTime2}')

        logging.debug('\nProcessing Loan Object...')
        baseLoan = Loan(dateTime1, dateTime2, 0.05, 50000, car)

    except TypeError as wrongAssetType:
        print(wrongAssetType)
        print('\n#################################################################################################################################################################################')
    except Exception as errorGeneral:
        print(errorGeneral)
    else:
        testPrints(car, baseLoan, 10)


    ##############################
    print('\nTest 2: Test when Loan object entered to a Loan Class and not an asset.')
    print('\n(2) varLoan and baseLoan:')

    # Dates Spec
    logging.info('DATES entered in the following format: YYYY mmmm dd (e.g. 2021 July 13).')
    dateTime1 = '2021 July 13'
    dateTime2 = '2051 July 13'

    format = ('%Y %B %d')

    logging.debug('\nProcessing BASE DATE...')
    dateTime1 = datetime.datetime.strptime(dateTime1, format)
    logging.debug(f'Value of generated datetime object: {dateTime1}')

    logging.debug('\nProcessing COMPARISON DATE...')
    dateTime2 = datetime.datetime.strptime(dateTime2, format)
    logging.debug(f'Value of generated datetime object: {dateTime2}')

    print('Initialize varLoan...')
    varLoan = VariableRateLoan(dateTime1, dateTime2, {5: 0.1, 10: 0.11, 15: 0.12, 20: 0.115, 30: 0.105}, 15000000, car)

    # Error-handling: TRY TESTS THE LOAN CLASS
    print('\nError-handling: Use TRY to initialize the base loan Class')
    try:
    # Loan Spec
        baseLoan = Loan(dateTime1, dateTime2, 0.05, 50000, varLoan)
    except TypeError as wrongAssetType:
        print(wrongAssetType)
        print('\n#################################################################################################################################################################################')
    except Exception as errorGeneral:
        print(errorGeneral)
    else:
        testPrints(car, baseLoan, 10)

    print('\nComment: Exception-Handling is working well.')




    ##############################
    print('\nTest 3: Test when car is entered in a mortgage.')

    print('\n(3) car and varMortgage:')
    print('Initialize car...')

    # 1 Asset Spec
    car = Car(100000)

    # Error-handling: TRY TESTS THE LOAN CLASS
    print('\nError-handling: Use TRY to initialize the Variable Mortgage Class')
    try:
        # Dates Spec
        logging.info('DATES entered in the following format: YYYY mmmm dd (e.g. 2021 July 13).')
        dateTime1 = '2021 July 13'
        dateTime2 = '2057 July 13'

        format = ('%Y %B %d')

        logging.debug('\nProcessing BASE DATE...')
        dateTime1 = datetime.datetime.strptime(dateTime1, format)
        logging.debug(f'Value of generated datetime object: {dateTime1}')

        logging.debug('\nProcessing COMPARISON DATE...')
        dateTime2 = datetime.datetime.strptime(dateTime2, format)
        logging.debug(f'Value of generated datetime object: {dateTime2}')

        varMortgage = VariableMortgage(dateTime1, dateTime2, {5: 0.1, 10: 0.11, 15: 0.12, 20: 0.115, 30: 0.105}, 10000000, car)
    except TypeError as wrongAssetType:
        print(wrongAssetType)
        print('\n#################################################################################################################################################################################')
    except Exception as errorGeneral:
        print(errorGeneral)
    else:
        testPrints(car, VariableMortgage, 10)

    print('\nComment: Exception-Handling is working well.')




    ##############################
    print('\nTest 4: Test when HouseBase is entered in an autoLoan.')
    print('\n(4) myMansion and carLoan:')
    print('Initialize carLoan...')

    # 1 Asset Spec
    myMansion = HouseBase(100000000)

    # Error-handling: TRY TESTS THE LOAN CLASS
    print('\nError-handling: Use TRY to initialize the autoLoan Class')
    try:
        # Dates Spec
        logging.info('DATES entered in the following format: YYYY mmmm dd (e.g. 2021 July 13).')
        dateTime1 = '2021 July 13'
        dateTime2 = '2028 July 13'

        format = ('%Y %B %d')

        logging.debug('\nProcessing BASE DATE...')
        dateTime1 = datetime.datetime.strptime(dateTime1, format)
        logging.debug(f'Value of generated datetime object: {dateTime1}')

        logging.debug('\nProcessing COMPARISON DATE...')
        dateTime2 = datetime.datetime.strptime(dateTime2, format)
        logging.debug(f'Value of generated datetime object: {dateTime2}')
        carLoan = autoLoan(dateTime1, dateTime2, 0.07, 400000, myMansion)

    except TypeError as wrongAssetType:
        print(wrongAssetType)
        print('\n#################################################################################################################################################################################')
    except Exception as errorGeneral:
        print(errorGeneral)
    else:
        testPrints(myMansion, carLoan, 10)

    print('\nComment: Exception-Handling is working well.')




    ##############################
    print('\nSanity Check -- Test 5: Test when car is entered in an autoLoan.')
    print('\n(5) car and carLoan:')
    print('Initialize carLoan...')

    # 1 Asset Spec
    car = Car(1000000)

    # Error-handling: TRY TESTS THE LOAN CLASS
    print('\nError-handling: Use TRY to initialize the autoLoan Class')
    try:
        # Dates Spec
        logging.info('DATES entered in the following format: YYYY mmmm dd (e.g. 2021 July 13).')
        dateTime1 = '2021 July 13'
        dateTime2 = '2028 July 13'

        format = ('%Y %B %d')

        logging.debug('\nProcessing BASE DATE...')
        dateTime1 = datetime.datetime.strptime(dateTime1, format)
        logging.debug(f'Value of generated datetime object: {dateTime1}')

        logging.debug('\nProcessing COMPARISON DATE...')
        dateTime2 = datetime.datetime.strptime(dateTime2, format)
        logging.debug(f'Value of generated datetime object: {dateTime2}')

        carLoan = autoLoan(dateTime1, dateTime2, 0.07, 400000, car)
    except TypeError as wrongAssetType:
        print(wrongAssetType)
        print('\n#################################################################################################################################################################################')
    except Exception as errorGeneral:
        print(errorGeneral)
    else:
        testPrints(car, carLoan, 10)

    print('\nComment: Exception-Handling is working well. After placing the correct asset in carLoan, data is now pulling.')




    ##############################
    print('VERDICT: Everything is working as intended.')




    print('\n\nTesting new functionalities introduced in 3_2_3 and 3_1_2 for Loan Class')

    ################################
    ## Instantiate LoanPool Class ##
    ################################

    lP = LoanPool()

    # (1) Set up Loan Collection
    print('\nI. Instantiating Loans...')

    print('\nSetting up collection of Loans...')

    # Dates Spec
    logging.info('DATES entered in the following format: YYYY mmmm dd (e.g. 2021 July 13).')
    dateTime1 = '2021 July 13'
    dateTime2 = '2051 July 13'
    dateTime3 = '2081 July 13'

    format = ('%Y %B %d')

    logging.debug('\nProcessing DATE1...')
    dateTime1 = datetime.datetime.strptime(dateTime1, format)
    logging.debug(f'Value of generated datetime object: {dateTime1}')

    logging.debug('\nProcessing DATE2...')
    dateTime2 = datetime.datetime.strptime(dateTime2, format)
    logging.debug(f'Value of generated datetime object: {dateTime2}')

    logging.debug('\nProcessing DATE3...')
    dateTime3 = datetime.datetime.strptime(dateTime3, format)
    logging.debug(f'Value of generated datetime object: {dateTime3}')

    lP.loanCollect(Loan(dateTime1, dateTime2, .05, 100000, Car(100000)))
    lP.loanCollect(Loan(dateTime1, dateTime3, 0.03, 200000, Car(100000)))

    print('Setting up collection of Variable Rate Loans...')
    lP.loanCollect(VariableRateLoan(dateTime1, dateTime2, {0: 0.03, 5: 0.05, 11: 0.07}, 100000, Car(100000)))

    print('\nSetting up collection of Fixed Rate Loans...')
    lP.loanCollect(FixedRateLoan(dateTime1, dateTime2, 0.05, 100000, Car(100000)))


    ##################################
    ## Testing the Iteration Method ##
    ##################################

    print('\nII. Testing the Methods:')
    print('***Testing new iteration functionality:')
    print('Initialize loanList...')

    print('Sanity Check for Object Type before testing if it is now an iterable:', type(lP))
    for loan in lP:
        print('\nLoan Notional:', loan.notional)
        print('Loan Term:', loan.term)
        print('Loan Rate:', loan.getRate(5)) # t used for variable rate loans

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
    # print('\tExplanation: Monthly Pay remains constant throught the term of the loans.'). ERRATA: This is not true for Variable rate Class.

    print('\n(f). Testing the activeLoanCount Method:')
    print('Number of Active Loans at Period 5:', lP.activeLoanCount(5))
    print('Number of Active Loans at Period 700:', lP.activeLoanCount(700))

    print('\n\nIII. Testing Ported-over functionalities:')
    print('I. Test WAM:')
    print('WAM = (365*100,000 + 730*200,000 + 365*100,000 + 365*100,000) / 500,000 = 511, CHECK:',lP.waMCalculate())
    print('\nII. Test WAR:')
    print('WAM = (0.05*100,000 + 0.03*200,000 + 0.05*100,000 + 0.05*100,000) / 500,000 = .042, CHECK:', lP.waRCalculate(5))
    print('Another Check: {0: 0.03, 5: 0.05, 11: 0.07}, At period 5, interest rate is 5%, and rate used for third loan is 5%, so good!')

#########################
if __name__ == '__main__':
    main()
