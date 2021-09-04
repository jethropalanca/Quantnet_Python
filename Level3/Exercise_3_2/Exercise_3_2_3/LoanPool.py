'''
Version 3 (Exercise 3) - Modified Per Avi Palley's comments + WAM / WAR formula changes
This program initializes the LoanPool (demonstrate composition).
'''

from Exercise_3_2.Exercise_3_2_3.loan import Loan
from functools import reduce
from math import prod



class LoanPool(object):
    # Initialization Function
    def __init__(self):
        '''
        This initialization function to initialize a LoanPool class.
        :param loans: This class takes a loan or a list of loans, or their attributes (i.e. Principal, Balance at t, Aggregate Principal, Interest and Total Payment at t).
         Inputs will be taken by the loanCollect and the loanAttr function.
        '''
        self._loans = []

    # Iter Method
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
            self._loans.append(loanObject)
        else:
            print('Object has not been appended, please input a valid Loan object.')

    # Return list of loans
    def getloans(self):
        '''
        This function returns a list of loan instantiations.
        '''
        return self._loans[:]

    # 3. Erase loan instantiations / Attributes
    # Erase current list of loans
    def loanErase(self):
        '''
        This function erases the current list of loans.
        '''
        self._loans = []

    # Return Final list of Loans for methods:
    def loanList(self):
        '''
        This function returns a list of loan instantiations within variables to make it easier to call loan class methods.
        '''
        loanList = self.getloans()

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

        return finalloanList

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
        return sum(lList[i].notional for i in range(len(lList)))

    # II. Total Loan Balance
    def totalBalance(self, t):
        '''
        This function returns the sum of the balance of the loans entered.
        '''

        # Version 3: Post - AP Comments
        lList = self.loanList()
        return sum(l.balance(t) for l in lList)

    # III. Methods for: (1) aggregatePrincipal, (2) aggregateInterest, and (3) totalPaymentDue in a given period
    # aggregatePrincipal:
    def principalDue(self, t):
        '''
        This function returns the sum of the principal due of the loans entered at a given t.
        '''

        # Version 3: Post - AP Comments
        lList = self.loanList()
        return sum(l.principalDue(t) for l in lList)

    # aggregateInterest:
    def interestDue(self, t):
        '''
        This function returns the sum of the interest due of the loans entered at a given t.
        '''

        # Version 3: Post - AP Comments
        lList = self.loanList()
        return sum(l.interestDue(t) for l in lList)

    # total Payment Due / Monthly Payment:
    def monthlyPayment(self, t):
        '''
        This function returns total monthly due of the loans entered at a given t.
        '''

        # Version 3: Post - AP Comments
        lList = self.loanList()
        return sum(l.monthlyPayment(t) for l in lList)

    # IV. Number of active loans
    def activeLoanCount(self, t):
        '''
        This function returns the number of loans in the list that have a balance > 0 at a given t.
        '''

        # Version 3: Post - AP Comments
        lList = self.loanList()
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
                       zip([lList[i].notional for i in range(len(lList))], [lList[i].term for i in range(len(lList))]),
                       0)

        totalNotional = self.totalPrincipal()
        return total / totalNotional

    def waRCalculate(self, t):
        '''
        This function calculates the weighted average rate. A period input is included to account for variable rate loans.
        It uses the reduce function with a lambda function as its callable.
        '''

        # Version 3: Post - AP Comments
        lList = self.loanList()
        total = reduce(lambda total, faceRate: total + (faceRate[0] * faceRate[1]),
                       zip([lList[i].notional for i in range(len(lList))], [lList[i].getRate(t) for i in range(len(lList))]),
                       0)

        totalNotional = self.totalPrincipal()
        return total / totalNotional
