'''
Create a program that specifies a loan and an asset, and returns a csv file
*** FOR THE PURPOSES OF THIS EXERCISE, USE AUTOLOAN AND FIXEDRATE LOAN ONLY (Per APalley Quantnet Comment)!
'''

from Exercise_4_3.Exercise_4_3_7.Loan_Package.fixed_mortgage import FixedMortgage
from Exercise_4_3.Exercise_4_3_7.Loan_Package.auto_loan import autoLoan
from Exercise_4_3.Exercise_4_3_7.Loan_Package.house_base import HouseBase, PrimaryHome, VacationHome
from Exercise_4_3.Exercise_4_3_7.Loan_Package.car import Car, Civic, Lexus, Lamborghini
import os
import logging



def csvCreate(loanList):
    logging.info('loanList has been specified. Time to enter them into a file...')

    # Get directory of current folder...
    logging.debug('Setting directory for new file...')
    logging.debug('Not an issue to create a text in the same folder here unlike creating a subdirectory in the same directory (Uneditable and causes errors)...')
    logging.debug('Getting current directory...')
    rootDir = os.getcwd()

    logging.debug('Setting directory for new file...')
    dirFinal = os.path.join(rootDir, 'loanfile.csv')

    logging.info(f'\nInitialization complete, final file path = {dirFinal}')
    logging.debug(f'\nWriting information on loan list to {dirFinal}...')

    s = ','

    with open(dirFinal, 'w', newline='') as finalList:
        for loan in loanList:
            a = loan.__class__.__name__  # Per APalley in Forum (see tips and tricks L2)
            b = loan.asset.__class__.__name__
            c = str(loan.asset.initialValue)
            d = str(loan.term)
            e = str(loan.rate)
            f = str(loan.notional)
            loan = [a, b, c, d, e, f'{f}\n']
            finalList.write(s.join(loan))

    logging.debug(f'\nWriting successful...')
    logging.debug(f'Exiting...')



