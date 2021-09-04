'''
PORTED OVER FROM 2.2.5 This program tests the new WAM and WAR.
'''

from Exercise_3_1.Exercise_3_1_2.loan_types import VariableRateLoan, FixedRateLoan
from Exercise_3_1.Exercise_3_1_2.loan import Loan
from Exercise_3_1.Exercise_3_1_2.LoanPool import LoanPool
from math import prod
from functools import reduce

# (1) Modify WAM and WAR from Exercise 1.5.8

#####################################
################ WAM ################
#####################################

# Sum Function that allows to take in new values iteratively, for waM Calculate (reduce version)
def reduce_sum(self, accumulator, new_value):
    return accumulator + prod(new_value)


# Functions ported over from Homework 1
def waMCalculate(self):
    '''
    This function calculates the weighted average maturity. It uses the reduce function with a REGULAR function as its callable.
    LoanPool waMCalculate has been modified accordingly.
    This has been reflected in LoanPool.py
    '''

    # Version 3: Post - AP Comments
    lList = self.loanList()
    total = reduce(self.reduce_sum,
                   zip([lList[i].notional for i in range(len(lList))], [lList[i].term for i in range(len(lList))]),
                   0)

    totalNotional = self.totalPrincipal()
    return total / totalNotional


#####################################
################ WAR ################
#####################################

def waRCalculate(self, t):
    '''
    This function calculates the weighted average rate. A period input is included to account for variable rate loans.
    It uses the reduce function with a lambda function as its callable.
    This has been reflected in LoanPool.py
    '''

    lList = self.loanList()
    total = reduce(lambda total, faceRate: total + (faceRate[0] * faceRate[1]),
                   zip([lList[i].notional for i in range(len(lList))],
                       [lList[i].getRate(t) for i in range(len(lList))]),
                   0)

    totalNotional = self.totalPrincipal()
    return total / totalNotional


# (2) Test formulas
def main():

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
    # print('\tExplanation: Monthly Pay remains constant throught the term of the loans.'). Not true because at different periods, VariableRateLoan might pay higher.

    print('\n(f). Testing the activeLoanCount Method:')
    print('Number of Active Loans at Period 5:', lP.activeLoanCount(5))
    print('Number of Active Loans at Period 700:', lP.activeLoanCount(700))

    print('\n\nIII. Testing Ported-over functionalities:')
    print('I. Test WAM:')
    print('WAM = (30*100,000 + 60*200,000 + 30*100,000 + 30*100,000) / 500,000 = 42, CHECK:',lP.waMCalculate())
    print('\nII. Test WAR:')
    print('WAM = (0.05*100,000 + 0.03*200,000 + 0.05*100,000 + 0.05*100,000) / 500,000 = .042, CHECK:', lP.waRCalculate(5))
    print('Another Check: {0: 0.03, 5: 0.05, 11: 0.07}, At period 5, interest rate is 5%, and rate used for third loan is 5%, so good!')



#########################
if __name__ == '__main__':
    main()
