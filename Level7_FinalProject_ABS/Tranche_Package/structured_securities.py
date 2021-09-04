'''
Structured Securities:
(1) Create a class called StructuredSecurities. This will be a composition of Tranche objects.
    It should be initialized with a total Notional amount.

(2) Contains Associated Functions such as GETWATERFALL and DOWATERFALL
'''

from Tranche_Package.standard_tranche import StandardTranche # Always a standard tranche
from Loan_Package.loan_pool import LoanPool

import logging
import operator
import math
import multiprocessing

############################################
######## Structured Security Object ########
############################################

class StructuredSecurities(object):
    # (1) Initialization Functions
    def __init__(self, totalNotional):
        '''
        This is the initialization function for the Structured Securities class:
        :param totalNotional: Total Notional
        '''

        # Parameter Variables
        # Ensure we are pulling numbers for rate/notional
        if (isinstance(totalNotional, float) or isinstance(totalNotional, int)):
            logging.info('\nAcceptable totalNotional input has been entered. Instantiating structured security...')
            self._totalNotional = totalNotional
        else:
            # 'Ensure that the asset parameter indeed contains an Asset object / any of its derived classes'
            logging.error('\nPlease enter a correct total notional input (float / integer). Exiting...')
            raise TypeError('Please enter a correct total notional input (float / integer). Exiting...')

        # Other variables
        self._t = 0  # Need to keep track of time periods (i.e. for when shortfalls occur/new cash from loans arrives...)
        self._mode = 0 # flag
        self._availableFunds = {self._t: 0} # Cash Balance, set to 0 at time 0 (like in excel). Sum of Collections and Reserves.
        self._trancheList = [] # tranche object
        self._istrancheAPaid = False
        self._prinrecfromLP = {self._t: 0} # Principal Collections, set to 0 at time 0 (like in excel). Sum of Principal Collection for all tranches.
        self._reserveAccount = {self._t: 0} # what is left after paying from principalrecfromLP.
        self._balanceA = 0
        self._runCounter = 0

    # Important function:
    # addTranche Function - Instantiate and add the tranche to the Structured Security's Internal List of Tranches
    def addTranche(self, trancheName, notionalPercent, rate, flagInput):
        '''
        This function allows the class to take in a (1) tranche name (2) percent of notional (3) rate (4) flag.
        :param trancheName: Name of Standard Tranche object.
        :param notionalPercent: Percent of total notional.
        :param rate: Interest rate.
        :param flag: Level of subordination flag.
        '''

        # Limit Inputs.
        if not (type(trancheName) == str and type(notionalPercent) == float and type(rate) == float): # flagInput already has a limiter w/in fnx
            raise Exception('Please Enter the appropriate data type (i.e. str/float) for the function above.')

        # Set addTranche Limits... (Only 2 tranches)
        if len(self._trancheList) > 2:
            logging.error('\nMaximum of two tranches only. Exiting...')
            raise TypeError('Maximum of two tranches only. Exiting...')
        else:
            logging.info(f'\n1 Tranche has been entered. {2 - len(self._trancheList)} slot(s) remain...')

        try:
            # Initialize tranche object
            logging.debug(f'\nInstantiating Standard Tranche with name {trancheName}...')
            placeHolder = StandardTranche(rate, notionalPercent * self._totalNotional)

            # set flag
            logging.debug(f'Setting flag for {trancheName} = {flagInput}...')
            placeHolder.flagsubLevel(flagInput)

            forAppend = locals()[trancheName] = placeHolder

            # append
            self._trancheList.append(forAppend)

        except ValueError as valError:
            logging.info('Wrong Value has been inputted (e.g. rate and notionalPercent are not numbers of the form 0.00), please try again.')
            logging.info(f'Exception: {valError}')

        except Exception as generalError:
            logging.info('Object has not been appended, please try again.')
            logging.info(f'Exception: {generalError}')


    # (2) Getters and Setters
    # Property Getter and Setter

    # totalNotional
    @property
    def totalNotional(self):
        return self._totalNotional

    @totalNotional.setter
    def totalNotional(self, itotalNotional):
        self._totalNotional = itotalNotional

    # t
    @property
    def t(self):
        return self._t

    @t.setter
    def t(self, it):
        self._t = it

    # mode
    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, imode):
        self._mode = imode

    # availableFunds
    @property
    def availableFunds(self):
        return self._availableFunds

    @availableFunds.setter
    def availableFunds(self, iavailableFunds):
        self._availableFunds = iavailableFunds

    # tranche Pool
    @property
    def trancheList(self):
        return self._trancheList

    @trancheList.setter
    def trancheList(self, itrancheList):
        self._trancheList = itrancheList

    # istrancheAPaid
    @property
    def istrancheAPaid(self):
        return self._istrancheAPaid

    @istrancheAPaid.setter
    def istrancheAPaid(self, iistrancheAPaid):
        self._istrancheAPaid = iistrancheAPaid

    # prinrecfromLP
    @property
    def prinrecfromLP(self):
        return self._prinrecfromLP

    @prinrecfromLP.setter
    def prinrecfromLP(self, iprinrecfromLP):
        self._prinrecfromLP = iprinrecfromLP

    # reserveAccount
    @property
    def reserveAccount(self):
        return self._reserveAccount

    @reserveAccount.setter
    def reserveAccount(self, ireserveAccount):
        self._reserveAccount = ireserveAccount

    # balanceA
    @property
    def balanceA(self):
        return self._balanceA

    @balanceA.setter
    def balanceA(self, ibalanceA):
        self._balanceA = ibalanceA


    # (3) Methods:
    # Flag Method (Sequential / Pro Rata)
    def flagMode(self, mode):
        '''
        Takes a mode input to instruct the structured security on how to handle the payments coming form the
        assets to service the liabilities.
        :param mode: Sets structured securities to handle payments sequentially or on a pro rata basis
        '''

        modesList = ['Sequential', 'Pro Rata']

        if mode not in modesList:
            logging.error('\nPlease enter a correct flag (Sequential/Pro Rata). Exiting...')
            raise TypeError('Please enter a correct flag (Sequential/Pro Rata). Exiting...')
        else:
            self._mode = mode
            logging.info(f'\nCash flows will be distributed on a {self._mode} basis.')
            return self._mode

    # Add a method that increases the current time period for each tranche.
    def increaseSSTimePeriod(self):
        '''
        Increase time period of (1) structured security and (2) tranches by 1.
        '''

        self._t = self._t + 1 # (1) Updating StructuredSecurity t (SSTimePeriod)

        for tranche in self._trancheList: # (2) Updating tranche... So that they move together.
            tranche.increaseTimePeriod() # Better than just increasing time period for SST and using that because tranche has increaseTimePeriod fnx.

        return self._trancheList

    # Store LP Principal Payments fnx:
    ## 'Principal due to the tranches are based on the TOTAL PRINCIPAL RECEIVED from the Loans in a given period.'
    def getprinPut(self, prinPut, t):
        '''
        Saves total principal due from a loan pool object
        :param prinPut: Total principal due from Loan Pool Object
        :param t: @ period t
        '''

        # Get principal payments from asset
        if t < 0:
            logging.error('Please enter a correct flag (Sequential/Pro Rata). Exiting...')
            raise ValueError('Please pass through a valid t (t>=0). Exiting...')
        else:
            self._prinrecfromLP[t] = prinPut
            return self._prinrecfromLP[t]


