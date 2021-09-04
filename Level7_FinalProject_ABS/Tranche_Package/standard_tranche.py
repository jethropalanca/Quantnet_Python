'''
Creates a Standard Tranche class and it's associated functionalities. ONLY Derived Class. But in practice, can derive other tranche types (Interest Only or Principal Only).

* Note: The WATERFALL tracks all the cashflows through each time period, from the pool of loans (assets).
* LP Cashflows are ALLOCATED to each tranche.
*Subordination Flag: Class B would be a SUBORDINATE of class A.
*Recall: ._Variable for Instance Attribute; .Variable for attribute
'''

from Tranche_Package.tranche import tranche
import logging


class StandardTranche(tranche):
    # (1) Initialization Functions
    def __init__(self, rate, notional):
        '''
        This is the initialization function for the derived StandardTranche class:
        '''

        # Inherits class variables
        # super(tranche, self).__init__(rate, notional): Big MISTAKE. Be careful...
        super(StandardTranche, self).__init__(rate, notional)

        # New class variables. Dictionary Variables START AT ZERO per excel file.
        # * add._ if parameter, no ._ if not parameter (i.e. allow to access outside the function)
        # Unsure whether {self._t: 0} would work. Decided to start with 0: 0 instead to be sure that the key = 0 at initialization.
        '''
        self.t = 0
        self.principalPayment = {self.t: 0} # self.principalpayment[self.t] = 0
        self.notionalBalanceVal = {self.t: 0}  # Notional Balance, set to 0 at time 0 (like in excel). Values to be entered in the notionalBalance function
        self.interestPayment = {self.t: 0}
        '''
        self.interestDueVal = {self.t: 0}
        self.interestShortfall = {self.t: 0}
        # self.prinPayColl = {} # Call this also in makePrincipalPayment. Causes circularity
        # self.intSFColl = {}  # Call this also in makeInterestPayment. Causes circularity

        # Modification: add self.boolean for makeprincipalPayment and makeinterestPayment instead of testing whether the value of result == 0
        # Reason: Can be zero even if called if fully paid / t == 0.
        self.calledmakeprinPay = {self.t: 0} # Won't work, do not change to {0: 0} for sanity check
        self.calledmakeintPay = {self.t: 0} # Won't work, do not change to {0: 0} for sanity check

        # Modification (Structured Securities):
        self.principalDue = {self.t: 0}
        self.principalSF = {self.t: 0}


    # NOTE:
    # Standard tranches:
    # (1) Start off with a certain notional.
    # (2) Keep track of all payments made to it: (2a) Interest payments and (2b) Principal payments made to it (2c) and at what time period...
    #
    # To this end, implement the following methods:


    # (2) Getter and Setter
    # For easier calling. Define EACH.

    # t
    @property
    def t(self):
        return self._t

    @t.setter
    def t(self, it):
        self._t = it

    '''
    # principalPayment
    @property
    def principalPayment(self):
        return self._principalPayment

    @principalPayment.setter
    def principalPayment(self, iprincipalPayment):
        self._principalPayment = iprincipalPayment

    # notionalBalanceVal
    @property
    def notionalBalanceVal(self):
        return self._notionalBalanceVal

    @notionalBalanceVal.setter
    def notionalBalanceVal(self, inotionalBalanceVal):
        self._notionalBalanceVal = inotionalBalanceVal

    # interestPayment
    @property
    def interestPayment(self):
        return self._interestPayment

    @interestPayment.setter
    def interestPayment(self, iinterestPayment):
        self._interestPayment = iinterestPayment
    '''

    # interestDueVal
    @property
    def interestDueVal(self):
        return self._interestDueVal

    @interestDueVal.setter
    def interestDueVal(self, iinterestDueVal):
        self._interestDueVal = iinterestDueVal

    # interestShortfall
    @property
    def interestShortfall(self):
        return self._interestShortfall

    @interestShortfall.setter
    def interestShortfall(self, iinterestShortfall):
        self._interestShortfall = iinterestShortfall

    # principalDue
    @property
    def principalDue(self):
        return self._principalDue

    @principalDue.setter
    def principalDue(self, iprincipalDue):
        self._principalDue = iprincipalDue

    # principalSF
    @property
    def principalSF(self):
        return self._principalSF

    @principalSF.setter
    def principalSF(self, iprincipalSF):
        self._principalSF = iprincipalSF

    # prinPayColl
    # @property
    # def prinPayColl(self):
    #     return self._prinPayColl

    # @prinPayColl.setter
    # def prinPayColl(self, iprinPayColl):
    #     self._prinPayColl = iprinPayColl

    # interestShortfall
    # @property
    # def intSFColl(self):
    #     return self._intSFColl

    # @intSFColl.setter
    # def intSFColl(self, iintSFColl):
    #     self._intSFColl = iintSFColl

    # calledmakeprinPay
    @property
    def calledmakeprinPay(self):
        return self._calledmakeprinPay

    @calledmakeprinPay.setter
    def calledmakeprinPay(self, icalledmakeprinPay):
        self._calledmakeprinPay = icalledmakeprinPay

    # calledmakeintPay
    @property
    def calledmakeintPay(self):
        return self._calledmakeintPay

    @calledmakeintPay.setter
    def calledmakeintPay(self, icalledmakeintPay):
        self._calledmakeintPay = icalledmakeintPay


    # (3) Methods
    @staticmethod
    def monthlyRate(annualRate):
        '''
        :param annualRate:
        :return: annualRate in terms of months
        '''

        logging.debug('\nCalculating monthly term from entered term in years (annual rate * 12) ...')  # Changed in 4_2_3
        return annualRate / 12

    def increaseTimePeriod(self):
        '''
        Increase the tranche's time period by 1. Resets counter for makePrincipalPayment
        and makeInterestPayment to ZERO.
        '''

        # Increase time period
        self.t = self.t + 1

        # Have to keep resetting this to be able to test them anew each iteration
        self.calledmakeprinPay = {self.t: 0}
        self.calledmakeintPay = {self.t: 0}
        return self.t

    def makePrincipalPayment(self, t, principalPaid, principalDue, principalSF):
        '''
        Calculates the amount of principal paid to the tranche
        :param t: @ period t
        :param principalPaid: principal payment PAID from structured security to tranche
        :param principalDue: principal payment DUE from structured security to tranche
        :param principalSF: principal shortfall (DUE - PAID) of payment from structured security to tranche
        '''

        # Limit Inputs.
        allowableTypes = [float, int]
        if not (type(t) == int and type(principalPaid) in allowableTypes and type(principalDue) in allowableTypes and type(principalSF) in allowableTypes):
            raise Exception('Please Enter the appropriate data type (i.e. float/int) for the function above.')

        # try:
        if not self.notionalBalance(t):
            self.principalPayment[t] = 0
            self.principalDue[t] = 0
            self.principalSF[t] = 0
            raise ValueError(f'Payment not accepted... Current Notional Balance at t = {t} is 0.')

            # Test if Principal Payment has only been recorded once.
        elif not self.calledmakeprinPay[t]:
            self.principalPayment[t] = principalPaid
            self.principalDue[t] = principalDue # structured_securities edit (Excel-required)
            self.principalSF[t] = principalSF if t > 0 else self.principalSF[0] # structured_securities edit
                # self.prinPayColl[t] = self.principalPayment[t] # Store this in the blank dict (Site of circularity)

            self.calledmakeprinPay[t] = 1
            return logging.debug(f'Principal Payment of {self.principalPayment[t]} has been paid for period = {t}.')

        else:
            raise ValueError(f'Payment has already been recorded for period t = {t}.')

        # except Exception as generalError:
        #     logging.info('Please enter a either a float/integer for each of the inputs of makePrincipalPayment.')
        #     logging.info(f'Exception: {generalError}')


    def makeInterestPayment(self, t, interestPaid):
        '''
        Calculates the amount of interest paid to the tranche
        :param t: @ period t
        :param interestPaid: interest PAID from structured security to tranche
        '''

        # Limit Inputs.
        allowableTypes = [float, int]
        if not (type(t) == int and type(interestPaid) in allowableTypes):
            raise Exception('Please Enter the appropriate data type (i.e. float/int) for the function above.')
        # Test if interest Due is 0 FIRST.
        # try:

        # ERROR: Do not test with an EMPTY dictionary like this, first:
        # if (not self.interestDueVal[t]) and t: # t has to be non-zero.
        #     raise ValueError(f'Payment not accepted... Current Interest Due at t = {t} is already 0.')
        # SOLUTION:
        self.interestDueVal[t] = self.interestDue(t) # Initialize this first to Allow IF to test
                # self.interestDueVal[t] == 0 without getting an empty dictionary error.

        if (not self.interestDueVal[t]) and t: # t has to be non-zero.
            self.interestPayment[t] = 0
            self.interestDueVal[t] = 0
            self.interestShortfall[t] = 0
            raise ValueError(f'Payment not accepted... Current Interest Due at t = {t} is already 0.')

        # Test if interest Payment has only been recorded once.
        elif not self.calledmakeintPay[t]:
            self.interestPayment[t] = interestPaid

            # self.interestShortfall[t] = (self.interestDueVal[t] - interestPaid) if self.interestDueVal > interestPaid else 0 # Similar with Excel
            self.interestShortfall[t] = (self.interestDueVal[t] - interestPaid) if self.interestDueVal[t] > interestPaid else 0 # Similar with Excel
            self.calledmakeintPay[t] = 1
            return logging.debug(f'Interest Payment of {self.interestPayment[t]} has been paid for period = {t}, with Interest Shortfall = {self.interestShortfall[t]}.')

        else:
            raise ValueError(f'Interest has already been recorded for period t = {self.t}.')
        # except Exception as generalError:
        #     logging.info('Please enter a either a float/integer for each of the inputs of makeInterestPayment.')
        #     logging.info(f'Exception: {generalError}')

    def notionalBalance(self, t): # Conditional on whether makeInt... and makePrin have been called.
        '''
        Calculates the balance of the notional that the tranche is owed at period t
        :param t: @ period t
        '''

        # Limit Inputs.
        if type(t) != int:
            raise Exception('Please Enter the appropriate data type (i.e. int) for the function above.')

        # try:
        if not t:
            self.notionalBalanceVal[t] = self._notional

        else: # If t!=0, makepay/int will always record interest paid, and if they record pay/int, can calculate notionalBalance
            # prinPayColl = [self.prinPayColl[i] for i in self.prinPayColl.keys() if i <= t] # get list based on keys (in this case, t) <= t
            # intSFColl = [self.intSFColl[i] for i in self.intSFColl.keys() if i <= t]  # get list based on keys (in this case, t) <= t

            # self.notionalBalanceVal[t] = self._notional - sum([self.principalPayment[i] for i in self.principalPayment.keys() if i <= (t)]) # VALIDATED IN EXCEL
            self.notionalBalanceVal[t] = self._notional - sum(self.principalPayment[i] for i in self.principalPayment.keys() if i <= (t))  # VALIDATED IN EXCEL
            # GENERATOR USED
            # Sanity Note: VALUE AT t = n is used t calculated stuff for t = n + 1

            # - sum([self.interestShortfall[i] for i in self.interestShortfall.keys() if i <= (t)])... Interest non-compounding. apply this instead to int due.

        return self.notionalBalanceVal[t]
        # except Exception as generalError:
        #     logging.info('Please enter a either a float/integer for each of the inputs of notionalBalance.')
        #     logging.info(f'Exception: {generalError}')

    def interestDue(self, t):
        '''
        Calculates the interest that the tranche is owed at period t
        :param t: @ period t
        '''

        # Limit Inputs.
        if type(t) != int:
            raise Exception('Please Enter the appropriate data type (i.e. int) for the function above.')

        # try:
        if not t:
            self.interestDueVal[t] = 0
            return self.interestDueVal[t]
        else:
            notionalBalanceforID = self.notionalBalance(max(0,t-1))
            self.interestDueVal[t] = StandardTranche.monthlyRate(self._rate) * notionalBalanceforID \
                                        + self.interestShortfall[max(0,t-1)] # version 2: see excel file (Only interest shortfall at t)
                                        # + sum([self.interestShortfall[i] for i in self.interestShortfall.keys() if i <= (t-1)]) # incorporates previous shortfalls
                                        # "gets added to the interest owed next period, THEREFORE t-1"
            return self.interestDueVal[t]
        # except Exception as generalError:
        #     logging.info('Please enter a either a float/integer for each of the inputs of interestDue.')
        #     logging.info(f'Exception: {generalError}')

    def reset(self):
        '''
        WARNING: RESETS TRANCHE CLASS VARIABLES.
        '''

        # Reset All Variables

        # New class variables. Dictionary Variables START AT ZERO per excel file.
        # * add._ if parameter, no ._ if not parameter (i.e. allow to access outside the function)
        # For flag

        # self.subLevel = 0 (do not reset)

        # For Tranche Metrics (From standard_tranche.py)
        self.t = 0
        self.principalPayment = {self.t: 0} # self.principalpayment[self.t] = 0
        self.notionalBalanceVal = {self.t: 0}  # Notional Balance, set to 0 at time 0 (like in excel). Values to be entered in the notionalBalance function
        self.interestPayment = {self.t: 0}
        self.interestDueVal = {self.t: 0}
        self.interestShortfall = {self.t: 0}
        # REMOVE self.prinPayColl = {} # Call this also in makePrincipalPayment. Causes circularity
        # REMOVE self.intSFColl = {}  # Call this also in makeInterestPayment. Causes circularity

        # Modification: add self.boolean for makeprincipalPayment and makeinterestPayment instead of testing whether the value of result == 0
        # Reason: Can be zero even if called if fully paid / t == 0.
        self.calledmakeprinPay = {self.t: 0} # Won't work, do not change to {0: 0} for sanity check
        self.calledmakeintPay = {self.t: 0} # Won't work, do not change to {0: 0} for sanity check

        # Modification (Structured Securities):
        self.principalDue = {self.t: 0}
        self.principalSF = {self.t: 0}

        # Tranche Metrics
        self.irr = 0
        self.dirr = 0
        self.al = 0
        self.dirrLetter = 0
        self.altprincipalPayment = []
        self.newprinPayment = {0: 0}

        # MC Metrics
        # self.alDict = {}. Collects AL as NSIM. Do not change.
        # self.dirrDict = {}. Collects dirr as NSIM. Do not change.

        '''
        self.t = 0
        self.principalPayment = {self.t: 0} # self.principalpayment[self.t] = 0
        self.notionalBalanceVal = {self.t: 0}  # Notional Balance, set to 0 at time 0 (like in excel). Values to be entered in the notionalBalance function
        self.interestPayment = {self.t: 0}
        self.interestDueVal = {self.t: 0}
        self.interestShortfall = {self.t: 0}
        # self.prinPayColl = {} # Call this also in makePrincipalPayment. Causes circularity
        # self.intSFColl = {}  # Call this also in makeInterestPayment. Causes circularity

        # Modification: add self.boolean for makeprincipalPayment and makeinterestPayment instead of testing whether the value of result == 0
        # Reason: Can be zero even if called if fully paid / t == 0.
        self.calledmakeprinPay = {self.t: 0} # Won't work, do not change to {0: 0} for sanity check
        self.calledmakeintPay = {self.t: 0} # Won't work, do not change to {0: 0} for sanity check

        # Modification (Structured Securities):
        self.principalDue = {self.t: 0}
        self.principalSF = {self.t: 0}
        '''

        return logging.info(f'Tranche {self.__class__.__name__}\'s attributes have been reset to their original state (t = 0).')