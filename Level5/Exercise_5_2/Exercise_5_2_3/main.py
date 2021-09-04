'''
Create a decorator that memoize’s the result of a function. This decorator should be flexible enough that it can work with a function with any number of parameters.
Modify the Timer class to work as a decorator (feel free to use the provided sample code).
Per QUANTNET site, NO RELATION TO TIMER CLASS. PORT OVER CODE FROM CLASS, IN VERBATIM.

'It should be a function, separate from the class. The function should reside in the same .py file as the Timer class.'
For consistency, the memoize function was also placed in the Timer.py.
'''

import time
import logging
import datetime
from Exercise_5_2.Exercise_5_2_3.Loan_Package.loan import Loan
from Exercise_5_2.Exercise_5_2_3.Loan_Package.car import Car
from Exercise_5_2.Exercise_5_2_3.Timer.Timer_Package.Timer import timer, memoize, Timer

# Test Function 1
@memoize
@timer
def interestDueRecursiveM(loan, t):
    return loan.interestDueRecursive(t)

# Test Function 2
@memoize
@timer
def principalDueRecursiveM(loan, t):
    return loan.principalDueRecursive(t)

# Test Function 3
@memoize
@timer
def balanceRecursiveM(loan, t):
    return loan.balanceRecursive(t)


def main():
    logging.basicConfig(format='%(message)s', level=logging.INFO)

    # t spec
    t = 5

    # 1 Asset Spec
    car = Car(100000)

    #2 Loan Spec
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
    baseLoan = Loan(dateTime1, dateTime2, 0.05, 500000, car)

    logging.info('I. Testing the first function...')
    logging.info(f'{interestDueRecursiveM(baseLoan, t)}')
    logging.info('\nTiming the first function after memoize...') # Need to time this again as the memoize x timer decorators are all saved in cache and only result is printed during the second run.
    with Timer('myTimer'):
        logging.info(interestDueRecursiveM(baseLoan, t))

    logging.info('II. Testing the second function...')
    logging.info(f'{principalDueRecursiveM(baseLoan, t)}')
    logging.info('\nTiming the second function after memoize...') # Need to time this again as the memoize x timer decorators are all saved in cache and only result is printed during the second run.
    with Timer('myTimer'):
        logging.info(principalDueRecursiveM(baseLoan, t))

    logging.info('III. Testing the third function...')
    logging.info(f'{balanceRecursiveM(baseLoan, t)}')
    logging.info('\nTiming the third function after memoize...') # Need to time this again as the memoize x timer decorators are all saved in cache and only result is printed during the second run.
    with Timer('myTimer'):
        logging.info(balanceRecursiveM(baseLoan, t))


#########################
if __name__ == '__main__':
    main()