'''
Test Run of Project with Financial monte Carlo (runMonte)

Create a LoanPool object that consists of 1,500 loans. Use the provided CSV file of loan data to create these Loan objects.

Instantiate your StructuredSecurities object, specify the total notional (from the LoanPool), add two
standard tranches (class A and class B in terms of subordination), and specify sequential or pro-rata mode.
The rates for each tranche can be arbitrary (for now). Note that subordinated tranches should always
have a higher rate, as they have increased risk.

Call doWaterfall and save the results into two CSV files (one for the asset side and one for the liabilities
side). All the tranches’ data for a given time period should be a single row in the CSV. The reserve
account balance should also be in liabilities CSV, for each time period. Each time period gets its own
row. Note that you may need to do some clever list comprehensions and string parsing to get this to
output correctly.
'''

# Created Packages
from Tranche_Package.structured_securities import StructuredSecurities
from Loan_Package.loan_pool import LoanPool
from Loan_Package.auto_loan import autoLoan
from Loan_Package.car import Car
import Tranche_Package.structured_securities as ssPackage
from Tools_Package.Timer import Timer

# Python Packages
import logging
import os


# Miscellaneous:
# Function (1)
def flatList(listofLists):
    flatList = []
    for result in listofLists:
        # term, rate, notional, car
        # TERM IS IN MONTHS. LOAN CLASS MODIFICATION NEEDED
        flattenedList = [item for sublist in result for item in sublist]
        flatList.append(flattenedList)

    return flatList


def main():
    logging.basicConfig(format='%(message)s', level=logging.INFO)  # Set level of logging -> INFO

    # I. Import Loans from CSV File. -> Loop LoanCollect to create LoanPool object of 1500 Loans.
    # File Saved as CSV File...

    # (1) READ FILE
    s = ('\\') # splitter
    cwd = os.getcwd().split(s) # get working directory
    cwd.insert(len(cwd), 'Loans.csv')
    # Test print(cwd)... Correct!

    cwd = s.join(cwd)
    logging.debug(f'\nFile path as been set: {cwd}')

    # Create list from the CSV
    autoloanList = []
    with open(cwd, 'r') as loanSource:
        for line in loanSource.readlines():
            line = line.strip('\n').split(',') # Remove space and separate each into different elements
            lineFinal = line[:-4]
            autoloanList.append(lineFinal)

    # Clean-up (Remove 1st Line)
    autoloanList.pop(0)
    # logging.info(autoloanList)
    logging.info(f'\nSample: {autoloanList[0]}')

    # Clean-up (Each String turn to a list)
    # newautoloanList = []
    # commaSplitter = (',')
    # for item in autoloanList:
    #     list(item.split(commaSplitter))
    #     newautoloanList.append(item)

    # logging.info(newautoloanList)

    # (2) Create 1500 Loan objects and place in Loan Pool
    lP = LoanPool() # Instantiate Loan Pool

    # Instantiate Loan Class
    # Name the Loan Class
    # Fead to Loan Pool

    i = 1
    for item in autoloanList:
        # term, rate, notional, car
        # TERM IS IN MONTHS. LOAN CLASS MODIFICATION NEEDED
        forAppend = locals()['autoLoan' + str(i)] = autoLoan(float(item[4]), float(item[3]), float(item[2]), Car(float(item[6])))
        lP.loanCollect(forAppend)
        i = i + 1

    # logging.info(lP). Works FINE.
    logging.info(f'Loan Pool Total Principal: {lP.totalPrincipal()}')
    # WORKS! for loan in lP:
    #     logging.info(loan.notional)

    # II. Instantiate your StructuredSecurities object. Specify (1) Total Notional (2) 2 Std Tranches (3) .a Sequential / .b Pro-Rata (4) Rates: tr A < tr B
    #     + Call simulateWaterfall

    # Instantiate Structured Security Object
    StructSecObject = StructuredSecurities(lP.totalPrincipal())

    # Instantiate Tranches (MC Simulation REQUIREMENTS: with 0.05 and 0.08)
    StructSecObject.addTranche('Tranche_1', .75, .05, 'A') # trancheName, notionalPercent, rate, flagInput
    StructSecObject.addTranche('Tranche_2', .25, .08, 'B')

    # Test MC Simulation (5 runs, simulateWaterfall version 1):
    with Timer('myTimer') as timer:
        timer.configureTimerDisplay('minutes')
        StructSecObject.flagMode('Sequential')  # Test Sequential
        results = ssPackage.runMonte(lP, StructSecObject, 0.005, 100) # Already returns the results.

    # Results with NSIM = 2.     2 Iterations, 0.7 Minutes.
    # Results with NSIM = 10.    2 Iterations, 4 Minutes.
    # Results with NSIM = 100.   2 Iterations, 41.98 Minutes.

    ################################################################

    # Tranche 1 RESULTS:
    # Tranche 1 Average DIRR: 0.0025553699999999986
    # Tranche 1 Rating: Baa2
    # Tranche 1 Average AL: 21.58893691143611
    # Tranche 1 Fair Yield: 0.0663641554487699

    # Tranche 2 RESULTS:
    # Tranche 2 Average DIRR: 0.0016272199999999998
    # Tranche 2 Rating: Baa1
    # Tranche 2 Average AL: 40.17063051535646
    # Tranche 2 Fair Yield: 0.06729611215482477

    ################################################################


#########################
if __name__ == '__main__':
    main()