'''
RESET to period version for Waterfall Runs
Version 3_3_4. Error-Handling Applied
This program initializes the autoLoan.
'''

from Loan_Package.loan_types import FixedRateLoan
from Loan_Package.car import Car
import logging


class autoLoan(FixedRateLoan):
    def __init__(self, term, rate, notional, car):
        '''
        This initialization function to initialize a autoLoan class.
        :param term:
        :param rate:
        :param notional:
        '''
        super(autoLoan, self).__init__(term, rate, notional, car)
        if isinstance(car, Car):
            self._car = car
        else:
            # 'Ensure that the car parameter indeed contains a Car object / any of its derived classes'
            logging.error('Please enter a Car class in the fourth parameter. Exiting...')
            raise TypeError('Please enter a Car class in the fourth parameter. Exiting...')

'''        
class autoLoan(FixedRateLoan):
    def __init__(self, startmaturity, endmaturity, rate, notional, car):

        This initialization function to initialize a autoLoan class.
        :param startmaturity:
        :param endmaturity:
        :param rate:
        :param notional:
        :param car:

        super(autoLoan, self).__init__(startmaturity, endmaturity, rate, notional, car)
        if isinstance(car, Car):
            self._car = car
        else:
            # 'Ensure that the car parameter indeed contains a Car object / any of its derived classes'
            logging.error('Please enter a Car class in the fifth parameter. Exiting...')
            raise TypeError('Please enter a Car class in the fifth parameter. Exiting...')
'''