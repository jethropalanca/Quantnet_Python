'''
This tests logging by combining timer and loan functionalities.
'''

from Exercise_4_2.Exercise_4_2_3_to_4.Loan_Package.loan_types import VariableRateLoan, FixedRateLoan
from Exercise_4_2.Exercise_4_2_3_to_4.Loan_Package.loan import Loan
from Exercise_4_2.Exercise_4_2_3_to_4.Loan_Package.auto_loan import autoLoan
from Exercise_4_2.Exercise_4_2_3_to_4.Loan_Package.house_base import HouseBase
from Exercise_4_2.Exercise_4_2_3_to_4.Loan_Package.loan_pool import LoanPool
from Exercise_4_2.Exercise_4_2_3_to_4.Loan_Package.variable_mortgage import VariableMortgage
from Exercise_4_2.Exercise_4_2_3_to_4.Loan_Package.car import Car
from Exercise_4_2.Exercise_4_2_3_to_4.Timer.Timer_Package.Timer import Timer
import logging



####################### Test Functions #######################

def testPrints(assetInput, loanInput, t):
    '''
    This initialization function to initialize a FixedMortgage class.
    :param assetInput: instantiated Asset
    :param loanInput: instantiated Loan
    :param t: time
    '''

    # For testing code: Instead of retyping everything again and again.

    logging.info('\n(a) Test Recovery Value:')
    logging.info(f'Recovery Value at (t = 0) = {loanInput.recoveryValue(0)} is equal to Manual Calculation .6 x {assetInput.value(0)} = .6 * {assetInput.value(0)}.')
    logging.info(f'Recovery Value = {loanInput.recoveryValue(t)}.')
    logging.info(f'\t* Value at time {t}: {assetInput.value(t)}.')
    logging.info(f'\t* Manual Calculation (Value above * 6) = {assetInput.value(t) * 0.6}.')

    logging.info('\n(b) Test Equity:')
    logging.info(f'Equity = {loanInput.equity(0)} is equal to Manual Calculation (At time 0 = Asset Value - Loan Balance), {assetInput.value(0)} - {loanInput.balance(0)}.')
    logging.info(f'Equity = {loanInput.equity(t)}.')

    logging.info(f'\t* Asset Value at time {t}: {assetInput.value(t)}.')
    logging.info(f'\t* Loan Balance at time {t}: {loanInput.balance(t)}.')
    logging.info(f'\t* Manual Calculation = {assetInput.value(t) - loanInput.balance(t)}.')

    logging.info('\n#################################################################################################################################################################################')

####################### Test Function #######################



