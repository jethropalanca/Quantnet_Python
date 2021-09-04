'''
This program initializes the FixedMortgage.
'''

from Loan_Package.mortgage_mixin import MortgageMixin
from Loan_Package.loan_types import FixedRateLoan


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


'''
class FixedMortgage(MortgageMixin, FixedRateLoan):
    def __init__(self, startmaturity, endmaturity, rate, notional, asset):
        
        This initialization function to initialize a FixedMortgage class.
        :param startmaturity:
        :param endmaturity:
        :param rate:
        :param notional:
        :param asset:
        
        super(FixedMortgage, self).__init__(startmaturity, endmaturity, rate, notional, asset)
'''
