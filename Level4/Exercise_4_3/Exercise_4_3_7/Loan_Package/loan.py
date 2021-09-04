'''
Version 4_2. Applied Logging
Version 3_3_4. Error-Handling Applied
This class improves upon the base class in Loan Folder 11 by adding a new attribute (asset) to the Loan class and related methods.
Latest Version: Fixed the Zero Division Error! Not fixed retroactively.
*** Made more efficient in Loan_Folder_6
*** Fixed Inconsistencies (e.g. lack of parameter t for some fnx) to make everything run smoothly in the main function.
'''

from Exercise_4_3.Exercise_4_3_7.Loan_Package.asset import Asset
import logging

class Loan(object):
    # (1) Initialization Functions
    def __init__(self, term, rate, notional, asset):
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
        if isinstance(asset, Asset):
            logging.debug('\nAppropriate asset class has been entered. Instantiating the loan...')  # Changed in 4_2_3
            self._asset = asset
        else:
            # 'Ensure that the asset parameter indeed contains an Asset object / any of its derived classes'
            logging.error('\nPlease enter an appropriate Asset class in the fourth parameter. Exiting...') # Changed in 4_2_3
            raise TypeError('Please enter an appropriate Asset class in the fourth parameter. Exiting...') # Changed in 4_2_3

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

    @property
    def asset(self):
        return self._asset

    @asset.setter
    def asset(self, iasset):
        self._asset = iasset

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
            logging.error('\nPlease re-instantiate your loan class with positive inputs. Exiting...') # Changed in 4_2_3
            raise ValueError('Please re-instantiate your loan class with positive inputs. Exiting...') # Changed in 4_2_3
            # logging.info('Please re-instantiate your loan class with positive inputs.') # removed in 4_2_3

        else:
            mRate = Loan.monthlyRate(rate) # (Calc to Static 1.) Originally a calculation, Now a Static Method
            # No Logging statements here else will be double-logged in the functions... Commented in 4_2_3

            # No Logging statements here else will be double-logged in the functions... Commented in 4_2_3
            mTerm = term * 12

            logging.debug('\nCalculating monthly payment from term, rate and notional (based on a formula)...')  # Changed in 4_2_3
            logging.debug('(monthly rate * notional) / (1 - (1 + monthly rate)^(-term in months))...')  # Changed in 4_2_3
            logging.debug('Calculation Successful!')  # Changed in 4_2_3
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

        # LOGIC TEST IS ALREADY DONE IN calcMonthlyPmt
        # No Logging statements here else will be double-logged in the functions... Commented in 4_2_3
        payment = cls.calcMonthlyPmt(term, rate, notional)


        if not payment:
            logging.error('\nPlease re-instantiate your loan class with positive inputs. Exiting...') # Changed in 4_2_3
            raise ValueError('Please re-instantiate your loan class with positive inputs. Exiting...') # Changed in 4_2_3
            # print('Please re-instantiate your loan class with positive inputs.')

        else:
            mRate = Loan.monthlyRate(rate)  # (Calc to Static 2.) Originally a calculation, Now a Static Method ... Only Rate is adjusted. Term already adjusted in monthlyPay and is only used there anyway.
            # No Logging statements here else will be double-logged in the functions... Commented in 4_2_3

            logging.debug('\nCalculating balance at period t as a function of term, rate, notional (based on a formula)...')  # Changed in 4_2_3
            logging.debug('notional * (1 + monthly rate)^(t)) - (payment * (((1 + monthly rate)^(t) - 1) / monthly rate)) ...')  # Changed in 4_2_3
            logging.debug('Calculation Successful!')  # Changed in 4_2_3
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
        logging.debug('\nCalculating monthly term from entered term in years (annual rate * 12) ...')  # Changed in 4_2_3
        return annualrate / 12

    @staticmethod
    def annualRate(monthlyRate):
        logging.debug('\nCalculating annual rate back from monthly rate (monthly rate / 12) ...')  # Changed in 4_2_3
        return monthlyRate * 12

    ##############################
    ####### Object Methods #######
    ##############################

    # (2.2_1) New method for rate calculation to be used in loan_types: getRate Function is also for rateDict compatibility
    def getRate(self, t):
        logging.debug(f'\nRetrieving rate from the instantiated Loan: {self}...')  # Changed in 4_2_3
        return self._rate

    def monthlyPayment(self, t = None):
        '''
        This function calculates the loan's monthly payment. No longer t = None due to getRate? No. STILL t = None as its dependents do not have t as parameter (e.g. totalPayments).
        '''

        # t is a dummy parameter to account for loans having monthly payment depending on t

        # No Logging statements here else will be double-logged in the functions... Commented in 4_2_3
        gRate = self.getRate(t) # Modification for Variable rate loans

        # No Logging statements here else will be double-logged in the functions... Commented in 4_2_3
        return self.calcMonthlyPmt(self._term, gRate, self._notional)

    def totalPayments(self):
        '''
        This function calculates the total payments (interest and principal) to be made over the life of the loan.
        '''

        # LOGIC TEST IS ALREADY DONE IN monthlyPAYMENT
        # if self._rate <= 0 or self._term <= 0 or self._notional <= 0:
        #     print('Please re-instantiate your loan class with positive inputs.')
        # else:
        payment = self.monthlyPayment(t = None)

        if not payment:
            logging.error('\nPlease re-instantiate your loan class with positive inputs. Exiting...') # Changed in 4_2_3
            raise ValueError('Please re-instantiate your loan class with positive inputs. Exiting...') # Changed in 4_2_3
            # print('Please re-instantiate your loan class with positive inputs.')

        else:
            logging.debug('\nCalculating total payments = term in months * monthly payment...')  # Changed in 4_2_3
            logging.debug('Calculation Successful!')  # Changed in 4_2_3
            return payment * 12 * self._term

    def totalInterest(self):
        '''
        This function calculates the total interest to be paid over the life of the loan.
        '''

        # LOGIC TEST IS ALREADY DONE IN monthlyPAYMENT > totalPayments
        totalPaid = self.totalPayments()
        if not totalPaid:
            logging.error('\nPlease re-instantiate your loan class with positive inputs. Exiting...') # Changed in 4_2_3
            raise ValueError('Please re-instantiate your loan class with positive inputs. Exiting...') # Changed in 4_2_3
            # print('Please re-instantiate your loan class with positive inputs.')

        else:
            logging.debug('\nCalculating total interest = total payments - notional of loan...')  # Changed in 4_2_3
            logging.debug('Calculation Successful!')  # Changed in 4_2_3

            return totalPaid - self.notional

    # 2.1_3 Additional Methods
    # Interest Formulas
    def interestDue(self, t):
        '''
        This function calculates interest due at time t.
        '''

        # LOGIC TEST IS ALREADY DONE IN calcMonthlyPAYMENT > calcBalance > balance

        #  ... Already CHECKED in balance due, interest due
        # Inform user that period should be within term
        # if t > (self._term * 12):
        #     logging.info(f'NOTICE: period is greater than term for {self}...')
        # logging.getLogger().setLevel(logging.ERROR)

        # For balance, gRate and mRate...
        # No Logging statements here else will be double-logged in the functions... Commented in 4_2_3
        # No Logging statements here else will be double-logged in the functions... Commented in 4_2_3
        # No Logging statements here else will be double-logged in the functions... Commented in 4_2_3

        balance = self.balance(t)
        gRate = self.getRate(t)  # Modification for Variable rate loans
        mRate = Loan.monthlyRate(gRate)  # (Calc to Static 8.) Originally a calculation, Now a Static Method ... Be careful! If you set rate above balance, you get the wrong values.

        logging.debug('\nCalculating interest due at period t = monthly rate * balance at t...')  # Changed in 4_2_3
        logging.debug('Calculation Successful!')  # Changed in 4_2_3
        return max(0, mRate * balance)

    def interestDueRecursive(self, t):
        '''
        This function RECURSIVELY calculates interest due at time t.
        '''

        # Inform user that recursive functions are expected to take a long time...
        logging.warning('Warning! Recursive functions are expected to take a long time (esp. at period > 20)...')  # Changed in 4_2_3

        # Inform user that period should be within term
        if t > (self._term * 12):
            logging.info(f'NOTICE: period is greater than term for {self}...')


        payment = self.monthlyPayment(t)
        getRate = self.monthlyRate(self.getRate(t))
        return self.interestDueRecursiveInside(t,getRate, payment)

    def interestDueRecursiveInside(self, t, rate, payment):

        if not t:
            logging.debug('\nRecursive Interest Due Calculation at t = 0...')  # Changed in 4_2_3
            logging.debug('Calculating interest due at period 0 = monthly rate * notional...')  # Changed in 4_2_3
            return rate * self._notional

        else:
            logging.debug('\nRecursive Interest Due Calculation at t != 0...')  # Changed in 4_2_3
            logging.debug(f't counter: {t}')  # Changed in 4_2_3
            logging.debug('\nRecursing monthly rate * balance...')  # Changed in 4_2_3

            balance = self.balanceRecursiveInside(t, rate, payment) # Code starts here.
            # Be careful! If you set rate above balance, you get the wrong values.
            return max(0, rate * balance) # (Calc to Static 7.) Originally a calculation, Now a Static Method ...


    # Principal Formulas
    def principalDue(self, t):
        '''
        This function calculates principal due at time t.
        '''

        #  ... Already CHECKED in balance due, interest due
        # Inform user that period should be within term
        # if t > (self._term * 12):
        #     logging.info(f'NOTICE: period is greater than term for {self}...')
        # logging.getLogger().setLevel(logging.ERROR)

        # LOGIC TEST IS ALREADY DONE IN calcMonthlyPAYMENT > calcBalance > balance > interestDue
        # rate and term already specified in interestDue and monthlyPayment

        # For interest and monthlyPay...
        # No Logging statements here else will be double-logged in the functions... Commented in 4_2_3
        # No Logging statements here else will be double-logged in the functions... Commented in 4_2_3

        interest = self.interestDue(t)
        monthlyPay = self.monthlyPayment(t)

        logging.debug('\nCalculating principal due at period t = monthly payment at t - interest at t...')  # Changed in 4_2_3
        logging.debug('Calculation Successful!')  # Changed in 4_2_3
        return min(monthlyPay, monthlyPay - interest)

    def principalDueRecursive(self, t):
        '''
        This function RECURSIVELY calculates principal due at time t.
        '''

        # Inform user that recursive functions are expected to take a long time...
        logging.warning('Warning! Recursive functions are expected to take a long time (esp. at period > 20)...')  # Changed in 4_2_3

        # Inform user that period should be within term
        if t > (self._term * 12):
            logging.info(f'NOTICE: period is greater than term for {self}...')

        payment = self.monthlyPayment(t)
        getRate = self.monthlyRate(self.getRate(t))
        return self.principalDueRecursiveInside(t, getRate, payment)

    def principalDueRecursiveInside(self, t, rate, payment):

        if not t:
            logging.debug('\nRecursive Principal Due Calculation at t = 0...')  # Changed in 4_2_3
            logging.debug(
                'Calculating Principal Due at period 0 = monthly payment - monthly rate * notional...')  # Changed in 4_2_3
            return payment - rate * self._notional  # (Calc to Static 4.) Originally a calculation, Now a Static Method ...

        else:
            logging.debug('\nRecursive Principal Due Calculation at t != 0...')  # Changed in 4_2_3
            logging.debug(f't counter: {t}')  # Changed in 4_2_3
            logging.debug('\nRecursing monthly payment - interest due...')  # Changed in 4_2_3

            interestDue = self.balanceRecursiveInside(t, rate,
                                                      payment) * rate  # (Calc to Static 5.) Originally a calculation, Now a Static Method ...
            return min(payment, payment - interestDue)

    # Balance Formulas
    def balance(self, t):
        '''
        This function calculates balance (principal and interest) at time t.
        '''

        # Inform user that period should be within term
        if t > (self._term * 12):
            logging.info(f'NOTICE: period is greater than term for {self}...')

        # For rate and balance...
        # No Logging statements here else will be double-logged in the functions... Commented in 4_2_3

        gRate = self.getRate(t)  # Modification for Variable rate loans
        return self.calcBalance(self._term, gRate, self._notional, t) # calcBalance already has monthly rate function.

    def balanceRecursive(self, t):
        '''
        This function RECURSIVELY calculates balance due (principal and interest) at time t.
        '''

        # Inform user that recursive functions are expected to take a long time...
        logging.warning('Warning! Recursive functions are expected to take a long time (esp. at period > 20)...')  # Changed in 4_2_3

        # Inform user that period should be within term
        if t > (self._term * 12):
            logging.info(f'NOTICE: period is greater than term for {self}...')

        payment = self.monthlyPayment(t)
        getRate = self.monthlyRate(self.getRate(t))
        return self.balanceRecursiveInside(t, getRate, payment)

    def balanceRecursiveInside(self, t, rate, payment):

        if not t:
            logging.debug('\nRecursive Balance Calculation at t = 0...')  # Changed in 4_2_3
            logging.debug('\nSimply the notional at t = 0.')  # Changed in 4_2_3
            return self._notional

        elif t == 1:
            logging.debug('\nRecursive Balance Calculation at t = 1...')  # Changed in 4_2_3
            logging.debug('\nNotional - (monthly payment - rate * notional at t = 1)')  # Changed in 4_2_3
            return self._notional - (payment - rate * self._notional) # (Calc to Static 3.) Originally a calculation, Now a Static Method

        else:
            logging.debug('\nRecursive Balance Calculation at t != 0 and t != 1...')  # Changed in 4_2_3
            logging.debug(f't counter: {t}')  # Changed in 4_2_3
            logging.debug('\nRecursing recursive balance (t - 1) - (payment - recursive interest due (t - 1))...')  # Changed in 4_2_3

            return max(0, self.balanceRecursiveInside(t - 1, rate, payment) - (payment - self.interestDueRecursiveInside(t - 1, rate, payment)))

    # Asset Method (1): Recovery Value
    def recoveryValue(self, t):
        '''
        This function calculates the recovery value of a loan based on the asset it paid for.
        '''

        logging.debug('\nCalculating recovery value at t as asset value at t * 0.6...')  # Changed in 4_2_3
        return self._asset.value(t) * 0.6

    # Asset Method (2): Equity Value
    def equity(self, t):
        '''
        This function calculates owner's equity as the difference between asset value and balance to pay.
        '''

        assetValue = self._asset.value(t) # No Logging statements here else will be double-logged in the functions... Commented in 4_2_3
        balance = self.balance(t) # No Logging statements here else will be double-logged in the functions... Commented in 4_2_3

        logging.debug('\nCalculating equity value at t = asset value - balance...')  # Changed in 4_2_3
        return assetValue - balance