####################################################################################################
####### SUPERMETHOD (DIFFICULT). TIP: USE THE WATERFALL EXAMPLE EXCEL FILE TO SAVE YOURSELF. #######
####################################################################################################

    # Make Payments methods (Superfunction to allocate payments at t for interest and principal, in both tranches)
    def makePayments(self, cash_amount, prinPut): # cash_amount includes int and prin pay (EXCEL)
        '''
        Cycles through all the tranches, in order of subordination, paying each tranche from the available cash amount.
        Cycle (FR EXCEL): Total Collections (Prin, Int, Reserve(t-1) - Int Paid (A) - Int Paid (B) - Prin Paid (A) - Prin Paid (B)
        Cycle (EXPENSES): TR(A) Interest -> TR(B) Interest -> TR(A) Principal -> TR(B) Principal

        Inputs:
        (1) cash_amount: Total monthly payment to Loan Pool Object
        (2) prinPut: Principal Owed at period t
        '''

        if not len(self._trancheList):
            logging.error('Tranche List cannot be empty. Exiting...')
            raise ValueError('Tranche List cannot be empty. Exiting...')
        else:
            logging.debug('Tranche List contains at least 1 tranche. Proceeding...')

        # Set-up:
        self._istrancheAPaid = 0 # Set ispaid to 0 for interest and principal: Marker for interest tranche A payment
        self._availableFunds[self._t] = cash_amount + self._reserveAccount[max(self._t - 1, 0)] # Prepare Cash Amount (TOTAL)
            # 'supplement cash account in next...' DIFFERENT FROM EXCEL
        self._trancheList = sorted(self._trancheList, key=operator.attrgetter("subLevel")) # Sort trancheList to loop A first then B.
            # Also for getting balanceA

        # TEST: (LOOKS GOOD)
        # logging.info(f'\n{self._t}')
        # logging.info(f'Cash Amount: {cash_amount}')
        # logging.info(f'Reserve Account: {self._reserveAccount[max(self._t - 1, 0)]}')
        # logging.info(f'Available Funds: {self._availableFunds[self._t]}')

        # Get prinPutVal and balanceA:
        # prinPutVal = self.getprinPut(prinPut, self._t)  # Set self._prinrecfromLP = prinPut
        balanceA = self.trancheList[0]._notional

        ###############################
        ###### interest payments ######
        ###############################
        for tranche in self._trancheList:
            if tranche.subLevel == 'A':
                # Check interest due and make the payment
                interestOwed = tranche.interestDue(tranche.t) # standard_tranche function
                payment = min(interestOwed, self._availableFunds[self._t]) # structured_securities (same with excel)

                # Make the Payment (ADD: If raise Error (due to call int pay only once), this step will be skipped if we have a try except)...
                try:
                    tranche.makeInterestPayment(tranche.t, payment) # make the payment, record in the tranche object if there is a shortfall
                except Exception as generalError:
                    logging.debug(f'Exception: {generalError}') # from INFO to DEBUG as this will get printed repeatedly when we get an error. It gets worse when a random component is added.

                # Subtract the amount from available funds
                self._availableFunds[self._t] = self._availableFunds[self._t] - payment # Deduct payment afterwards (Exce

                # Set tranche A paid:
                self._istrancheAPaid = 1

            elif self._istrancheAPaid == 1 or self._availableFunds[self._t] == 0: # accounts for case where tranche A interest is not paid but still need to record tranche values
                # Check interest due and make the payment
                interestOwed = tranche.interestDue(tranche.t) # standard_tranche function
                payment = min(interestOwed, self._availableFunds[self._t]) # structured_securities (same with excel)

                # Make the Payment (ADD: If raise Error (due to call int pay only once), this step will be skipped if we have a try except)...
                try:
                    tranche.makeInterestPayment(tranche.t, payment) # make the payment, record in the tranche object if there is a shortfall
                except Exception as generalError:
                    logging.debug(f'Exception: {generalError}') # from INFO to DEBUG as this will get printed repeatedly when we get an error. It gets worse when a random component is added.

                # TEST: logging.info(f'\nInterest Payment (Seq B): {payment}')
                # Subtract the amount from available funds
                self._availableFunds[self._t] = self._availableFunds[self._t] - payment # Deduct payment afterwards (Excel)
                # Already net of payment for tranche A

        # NOTE (7.23.2021): interest payments are good to go. Checked with EXCEL.
        # At this point, self._availableFunds now net of principalPayment to tranche 1 and tranche 2

        ################################
        ###### principal payments ######
        ################################
        ## BASED ON TOTAL PRINCIPAL RECEIVED FROM LOANS IN A GIVEN PERIOD (not total available cash)
        # * self._availableFunds[self._t] = self._availableFunds[self._t] + prinPutVal # Add prinPutVal as this is added to interest to get total cash.
        # * EXCEL: Add Prin Due (Owed) and Prin SF to Tranche as these are needed in the calculations

        if self.mode == 'Sequential': # else 'Pro Rata' # Ask for balance and pay min (min(principal received + prior principal shortfalls, available cash, balance))
            for tranche in self._trancheList: # Cycle through each tranche (in order of subordination), making the maximum principal payment
                if tranche.subLevel == 'A':
                    # Derive inputs for prinOwed:
                    balance = tranche.notionalBalance(max(tranche.t - 1, 0)) # Get Balance. Negative t has been accounted for in standard_tranche
                    prinArg = self.getprinPut(prinPut, self._t) + tranche.principalSF[max(tranche.t - 1, 0)] # Negative t has been accounted for in standard_tranche

                    # Arguments for makePrinPayment
                    prinOwed = min(balance, prinArg)
                    payment = min(prinOwed, self._availableFunds[self._t]) # if available funds = 0, no payment condition is fulfilled.
                    principalSF = prinOwed - payment

                    # Make the Payment (ADD: If raise Error (due to call int pay only once), this step will be skipped if we have a try except)...
                    try:
                        tranche.makePrincipalPayment(tranche.t, payment, prinOwed, principalSF)  # makePrincipalPayment: principalPaid, principalDue, principalSF
                    except Exception as generalError:
                        logging.debug(f'Exception: {generalError}') # from INFO to DEBUG as this will get printed repeatedly when we get an error. It gets worse when a random component is added.

                    # self._changePrin = prinPutVal - payment
                    self._availableFunds[self._t] = self._availableFunds[self._t] - payment # Deduct from funds (Excel). prinPut only for prinCalc, NOTHING MOR

                    # Correct Dictionary (For Presentation):
                    tranche.newprinPayment[tranche.t+1] = tranche.principalPayment[tranche.t]

                elif tranche.subLevel == 'B':
                    # Derive inputs for prinOwed:
                    balance = tranche.notionalBalance(max(tranche.t - 1, 0)) # Get Balance (tranche B)
                    # cumPrin = sum([self._prinrecfromLP[i] for i in self._prinrecfromLP.keys() if i <= (self._t)]) # Cumulative principal @ t
                    cumPrin = sum(self._prinrecfromLP[i] for i in self._prinrecfromLP.keys() if i <= (self._t))  # GENERATOR: Cumulative principal @ t
                    balance2 = balanceA # Balance of Tranche A at t = 0
                    # cumPrinminus1 = sum([self._prinrecfromLP[i] for i in self._prinrecfromLP.keys() if i <= (max(0, self._t-1))]) # Cumulative principal @ t - 1
                    cumPrinminus1 = sum(self._prinrecfromLP[i] for i in self._prinrecfromLP.keys() if i <= (max(0, self._t - 1)))  # GENERATOR: Cumulative principal @ t - 1
                    principalSF = tranche.principalSF[max(0, self._t-1)] # Shortfall @ t - 1

                    # Arguments for makePrinPayment
                    prinOwed = min(balance, max(0, cumPrin - max(balance2, cumPrinminus1))) + principalSF # this is what is meant by the tear-jerking statement in sequential
                    payment = min(prinOwed, self._availableFunds[self._t]) # if available funds = 0, no payment condition is fulfilled.
                    principalSF = prinOwed - payment

                    # Make the Payment (ADD: If raise Error (due to call int pay only once), this step will be skipped if we have a try except)...
                    try:
                        tranche.makePrincipalPayment(tranche.t, payment, prinOwed, principalSF)  # makePrincipalPayment: principalPaid, principalDue, principalSF
                    except Exception as generalError:
                        logging.debug(f'Exception: {generalError}') # from INFO to DEBUG as this will get printed repeatedly when we get an error. It gets worse when a random component is added.

                    # self._changePrin = prinPutVal - payment
                    self._availableFunds[self._t] = self._availableFunds[self._t] - payment # Deduct from funds (Excel). prinPut only for prinCalc, NOTHING MOR
                    # TEST: logging.info(f'Available Funds (Seq B): {self._availableFunds[self._t]}')
                    # TEST: logging.info(f'Payment (Seq B): {payment}')

                    # Correct Dictionary (For Presentation):
                    tranche.newprinPayment[tranche.t + 1] = tranche.principalPayment[tranche.t]

                    # Reserve storage...
                    self._reserveAccount[self._t] = self._availableFunds[self._t]


        elif self.mode == 'Pro Rata':
            for tranche in self._trancheList: # Cycle through each tranche (in order of subordination), making the maximum principal payment
                if tranche.subLevel == 'A' or (tranche.subLevel == 'A' and self._availableFunds[self._t] == 0):
                    # Derive inputs for prinOwed:
                    balance = tranche.notionalBalance(max(tranche.t - 1, 0)) # Get Balance
                    prinArg = self.getprinPut(prinPut, self._t) * (tranche._notional / self._totalNotional) + tranche.principalSF[max(tranche.t - 1, 0)]

                    # Arguments for makePrinPayment
                    prinOwed = min(balance, prinArg)
                    payment = min(prinOwed, self._availableFunds[self._t]) # if available funds = 0, no payment condition is fulfilled.
                    principalSF = prinOwed - payment

                    # Make the Payment (ADD: If raise Error (due to call int pay only once), this step will be skipped if we have a try except)...
                    try:
                        tranche.makePrincipalPayment(tranche.t, payment, prinOwed, principalSF)  # makePrincipalPayment: principalPaid, principalDue, principalSF
                    except Exception as generalError:
                        logging.debug(f'Exception: {generalError}') # from INFO to DEBUG as this will get printed repeatedly when we get an error. It gets worse when a random component is added.

                    # self._changePrin = prinPutVal - payment
                    self._availableFunds[self._t] = self._availableFunds[self._t] - payment # Deduct from funds (Excel). prinPut only for prinCalc, NOTHING MORE

                    # Correct Dictionary:
                    tranche.newprinPayment[tranche.t + 1] = tranche.principalPayment[tranche.t]

                elif tranche.subLevel == 'B' or (tranche.subLevel == 'B' and self._availableFunds[self._t] == 0):
                    # Derive inputs for prinOwed:
                    balance = tranche.notionalBalance(max(tranche.t - 1, 0)) # Get Balance
                    prinArg = self.getprinPut(prinPut, self._t) * (tranche._notional / self._totalNotional) # + tranche.principalSF[max(tranche.t - 1, 0)] (Added to MIN)

                    # Arguments for makePrinPayment
                    prinOwed = min(balance, prinArg) + tranche.principalSF[max(tranche.t - 1, 0)]
                    payment = min(prinOwed, self._availableFunds[self._t]) # if available funds = 0, no payment condition is fulfilled.
                    principalSF = prinOwed - payment

                    # Make the Payment (ADD: If raise Error (due to call int pay only once), this step will be skipped if we have a try except)...
                    try:
                        tranche.makePrincipalPayment(tranche.t, payment, prinOwed, principalSF)  # makePrincipalPayment: principalPaid, principalDue, principalSF
                    except Exception as generalError:
                        logging.debug(f'Exception: {generalError}') # from INFO to DEBUG as this will get printed repeatedly when we get an error. It gets worse when a random component is added.

                    # self._changePrin = self.getprinPut(prinPut, self._t) - payment
                    self._availableFunds[self._t] = self._availableFunds[self._t] - payment # Deduct from funds (Excel). prinPut only for prinCalc, NOTHING MORE

                    # Correct Dictionary:
                    tranche.newprinPayment[tranche.t + 1] = tranche.principalPayment[tranche.t]

                    # Reserve storage...
                    self._reserveAccount[self._t] = self._availableFunds[self._t]


        # NOTE (7.23.2021): principal payments are good to go. Checked with EXCEL.

        return f'Payments for time = {self._t} have been made to the tranches of the StructuredSecurity object.'

        # No need for the else case. Already factored in as payment = 0 if availableFunds = 0.
        # else:
        #     for tranche in self._trancheList:
        #         tranche.makePrincipalPayment(tranche.t, 0, 0, 0) # principalPaid, principalDue, principalSF

    # getWaterfall
    def getWaterfall(self, t):
        '''
        Returns a list of list. Each inner list represents a tranche, and contains the the following values for a given period:
        Int Due, Int Paid, Int SF, Prin Paid, Balance
        '''

        trancheinfoList = []
        for tranche in self._trancheList:
            trancheinfoList.append([tranche.interestDueVal[t], tranche.interestPayment[t], tranche.interestShortfall[t],
                                    tranche.newprinPayment[t], tranche.notionalBalanceVal[t]]) # tranche.principalPayment[t]
        trancheinfoList.append([self._reserveAccount[t]]) # (*) ... as well as any amount in the reserve account (from doWaterfall)
                # Has to be a list for list flattening to work
        return trancheinfoList

    # Ensure 0 Start to waterfall
    def cleanSlate(self):
        '''
        Reset structured security class variables and all tranche variables.
        '''

        for tranche in self._trancheList:
            tranche.reset()

        # Reset structured securities
        self._t = 0  # Need to keep track of time periods (i.e. for when shortfalls occur/new cash from loans arrives...)
        # self._mode = 0 # flag. DO NOT RESET... has to be sequential / pro rata all throughought NSIM.
        self._availableFunds = {self._t: 0} # Cash Balance, set to 0 at time 0 (like in excel). Sum of Collections and Reserves.
        # self._trancheList = [] # tranche object. DO NOT RESET... No need to specify trancheList again and again throughout NSIM.
        self._istrancheAPaid = False
        self._prinrecfromLP = {self._t: 0} # Principal Collections, set to 0 at time 0 (like in excel). Sum of Principal Collection for all tranches.
        self._reserveAccount = {self._t: 0} # what is left after paying from principalrecfromLP.
        self._balanceA = 0
        # self._runCounter = 0. DO NOT RESET... need to keep track of runCounter throughout NSIM.

        return logging.info('All tranche attributes have been reset to their original state (t = 0).')


    def clearSim(self):
        '''
        Call this before switching between Sequential and Pro Rata. Clears except self._trancheList as this is needed.
        '''

        for tranche in self._trancheList:
            tranche.reset()

        self._t = 0  # Need to keep track of time periods (i.e. for when shortfalls occur/new cash from loans arrives...)
        self._mode = 0 # flag. DO NOT RESET... has to be sequential / pro rata all throughought NSIM.
        self._availableFunds = {self._t: 0} # Cash Balance, set to 0 at time 0 (like in excel). Sum of Collections and Reserves.
        # self._trancheList = [] # tranche object. DO NOT RESET... No need to specify trancheList again and again throughout NSIM.
        self._istrancheAPaid = False
        self._prinrecfromLP = {self._t: 0} # Principal Collections, set to 0 at time 0 (like in excel). Sum of Principal Collection for all tranches.
        self._reserveAccount = {self._t: 0} # what is left after paying from principalrecfromLP.
        self._balanceA = 0
        self._runCounter = 0