def csvGenerator():
    loanList = []  # Create list of Loan Objects
    optionDecision = ''
    i = 0

    while True:
        i += 1
        logging.debug(f'\nLoop Number: {i}\n')

        # Set up Choice Question...
        logging.debug('Initializing program...')
        logging.info(
            'Choice 1: Add Loan (Proceeds to ask for more inputs to specify (1) Loan Type, (2) Asset Type, (3) Asset Value, (4) Amount, (5) Rate, (6) Term).')
        logging.info('Choice 2: Write CSV File and Exit.')

        try:
            optionDecision = int(
                input('Please choose between 1 and 2. Input the number of your choice only (e.g. 1)...\n'))
            if not [1, 2].count(optionDecision):
                raise ValueError('Exception: Please enter 1 or 2 only.')
            else:
                pass

        except ValueError as wrongInput:
            logging.info(f'\nError: {wrongInput}')
            logging.error(ValueError)
            break

        except TypeError as wrongType:
            logging.info(f'\nError: {wrongType}')
            logging.error(TypeError)
            break

        except Exception as errorGeneral:
            logging.info(f'\nException: {errorGeneral}')
            logging.exception(Exception)
            break

        if optionDecision != 2:
            loanObj = []

            # (1 - 3) Select Loan Type + Asset + Asset Value:
            try:
                loanType = [FixedMortgage, autoLoan]
                logging.info('\nChoice 1: Fixed Mortgage')
                logging.info('Choice 2: Auto Loan')

                loanTypeDecision = int(input(
                    'Choose your Loan Type... Please choose between 1 and 2. Input the number of your choice only (e.g. 1)...'))

                if 0 < loanTypeDecision < 3:
                    loanObj.append(loanType[(loanTypeDecision - 1)])
                else:
                    raise ValueError('Exception: Please enter 1 or 2 only.')

                # (2 - 3) Select Asset Type and Get its Value:
                try:
                    if loanTypeDecision == 1:
                        homeInstObj = [HouseBase, PrimaryHome, VacationHome]

                        logging.info('\nChoices... 1: Generic Home, 2: Primary Home, 3: Vacation Home')
                        AssetTypeDecision = int(input(
                            '\nPlease choose between between 1 to 3. Input the number of your choice only (e.g. 1)...'))

                        # Giving the asset its Value
                        valueAsset = float(input(f'\nPlease enter the value of your asset...'))

                        assetObj = homeInstObj[AssetTypeDecision - 1]
                        loanObj.append(assetObj)
                        loanObj.append(valueAsset)

                    elif loanTypeDecision == 2:
                        carInstObj = [Car, Civic, Lexus, Lamborghini]

                        logging.info('\nChoices... 1: Car, 2: Civic, 3: Lexus, 4: Lamborghini')
                        AssetTypeDecision = int(input(
                            '\nPlease choose between between 1 to 4. Input the number of your choice only (e.g. 1)...'))

                        # Naming the Object and Giving it it's Value
                        valueAsset = float(input(f'\nPlease enter the value of your asset...'))

                        assetObj = carInstObj[AssetTypeDecision - 1]
                        loanObj.append(assetObj)
                        loanObj.append(valueAsset)

                    else:
                        raise ValueError('Exception: Please enter a number within the choices only only.')

                except ValueError as wrongInput:
                    logging.info(f'\nError: {wrongInput}')
                    logging.error(ValueError)
                    break

                except TypeError as wrongType:
                    logging.info(f'\nError: {wrongType}')
                    logging.error(TypeError)
                    break

                except Exception as errorGeneral:
                    logging.info(f'\nException: {errorGeneral}')
                    logging.exception(Exception)
                    break

            except ValueError as wrongInput:
                logging.info(f'\nError: {wrongInput}')
                logging.error(ValueError)
                break

            except TypeError as wrongType:
                logging.info(f'\nError: {wrongType}')
                logging.error(TypeError)
                break

            except Exception as errorGeneral:
                logging.info(f'\nException: {errorGeneral}')
                logging.exception(Exception)
                break

            # (4 - 6) Select Loan Type:
            try:
                amount = int(
                    input(f'Please input the face amount (in actuals) of your {loanObj[0].__name__}...'))
                rate = float(input(f'Please input the rate (in decimals) of your {loanObj[0].__name__}...'))
                term = int(input(f'Please input the term (in years) of your {loanObj[0].__name__}...'))

                # Appending...
                loanObj.append(amount)
                loanObj.append(rate)
                loanObj.append(term)

            except ValueError as wrongInput:
                logging.info(f'\nError: {wrongInput}')
                logging.error(ValueError)
                break

            except TypeError as wrongType:
                logging.info(f'\nError: {wrongType}')
                logging.error(TypeError)
                break

            except Exception as errorGeneral:
                logging.info(f'\nException: {errorGeneral}')
                logging.exception(Exception)
                break

            # Creating Loan Object
            logging.debug(f'temporary: {loanObj}')
            loanFunc = loanObj[0]

            loanObjFinal = loanFunc(loanObj[3], loanObj[4], loanObj[5], assetObj(loanObj[2]))

            loanList.append(loanObjFinal)
            logging.debug(f'temporary: {loanList}')

            # Notify user of progress:
            logging.info(f'\nLoan has been recorded. Returning to main menu...')

        else:
            break

    # IF 2 is finally selected.
    try:
        if optionDecision != 2:

            logging.debug('Dealing with scenario when loanList is not empty...')
            if len(loanList):
                loansaveDecision = input('\nWould you like to save what you have so far (Yes or No)?...')

                if loansaveDecision == 'Yes':
                    logging.debug('\nSaving what we can...')

                    try:
                        # run function above
                        logging.debug(f'\nRunning csv writing operations via the function above...')
                        csvCreate(loanList)

                    except Exception as generalError:
                        logging.info(f'\nError: {generalError}')
                        logging.info('Possible Scenarios:')
                        logging.info('(1) Forgetting to close the file before running the program')
                        logging.info('(2) Wrong inputs')
                        logging.error(Exception)

                elif loansaveDecision == 'No':
                    logging.debug('Discarding loanList...')
                    logging.info('\nFile will not be saved. Exiting...')
                else:
                    raise Exception('Exception: Code executed incorrectly, please try again...')

            else:
                raise Exception('Exception: Code executed incorrectly, please try again...')

        elif optionDecision == 2:
            if len(loanList):
                # run function above
                logging.debug(f'\nRunning csv writing operations via the function above...')
                csvCreate(loanList)

            else:
                logging.info(
                    f'\nYou have not yet entered a loan to your loan list... Exiting without creating a csv file...')

    except Exception as generalError:
        logging.info(f'\nError: {generalError}')
        logging.info('Possible Scenarios:')
        logging.info('(1) Forgetting to close the file before running the program')
        logging.info('(2) Wrong inputs')
        logging.error(Exception)

    # MAIN CODE: MAJOR STP 1 SPECIFY LOAN (C1)-> INPUTS MAJOR (C2 C3 C4) STP 2 SPECIFY ASSET (C5) -> TAKE VALUE (C6)

    # Code Set 2: Double while. (a) WHILE logic to keep proceeding to fill up DICT before going back to input statement (b) WHILE not (2) keep going
    # Code Set 3: Allow pre-mature exit. No progress saved.
    # Code Set 4: Error-trap for valid inputs in Code Set 1...
    # Code Set 5: Error-trap for valid inputs in Code Set 2


def main():
    logging.basicConfig(format='%(message)s', level=logging.INFO)

    # Code Set 1: Give user choice of two options: (1) Add Loan and (2) Write file and exit.
    logging.info(f'Checking if file already exists...')
    dirTest = os.path.join(os.getcwd(), 'loanfile.csv')

    try:
        if os.path.exists(dirTest):
            logging.info(f'loanfile.csv already exists...')
            proceedDecision = input('Do you wish to proceed? Proceeding will risk overwriting your original file... (Yes or No)\n')
            if proceedDecision == 'Yes':
                csvGenerator()
            elif proceedDecision == 'No':
                logging.info('Exiting...')
            else:
                raise ValueError('Error in code execution, please try again.')

        elif not os.path.exists(dirTest):
            logging.info(f'loanfile.csv does not yet exist...')
            csvGenerator()

        else:
            raise Exception('Error in code execution, please try again.')

    except ValueError as wrongInput:
        logging.info(f'\nError: {wrongInput}')
        logging.error(ValueError)

    except TypeError as wrongType:
        logging.info(f'\nError: {wrongType}')
        logging.error(TypeError)

    except Exception as errorGeneral:
        logging.info(f'\nException: {errorGeneral}')
        logging.exception(Exception)




#########################
if __name__ == '__main__':
    main()
