'''
This class describes a Fixed Rate Loan and a Variable Rate Loan. Grouped in one file per QuantNet Forum answer 'No need to put subclasses of similar class in separate files'.
Recursion Workaround included for VariableRateLoan
'''

from Loan_Folder_10.Loan_Package.loan import Loan


class FixedRateLoan(Loan):
    # (1) Initialization Functions
    # No need for an initialization function (uses Loan's)

    # (2) Methods
    # Overwrite rate:
    def getRate(self, t):
        # Overrides the base class getRate
        return self._rate


class VariableRateLoan(Loan):
    # (1) Initialization Functions
    # Overwrite initialization function in loan.py as this does not contain a rateDict
    def __init__(self, term, rateDict, notional):
        self._rateDict = rateDict

        if type(rateDict) != dict:
            print('The rateDict data type test is now complete: Error! Please input a dictionary containing startPeriod as key and rate as value.')
        else:
            print('The rateDict data type test is now complete: Rate Dictionary has been correctly specified.')

        # Allow for new variables: super
        super(VariableRateLoan, self).__init__(term, None, notional)

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
        if self.rateDict.get(t) is None:
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
            return self.rateDict.get(t)

    # balanceRecursive Recursion Override:
    # Run a function that runs xxRecursive while declaring the parts I don't want to recurse outside the recursion.
    def balanceRecursive(self, t):
        '''
        This function RECURSIVELY calculates balance due (principal and interest) at time t.
        '''

        payment = self.monthlyPayment(t)
        getRate = self.monthlyRate(self.getRate(t))
        return self.balanceRecursiveInside(t, getRate, payment)

    def balanceRecursiveInside(self, t, rate, payment):
        if not t:
            return self._notional
        elif t == 1:
            return self._notional - (payment - rate * self._notional) # (Calc to Static 3.) Originally a calculation, Now a Static Method
        else:
            return max(0, self.balanceRecursiveInside(t - 1, rate, payment) - (payment - self.interestDueRecursiveInside(t - 1, rate, payment)))


    # interestDueRecursive Recursion Override:
    # Run a function that runs xxRecursive while declaring the parts I don't want to recurse outside the recursion.
    def interestDueRecursive(self, t):
        '''
        This function RECURSIVELY calculates interest due at time t.
        '''

        payment = self.monthlyPayment(t)
        getRate = self.monthlyRate(self.getRate(t))
        return self.interestDueRecursiveInside(t,getRate, payment)

    def interestDueRecursiveInside(self, t, rate, payment):
        if not t:
            return rate * self._notional
        else:
            balance = self.balanceRecursiveInside(t, rate, payment) # Code starts here.
            # Be careful! If you set rate above balance, you get the wrong values.
            return max(0, rate * balance) # (Calc to Static 7.) Originally a calculation, Now a Static Method ...


    # principalDueRecursive Recursion Override:
    # Run a function that runs xxRecursive while declaring the parts I don't want to recurse outside the recursion.
    def principalDueRecursive(self, t):
        '''
        This function RECURSIVELY calculates principal due at time t.
        '''

        payment = self.monthlyPayment(t)
        getRate = self.monthlyRate(self.getRate(t))
        return self.principalDueRecursiveInside(t, getRate, payment)

    def principalDueRecursiveInside(self, t, rate, payment):
        if not t:
            return payment - rate * self._notional # (Calc to Static 4.) Originally a calculation, Now a Static Method ...
        else:
            interestDue = self.balanceRecursiveInside(t, rate, payment) * rate # (Calc to Static 5.) Originally a calculation, Now a Static Method ...
            return min(payment, payment - interestDue)