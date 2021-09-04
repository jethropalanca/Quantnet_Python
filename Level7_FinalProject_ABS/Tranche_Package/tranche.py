'''
Creates a base Tranche class and it's associated functionalities.
Note: The WATERFALL tracks all the cashflows through each time period, from the pool of loans (assets).
LP Cashflows are ALLOCATED to each tranche.

*Subordination Flag: Class B would be a SUBORDINATE of class A.
'''

import logging
import numpy_financial
import operator


class tranche(object):
    # (1) Initialization Functions
    def __init__(self, rate, notional):
        '''
        This is the initialization function for the tranche class:
        :param rate: Annualized rate
        :param notional: Face value
        :param subLevel: Flag for level of subordination
        '''

        # Ensure we are pulling numbers for rate/notional
        if isinstance(rate, float) and (isinstance(notional, float) or isinstance(notional, int)):
            logging.debug('\nAcceptable rate and notional have been entered. Instantiating tranche...')
            self._notional = notional
            self._rate = rate
        else:
            # 'Ensure that the asset parameter indeed contains an Asset object / any of its derived classes'
            logging.error('\nPlease enter the correct rate (a float) or notional (float / integer). Exiting...')
            raise ValueError('Please enter the correct rate (a float) or notional (float / integer). Exiting...')

        # For flag
        self.subLevel = 0

        # For Tranche Metrics (From standard_tranche.py)
        self.t = 0
        self.principalPayment = {self.t: 0} # self.principalpayment[self.t] = 0
        self.notionalBalanceVal = {self.t: 0}  # Notional Balance, set to 0 at time 0 (like in excel). Values to be entered in the notionalBalance function
        self.interestPayment = {self.t: 0}

        # Waterfall Metrics
        self.irr = 0
        self.dirr = 0
        self.al = 0
        self.dirrLetter = 0
        self.altprincipalPayment = []
        self.newprinPayment = {0: 0}

        # MC Simulation
        self.alDict = {}
        self.dirrDict = {}

    # (2) Getters and Setters
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
    def subLevel(self):
        return self._subLevel

    @subLevel.setter
    def subLevel(self, isubLevel):
        self._subLevel = isubLevel

    #### From standard_tranche ####
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
    ###############################

    # Right way: Subordination
    # ...the percent of notional, the rate, and the subordination level.
    # Setter Function
    # Works well! Is capable of setting isSubordinate and prints status
    # def setisSubordinate(self, subordornot):
    #     self.isSubordinate = subordornot
    #
    #     # Result of function
    #     return self.isSubordinate


    # (3) Method
    # subList flag
    def flagsubLevel(self, subLevel):
        '''
        :param subLevel: Enter A or B to specify tranche priority.
        :return: Returns tranche priority.
        '''

        subLevelList = ['A', 'B']
        if subLevel not in subLevelList:
            logging.error('Please enter a correct flag (A/B). Exiting...')
            raise ValueError('Please enter a correct flag (A/B). Exiting...')
        else:
            self.subLevel = subLevel
            logging.info(f'This tranche is designated as tranche {self.subLevel}.')
            return self.subLevel


    # self._isSubordinate = None, not general enough (need to take in letters/numbers).
    # Building it this way allows me to specify more tranches in the future if need be.

    ###################################
    ######## Waterfall Metrics ########
    ###################################

    ###################################
    # (1) IRR: Interest Rate that results in the PV of all (monthly) cash flows being equal to the initial investment amount.
    #     numpy_financial.IRR
    #     (*) REALIZED return
    def calcIRR(self):
        '''
        Calculates IRR based on class objects that were populated using structured securities methods, using numpy_financial.irr.
        '''

        # Get notionalBalance[0]
        notionalBalance = self.notionalBalanceVal[0]

        # Get List Values of Principal Payment. Add 0 to Start. Remove 0 from last.
        prinPayList = list(self.principalPayment.values()) # In order cause input was in order...
        prinPayList = prinPayList[:-1] # remove last item of the list. It's okay as actual payment is made at t-1, so self._t payment is not important
        prinPayList.insert(0, 0)  # Insert element to the list
        self.altprincipalPayment = prinPayList # Create a new list for presentation and ROI calculation purposes
        # logging.info(prinPayList)

        # Get List Values of Interest Payment. Combine with Principal Payment
        intPayList = list(self.interestPayment.values()) # In order cause input was in order...
        # logging.info(intPayList)

        # Merge prinPayList and intPayList
        cashflowList = list(map(operator.add, prinPayList, intPayList)) # ADD (operator)
        cashflowList[0] = -notionalBalance # Insert element to the list
        # logging.info(cashflowList)
        self.irr = numpy_financial.irr(cashflowList) * 12
        return self.irr

    ###################################
    # (2) AL: AVERAGE LIFE. Average time that each dollar of a security's UNPAID PRINCIPAL remains unpaid.
    #     Answers length of time to recoup their principal (early in the waterfall or later?)
    #     (*) Never Paid Down: INFINITE AL
    def calcAL(self):
        '''
        Calculates Average Life based on class objects that were populated using structured securities methods.
        '''

        list1 = list(self.principalPayment.keys())
        list2 = self.altprincipalPayment
        # self.al = sum([(list1[i] * list2[i]) for i in range(len(list1))])/self._notional
        self.al = sum((list1[i] * list2[i]) for i in range(len(list1))) / self._notional # Generator

        return self.al if not self.notionalBalanceVal[len(list1) - 1] else None

    ###################################
    # (3) DIRR: REDUCTION IN YIELD. Tranche rate 'Expected' - Annual IRR 'Realized'.
    #     Specifies HOW MUCH THE INVESTOR LOST OUT ON the tranche rate (maximum rate)
    #     Derives LETTER RATING
    def calcDIRR(self):
        '''
        Calculates DIRR based on class object (tranch rate) and saved output from the IRR calculator function.
        '''

        self.dirr = round(self._rate - self.calcIRR(), 6)
        return self.dirr

    # *(4) Converts DIRR to its corresponding letter rating based on the table provided.
    def convDIRR(self, DIRR):
        '''
        Converts generated DIRR from calcDIRR to a letter based on a specified list.
        '''

        DIRR = DIRR * 10000 # To get DIRR in bps (bps/100 = percent, percent/100 = decimal), therefore multiply by 10000

        # dirrBP = DIRR / 100 # 'Might need to convert to BPS to match... (Already in bps).
        ratingsDict = {'Aaa': 0.06, 'Aa1': 0.67, 'Aa2': 1.3, 'Aa3': 2.7, 'A1': 5.2, 'A2': 8.9, 'A3': 13, 'Baa1': 19, 'Baa2': 27,
                       'Baa3': 46, 'Ba1': 72, 'Ba2': 106, 'Ba3': 143, 'B1': 183, 'B2': 231, 'B3': 311, 'Caa': 2500, 'Ca': 10000} # 10,000 bps is 100%

        ratingsList = list(ratingsDict.values()) # use as key in ratingsDict to get corresponding letter

        if DIRR < 0 or DIRR > 10000:
            self.dirrLetter = 'N/A'

        else:
            ratingsAnswer = [1 if DIRR <= item else 0 for item in ratingsList]
            index = ratingsAnswer.index(1)  # 1
            self.dirrLetter = 'N/A' if 1 not in ratingsAnswer else list(ratingsDict.keys())[index]

        '''
        Too Messy... Removed.
        logging.info(f'\nConverting {DIRR/10000} to bps = {DIRR}')
        logging.info('(*) Ratings Table (For Reference):')
        for letter, value in ratingsDict.items():
            logging.info(f'{letter}: Upto {value} bps')  # print ratings
        '''
        return self.dirrLetter