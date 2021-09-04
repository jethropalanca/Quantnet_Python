'''
This program initializes the LoanPool (demonstrate composition).
'''

from Loan_Folder_12.Loan_Package.loan_types import VariableRateLoan
from Loan_Folder_12.Loan_Package.loan import Loan
from Loan_Folder_12.Loan_Package.loan_types import FixedRateLoan

class LoanPool(object):
    # Initialization Function

    def __init__(self):
        '''
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

        # Loan Objects
    # @property
    # def attrObject(self):
    #     return self._attrObject

    # @attrObject.setter
    # def attrObject(self, iattrObject):
    #     self._attrObject = iattrObject

    # Methods
    # I. Total Loan Principal
    def totalPrincipal(self):
        '''
        This function returns the sum of the principal of the loans entered at a given t.
        '''
        lList = self.loanList()
        sumlList = [lList[i].notional for i in range(len(lList))]
        return sum(sumlList)


    # II. Total Loan Balance
    def totalBalance(self, t):
        '''
        This function returns the sum of the balance of the loans entered.
        '''
        lList = self.loanList()
        balancelList = []
        print('\n')
        for i in range(len(lList)):
            if isinstance(lList[i],VariableRateLoan):
                k = lList[i].balance(t)
                if k < 0:
                    pass
                else:
                    print('Remaining balance for loan', i,':', k)
                    balancelList.append(k)
            else:
                k = lList[i].balance(t)
                if k < 0:
                    pass
                else:
                    print('Remaining balance for loan', i,':', k)
                    balancelList.append(k)
        # return max(0, sum(balancelList))  # To prevent negative values if a really big period was entered (Initial Code)
        return sum(balancelList)

    # III. Methods for: (1) aggregatePrincipal, (2) aggregateInterest, and (3) totalPaymentDue in a given period
    # aggregatePrincipal:
    def principalDue(self, t):
        '''
        This function returns the sum of the principal due of the loans entered at a given t.
        '''
        lList = self.loanList()
        prinduelList = []
        print('\n')
        for i in range(len(lList)):
            if isinstance(lList[i],VariableRateLoan):
                k = lList[i].principalDue(t)
                print('At period ',t,', principal due for loan', i,':', k)
                prinduelList.append(k)
            else:
                k = lList[i].principalDue(t)
                print('At period ',t,', principal due for loan', i,':', k)
                prinduelList.append(k)
        return sum(prinduelList)

    # aggregateInterest:
    def interestDue(self, t):
        '''
        This function returns the sum of the interest due of the loans entered at a given t.
        '''
        lList = self.loanList()
        intduelList = []
        print('\n')
        for i in range(len(lList)):
            if isinstance(lList[i],VariableRateLoan):
                k = lList[i].interestDue(t)
                if k < 0:
                    pass
                else:
                    print('At period ',t,', Interest due for loan', i,':', k)
                    intduelList.append(k)
            else:
                k = lList[i].interestDue(t)
                if k < 0:
                    pass
                else:
                    print('At period ',t,', Interest due for loan', i,':', k)
                    intduelList.append(k)
        return sum(intduelList)

    # total Payment Due / Monthly Payment:
    def monthlyPayment(self, t):
        '''
        This function returns total monthly due of the loans entered at a given t.
        '''
        lList = self.loanList()
        monthlypaylList = []
        print('\n')
        for i in range(len(lList)):
            if isinstance(lList[i],VariableRateLoan):
                k = lList[i].monthlyPayment(t)
                print('At period ',t,', payment due for loan', i,':', k)
                monthlypaylList.append(k)
            else:
                k = lList[i].monthlyPayment(t)
                print('At period ',t,', payment due for loan', i,':', k)
                monthlypaylList.append(k)
        return sum(monthlypaylList)

    # IV. Number of active loans
    def activeLoanCount(self, t):
        '''
        This function returns the number of loans in the list that have a balance > 0 at a given t.
        '''
        lList = self.loanList()
        print('\n')
        count = 0
        for i in range(len(lList)):
            if isinstance(lList[i],VariableRateLoan):
                k = lList[i].balance(t)
                print(k)
                if k > 0:
                    count = count + 1
                else:
                    pass
            else:
                k = lList[i].balance(t)
                print(k)
                if k > 0:
                    count = count + 1
                else:
                    pass
        return count

    '''
    Counts the number of active loans: Active loans are loans that have a balance greater than zero.
    '''

    # Functions ported over from Homework 1
    def waMCalculate(self):
        '''
        This function calculates the weighted average maturity.
        '''
        lList = self.loanList()
        total = 0.0

        for i in range(len(lList)):
            total+= lList[i]._notional * lList[i]._term

        totalNotional = self.totalPrincipal()
        return total / totalNotional

    def waRCalculate(self, t):
        '''
        This function calculates the weighted average rate. A period input is included to account for variable rate loans.
        '''
        lList = self.loanList()
        total = 0.0

        for i in range(len(lList)):
            if isinstance(lList[i],VariableRateLoan):
                notional = lList[i]._notional
                rate = lList[i].getRate(t)

            else:
                notional = lList[i]._notional
                rate = lList[i]._rate

            total += notional * rate

        totalNotional = self.totalPrincipal()
        return total / totalNotional
