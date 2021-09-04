'''
This program initializes the VariableMortgage.
'''

from Exercise_4_2.Exercise_4_2_3_to_4.Loan_Package.mortgage_mixin import MortgageMixin
from Exercise_4_2.Exercise_4_2_3_to_4.Loan_Package.loan_types import VariableRateLoan


class VariableMortgage(MortgageMixin, VariableRateLoan):
    def __init__(self, term, rateDict, notional, asset):
        '''
        This initialization function to initialize a VariableMortgage class.
        :param term:
        :param rateDict:
        :param notional:
        :param asset:
        '''
        super(VariableMortgage, self).__init__(term, rateDict, notional, asset)