#####################################
###### Waterfall Formulas ###########
#####################################


# Create a standalone function called doWaterfall
def doWaterfall(LPObject, StructSecObject):
    '''
    This function should take two parameters: A LoanPool object and a StructuredSecurities object.
    The function should loop through time periods, starting from 0, and keep going until the LoanPool
    has no more active loans (no more payments coming from the LoanPool).
    '''

    # Ensure we are pulling numbers for rate/notional
    if isinstance(LPObject, LoanPool) and isinstance(StructSecObject, StructuredSecurities):
        logging.debug('\nAcceptable Loan Pool and Structured Security have been entered. Running doWaterfall...')
    else:
        # 'Ensure that the asset parameter indeed contains an Asset object / any of its derived classes'
        logging.error('\nPlease enter a Loan Pool object or a Structured Security Object in the appropriate order (LP, Structured Security). Exiting...')
        raise ValueError('Please enter a Loan Pool object or a Structured Security Object in the appropriate order (LP, Structured Security). Exiting...')

    results = [] # Liabilities results list
    results2 = []  # Assets results list

    logging.info('\nLiabilities:')
    logging.info('Each list in the list contains:')
    logging.info('(1) Tranche A Output')
    logging.info('(2) Tranche B Output (If two tranches are entered)')
    logging.info('(3) Reserve Balance/Structured Security Shortfall (appended)')

    logging.info('\n(1) and (2) both contain:')
    logging.info('1. intDue, 2. intPaid, 3. intSF, 4. prinPaid, 5. Balance.')

    logging.info('\nAssets:')
    logging.info('Each list in the list contains:')
    logging.info('(1) Loan Pool Output')

    logging.info('\n(1) contains:')
    logging.info('1. monthlyPay, 2. principalDue, 3. totalBalance, 4. interestDue, 5. activeLoanCount.')

    # Loop through the time periods:
    while LPObject.activeLoanCount(StructSecObject._t):
        # Start with 0.

        # Total Payment to LoanPool for time = t
        ## recoveryAmount = LPObject.totalassetValue(StructSecObject._t)
        cashAmount = LPObject.monthlyPayment(StructSecObject._t) + LPObject.checkDefaults(StructSecObject._t)
        prinAmount = LPObject.principalDue(StructSecObject._t) + LPObject.checkDefaults(StructSecObject._t) # Workaround to match timings
        # prinAmount = LPObject.principalDue(StructSecObject._t - 1) if StructSecObject._t > 0 else 0 # Trades off Early Prin Appearance for EARLY PAY

        ################################################################ Asset Get Waterfall ################################################################
        results2.append([LPObject.monthlyPayment(StructSecObject._t), LPObject.principalDue(StructSecObject._t),
                         LPObject.totalBalance(StructSecObject._t), LPObject.interestDue(StructSecObject._t), LPObject.activeLoanCount(StructSecObject._t)])
        #####################################################################################################################################################

        # Pay the Structured Securities with the amount provided by the LoanPool
        StructSecObject.makePayments(cashAmount, prinAmount)

        # Call getWaterfall(self, t) to get the results for each period t + Save the info to results variable
        ## Already contains LP and Struct Sec Items...
        results.append(StructSecObject.getWaterfall(StructSecObject._t))

        # print(LPObject.activeLoanCount(StructSecObject._t))... Really does do while not zero
        # Add one to t AFTER. Start at 0.
        StructSecObject.increaseSSTimePeriod()

    logging.info('\nResults successfully unpacked.')

    try:
        i = 1
        for tranche in StructSecObject._trancheList:
            logging.info(f'Tranche Metrics for Tranche #{i}:')
            logging.info(f'IRR = {tranche.calcIRR()}') # Returns IRR
            logging.info(f'DIRR = {tranche.calcDIRR()}')  # Returns DIRR
            logging.info(f'AL = {tranche.calcAL()}')  # Returns AL
            # tranche.notionalBalanceVal[len(list(tranche.principalPayment.keys())) - 1] =  TEST to get AL = None... WORKS!
            logging.info(f'Letter Rating = {tranche.convDIRR(tranche.calcDIRR())}\n')  # Returns DIRRLETTER

            '''
            logging.info(f'Letter Rating = {tranche.convDIRR(0.07)}')  # Returns DIRRLETTER
            logging.info(f'Letter Rating = {tranche.convDIRR(0.17)}')  # Returns DIRRLETTER
            logging.info(f'Letter Rating = {tranche.convDIRR(0.56)}')  # Returns DIRRLETTER
            logging.info(f'Letter Rating = {tranche.convDIRR(0)}')  # # Returns DIRRLETTER
            logging.info(f'Letter Rating = {tranche.convDIRR(1000000000000000000000)}')  # Returns N/A
            logging.info(f'Letter Rating = {tranche.convDIRR(-12)}')  # Returns N/A
            logging.info(f'Letter Rating = {tranche.convDIRR(10000)}')  # Returns # Returns DIRRLETTER
            logging.info(f'Letter Rating = {tranche.convDIRR(10001)}')  # Returns # Returns N/A
            '''

            # logging.info(tranche.newprinPayment)
            # logging.info(tranche.principalPayment)

            # Store Results in class variable lists:
            tranche.dirrDict[StructSecObject._runCounter] = tranche.calcDIRR()
            tranche.alDict[StructSecObject._runCounter] = tranche.calcAL() if tranche.calcAL() is not None else 0

            i = i + 1 # Proceed with Next Tranche

    except ValueError as valError:
        logging.info('Wrong Value has been inputted, please try again.')
        logging.info(f'Exception: {valError}')

    except Exception as generalError:
        logging.info('Unknown Error.')
        logging.info(f'Exception: {generalError}')

    StructSecObject._runCounter = StructSecObject._runCounter + 1
    resultsFINAL = [results, results2]
    return resultsFINAL


