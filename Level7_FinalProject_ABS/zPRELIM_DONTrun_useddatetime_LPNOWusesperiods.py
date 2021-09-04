'''
TEST RUN when Loan_Package Used DATETIME.

Contains commands that were used to test the functions...
'''

# Created Packages
from Tranche_Package.tranche import tranche
from Tranche_Package.standard_tranche import StandardTranche
from Tranche_Package.structured_securities import StructuredSecurities
from Loan_Package.loan_pool import LoanPool
from Loan_Package.loan import Loan
from Loan_Package.car import Car, Lamborghini, Lexus, Civic
from Loan_Package.house_base import VacationHome

# Python Packages
import logging
import datetime
import Tranche_Package.structured_securities as structure_securities


def main():
    logging.basicConfig(format='%(message)s', level=logging.INFO)  # Set level of logging -> INFO

    #################### VERDICT (7.25.2021): CODE WORKS WELL. TIME TO IMPLEMENT MAIN CODE ####################

    ####################################
    ##### STRUCTURED_SECURITIES.PY #####
    ####################################

    ########## Test 1: 1 Loan ##########

    # Instantiate LP:
    lP = LoanPool()

    # 1 Asset Spec
    car = Car(100000)

    # 2 Loan Spec
    # Dates
    dateTime1 = '2021 July 13'
    dateTime2 = '2026 July 13'
    format = ('%Y %B %d')
    dateTime1 = datetime.datetime.strptime(dateTime1, format)
    dateTime2 = datetime.datetime.strptime(dateTime2, format)

    # Loan Object
    baseLoan = Loan(dateTime1, dateTime2, 0.05, 500000, car)
    lP.loanCollect(baseLoan)

    logging.info('Loan Pool and Loan Objects have been successfully instantiated.')

    ##############
    # Tranches:
    StructSecObject = StructuredSecurities(lP.totalPrincipal())

    # Sequential --
    ## Test 2 Tranches:
    StructSecObject.addTranche('Tranche_1', .75, .04, 'A') # trancheName, notionalPercent, rate, flagInput
    StructSecObject.addTranche('Tranche_2', .25, .07, 'B')

    StructSecObject.flagMode('Sequential') # Test Sequential
    results1 = structure_securities.doWaterfall(lP, StructSecObject) # do Waterfall (Working GOOD. Just need to deal with ERRORS).
    for index in range(len(results1)):
        value = results1[index]
        print(index, value)

    # Pro Rata --
    ## Test 2 Tranches:
    StructSecObject2 = StructuredSecurities(lP.totalPrincipal())

    StructSecObject2.addTranche('Tranche_1', .75, .04, 'A') # trancheName, notionalPercent, rate, flagInput
    StructSecObject2.addTranche('Tranche_2', .25, .07, 'B')

    StructSecObject2.flagMode('Pro Rata') # Pro Rata
    results2 = structure_securities.doWaterfall(lP, StructSecObject2) # do Waterfall (Working GOOD. Just need to deal with ERRORS).
    for index in range(len(results2)):
        value = results2[index]
        print(index, value)

    # Test 2: 5 Loans
    # Instantiate LP:
    lP = LoanPool()

    # 1 Asset Spec
    car = Car(100000)
    lambo = Lamborghini(1000000) # addl asset
    vacay = VacationHome(5000000) # addl asset
    civic = Civic(250000) # addl asset
    lexus = Lexus(300000) # addl asset

    # 2 Loan Spec
    # Dates
    dateTime1 = '2021 July 13'
    dateTime2 = '2026 July 13'
    dateTime3 = '2031 July 13' # addl date
    dateTime4 = '2036 July 13' # addl date
    dateTime5 = '2028 July 13' # addl date
    dateTime6 = '2027 July 13' # addl date

    format = ('%Y %B %d')
    dateTime1 = datetime.datetime.strptime(dateTime1, format)
    dateTime2 = datetime.datetime.strptime(dateTime2, format)
    dateTime3 = datetime.datetime.strptime(dateTime3, format) # addl date (processing)
    dateTime4 = datetime.datetime.strptime(dateTime4, format)  # addl date (processing)
    dateTime5 = datetime.datetime.strptime(dateTime5, format)  # addl date (processing)
    dateTime6 = datetime.datetime.strptime(dateTime6, format)  # addl date (processing)

    # Loan Object
    loan1 = Loan(dateTime1, dateTime2, 0.05, 500000, car)
    loan2 = Loan(dateTime1, dateTime3, 0.05, 500000, lambo)
    loan3 = Loan(dateTime1, dateTime4, 0.05, 500000, vacay)
    loan4 = Loan(dateTime1, dateTime5, 0.05, 500000, civic)
    loan5 = Loan(dateTime1, dateTime6, 0.05, 500000, lexus)

    lP.loanCollect(loan1) # Load
    lP.loanCollect(loan2)  # Load
    lP.loanCollect(loan3)  # Load
    lP.loanCollect(loan4)  # Load
    lP.loanCollect(loan5)  # Load

    logging.info('Loan Pool and Loan Objects have been successfully instantiated.')

    # Sequential --
    ## Test 2 Tranches:
    StructSecObject3 = StructuredSecurities(lP.totalPrincipal())

    StructSecObject3.addTranche('Tranche_1', .75, .04, 'A') # trancheName, notionalPercent, rate, flagInput
    StructSecObject3.addTranche('Tranche_2', .25, .07, 'B')

    StructSecObject3.flagMode('Sequential') # Test Sequential
    results3 = structure_securities.doWaterfall(lP, StructSecObject3) # do Waterfall (Working GOOD. Just need to deal with ERRORS).
    for index in range(len(results3)):
        value = results3[index]
        print(index, value)

    # Pro Rata --
    ## Test 2 Tranches:
    StructSecObject4 = StructuredSecurities(lP.totalPrincipal())

    StructSecObject4 = StructuredSecurities(lP.totalPrincipal())

    StructSecObject4.addTranche('Tranche_1', .75, .04, 'A') # trancheName, notionalPercent, rate, flagInput
    StructSecObject4.addTranche('Tranche_2', .25, .07, 'B')

    StructSecObject4.flagMode('Pro Rata') # Pro Rata
    results4 = structure_securities.doWaterfall(lP, StructSecObject4) # do Waterfall (Working GOOD. Just need to deal with ERRORS).
    for index in range(len(results4)):
        value = results4[index]
        print(index, value)

    #######################################################################################################################################
    ################################################### Previous Tests: TRANCHE Methods ###################################################
    #######################################################################################################################################

    ######################
    ##### TRANCHE.PY #####
    ######################

    # Error Case: WORKS!
    # sampleTranche = tranche(1,0) # Need to assign apt data types

    # Successfully Created a sampleTranche
    logging.info('\n\n\nBase Tranche Test:')
    sampleTranche = tranche(0.05, 1000000)
    logging.info(sampleTranche)

    # Error Case: WORKS!
    # sampleTranche.flagsubLevel('C') # Cannot assign outside A/B
    sampleTranche.flagsubLevel('A')
    logging.info(sampleTranche.subLevel)

    ###############################
    ##### STANDARD_TRANCHE.PY #####
    ###############################

    # Inherit Errors? Still an error
    # samplestdTranche = StandardTranche(1,0)

    # Create a samplestdTranche:
    logging.info('\nStandard Tranche Test:')
    samplestdTranche = StandardTranche(0.05, 1000000)
    logging.info('Rate = 0.05')
    logging.info('Notional = 1000000\n')

    # Get t
    logging.info(samplestdTranche.t)

    # Increase t
    samplestdTranche.increaseTimePeriod()
    logging.info(samplestdTranche.t) # Works

    # Error because t now out of bounds. Modified code so it now works
    logging.info(samplestdTranche.calledmakeintPay[samplestdTranche.t])
    logging.info(samplestdTranche.calledmakeprinPay[samplestdTranche.t])

    # Reset t then test other functions. # Reset Works.
    samplestdTranche.reset()
    logging.info(samplestdTranche.calledmakeintPay[0])
    logging.info(samplestdTranche.calledmakeprinPay[0])

    # Test makePrincipalPayment
    # t = samplestdTranche.t # CANNOT USE VARIABLES
    logging.info(f'\nTest makePrincipalPayment')
    logging.info(f'TEST PERIOD: {samplestdTranche.t}')

    # ERROR TEST: WILL ACCEPT LETTERS, ETC. if functions are used on their own
    # try:
    #     logging.info(f'\nPERIOD: {samplestdTranche.t}')
    #     samplestdTranche.makePrincipalPayment(samplestdTranche.t, 'A', 50000, 0)
    #     logging.info(samplestdTranche.principalPayment[samplestdTranche.t])
    #     logging.info(samplestdTranche.principalDue[samplestdTranche.t])
    #     logging.info(samplestdTranche.principalSF[samplestdTranche.t])
    #     samplestdTranche.increaseTimePeriod()

    # except Exception as generalError:
    #     logging.info('Please enter a either a float/integer for each of the inputs of makeInterestPayment.')
    #     logging.info(f'Exception: {generalError}')

    # 1
    logging.info(f'\nPERIOD: {samplestdTranche.t}')
    # samplestdTranche.makePrincipalPayment(samplestdTranche.t,'A',50000,0)
    # samplestdTranche.makePrincipalPayment(samplestdTranche.t, 50000, 50000, 0) # ERROR correctly triggered.
    # LESSON: REMOVED TRY EXCEPT... WILL CAUSE TWO ERRORS TO APPEAR. BETTER TO DO THE TRY/EXCEPT during implementation
    samplestdTranche.makePrincipalPayment(samplestdTranche.t,50000,50000,0)
    logging.info(samplestdTranche.principalPayment[samplestdTranche.t])
    logging.info(samplestdTranche.principalDue[samplestdTranche.t])
    logging.info(samplestdTranche.principalSF[samplestdTranche.t])
    samplestdTranche.increaseTimePeriod()
    # logging.info(samplestdTranche.increaseTimePeriod()) not like this, will increase time period too
    logging.info(f'Next Period = {samplestdTranche.t}')

    # 2
    logging.info(f'\nPERIOD: {samplestdTranche.t}')
    samplestdTranche.makePrincipalPayment(samplestdTranche.t,50000,50000,0)
    logging.info(samplestdTranche.principalPayment[samplestdTranche.t])
    logging.info(samplestdTranche.principalDue[samplestdTranche.t])
    logging.info(samplestdTranche.principalSF[samplestdTranche.t])
    samplestdTranche.increaseTimePeriod()
    logging.info(f'Next Period = {samplestdTranche.t}')


    # 3
    logging.info(f'\nPERIOD: {samplestdTranche.t}')
    samplestdTranche.makePrincipalPayment(samplestdTranche.t,50000,50000,0)
    logging.info(samplestdTranche.principalPayment[samplestdTranche.t])
    logging.info(samplestdTranche.principalDue[samplestdTranche.t])
    logging.info(samplestdTranche.principalSF[samplestdTranche.t])
    samplestdTranche.increaseTimePeriod()
    logging.info(f'Next Period = {samplestdTranche.t}')

    # ERROR at t = 20. Current Notional is ZERO. NOTIONAL EARLIER is 100k. NOW 0 AT t = 20
    # More Tests:
    # for i in range(100000):
    #     logging.info(f'\nPERIOD: {samplestdTranche.t}')
    #     samplestdTranche.makePrincipalPayment(samplestdTranche.t, 50000, 50000, 0)
    #     logging.info(samplestdTranche.principalPayment[samplestdTranche.t])
    #     logging.info(samplestdTranche.principalDue[samplestdTranche.t])
    #     logging.info(samplestdTranche.principalSF[samplestdTranche.t])
    #     logging.info(samplestdTranche.notionalBalance(samplestdTranche.t))
    #     samplestdTranche.increaseTimePeriod()
    #     logging.info(f'Next Period = {samplestdTranche.t}')

    samplestdTranche.reset()


    # Test makeInterestPayment
    # t = samplestdTranche.t # CANNOT USE VARIABLES
    logging.info(f'\nTest makeInterestPayment')

    # 1
    logging.info(f'\nPERIOD: {samplestdTranche.t}')
    # samplestdTranche.makePrincipalPayment(samplestdTranche.t,'A',50000,0)
    # samplestdTranche.makePrincipalPayment(samplestdTranche.t, 50000, 50000, 0) # ERROR correctly triggered.
    # LESSON: REMOVED TRY EXCEPT... WILL CAUSE TWO ERRORS TO APPEAR. BETTER TO DO THE TRY/EXCEPT during implementation
    samplestdTranche.makeInterestPayment(samplestdTranche.t, 100000)
    logging.info(samplestdTranche.interestPayment[samplestdTranche.t])
    logging.info(samplestdTranche.interestDueVal[samplestdTranche.t])
    logging.info(samplestdTranche.interestShortfall[samplestdTranche.t])
    samplestdTranche.increaseTimePeriod()
    # logging.info(samplestdTranche.increaseTimePeriod()) not like this, will increase time period too
    logging.info(f'Next Period = {samplestdTranche.t}')

    # 2 (BE CAREFUL. Had to initialize self.InterestDueVal before cycling through the if statements else empty dict error)
    logging.info(f'\nPERIOD: {samplestdTranche.t}')
    samplestdTranche.makeInterestPayment(samplestdTranche.t, 100000)
    # samplestdTranche.makeInterestPayment(samplestdTranche.t, 'A') ERROR
    logging.info(samplestdTranche.interestPayment[samplestdTranche.t])
    logging.info(samplestdTranche.interestDueVal[samplestdTranche.t])
    logging.info(samplestdTranche.interestShortfall[samplestdTranche.t])
    samplestdTranche.increaseTimePeriod()
    # logging.info(samplestdTranche.increaseTimePeriod()) not like this, will increase time period too
    logging.info(f'Next Period = {samplestdTranche.t}')

    # More Tests: (LOOKS GOOD)
    # for i in range(100000):
    #     logging.info(f'\nPERIOD: {samplestdTranche.t}')
    #     samplestdTranche.makeInterestPayment(samplestdTranche.t, 100000)
    #     # samplestdTranche.makeInterestPayment(samplestdTranche.t, 'A') ERROR
    #     logging.info(samplestdTranche.interestPayment[samplestdTranche.t])
    #     logging.info(samplestdTranche.interestDueVal[samplestdTranche.t])
    #     logging.info(samplestdTranche.interestShortfall[samplestdTranche.t])
    #     samplestdTranche.increaseTimePeriod()
    #     # logging.info(samplestdTranche.increaseTimePeriod()) not like this, will increase time period too
    #     logging.info(f'Next Period = {samplestdTranche.t}')

    # samplestdTranche.reset()

    # Test notionalBalance... NO CHANGE BECAUSE NO PRIN INPUT.
    # logging.info(f'\nTest notionalBalance')
    # for i in range(5):
    #     logging.info(f'\nPERIOD: {samplestdTranche.t}')
    #     logging.info(samplestdTranche.notionalBalance(samplestdTranche.t))
    #     samplestdTranche.increaseTimePeriod()

    # samplestdTranche.reset()

    # Test interestDue (Cannot loop this, beyond 2nd t = 2, already need to have values for shortfall which it can
    # only have if makeInterestPayment is called...
    # logging.info(f'\nTest interestDue')
    # for i in range(10000):
    #     logging.info(f'\nPERIOD: {samplestdTranche.t}')
    #     logging.info(samplestdTranche.interestDue(samplestdTranche.t))
    #     samplestdTranche.increaseTimePeriod()

    # samplestdTranche.reset()

#########################
if __name__ == '__main__':
    main()