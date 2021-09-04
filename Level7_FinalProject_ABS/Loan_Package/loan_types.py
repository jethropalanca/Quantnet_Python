'''
This class describes a Fixed Rate Loan and a Variable Rate Loan. Grouped in one file per QuantNet Forum answer 'No need to put subclasses of similar class in separate files'.
Recursion Workaround included for VariableRateLoan
'''

from Loan_Package.loan import Loan
import logging


class FixedRateLoan(Loan):
    # (1) Initialization Functions
    # No need for an initialization function (uses Loan's)

    # (2) Methods
    # Overwrite rate:
    def getRate(self, t):
        # Overrides the base class getRate
        logging.debug(f'\nRetrieving rate from the instantiated Loan: {self}...')  # Changed in 4_2_3
        return self._rate


class VariableRateLoan(Loan):
    # (1) Initialization Functions
    # Overwrite initialization function in loan.py as this does not contain a rateDict
    def __init__(self, term, rateDict, notional, asset):
        self._rateDict = rateDict

        if type(rateDict) != dict:
            # Changed in 4_2_3
            logging.error('\nThe rateDict data type test is now complete: Error! Please input a dictionary containing startPeriod as key and rate as value. Exiting...') # Changed in 4_2_3
            raise TypeError('The rateDict data type test is now complete: Error! Please input a dictionary containing startPeriod as key and rate as value. Exiting...') # Changed in 4_2_3
        else:
            logging.info('The rateDict data type test is now complete: Rate Dictionary has been correctly specified.')

        # Allow for new variables: super
        super(VariableRateLoan, self).__init__(term, None, notional, asset)

    '''  
    def __init__(self, startmaturity, endmaturity, rateDict, notional, asset):
        self._rateDict = rateDict

        if type(rateDict) != dict:
            # Changed in 4_2_3
            logging.error('\nThe rateDict data type test is now complete: Error! Please input a dictionary containing startPeriod as key and rate as value. Exiting...') # Changed in 4_2_3
            raise TypeError('The rateDict data type test is now complete: Error! Please input a dictionary containing startPeriod as key and rate as value. Exiting...') # Changed in 4_2_3
        else:
            logging.info('The rateDict data type test is now complete: Rate Dictionary has been correctly specified.')

        # Allow for new variables: super
        super(VariableRateLoan, self).__init__(startmaturity, endmaturity, None, notional, asset)
    '''

    # rateDict getter and setter
    @property
    def rateDict(self):
        return self._rateDict

    @rateDict.setter
    def rateDict(self, irateDict):
        self._rateDict = irateDict

    # (2) Methods
    # Overwrite rate:
    def getRate(self, t):

        logging.debug(f'\nRetrieving rate from the instantiated Variable Rate Loan: {self}...')  # Changed in 4_2_3
        if not self.rateDict.get(t): # original: is None
            # Prepare for inference, if key not in list:
            List = list(self.rateDict.keys())
            List.append(t)
            List.sort()

            # If statement
            if List.index(t) == 0:
                return self.rateDict.get(List[1]) # Version 2 modification to allow 0 to be the first startkey.
            else:
                return self.rateDict.get(List[List.index(t) - 1])
        else:
            logging.debug(f'\nRate successfully retrieved for period {t}...')  # Changed in 4_2_3
            return self.rateDict.get(t)