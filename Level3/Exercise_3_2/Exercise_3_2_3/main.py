'''
PORTED OVER FROM 3_1_2 This program tests the loan pool functions.
'''

from Exercise_3_2.Exercise_3_2_3.loan_types import VariableRateLoan, FixedRateLoan
from Exercise_3_2.Exercise_3_2_3.loan import Loan
from Exercise_3_2.Exercise_3_2_3.LoanPool import LoanPool
from math import prod
from functools import reduce

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
        print('Loan Term:', loan.getRate(5)) # t used for variable rate loans

#########################
if __name__ == '__main__':
    main()
