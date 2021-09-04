'''
This program initializes the VariableMortgage.
'''

from Exercise_5_1.Exercise_5_1_6.Loan_Package.mortgage_mixin import MortgageMixin
from Exercise_5_1.Exercise_5_1_6.Loan_Package.loan_types import VariableRateLoan


class VariableMortgage(MortgageMixin, VariableRateLoan):
    def __init__(self, startmaturity, endmaturity, rateDict, notional, asset):
        '''
        This initialization function to initialize a VariableMortgage class.
        :param startmaturity:
        :param endmaturity:
        :param rateDict:
        :param notional:
        :param asset:
        '''
        super(VariableMortgage, self).__init__(startmaturity, endmaturity, rateDict, notional, asset)