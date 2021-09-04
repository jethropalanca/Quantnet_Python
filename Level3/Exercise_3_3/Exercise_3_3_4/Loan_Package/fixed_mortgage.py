'''
This program initializes the FixedMortgage.
'''

from Exercise_3_3.Exercise_3_3_4.Loan_Package.mortgage_mixin import MortgageMixin
from Exercise_3_3.Exercise_3_3_4.Loan_Package.loan_types import FixedRateLoan


class FixedMortgage(MortgageMixin, FixedRateLoan):
    def __init__(self, term, rate, notional, asset):
        '''
        This initialization function to initialize a FixedMortgage class.
        :param term:
        :param rate:
        :param notional:
        :param asset:
        '''
        super(FixedMortgage, self).__init__(term, rate, notional, asset)
