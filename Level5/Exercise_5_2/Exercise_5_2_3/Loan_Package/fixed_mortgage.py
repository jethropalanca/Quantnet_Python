'''
This program initializes the FixedMortgage.
'''

from Exercise_5_2.Exercise_5_2_3.Loan_Package.mortgage_mixin import MortgageMixin
from Exercise_5_2.Exercise_5_2_3.Loan_Package.loan_types import FixedRateLoan


class FixedMortgage(MortgageMixin, FixedRateLoan):
    def __init__(self, startmaturity, endmaturity, rate, notional, asset):
        '''
        This initialization function to initialize a FixedMortgage class.
        :param startmaturity:
        :param endmaturity:
        :param rate:
        :param notional:
        :param asset:
        '''
        super(FixedMortgage, self).__init__(startmaturity, endmaturity, rate, notional, asset)