def main():

    logging.basicConfig(format='%(message)s', level=logging.DEBUG) # Set level of logging -> INFO

    ########################################################
    ######### Test: Where it all comes together v3 #########
    ########################################################

    logging.info('\nPart 1:')
    logging.info('(*) Test Recursive Functions:')

    # Set t
    t = 15

    # 1 Asset Spec
    car = Car(100000)

    #2 Loan Spec
    try:
        loan = Loan(5, 0.05, 50000, car)

    except ValueError as wrongInput:
        logging.info(f'Error: {wrongInput}')
        logging.error(ValueError)

    except TypeError as wrongAssetType:
        logging.info(f'Error: {wrongAssetType}')
        logging.error(TypeError)

    except Exception as errorGeneral:
        logging.info(f'Exception: {errorGeneral}')
        logging.exception(Exception)

    else:
        logging.getLogger().setLevel(logging.INFO)  # Prevent recursion from showing all debug logs

        for i in ['seconds', 'minutes', 'hours']:
            logging.info(f'\n\nTesting the timer if Configure Display = {i.upper()}')

            # Time PROCESS 1
            try:
                with Timer('myTimer') as timer:
                    timer.configureTimerDisplay(i)
                    # Balance Outstanding at t-1
                    logging.info(f'\nBalance Outstanding (t=0): {loan.balanceRecursive(0)}')
                    logging.info(f'\nBalance Outstanding Recursive at t: {loan.balanceRecursive(t)}')
                    logging.info(f'Balance Outstanding (formula) at t: {loan.balance(t)}')

            except ValueError as errorValue:
                logging.info(
                    'Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.')
                logging.info(f'Exception: {errorValue}')

            except Exception as errorGeneral:
                logging.info(
                    'Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.')
                logging.info(f'Exception: {errorGeneral}')

            # Time PROCESS 2
            try:
                with Timer('myTimer') as timer:
                    timer.configureTimerDisplay(i)
                    # Interest Due at time t:
                    logging.info(f'\nInterest Due (t=0): {loan.interestDueRecursive(0)}')
                    logging.info(f'\nInterest Due Recursive at t: {loan.interestDueRecursive(t)}')
                    logging.info(f'Interest Due (formula) at t: {loan.interestDue(t)}')

            except ValueError as errorValue:
                logging.info(
                    'Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.')
                logging.info(f'Exception: {errorValue}')

            except Exception as errorGeneral:
                logging.info(
                    'Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.')
                logging.info(f'Exception: {errorGeneral}')

            # Time PROCESS 3
            try:
                with Timer('myTimer') as timer:
                    timer.configureTimerDisplay(i)
                    # Principal Due at time t:
                    logging.info(f'\nPrincipal Due (t=0): {loan.principalDueRecursive(0)}')
                    logging.info(f'\nPrincipal Due Recursive at t: {loan.principalDueRecursive(t)}')
                    logging.info(f'Principal Due (Formula) at t: {loan.principalDue(t)}')

            except ValueError as errorValue:
                logging.info(
                    'Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.')
                logging.info(f'Exception: {errorValue}')

            except Exception as errorGeneral:
                logging.info(
                    'Please enter either seconds, minutes, or hours only. Please note that these are case-sensitive.')
                logging.info(f'Exception: {errorGeneral}')


    logging.getLogger().setLevel(logging.DEBUG) # Set to debug again
    logging.info('\n\nPart 2:')
    logging.info('ERROR-HANDLING VERSION:')
    logging.info('This program: Tests (1) Recovery Value, (2) Equity, after instantiating all of the loans above.')
    logging.info('Logging has been set to debug to show illustrate how the loan formulas work.')

    ##############################
    logging.info('\n####################')
    logging.info('Test 1: Ordinary Run')
    logging.info('####################')

    logging.info('\n(1) Base Loan and Car:')

    # 1 Asset Spec
    car = Car(100000)

    #2 Loan Spec
    try:
        baseLoan = Loan(5, 0.05, 50000, car)
    except ValueError as wrongInput:
        logging.info(f'Error: {wrongInput}')
        logging.error(ValueError)
        logging.info('\n#################################################################################################################################################################################')

    except TypeError as wrongAssetType:
        logging.info(f'Error: {wrongAssetType}')
        logging.error(TypeError)
        logging.info('\n#################################################################################################################################################################################')

    except Exception as errorGeneral:
        logging.info(f'Exception: {errorGeneral}')
        logging.exception(Exception)
        logging.info('\n#################################################################################################################################################################################')


    else:
        testPrints(car, baseLoan, 10)






    ##############################
    logging.info('Steps already shown: in the first example, setting logs back to INFO...')
    logging.getLogger().setLevel(logging.INFO)

    logging.info('\nTest 2: Test when Loan object entered to a Loan Class and not an asset.')
    logging.info('\n(2) varLoan and baseLoan:')

    # Asset Spec (Supposedly)
    logging.info('Initialize varLoan...')
    varLoan = VariableRateLoan(30, {5: 0.1, 10: 0.11, 15: 0.12, 20: 0.115, 30: 0.105}, 15000000, car)

    # Error-handling: TRY TESTS THE LOAN CLASS
    logging.info('\nError-handling: Use TRY to initialize the base loan Class')
    try:
    # Loan Spec
        baseLoan = Loan(5, 0.05, 50000, varLoan)
    except ValueError as wrongInput:
        logging.info(f'Error: {wrongInput}')
        logging.error(ValueError)
        logging.info('\n#################################################################################################################################################################################')

    except TypeError as wrongAssetType:
        logging.info(f'Error: {wrongAssetType}')
        logging.error(TypeError)
        logging.info('\n#################################################################################################################################################################################')

    except Exception as errorGeneral:
        logging.info(f'Exception: {errorGeneral}')
        logging.exception(Exception)
        logging.info('\n#################################################################################################################################################################################')


    else:
        testPrints(car, baseLoan, 10)

    logging.info('\nComment: Exception-Handling is working well.')




    ##############################
    logging.info('\nTest 3: Test when car is entered in a mortgage.')

    logging.info('\n(3) car and varMortgage:')
    logging.info('Initialize car...')

    # 1 Asset Spec
    car = Car(100000)

    # Error-handling: TRY TESTS THE LOAN CLASS
    logging.info('\nError-handling: Use TRY to initialize the Variable Mortgage Class')
    try:
        varMortgage = VariableMortgage(36, {5: 0.1, 10: 0.11, 15: 0.12, 20: 0.115, 30: 0.105}, 10000000, car)
    except ValueError as wrongInput:
        logging.info(f'Error: {wrongInput}')
        logging.error(ValueError)
        logging.info('\n#################################################################################################################################################################################')

    except TypeError as wrongAssetType:
        logging.info(f'Error: {wrongAssetType}')
        logging.error(TypeError)
        logging.info('\n#################################################################################################################################################################################')

    except Exception as errorGeneral:
        logging.info(f'Exception: {errorGeneral}')
        logging.exception(Exception)
        logging.info('\n#################################################################################################################################################################################')


    else:
        testPrints(car, VariableMortgage, 10)

    logging.info('\nComment: Exception-Handling is working well.')




    ##############################
    logging.info('\nTest 4: Test when HouseBase is entered in an autoLoan.')
    logging.info('\n(4) myMansion and carLoan:')
    logging.info('Initialize carLoan...')

    # 1 Asset Spec
    myMansion = HouseBase(100000000)

    # Error-handling: TRY TESTS THE LOAN CLASS
    logging.info('\nError-handling: Use TRY to initialize the autoLoan Class')
    try:
        carLoan = autoLoan(7, 0.07, 400000, myMansion)
    except ValueError as wrongInput:
        logging.info(f'Error: {wrongInput}')
        logging.error(ValueError)
        logging.info('\n#################################################################################################################################################################################')

    except TypeError as wrongAssetType:
        logging.info(f'Error: {wrongAssetType}')
        logging.error(TypeError)
        logging.info('\n#################################################################################################################################################################################')

    except Exception as errorGeneral:
        logging.info(f'Exception: {errorGeneral}')
        logging.exception(Exception)
        logging.info('\n#################################################################################################################################################################################')


    else:
        testPrints(myMansion, carLoan, 10)

    logging.info('\nComment: Exception-Handling is working well.')




    ##############################
    logging.info('\nSanity Check -- Test 5: Test when car is entered in an autoLoan.')
    logging.info('\n(5) car and carLoan:')
    logging.info('Initialize carLoan...')

    # 1 Asset Spec
    car = Car(100000)

    # Error-handling: TRY TESTS THE LOAN CLASS
    logging.info('\nError-handling: Use TRY to initialize the autoLoan Class')
    try:
        carLoan = autoLoan(7, 0.07, 400000, car)
    except ValueError as wrongInput:
        logging.info(f'Error: {wrongInput}')
        logging.error(ValueError)
        logging.info('\n#################################################################################################################################################################################')

    except TypeError as wrongAssetType:
        logging.info(f'Error: {wrongAssetType}')
        logging.error(TypeError)
        logging.info('\n#################################################################################################################################################################################')

    except Exception as errorGeneral:
        logging.info(f'Exception: {errorGeneral}')
        logging.exception(Exception)
        logging.info('\n#################################################################################################################################################################################')


    else:
        testPrints(car, carLoan, 10)

    logging.info('\nComment: Exception-Handling is working well. After placing the correct asset in carLoan, data is now pulling.')




    ##############################
    logging.info('\nSanity Check -- Test 6: Test when house is entered in an Variable Mortgage.')
    logging.info('\n(6) house and Variable Mortgage:')
    logging.info('Initialize Variable Mortgage...')

    # 1 Asset Spec
    home = HouseBase(1000000)

    # Error-handling: TRY TESTS THE LOAN CLASS
    logging.info('\nError-handling: Use TRY to initialize the Variable Mortgage Class')
    try:
        varMort = VariableMortgage(7, {5: 0.1, 10: 0.11, 15: 0.12, 20: 0.115, 30: 0.105}, 500000, home)
    except ValueError as wrongInput:
        logging.info(f'Error: {wrongInput}')
        logging.error(ValueError)
        logging.info('\n#################################################################################################################################################################################')

    except TypeError as wrongAssetType:
        logging.info(f'Error: {wrongAssetType}')
        logging.error(TypeError)
        logging.info('\n#################################################################################################################################################################################')

    except Exception as errorGeneral:
        logging.info(f'Exception: {errorGeneral}')
        logging.exception(Exception)
        logging.info('\n#################################################################################################################################################################################')


    else:
        testPrints(home, varMort, 10)




    ##############################
    logging.info('VERDICT: Everything is working as intended.')

    logging.info('\n\nTesting new functionalities introduced in 3_2_3 and 3_1_2 for Loan Class')
    logging.info('Will NOT set to debug level logs as the steps are too voluminous...')
    logging.info('This is because the steps for balance/interest/principal at time t will be repeated for n loans entered...')

    ################################
    ## Instantiate LoanPool Class ##
    ################################

    lP = LoanPool()

    # (1) Set up Loan Collection
    logging.info('\nI. Instantiating Loans...')

    logging.info('\n(a) Setting up collection of Loans...')

    lP.loanCollect(Loan(30, 0.05, 100000, Car(100000)))
    lP.loanCollect(Loan(60, 0.03, 200000, Car(100000)))

    logging.info('(a)Setting up collection of Variable Rate Loans...')
    lP.loanCollect(VariableRateLoan(30, {0: 0.03, 5: 0.05, 11: 0.07}, 100000, Car(100000)))

    logging.info('\n(a)Setting up collection of Fixed Rate Loans...')
    lP.loanCollect(FixedRateLoan(30, 0.05, 100000, Car(100000)))


    ##################################
    ## Testing the Iteration Method ##
    ##################################

    logging.info('\nII. Testing the Methods:')
    logging.info('***Testing new iteration functionality:')
    logging.info('Initialize loanList...')

    logging.info(f'Sanity Check for Object Type before testing if it is now an iterable: {type(lP)}')
    for loan in lP:
        logging.info(f'\nLoan Notional: {loan.notional}')
        logging.info(f'Loan Term: {loan.term}')
        logging.info(f'Loan Term: {loan.getRate(5)}') # t used for variable rate loans


    #########################
    ## Testing the Methods ##
    #########################

    logging.info('\n\nII. Testing the Methods:')
    logging.info('***Testing new list functionalities:')
    lPTest = lP.loanList()

    logging.info(f'Print Notional of 2nd Loan in List: {lPTest[2].notional}')
    logging.info(f'Print Balance of 2nd Loan in List: {lPTest[2].balance(0)}')
    logging.info(f'Print Term of 2nd Loan: {lPTest[2].term}')
    logging.info(f'\nTest Get rate Function for use in Balance: {lPTest[2].getRate(15)}')
    logging.info(f'Is the second loan in our list a Variable Rate Loan? {type(lPTest[2]) == VariableRateLoan}')


    # No need to call loanList and assign to variable (can't do list operations here as the class method cannot be used to a list even if it does contain our instantiated loans)
    logging.info('\n(a). Testing the totalPrincipal Method:')
    logging.info(f'Total Principal: {lP.totalPrincipal()}')

    logging.info('\n(b). Testing the totalBalance Method:')
    logging.info(f'Total Balance Remaining at Period 5: {lP.totalBalance(5)}')
    logging.info(f'\nTotal Balance Remaining at Period 700 (Demonstrates max of 0 condition): {lP.totalBalance(700)}') # demonstrates max of 0 condition in return sum balance
    logging.info('\tExplanation: If all balance due < 0, we get a 0. If some loans are still non-zero, we only get the sum of that loan.')

    logging.info('\n(c). Testing the principalDue Method:')
    logging.info(f'Total Principal Due at Period 5: {lP.principalDue(5)}')
    logging.info(f'\nTotal Principal Due at Period 700: {lP.principalDue(700)}')

    logging.info('\n(d). Testing the interestDue Method:')
    logging.info(f'Total Interest Due at Period 5: {lP.interestDue(5)}')
    logging.info(f'\nTotal Interest Due Due at Period 700 (Demonstrates max of 0 condition): {lP.interestDue(700)}') # demonstrates max of 0 condition in return sum balance

    logging.info('\n(e). Testing the paymentDue Method:')
    logging.info(f'Total Payment Due at Period 5: {lP.monthlyPayment(5)}')
    logging.info(f'\nTotal Payment Due at Period 700: {lP.monthlyPayment(700)}')

    logging.info('\n(f). Testing the activeLoanCount Method:')
    logging.info(f'Number of Active Loans at Period 5: {lP.activeLoanCount(5)}')
    logging.info(f'\nNumber of Active Loans at Period 700: {lP.activeLoanCount(700)}')

    logging.info('\n\nIII. Testing Ported-over functionalities:')
    logging.info('I. Test WAM:')
    logging.info(f'WAM = (30*100,000 + 60*200,000 + 30*100,000 + 30*100,000) / 500,000 = 42, CHECK: {lP.waMCalculate()}')
    logging.info('\nII. Test WAR:')
    logging.info(f'WAR = (0.05*100,000 + 0.03*200,000 + 0.05*100,000 + 0.05*100,000) / 500,000 = .042, CHECK: {lP.waRCalculate(5)}')
    logging.info('Another Check: {0: 0.03, 5: 0.05, 11: 0.07}, At period 5, interest rate is 5%, and rate used for third loan is 5%, so good!')



#########################
if __name__ == '__main__':
    main()
