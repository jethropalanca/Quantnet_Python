'''
This class improves upon the base class in Loan Folder 1 by adding methods.
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
        if self._rate <= 0 or self._term <= 0 or self._notional <= 0:
            print('Please re-instantiate your loan class with positive inputs.')
        else:
            mRate = self._rate / 12
            mTerm = self._term * 12
            return (mRate * self._notional) / (1 - (1 + mRate) ** (-mTerm))

    def totalPayments(self):
        '''
        This function calculates the total payments (interest and principal) to be made over the life of the loan.
        '''
        if self._rate <= 0 or self._term <= 0 or self._notional <= 0:
            print('Please re-instantiate your loan class with positive inputs.')
        else:
            payment = self.monthlyPayment()
            return payment * 12 * self._term

    def totalInterest(self):
        '''
        This function calculates the total interest to be paid over the life of the loan.
        '''
        if self._rate <= 0 or self._term <= 0 or self._notional <= 0:
            print('Please re-instantiate your loan class with positive inputs.')
        else:
            totalPaid = self.totalPayments()
            return totalPaid - self.notional

    # 2.1_3 Additional Methods
    # Interest Formulas
    def interestDue(self, t):
        '''
        This function calculates interest due at time t.
        '''
        if self._rate <= 0 or self._term <= 0 or self._notional <= 0:
            print('Please re-instantiate your loan class with positive inputs.')
        else:
            balance = self.balance(t)
            mRate = self._rate / 12  # Be careful! If you set rate above balance, you get the wrong values.
            return max(0, mRate * balance)

    def interestDueRecursive(self, t):
        '''
        This function RECURSIVELY calculates interest due at time t.
        '''
        if self._rate <= 0 or self._term <= 0 or self._notional <= 0:
            print('Please re-instantiate your loan class with positive inputs.')
        else:
            if not t:
                mRate = self._rate / 12
                return mRate * self._notional
            else:
                balance = self.balanceRecursive(t)
                # Be careful! If you set rate above balance, you get the wrong values.
                return max(0, (self._rate / 12) * balance)

    # Principal Formulas
    def principalDue(self, t):
        '''
        This function calculates principal due at time t.
        '''
        # rate and term already specified in interestDue and monthlyPayment
        if self._rate <= 0 or self._term <= 0 or self._notional <= 0:
            print('Please re-instantiate your loan class with positive inputs.')
        else:
            interest = self.interestDue(t)
            monthlyPay = self.monthlyPayment()
            return min(monthlyPay, monthlyPay - interest)

    def principalDueRecursive(self, t):
        '''
        This function RECURSIVELY calculates principal due at time t.
        '''
        if self._rate <= 0 or self._term <= 0 or self._notional <= 0:
            print('Please re-instantiate your loan class with positive inputs.')
        else:
            monthlyPay = self.monthlyPayment()
            if not t:
                mRate = self._rate / 12
                return monthlyPay - mRate * self._notional
            else:
                interestDue = self.balanceRecursive(t) * self._rate / 12
                return min(monthlyPay, monthlyPay - interestDue)

    # Balance Formulas
    def balance(self, t):
        '''
        This function calculates balance due (principal and interest) at time t.
        '''
        if self._rate <= 0 or self._term <= 0 or self._notional <= 0:
            print('Please re-instantiate your loan class with positive inputs.')
        else:
            payment = self.monthlyPayment()
            mRate = self._rate / 12  # Only Rate is adjusted. Term already adjusted in monthlyPay and is only used there anyway.
            return max(0, (self._notional * (1 + mRate) ** (t)) - (payment * (((1 + mRate) ** (t) - 1) / mRate)))

    def balanceRecursive(self, t):
        '''
        This function RECURSIVELY calculates balance due (principal and interest) at time t.
        '''
        if self._rate <= 0 or self._term <= 0 or self._notional <= 0:
            print('Please re-instantiate your loan class with positive inputs.')
        else:
            payment = self.monthlyPayment()
            if not t:
                return self._notional
            elif t == 1:
                return self._notional - (payment - (self._rate / 12) * self._notional)
            else:
                return max(0, self.balanceRecursive(t - 1) - (payment - self.interestDueRecursive(t - 1)))