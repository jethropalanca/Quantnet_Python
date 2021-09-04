'''
This class defines the MortgageMixin that implements the concept of PMI.
Correct version in Version 2.
'''

from Loan_Folder_12.Loan_Package.HouseBase import HouseBase

class MortgageMixin(object):
    # (1) Initialization Functions
    # MortgageMixin does not derive from a loan. Defines things specific to a mortgage. Related to a loan class.
    def __init__(self, term, rate, notional, home):
        # MortgageMixin.__init__(self)
        # Invokes Ini fnx of base class, if there is a base class. Term, Rate, Notional have been entered in __init__ per forum.
        super(MortgageMixin, self).__init__(term, rate, notional, home)
        if isinstance(home, HouseBase):
            self._home = home
        else:
            # 'Ensure that the asset parameter indeed contains an Asset object / any of its derived classes'
            exit('Please enter an appropriate Asset class in the fourth parameter. Exiting...')

    # (3) Methods
    def PMI(self, t=None):
        '''
        Private Mortgage Insurance Function
        '''

        homeValue = self._home._initialValue

        loanToValue = 1
        if loanToValue >= .8:
            return homeValue * .0075
        else:
            return 0

    # Override in loan class, function 1:
    def monthlyPayment(self, t):
        '''
        This function calculates the loan's monthly payment. No longer t = None due to getRate? No. STILL t = None as its dependents do not have t as parameter (e.g. totalPayments).
        '''

        # Should still run well.
        monthlyPayment = super(MortgageMixin, self).monthlyPayment(t)
        return monthlyPayment + self.PMI(t=None)

    # Override in loan class, function 2:
    def principalDue(self, t):
        '''
        This function calculates the loan's monthly payment. No longer t = None due to getRate? No. STILL t = None as its dependents do not have t as parameter (e.g. totalPayments).
        '''

        # t is a dummy parameter to account for loans having monthly payment depending on t
        principalDue = super(MortgageMixin, self).principalDue(t)
        return principalDue - self.PMI(t=None)

    def principalDueRecursive(self, t):
        '''
        This function calculates the loan's monthly payment. No longer t = None due to getRate? No. STILL t = None as its dependents do not have t as parameter (e.g. totalPayments).
        '''

        # t is a dummy parameter to account for loans having monthly payment depending on t
        principalDueRecursive = super(MortgageMixin, self).principalDueRecursive(t)
        return principalDueRecursive - self.PMI(t=None)
