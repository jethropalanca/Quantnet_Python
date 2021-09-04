'''
This program initializes the autoLoan.
'''

from Loan_Folder_12.Loan_Package.loan_types import FixedRateLoan
from Loan_Folder_12.Loan_Package.car import Car


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
            exit('Please enter an appropriate Car class in the fourth parameter. Exiting...')