# Create a standalone function called doWaterfall
def simulateWaterfall(LPObject, StructSecObject, NSIM):
    '''
    Runs doWaterfall, NSIM times.

    :param LPObject: Loan Pool Object
    :param StructSecObject: Structured Security Object
    :param NSIM: Number of Simulations
    '''

    # Note: sum([0, None]) is an error, therefore need to set None to 0.
    for i in range(NSIM):

        # doWaterfall simulations
        doWaterfall(LPObject, StructSecObject)

        # Reset (Need to reset LPObject as well else defaulted loans will stay defaulted and cash flows will be impacted)
        StructSecObject.cleanSlate()
        LPObject.resetdefaultparams()

    # Create lists to store results for each tranche, and then use for Loop to store to these lists
    aveDIRRfinal= []
    aveALfinal = []

    for tranche in StructSecObject._trancheList:
        aveDIRR = sum(tranche.dirrDict.values()) / len(tranche.dirrDict.values())
        aveAL = sum(tranche.alDict.values()) / len([item for item in list(tranche.alDict.values()) if item])

        aveDIRRfinal.append(aveDIRR)
        aveALfinal.append(aveAL)

    return [aveDIRRfinal, aveALfinal]


# runMonte (infinite loop)
def runMonte(LPObject, StructSecObject, tolerance, NSIM, numProcesses):
    '''
    Implementation of financial monte carlo to value the ABS.
    # Added input 'numProcesses' for multi-processing.
    '''

    # Do this outside to speed up code (No need to loop this)...
    notionalA = StructSecObject._trancheList[0]._notional  # Old Tranche A Rate
    notionalB = StructSecObject._trancheList[1]._notional  # Old Tranche B Rate
    totalNotional = notionalA + notionalB

    # Kick-off Infinite Loop:
    runCounter = 1

    while True: # Infinite loop with if break
        # logging.info(f'\nLoop #{runCounter}')

        # Run simulateWaterfall and store Results
        # result = simulateWaterfall(LPObject, StructSecObject, NSIM)
        result = simulateWaterfallParallel(LPObject, StructSecObject, NSIM, numProcesses) # New functino for multi-processing
        logging.info('\nFinished simulating waterfall, calculating fair rate for ABS...')

        # Get DIRR and AL for each tranche.
        tr1aveDIRR = result[0][0]
        tr1aveAL = result[1][0]
        tr2aveDIRR = result[0][1]
        tr2aveAL = result[1][1]
        '''
        From main. Sample
        logging.info(f'\nTranche 1 average DIRR: {results[0][0]}')
        logging.info(f'Tranche 2 average DIRR: {results[0][1]}')
        logging.info(f'Tranche 1 average AL: {results[1][0]}')
        logging.info(f'Tranche 2 average AL: {results[1][1]}\n')
        '''

        # Yield Calculation based on old tranche rates and calculateYield via relaxation (to speed up conversion)
        yieldResultA = calculateYield(tr1aveDIRR, tr1aveAL)
        yieldResultB = calculateYield(tr2aveDIRR, tr2aveAL)

        newTranchRateA = StructSecObject._trancheList[0]._rate + 1.2 * (yieldResultA - StructSecObject._trancheList[0]._rate)
        newTranchRateB = StructSecObject._trancheList[1]._rate + 0.8 * (yieldResultB - StructSecObject._trancheList[1]._rate)

        # Check if the new tranche rate differs from the previous tranche rate, for each tranche, by more than TOLERANCE:
        ## Other Inputs:
        # notionalA = StructSecObject._trancheList[0]._notional # Old Tranche A Rate
        # notionalB = StructSecObject._trancheList[1]._notional # Old Tranche B Rate
        # totalNotional = notionalA + notionalB
        oldTranchRateA = StructSecObject._trancheList[0]._rate # Old Tranche A Rate
        oldTranchRateB = StructSecObject._trancheList[1]._rate # Old Tranche B Rate

        # Calculate Difference
        diff = diffFRTol(notionalA, notionalB, totalNotional, oldTranchRateA, newTranchRateA, oldTranchRateB, newTranchRateB)

        if diff > tolerance: # Test this first
            # This is why it's key NOT to modify trancheList / i.e. exclude it from the reset functions. Else you erase your exsiting tranches and cannot do a modification.
            StructSecObject._trancheList[0]._rate = yieldResultA  # Old Tranche A Rate
            StructSecObject._trancheList[1]._rate = yieldResultB  # Old Tranche B Rate

            runCounter = runCounter + 1
            logging.info(f'Difference between yields and old rates is not yet within acceptable tolerance (tol = {tolerance}). Re-calculating...')

        else: # Break Condition
            break

    # Convert DIRR to rating
    tr1Rating = StructSecObject._trancheList[0].convDIRR(tr1aveDIRR) # Convert to Rating
    tr2Rating = StructSecObject._trancheList[1].convDIRR(tr2aveDIRR)  # Convert to Rating

    # Results:
    logging.info('\nSuccessfully ran the monte carlo simulation!')
    logging.info(f'Fair rates were calculated after {runCounter} iterations.')

    logging.info('\n################################################################')
    # 'Once you receive the results, translate the DIRR to a letter rating and output: DIRR, Rating, WAL, Rate of each tranche.
    logging.info(f'\nTranche 1 RESULTS:')
    logging.info(f'Tranche 1 Average DIRR: {tr1aveDIRR}')
    logging.info(f'Tranche 1 Rating: {tr1Rating}')
    logging.info(f'Tranche 1 Average AL: {tr1aveAL}')
    logging.info(f'Tranche 1 Fair Yield: {yieldResultA}')

    logging.info(f'\nTranche 2 RESULTS:')
    logging.info(f'Tranche 2 Average DIRR: {tr2aveDIRR}')
    logging.info(f'Tranche 2 Rating: {tr2Rating}')
    logging.info(f'Tranche 2 Average AL: {tr2aveAL}')
    logging.info(f'Tranche 2 Fair Yield: {yieldResultB}\n')
    logging.info('################################################################\n')

    return [[tr1aveDIRR, tr1aveAL, tr1Rating, yieldResultA], [tr2aveDIRR, tr2aveAL, tr2Rating, yieldResultB]]


