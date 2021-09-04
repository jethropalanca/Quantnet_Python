'''
This class defines a basic loan class exactly as demonstrated in the lecture.
'''


class Loan(object):
    # (1) Initialization Functions
    def __init__(self, term, rate, notional):
        '''
        This is the initialization function for the loan class:
        :param term:
        :param rate:
        :param notional:
        '''
        self._term = term
        self._rate = rate
        self._notional = notional

    # (2) Getter/Setter Properties
    @property
    def term(self):
        return self._term

    @term.setter
    def term(self, iterm):
        self._term = iterm

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, irate):
        self._rate = irate

    @property
    def notional(self):
        return self._notional

    @notional.setter
    def notional(self, inotional):
        self._notional = inotional

    # (3) Methods
    def monthlyPayment(self, t = None):
        '''
        This function calculates the loan's monthly payment.
        '''
        # t is a dummy parameter to account for loans having monthly payment depending on t
        if self._rate <= 0 or self._term <=0 or self._notional <= 0:
            print('Please re-instantiate your loan class with positive inputs.')
        else:
            mRate = self._rate / 12
            mTerm = self._term * 12
            return (mRate * self._notional) / (1 - (1 + mRate) ** (-mTerm))

    def totalPayments(self):
        '''
        This function calculates the total payments (interest and principal) to be made over the life of the loan.
        '''
        if self._rate <= 0 or self._term <=0 or self._notional <= 0:
            print('Please re-instantiate your loan class with positive inputs.')
        else:
            payment = self.monthlyPayment()
            return payment * 12 * self._term


    def totalInterest(self):
        '''
        This function calculates the total interest to be paid over the life of the loan.
        '''
        if self._rate <= 0 or self._term <=0 or self._notional <= 0:
            print('Please re-instantiate your loan class with positive inputs.')
        else:
            totalPaid = self.totalPayments()
            return totalPaid - self.notional