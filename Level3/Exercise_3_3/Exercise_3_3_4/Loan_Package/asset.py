'''
This class defines the Asset covered by the loan.
This class defines the Asset covered by the loan (Version 2 - Rework).
'''


class Asset(object):
    # (1) Initialization Functions
    def __init__(self, value):
        '''
        This function initializes the Asset Class.
        '''
        self._initialValue = value

    # (2) Getter/Setter Properties
    @property
    def initialValue(self):
        return self._initialValue

    @initialValue.setter
    def initialValue(self, iinitialValue):
        self._initialValue = iinitialValue

    # (3) Methods
    # 1. Returns yearly depreciation rate
    def annualDepr(self):
        '''
        This function returns a previously specified annual depreciation rate (10%).
        '''
        raise NotImplementedError

    # 2. Returns monthly depreciation rate
    def monthlyDepr(self):
        '''
        This calculates the monthly depreciation rate for an Asset.
        '''
        return self.annualDepr() / 12

    # 3 . Returns current value of the asset for a given period.
    def value(self, t):
        '''
        This calculates Asset value at time t. It multiplies the initial value of the asset entered at initialization by a compounding factor f(depreciation rate, t).
        :param t:
        '''
        return self._initialValue * ((1 - self.monthlyDepr()) ** (t))