# Monte Carlo Sub-formulas:
# Measures NEW fair yield based on waterfall metrics
def calculateYield(aveDIRR, aveAL):
    '''
    Calculates the yield rate using passed-in average DIRR and average AL using a formula.
    :param aveDIRR
    :param aveAL
    '''

    yieldResult =((7/(1 + (.08 * math.exp(-.19 * (aveAL / 12))))) + (.019 * (math.sqrt((aveAL / 12) * (aveDIRR * 100)))))/100
    return yieldResult

# Measures Difference between new yield and old yield
def diffFRTol(notionalA, notionalB, totalNotional, lastARate, newARate, lastBRate, newBRate):
    '''
    This function calculates the difference between the new tranche rate and the old tranche rate via a formula.
    '''

    diff = ((notionalA * abs((lastARate - newARate)/lastARate)) + (notionalB * abs((lastBRate - newBRate)/lastBRate))) / totalNotional
    return diff


#####################################
### Concurrency: Multi-processing ###
#####################################

# (1) Run Simulation (Inner Code)
# if inputs to this f is more than 1, add more to the arguments tuple...
# def simulateWaterfall(a, b, c):
#    Already
#    Coded
#    Above

# (2) doWork
# Function to interact with input queue and output queue (main process)
# Also Starts an INFINITE LOOP. At each iteration, calls get on input queue
def doWork(input, output): # Input_queue and output_queue
    f, args = input.get(timeout=1) # Unpacking the tuple (function name, parameters). Fully created before processes start. Don't want it to block. If anytime time takes more than 1, stop process.
    res = f(*args) # Call function with list of arguments
    # len(res)... Do this instead below.
    output.put(res)
    # output.put('Done') # In the do work, also seen in the main process
    # Removed as a potential site of slowness (per QuantNet)


