'''
This class improves upon the base class in Loan Folder 5 by modifying the functions to accommodate VariableRateLoan functionalities.
Latest Version: Fixed the Zero Division Error! Not fixed retroactively.
*** Made more efficient in Loan_Folder_6
*** Fixed Inconsistencies (e.g. lack of parameter t for some fnx) to make everything run smoothly in the main function.
'''


class Loan(object):
    # (1) Initialization Functions
    def __init__(self, term, rate, notional):
        '''
        This is the initialization function for the loan class:
        Latest Version: Fixed the Zero Division Error!
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

    # Will take in getRate via the methods that use these class-level methods
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
            mRate = Loan.monthlyRate(rate) # (Calc to Static 1.) Originally a calculation, Now a Static Method
            mTerm = term * 12
            return (mRate * notional) / (1 - (1 + mRate) ** (-mTerm))

    @classmethod
    # Will take in getRate via the methods that use these class-level methods
    def calcBalance(cls, term, rate, notional, t):
        '''
        Class Method: This function calculates the loan's balance at time t.
        :param term: Annual Input, to be converted to months in the formulas via term x 12, i.e. term 30 = term 360.
        :param rate: Annualized rate
        :param notional: Loan face value
        :param t: Monthly Period. i.e. an input of 25 = period 25 of term 360 if term was set to 360.
        '''

        # LOGIC TEST IS ALREADY DONE IN calcMonthlyPAYMENT
        payment = cls.calcMonthlyPmt(term, rate, notional)
        if not payment:
            print('Please re-instantiate your loan class with positive inputs.')
        else:
            mRate = Loan.monthlyRate(rate)  # (Calc to Static 2.) Originally a calculation, Now a Static Method ... Only Rate is adjusted. Term already adjusted in monthlyPay and is only used there anyway.
            return max(0, (notional * (1 + mRate) ** (t)) - (payment * (((1 + mRate) ** (t) - 1) / mRate)))

    # Modify Object-Level methods to delegate to the class-level methods:
    # (1) monthlyPayment
    # def monthlyPayment(self, term, rate, notional):
    #     self.calcMonthlyPmt(term, rate, notional)

    # (2) balance
    # def balance(self, term, rate, notional, t):
    #     self.calcBalance(term, rate, notional, t)

    ##############################
    ####### Static Methods #######
    ##############################

    @staticmethod
    def monthlyRate(annualrate):
        return annualrate / 12

    @staticmethod
    def annualRate(monthlyRate):
        return monthlyRate * 12

    ##############################
    ####### Object Methods #######
    ##############################

    # (2.2_1) New method for rate calculation to be used in loan_types: getRate Function is also for rateDict compatibility
    def getRate(self, t):
        return self._rate

    def monthlyPayment(self, t = None):
        '''
        This function calculates the loan's monthly payment. No longer t = None due to getRate? No. STILL t = None as its dependents do not have t as parameter (e.g. totalPayments).
        '''
        # t is a dummy parameter to account for loans having monthly payment depending on t
        gRate = self.getRate(t) # Modification for Variable rate loans
        return self.calcMonthlyPmt(self._term, gRate, self._notional)

    def totalPayments(self):
        '''
        This function calculates the total payments (interest and principal) to be made over the life of the loan.
        '''

        # LOGIC TEST IS ALREADY DONE IN monthlyPAYMENT
        # if self._rate <= 0 or self._term <= 0 or self._notional <= 0:
        #     print('Please re-instantiate your loan class with positive inputs.')
        # else:
        payment = self.monthlyPayment(t=None)
        if not payment:
            print('Please re-instantiate your loan class with positive inputs.')
        else:
            return payment * 12 * self._term

    def totalInterest(self):
        '''
        This function calculates the total interest to be paid over the life of the loan.
        '''

        # LOGIC TEST IS ALREADY DONE IN monthlyPAYMENT > totalPayments
        totalPaid = self.totalPayments()
        if not totalPaid:
            print('Please re-instantiate your loan class with positive inputs.')
        else:
            return totalPaid - self.notional

    # 2.1_3 Additional Methods
    # Interest Formulas
    def interestDue(self, t):
        '''
        This function calculates interest due at time t.
        '''

        # LOGIC TEST IS ALREADY DONE IN calcMonthlyPAYMENT > calcBalance > balance
        balance = self.balance(t)
        gRate = self.getRate(t)  # Modification for Variable rate loans
        mRate = Loan.monthlyRate(gRate)  # (Calc to Static 8.) Originally a calculation, Now a Static Method ... Be careful! If you set rate above balance, you get the wrong values.
        return max(0, mRate * balance)

    def interestDueRecursive(self, t):
        '''
        This function RECURSIVELY calculates interest due at time t.
        '''

        # LOGIC TEST IS ALREADY DONE IN balanceRecursive
        if not t:
            gRate = self.getRate(t)  # Modification for Variable rate loans
            mRate = Loan.monthlyRate(gRate) # (Calc to Static 6.) Originally a calculation, Now a Static Method ...
            return mRate * self._notional
        else:
            balance = self.balanceRecursive(t) # Code starts here.
            # Be careful! If you set rate above balance, you get the wrong values.
            return max(0, Loan.monthlyRate(self._rate) * balance) # (Calc to Static 7.) Originally a calculation, Now a Static Method ...


    # Principal Formulas
    def principalDue(self, t):
        '''
        This function calculates principal due at time t.
        '''

        # LOGIC TEST IS ALREADY DONE IN calcMonthlyPAYMENT > calcBalance > balance > interestDue
        # rate and term already specified in interestDue and monthlyPayment
        interest = self.interestDue(t)
        monthlyPay = self.monthlyPayment(t)
        return min(monthlyPay, monthlyPay - interest)

    def principalDueRecursive(self, t):
        '''
        This function RECURSIVELY calculates principal due at time t.
        '''

        # LOGIC TEST IS ALREADY DONE IN monthlyPAYMENT
        monthlyPay = self.monthlyPayment(t)
        if not t:
            gRate = self.getRate(t)  # Modification for Variable rate loans
            return monthlyPay - Loan.monthlyRate(gRate) * self._notional # (Calc to Static 4.) Originally a calculation, Now a Static Method ...
        else:
            gRate = self.getRate(t)  # Modification for Variable rate loans
            interestDue = self.balanceRecursive(t) * Loan.monthlyRate(gRate) # (Calc to Static 5.) Originally a calculation, Now a Static Method ...
            return min(monthlyPay, monthlyPay - interestDue)

    # Balance Formulas
    def balance(self, t):
        '''
        This function calculates balance due (principal and interest) at time t.
        '''
        gRate = self.getRate(t)  # Modification for Variable rate loans
        return self.calcBalance(self._term, gRate, self._notional, t) # calcBalance already has monthly rate function.

    def balanceRecursive(self, t):
        '''
        This function RECURSIVELY calculates balance due (principal and interest) at time t.
        '''

        # LOGIC TEST IS ALREADY DONE IN monthlyPAYMENT
        payment = self.monthlyPayment(t)
        if not t:
            return self._notional
        elif t == 1:
            gRate = self.getRate(t)  # Modification for Variable rate loans
            return self._notional - (payment - Loan.monthlyRate(gRate) * self._notional) # (Calc to Static 3.) Originally a calculation, Now a Static Method
        else:
            return max(0, self.balanceRecursive(t - 1) - (payment - self.interestDueRecursive(t - 1)))