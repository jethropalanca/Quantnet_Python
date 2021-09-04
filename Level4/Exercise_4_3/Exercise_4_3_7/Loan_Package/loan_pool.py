'''
Version 3 (Exercise 3) - Modified Per Avi Palley's comments + WAM / WAR formula changes. Fixed loanObject to raise an error if anything other than Loan object was entered.
This program initializes the LoanPool (demonstrate composition).
'''

from Exercise_4_3.Exercise_4_3_7.Loan_Package.loan import Loan
from functools import reduce
from math import prod
import logging


class LoanPool(object):
    # Initialization Function

    def __init__(self):
        '''
        Version 3_3_4: Iter Function added from HW 3_2_3
        This initialization function to initialize a LoanPool class.
        :param loans: This class takes a loan or a list of loans, or their attributes (i.e. Principal, Balance at t, Aggregate Principal, Interest and Total Payment at t).
        Inputs will be taken by the loanCollect and the loanAttr function.
        '''
        self._loans = []
        # self._loanAttr = []
        # self._loansPrin = []
        # self._loansBal = []
        # self._loansTPrin = []
        # self._loansTInt = []
        # self._loansTDue = []

    # Iter Method (from HW 3_2_3)
    def __iter__(self):
        for loan in self._loans:
            yield loan


    # loanCollect Function

    # 1. Collect Loans (Codefellows):
    def loanCollect(self, loanObject):
        '''
        This function allows the class to take in loanObject which are instantiations of the loans themselves.
        :param loanObject: Any loan object falling under Loan, Variable Rate Loan, or Fixed Rate Loan.
        '''

        if isinstance(loanObject, Loan):
            logging.debug('\nLoans object has been successfully updated.')  # Changed in 4_2_3
            self._loans.append(loanObject)
        else:
            logging.error('Object has not been appended, please input a valid Loan object.')
            raise TypeError('Object has not been appended, please input a valid Loan object.')

    # Return list of loans
    def getloans(self):
        '''
        This function returns a list of loan instantiations.
        '''

        logging.debug('\nReturning list of loans...')  # Changed in 4_2_3
        return self._loans[:]

    # 2. Collect LoanAttr:
    # def loanCollectAttr(self, attrObject):
    #    '''
    #    This function allows the class to take in attrObject which are loan attributes.
    #    :param attrObject: Any loan attribute falling under Principal, Balance at t, Aggregate Principal at t, Interest at t, and Total Payment at t.
    #    '''
    #    # if type(attrObject) == VariableRateLoan or type(attrObject) == FixedRateLoan or type(attrObject) == 'noneType':
    #    self._loanAttr.append(attrObject)
    #    # else:
    #    #     print('Object has not been appended, please input a valid Loan object.')

    # 3. Erase loan instantiations / Attributes
    # Erase current list of loans
    def loanErase(self):
        '''
        This function erases the current list of loans.
        '''

        logging.debug('\nErasing list of loans...')  # Changed in 4_2_3
        self._loans = []

    # Return Final list of Loans for methods:
    def loanList(self):
        '''
        This function returns a list of loan instantiations within variables to make it easier to call loan class methods.
        '''
        loanList = self.getloans()

        logging.debug('\nCreating a list of loans from the loan pool object...')  # Changed in 4_2_3
        len(loanList)
        listNames = []
        for i, _ in enumerate(loanList):
            listNames.append('loan' + str(i + 1))

        finalloanList = []
        i = 0
        for i in range(len(loanList)):
            k = locals()[listNames[i]] = loanList[i]
            finalloanList.append(k)
            i = i + 1

        logging.debug('\nSuccessfully generated a list of loans...')  # Changed in 4_2_3
        return finalloanList

    #Getter and Setter Functions
    # def loanAttrErase(self):
    #     self._loanAttr = []

    # Return list of loans
    # def getloanAttr(self):
    #     return self._loanAttr[:]

    ### if type(loanObject) == VariableRateLoan:
    ### VariableRateLoan.balance(self, term, rate, notional, t)

    # Property Getter and Setter
    # Loan Pool
    @property
    def loans(self):
        return self._loans

    @loans.setter
    def loans(self, iloans):
        self._loans = iloans

    # Loan Objects
    @property
    def loanObject(self):
        return self._loanObject

    @loanObject.setter
    def loanObject(self, iloanObject):
        self._loanObject = iloanObject

    # Methods
    # I. Total Loan Principal
    def totalPrincipal(self):
        '''
        This function returns the sum of the principal of the loans entered at a given t.
        '''

        # Post - AP Comments
        lList = self.loanList()

        logging.debug('\nCalculating total principal of loans in loan pool...')  # Changed in 4_2_3
        return sum(lList[i].notional for i in range(len(lList)))

    # II. Total Loan Balance
    def totalBalance(self, t):
        '''
        This function returns the sum of the balance of the loans entered.
        '''

        # Version 3: Post - AP Comments
        lList = self.loanList()

        logging.debug('\nCalculating total balance of loans in loan pool...')  # Changed in 4_2_3
        return sum(l.balance(t) for l in lList)

    # III. Methods for: (1) aggregatePrincipal, (2) aggregateInterest, and (3) totalPaymentDue in a given period
    # aggregatePrincipal:
    def principalDue(self, t):
        '''
        This function returns the sum of the principal due of the loans entered at a given t.
        '''

        # Version 3: Post - AP Comments
        lList = self.loanList()

        logging.debug('\nCalculating total principal due at t of loans in loan pool...')  # Changed in 4_2_3
        return sum(l.principalDue(t) for l in lList)

    # aggregateInterest:
    def interestDue(self, t):
        '''
        This function returns the sum of the interest due of the loans entered at a given t.
        '''

        # Version 3: Post - AP Comments
        lList = self.loanList()

        logging.debug('\nCalculating interest due at t of loans in loan pool...')  # Changed in 4_2_3
        return sum(l.interestDue(t) for l in lList)

    # total Payment Due / Monthly Payment:
    def monthlyPayment(self, t):
        '''
        This function returns total monthly due of the loans entered at a given t.
        '''

        # Version 3: Post - AP Comments
        lList = self.loanList()

        logging.debug('\nCalculating total monthly payment at t of loans in loan pool...')  # Changed in 4_2_3
        return sum(l.monthlyPayment(t) for l in lList)

    # IV. Number of active loans
    def activeLoanCount(self, t):
        '''
        This function returns the number of loans in the list that have a balance > 0 at a given t.
        '''

        # Version 3: Post - AP Comments
        lList = self.loanList()

        logging.debug('\nCalculating loans with balance > 0 at t of loans in loan pool...')  # Changed in 4_2_3
        return len([l for l in lList if l.balance(t) > 0])

    # Sum Function that allows to take in new values iteratively, for waM Calculate (reduce version)
    def reduce_sum(self, accumulator, new_value):
        return accumulator + prod(new_value)

    # Functions ported over from Homework 1
    def waMCalculate(self):
        '''
        This function calculates the weighted average maturity. It uses the reduce function with a REGULAR function as its callable.
        '''

        # Version 3: Post - AP Comments
        lList = self.loanList()
        total = reduce(self.reduce_sum,
                        zip([lList[i].notional for i in range(len(lList))],
                           [lList[i].term for i in range(len(lList))]),
                       0)

        totalNotional = self.totalPrincipal()

        logging.debug('\nCalculating weighted average maturity = [notional (loan i) * term (loan i)] / total notional ...')  # Changed in 4_2_3
        return total / totalNotional

    def waRCalculate(self, t):
        '''
        This function calculates the weighted average rate. A period input is included to account for variable rate loans.
        It uses the reduce function with a lambda function as its callable.
        '''

        # Version 3: Post - AP Comments
        lList = self.loanList()
        total = reduce(lambda total, faceRate: total + (faceRate[0] * faceRate[1]),
                        zip([lList[i].notional for i in range(len(lList))],
                           [lList[i].getRate(t) for i in range(len(lList))]),
                       0)

        logging.debug('\nCalculating weighted average rate = [notional (loan i) * rate (loan i)] / total notional ...')  # Changed in 4_2_3
        totalNotional = self.totalPrincipal()
        return total / totalNotional