# MultiProcessing
def simulateWaterfallParallel(LPObject, StructSecObject, NSIM, numProcesses):
    '''
    New simulateWaterfall Function to allow for multiprocessing.
    '''

    nsimInput = max(round(NSIM/numProcesses), 1) # Rounds down.

    ###: I. QUEUE II. PROCESS
    # STEP 1: Create Queue Objects
    # POI 1 - QUEUE. Threadsafe / Process-safe. Visible to any process with a handle to this queue
    input_queue = multiprocessing.Queue() # WHAT WE WANT THE PROCESSES TO DO
    output_queue = multiprocessing.Queue() # RESULTS after all the processes finish

    # STEP 2: Process to put on to the Queue
    # ALREADY HAVE TIMER CONTEXT MANAGER!... s = time.time() # how long process takes
    for i in range(numProcesses): # The NSIM argument for runSimulation should be NSIM divided by numProcesses (i.e. nsimInput)
        input_queue.put((simulateWaterfall, (LPObject, StructSecObject, nsimInput)))  # QUEUE (FIFO) ... STACK (LIFO)

    #################################
    ####### Main Process Code #######
    #################################

    # STEP 3: Create n Child Processes. Start FIVE Processes. Function gets called upon starting.
    processList = []  # for join/terminate per tips and tricks
    for i in range(numProcesses):
        p = multiprocessing.Process(target=doWork, args = (input_queue, output_queue)) # target = kwarg, function that you want the process to call (doWork). args -> Passed into doWork
        p.start() # kwarg can be as many as you need. Returns a HANDLE for each start.
        processList.append(p)

    # Step 4 (Creates Infinite Loop, monitors output queue). Starts off as empty.
    ## Other processes ARE RUNNING in the background...

    res = []
    while(True):
        # If this is here, will never start
        # r = output_queue.get() # STARTS OFF AS BLOCK. Takes something off of the queue. Just stays here until output queue contains something... Eventually will contain something as it is MULTIPROCESSING.
        if len(res) != numProcesses: # If contains the word done, DONE (found in do-work process, can be modified to prevent racing problem)
            r = output_queue.get() # [11th hour fix whooo] GET ONLY WHEN NOT EQUAL TO PROCESS. Stop when equal...
            res.append(r) # when it finally contains something, add that to list of results.
        else:
            break

    # Step 5 (stack: difference between terminate/join):
    for process in processList:
        process.join() # Wait till finished, then terminate.

    # FINAL STEP: 'Once the output Queue monitoring loop completes, aggregate and average the resulting tranche metrics
    #              from each process and return these to runMonte.
    # simulateWaterfall retruns a list of [a,b]. Therefore results list = [[[a1,b1], [a2, b2]], ...]]

    # logging.info(res)
    # Get list of results, separated into list of DIRR results and list of AL results
    aveDIRRList = [list[0] for list in res]
    aveALList = [list[1] for list in res]

    # Collate DIRR for tranche i, AL for tranch i
    trADIRRList = [list[0] for list in aveDIRRList]
    trBDIRRList = [list[1] for list in aveDIRRList]
    trAALList = [list[0] for list in aveALList]
    trBALList = [list[1] for list in aveALList]

    # Visual Test:
    # logging.info(trADIRRList)
    # logging.info(trBDIRRList)
    # logging.info(trAALList)
    # logging.info(trBALList)

    # Get Values
    trADIRRFinal = sum(trADIRRList) / len(trADIRRList)
    trBDIRRFinal = sum(trBDIRRList) / len(trBDIRRList)
    trAALFinal = sum(trAALList) / len(trAALList)
    trBALFinal = sum(trBALList) / len(trBALList)

    # Place in list
    resultsFinal = [[trADIRRFinal, trBDIRRFinal], [trAALFinal, trBALFinal]]

    # Guide for creating resultsFinal List: [[tr1DIRR, tr2DIRR], [tr1AL, tr2AL]]
    # aveDIRR = sum(tranche.dirrDict.values()) / len(tranche.dirrDict.values())
    # aveAL = sum(tranche.alDict.values()) / len([item for item in list(tranche.alDict.values()) if item])

    # aveDIRRfinal.append(aveDIRR)
    # aveALfinal.append(aveAL)

    #return [aveDIRRfinal, aveALfinal]

    # ALREADY HAVE TIMER CONTEXT MANAGER!... e = time.time()

    return resultsFinal