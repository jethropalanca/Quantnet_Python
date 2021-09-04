'''
Test Run of Project with Financial monte Carlo (runMonte). WITH Multi-processing.

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
    flagMode = 'Sequential' # Input for doWaterfall

    # Instantiate Tranches (MC Simulation REQUIREMENTS: with 0.05 and 0.08)
    StructSecObject.addTranche('Tranche_1', .75, .05, 'A') # trancheName, notionalPercent, rate, flagInput
    StructSecObject.addTranche('Tranche_2', .25, .08, 'B')

    # Test MC Simulation (5 runs, simulateWaterfall version 1):
    with Timer('myTimer') as timer:
        timer.configureTimerDisplay('minutes')
        StructSecObject.flagMode(flagMode)  # Test Sequential
        resultz = ssPackage.runMonte(lP, StructSecObject, 0.005, 5, 5) # Already returns the results.
        # Uncomment LINE 188 Onwards to activate -> CSV program.

    # Result of Run WITH multi-processing:
    # Results with NSIM = 5, 20 Processes: 2.6 minutes. # Ensures minimum of one process if NSIM/NPROCESS <1
    # Results with NSIM = 5, 5 Processes: 2.5 minutes.
    # Results with NSIM = 5, 5 Processes: 0.8 minutes. # Run after some code edits to speed things up.
    # Results with NSIM = 5, 5 Processes: 0.7 minutes. # Run after some code edits to speed things up: Basic Clean-up, List Comp to Generators
    # Results with NSIM = 10, 10 Processes: 1.3 minutes. # Run after some code edits to speed things up.
    # Results with NSIM = 100, 20 Processes: 13 minutes. Took 42 minutes without multi-processing.
    # Results with NSIM = 100, 20 Processes: 11.9 minutes.  # Run after some code edits to speed things up: Basic Clean-up
    # Results with NSIM = 100, 20 Processes: STILL 11.9 minutes.  # Run after some code edits to speed things up: Basic Clean-up, List Comp to Generators
    # Results with NSIM = 2000, 20 Processes: 227 minutes.
    ## Takes 2 hours +. Way faster, but only shows how much processing power is needed for this to run without multiprocessing (almost 1 day).
    ################################################################
    # (*) Pro Rata
    # Tranche 1 RESULTS:
    # Tranche 1 Average DIRR: 0.0023793549999999997
    # Tranche 1 Rating: Baa2
    # Tranche 1 Average AL: 26.24233340654761
    # Tranche 1 Fair Yield: 0.0666263769138349

    # Tranche 2 RESULTS:
    # Tranche 2 Average DIRR: 0.002380362
    # Tranche 2 Rating: Baa2
    # Tranche 2 Average AL: 26.24233340654761
    # Tranche 2 Fair Yield: 0.06662640591317476

    ################################################################
    # Results with NSIM = 2000, 100 Processes: CRASH.
    # (*) There is insufficient memory for the Java Runtime Environment to continue. My RAM is only 4GB so that must have been the issue.
    # Results with NSIM = 2000, 50 Processes: CRASH.
    # (*) There is insufficient memory for the Java Runtime Environment to continue. My RAM is only 4GB so that must have been the issue.
    # Results with NSIM = 2000, 40 Processes: 235 minutes.
    ################################################################
    # (*) Pro Rata
    # Tranche 1 RESULTS:
    # Tranche 1 Average DIRR: 0.0029028129999999993
    # Tranche 1 Rating: Baa3
    # Tranche 1 Average AL: 21.578920382710756
    # Tranche 1 Fair Yield: 0.06637203758134086

    # Tranche 2 RESULTS:
    # Tranche 2 Average DIRR: 0.0015062880000000002
    # Tranche 2 Rating: Baa1
    # Tranche 2 Average AL: 40.11340810167336
    # Tranche 2 Fair Yield: 0.06728823146192421

    ################################################################


    # Result of Runs without multi-processing:
    # Results with NSIM = 2.     2 Iterations, 0.7 Minutes.
    # Results with NSIM = 10.    2 Iterations, 4 Minutes.
    # Results with NSIM = 100.   2 Iterations, 41.98 Minutes.

    ################################################################
    # (*) Sequential
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

    '''
    #####################
    ### UNCOMMENT ME! ###
    #####################
    # Code to generate CSV Files...
    
    # Instantiate Tranches (MC Simulation REQUIREMENTS: with 0.05 and 0.08) with NEW rates...
    StructSecObject._trancheList = [] # reset

    StructSecObject.addTranche('Tranche_1', .75, resultz[0][3], 'A') # trancheName, notionalPercent, rate, flagInput
    StructSecObject.addTranche('Tranche_2', .25, resultz[1][3], 'B')

    # Run
    results = ssPackage.doWaterfall(lP, StructSecObject) # do Waterfall

    resultsa = results[0]
    resultsb = results[1]

    logging.info(f'\nLength of Results List ({StructSecObject._mode}) for Liabilities: {len(resultsa)}')
    logging.info(f'Length of Results List ({StructSecObject._mode}) for Asset: {len(resultsb)}')

    # III. (1) Save results in two CSV Files. (2) Each result in a single row. (3) Reserve should be in Liabs. (4) Each Time Period gets its own row.
    # REQUIREMENT: LIST COMPREHENSION AND STRING PARSING.
    # Output: I. sequentialLiabsWFMultProcess II. sequentialAssetWFMultProcess III. prorataLiabsWFMultProcess IV. prorataAssetWFMultProcess
    logging.info('\nImporting to CSV Files (4x)')
    logging.info(f'I. {StructSecObject._mode}LiabsWFMultProcess II. {StructSecObject._mode}AssetWFMultProcess III. {StructSecObject._mode}LiabsWFMultProcess IV. {StructSecObject._mode}AssetWFMultProcess')

    # I. WD
    rootDir = os.getcwd() # get working directory
    logging.debug('Setting directory for new files...')

    # filenames
    filenames = [f'{StructSecObject._mode}LiabsWFMultProcess.csv', f'{StructSecObject._mode}AssetWFMultProcess.csv']

    # listnames (prepare)
    listnames = [flatList(resultsa), resultsb] # No need to flatten LP items...

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
    '''

#########################
if __name__ == '__main__':
    main()