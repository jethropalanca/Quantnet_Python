'''
This program initializes the autoLoan.
'''

from Loan_Folder_10.Loan_Package.loan_types import FixedRateLoan


class autoLoan(FixedRateLoan):
    def __init__(self, term, rate, notional):
        '''
        This initialization function to initialize a autoLoan class.
        :param term:
        :param rate:
        :param notional:
        '''
        super(autoLoan, self).__init__(term, rate, notional)
