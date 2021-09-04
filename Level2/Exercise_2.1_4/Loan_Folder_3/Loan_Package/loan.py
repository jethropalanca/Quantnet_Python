'''
This class improves upon the base class in Loan Folder 2 by adding class methods.
'''


class Loan(object):
    # (1) Initialization Functions
    def __init__(self, term, rate, notional):
        '''
        This is the initialization function for the loan class:
        :param term: Annual Input, to be converted to months in the formulas via term x 12, i.e. term 30 = term 360.
        :param rate: Annualized rate
        :param notional: Loan face value
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

    #####################################
    ####### Class - Level Methods #######
    #####################################

    # Class-level Method (Naturally associated with the object; class level so no access to object's attributes)
    @classmethod
    def calcMonthlyPmt(cls, term, rate, notional):
        '''
        Class Method: This function calculates the loan's monthly payment.
        :param term: Annual Input, to be converted to months in the formulas via term x 12, i.e. term 30 = term 360.
        :param rate: Annualized rate
        :param notional: Loan face value
        '''
        if rate <= 0 or term <= 0 or notional <= 0:
            print('Please re-instantiate your loan class with positive inputs.')
        else:
            mRate = rate / 12
            mTerm = term * 12
            return (mRate * notional) / (1 - (1 + mRate) ** (-mTerm))

    @classmethod
    def calcBalance(cls, term, rate, notional, t):
        '''
        Class Method: This function calculates the loan's balance at time t.
        :param term: Annual Input, to be converted to months in the formulas via term x 12, i.e. term 30 = term 360.
        :param rate: Annualized rate
        :param notional: Loan face value
        :param t: Monthly Period. i.e. an input of 25 = period 25 of term 360 if term was set to 360.
        '''
        if rate <= 0 or term <= 0 or notional <= 0:
            print('Please re-instantiate your loan class with positive inputs.')
        else:
            payment = cls.calcMonthlyPmt(term, rate, notional)
            mRate = rate / 12  # Only Rate is adjusted. Term already adjusted in monthlyPay and is only used there anyway.
            return max(0, (notional * (1 + mRate) ** (t)) - (payment * (((1 + mRate) ** (t) - 1) / mRate)))

    # Modify Object-Level methods to delegate to the class-level methods:
    # (1) monthlyPayment
    # def monthlyPayment(self, term, rate, notional):
    #     self.calcMonthlyPmt(term, rate, notional)

    # (2) balance
    # def balance(self, term, rate, notional, t):
    #     self.calcBalance(term, rate, notional, t)

    ##############################
    ####### Object Methods #######
    ##############################

    def monthlyPayment(self, t = None):
        '''
        This function calculates the loan's monthly payment.
        '''
        # t is a dummy parameter to account for loans having monthly payment depending on t
        return self.calcMonthlyPmt(self._term, self._rate, self._notional)

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
        return self.calcBalance(self._term, self._rate, self._notional, t)

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