'''
Test Run of Project with Random Component

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
    #     + Call doWaterfall

    # (A) SEQUENTIAL TEST
    # Instantiate Structured Security Object
    StructSecObject = StructuredSecurities(lP.totalPrincipal())

    # Instantiate Tranches
    StructSecObject.addTranche('Tranche_1', .75, .06, 'A') # trancheName, notionalPercent, rate, flagInput
    StructSecObject.addTranche('Tranche_2', .25, .1, 'B')

    StructSecObject.flagMode('Sequential') # Test Sequential

    results = ssPackage.doWaterfall(lP, StructSecObject) # do Waterfall (Working GOOD. Just need to deal with ERRORS).

    # TEST CODE TO VIEW RESULTS:
    # for index in range(len(results)):
    #     value = results[index]
    #     print(index, value)
    resultsa = results[0]
    resultsb = results[1]
    logging.info(f'Length of Results List (Sequential) for Liabilities: {len(resultsa)}')
    logging.info(f'Length of Results List (Sequential) for Asset: {len(resultsb)}')

    # (A) PRO RATA TEST
    StructSecObject2 = StructuredSecurities(lP.totalPrincipal())

    # Instantiate Tranches
    StructSecObject2.addTranche('Tranche_1', .75, .06, 'A') # trancheName, notionalPercent, rate, flagInput
    StructSecObject2.addTranche('Tranche_2', .25, .1, 'B')

    StructSecObject2.flagMode('Pro Rata') # Test Sequential

    results2 = ssPackage.doWaterfall(lP, StructSecObject2) # do Waterfall (Working GOOD. Just need to deal with ERRORS).

    # TEST CODE TO VIEW RESULTS:
    # for index in range(len(results2)):
    #     value = results2[index]
    #     print(index, value)
    results2a = results2[0]
    results2b = results2[1]
    logging.info(f'\nSample Output:')
    logging.info(f'{results2a[0]}')
    logging.info(f'{results2b[0]}')

    # results2afinal = flatList(results2a)
    # logging.info(f'{results2afinal[0]}')

    # for result in results2a:
    #     # term, rate, notional, car
    #     # TERM IS IN MONTHS. LOAN CLASS MODIFICATION NEEDED
    #     flattenedList = [item for sublist in result for item in sublist]
    #     results2afinal.append(flattenedList)
    #     i = i + 1

    logging.info(f'\nLength of Results List (Sequential) for Liabilities: {len(results2a)}')
    logging.info(f'Length of Results List (Sequential) for Asset: {len(results2b)}')


    # III. (1) Save results in two CSV Files. (2) Each result in a single row. (3) Reserve should be in Liabs. (4) Each Time Period gets its own row.
    # REQUIREMENT: LIST COMPREHENSION AND STRING PARSING.
    # Output: I. sequentialLiabsWF II. sequentialAssetWF III. prorataLiabsWF IV. prorataAssetWF
    logging.info('\nImporting to CSV Files (4x)')
    logging.info('I. sequentialLiabsWFRandom II. sequentialAssetWFRandom III. prorataLiabsWFRandom IV. prorataAssetWFRandom')

    # I. sequentialLiabsWF
    rootDir = os.getcwd() # get working directory
    logging.debug('Setting directory for new file...')

    # filenames
    filenames = ['sequentialLiabsWFRandom.csv', 'sequentialAssetWFRandom.csv', 'prorataLiabsWFRandom.csv', 'prorataAssetWFRandom.csv']

    # listnames (prepare)
    listnames = [flatList(resultsa), resultsb, flatList(results2a), results2b] # No need to flatten LP items...

    # headers
    header1 = ['TR_A_interestDueVal_t', 'TR_A_interestPayment_t', 'TR_A_interestShortfall_t', 'TR_A_principalPayment_t', 'TR_A_notionalBalanceVal_t',
               'TR_B_interestDueVal_t', 'TR_B_interestPayment_t', 'TR_B_interestShortfall_t', 'TR_B_principalPayment_t', 'TR_B_notionalBalanceVal_t',
               'reserveAccount_t']
    header2 = ['monthlyPayment_t', 'principalDue_t', 'totalBalance_t', 'interestDue_t', 'activeLoanCount_t']

    try:
        i = 0
        for listname in listnames:
            dirFinal = os.path.join(rootDir, filenames[i])
            logging.info(f'\nInitialization complete, final file path = {dirFinal}')
            logging.debug(f'Writing information on loan list to {dirFinal}...')
            s = ','

            if len(listname[0]) > 5:
                with open(dirFinal, 'w', newline='') as finalList:
                    finalList.write(s.join(header1) + '\n')
                    for list in listname:
                        finalList.write(s.join(map(str, list)) + '\n')
                logging.info(f'File {filenames[i]} was successfully created.')
            else:
                with open(dirFinal, 'w', newline='') as finalList:
                    finalList.write(s.join(header2) + '\n')
                    for list in listname:
                        list = [str(i) for i in list]
                        finalList.write(s.join(map(str, list)) + '\n')
                logging.info(f'File {filenames[i]} was successfully created.')
            i = i + 1
    except Exception as generalEx:
        logging.info('Please ensure that the csv files have not been opened before running the program. Exiting...')
        logging.info(f'Exception: {generalEx}')

    # Clean up:
    logging.info('\n')
    StructSecObject.cleanSlate()
    StructSecObject2.cleanSlate()

    # Q: Did each tranche's balance get successfully paid down to 0? If they did, was there any money left in the end?
    # A: Yes and Yes. Money was left in the end as there were still active loans that were providing cash flow, and it took a few periods to fully receive those
    #    cash flows, which were then stored in the Reserve Balance.

    #    Moreover, Reserve balance tends to be higher for pro-rata as extra money is not being used as a maximum payment to pay off a loan at any given point in time.
    #    This is especially evident in the case where you have multiple loans and your tranches' principal is way less i.e. 100,000 to total notional of millions.

    # Update! MUCH FASTER PAYMENT OF LOANS THIS TIME. Defaults Lead to lowering of balances.


#########################
if __name__ == '__main__':
    main()