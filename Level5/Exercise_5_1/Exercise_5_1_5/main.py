'''
Creating a date differential program...
'''

import logging
import datetime


def dateDifferential():
    logging.debug('Initializing dateCalculator...')
    logging.debug('Setting format...')
    format = ('%Y %B %d %I:%M:%S:%f %p')

    logging.debug('\nThis program takes the difference of the first date entered MINUS the second date entered...')
    logging.debug('Taking inputs...')

    dateTime1 = input('\nPlease a BASE DATE in the following format: YYYY mmmm dd h:m:s:ms AM/PM (e.g. 1968 June 25 06:21:12:999999 PM).')
    dateTime2 = input('Please a COMPARISON DATE in the following format: YYYY mmmm dd h:m:s:ms AM/PM (e.g. 2016 September 25 06:24:14:12342 PM).')

    logging.debug('\nProcessing BASE DATE...')
    dateTime1 = datetime.datetime.strptime(dateTime1, format)
    logging.debug(f'Value of generated datetime object: {dateTime1}')

    logging.debug('\nProcessing COMPARISON DATE...')
    dateTime2 = datetime.datetime.strptime(dateTime2, format)
    logging.debug(f'Value of generated datetime object: {dateTime2}')

    logging.debug('\nProcessing Date Differential...')
    if isinstance(dateTime1, datetime.datetime) and isinstance(dateTime2, datetime.datetime):
        logging.debug('Subtracting the two dates...')
        dateDifference = dateTime2 - dateTime1

        logging.info('Manually calculate from total_seconds to get values with decimals (days/seconds/microseconds are ambiguous and include rounding-off of other components (e.g. hour))...')
        logging.info(dateDifference)
        secondsDiff = dateDifference.total_seconds()

        logging.debug('\nPresenting the difference in days/hours/minutes/seconds/microseconds/in a sentence (NA if unavailable)...')
        logging.debug('Setting up list for cleaner code...')
        listRes = [secondsDiff / 86400, secondsDiff / 3600, secondsDiff / 60, secondsDiff, secondsDiff * 1000000]

        logging.info(f'\ni. Total number of days (including fractions of days) {listRes[0]}')
        logging.info(f'ii. Total number of hours (including fractions of hours) {listRes[1]}')
        logging.info(f'iii. Total number of minutes (including fractions of minutes) {listRes[2]}')
        logging.info(f'iv. Total number of seconds (including fractions of seconds) {listRes[3]}')
        logging.info(f'v. Total number of microseconds (including fractions of microseconds) {listRes[4]}') # per documentation (in range(1000000))


        # Prepare List...
        dateDifference = str(dateDifference)
        dateDifference = dateDifference.split(':') # len 3 or 4...

        dateDiffFrontApend = []
        dateDiffBackAppend = []

        # Append List
        if dateDifference[0].find(',') != -1 and dateDifference[-1].find('.') != -1:
            dateDiffFrontApend = dateDifference[-1].split('.')

            dateDiffBackAppend = dateDifference[0].split(',')
            dDBAstep1 = dateDiffBackAppend[0]
            dDBAstep2 = dDBAstep1.split(' ')[0]
            dDBAotherNumbstep1 = dateDiffBackAppend[1].strip(' ')

            dateDiffBackAppend = [dDBAstep2, dDBAotherNumbstep1]

        elif dateDifference[-1].find('.') != -1:
            dateDiffFrontApend = dateDifference[-1].split('.')

        elif dateDifference[0].find(',') != -1:
            dateDiffBackAppend = dateDifference[0].split(',')
            dDBAstep1 = dateDiffBackAppend[0]
            dDBAstep2 = dDBAstep1.split(',')[0]
            dDBAstep3 = dDBAstep2.split(' ')[0]

            # workaround if no microseconds
            if dateDifference[-1].find('.') == -1:
                dateDiffBackAppend = [dDBAstep3, dateDiffBackAppend[1]]
            else:
                dateDiffBackAppend = [dDBAstep3, dDBAstep1.split(',')[1]]


        # Number List
        listNumbers = []
        if dateDifference[0].find(',') != -1 and dateDifference[-1].find('.') != -1:
            listNumbers = [int(dateDiffBackAppend[0]), int(dateDiffBackAppend[1]), int(dateDifference[1]), int(dateDiffFrontApend[0]), int(dateDiffFrontApend[1])]
            listLabel = [f' {listNumbers[0]} days', f' {listNumbers[1]} hours', f' {listNumbers[2]} minutes', f' {listNumbers[3]} seconds', f' {listNumbers[4]} microseconds']
            res = [idx for idx, val in enumerate(listNumbers) if val != 0]  # Geeks for Geeks

            if len([x for x in listNumbers if x!=0]) == 0:
                logging.info(f'vi. The difference is NA. BASE Date and COMPARISON Date are both equal.')

            elif len([x for x in listNumbers if x!=0]) == 1:
                logging.info(f'vi. The difference is {listLabel[res[0]]}.')

            elif len([x for x in listNumbers if x!=0]) == 2:
                logging.info(f'vi. The difference is {listLabel[res[0]]}, and {listLabel[res[1]]}.')

            elif len([x for x in listNumbers if x!=0]) == 3:
                logging.info(f'vi. The difference is {listLabel[res[0]]}, {listLabel[res[1]]}, and {listLabel[res[2]]}.')

            elif len([x for x in listNumbers if x!=0]) == 4:
                logging.info(f'vi. The difference is {listLabel[res[0]]}, {listLabel[res[1]]}, {listLabel[res[2]]}, and {listLabel[res[3]]}.')

            elif len([x for x in listNumbers if x!=0]) == 5:
                logging.info(f'vi. The difference is {listLabel[res[0]]}, {listLabel[res[1]]}, {listLabel[res[2]]}, {listLabel[res[3]]}, and {listLabel[res[4]]}.')

        elif dateDifference[-1].find('.') != -1:
            listNumbers = [0, int(dateDifference[0]), int(dateDifference[1]), int(dateDiffFrontApend[0]), int(dateDiffFrontApend[1])]
            listLabel = [f' {listNumbers[0]} days', f' {listNumbers[1]} hours', f' {listNumbers[2]} minutes', f' {listNumbers[3]} seconds', f' {listNumbers[4]} microseconds']
            res = [idx for idx, val in enumerate(listNumbers) if val != 0]  # Geeks for Geeks

            if len([x for x in listNumbers if x != 0]) == 0:
                logging.info(f'vi. The difference is NA. BASE Date and COMPARISON Date are both equal.')

            elif len([x for x in listNumbers if x != 0]) == 1:
                logging.info(f'vi. The difference is {listLabel[res[0]]}.')

            elif len([x for x in listNumbers if x != 0]) == 2:
                logging.info(f'vi. The difference is {listLabel[res[0]]}, and {listLabel[res[1]]}.')

            elif len([x for x in listNumbers if x != 0]) == 3:
                logging.info(
                    f'vi. The difference is {listLabel[res[0]]}, {listLabel[res[1]]}, and {listLabel[res[2]]}.')

            elif len([x for x in listNumbers if x != 0]) == 4:
                logging.info(
                    f'vi. The difference is {listLabel[res[0]]}, {listLabel[res[1]]}, {listLabel[res[2]]}, and {listLabel[res[3]]}.')

        elif dateDifference[0].find(',') != -1:
            listNumbers = [int(dateDiffBackAppend[0]), int(dateDiffBackAppend[1]), int(dateDifference[1]), int(dateDifference[2]), 0]
            listLabel = [f' {listNumbers[0]} days', f' {listNumbers[1]} hours', f' {listNumbers[2]} minutes', f' {listNumbers[3]} seconds', f' {listNumbers[4]} microseconds']
            res = [idx for idx, val in enumerate(listNumbers) if val != 0]  # Geeks for Geeks

            if len([x for x in listNumbers if x != 0]) == 0:
                logging.info(f'vi. The difference is NA. BASE Date and COMPARISON Date are both equal.')

            elif len([x for x in listNumbers if x != 0]) == 1:
                logging.info(f'vi. The difference is {listLabel[res[0]]}.')

            elif len([x for x in listNumbers if x != 0]) == 2:
                logging.info(f'vi. The difference is {listLabel[res[0]]}, and {listLabel[res[1]]}.')

            elif len([x for x in listNumbers if x != 0]) == 3:
                logging.info(
                    f'vi. The difference is {listLabel[res[0]]}, {listLabel[res[1]]}, and {listLabel[res[2]]}.')

            elif len([x for x in listNumbers if x != 0]) == 4:
                logging.info(
                    f'vi. The difference is {listLabel[res[0]]}, {listLabel[res[1]]}, {listLabel[res[2]]}, and {listLabel[res[3]]}.')

        elif len(dateDifference) == 3:
            listNumbers = [0, int(dateDifference[0]), int(dateDifference[1]), int(dateDifference[2]), 0]
            listLabel = [f' {listNumbers[0]} days', f' {listNumbers[1]} hours', f' {listNumbers[2]} minutes', f' {listNumbers[3]} seconds', f' {listNumbers[4]} microseconds']
            res = [idx for idx, val in enumerate(listNumbers) if val != 0]  # Geeks for Geeks

            if len([x for x in listNumbers if x!=0]) == 0:
                logging.info(f'vi. The difference is NA. BASE Date and COMPARISON Date are both equal.')

            elif len([x for x in listNumbers if x!=0]) == 1:
                logging.info(f'vi. The difference is {listLabel[res[0]]}.')

            elif len([x for x in listNumbers if x!=0]) == 2:
                logging.info(f'vi. The difference is {listLabel[res[0]]}, and {listLabel[res[1]]}.')

            elif len([x for x in listNumbers if x!=0]) == 3:
                logging.info(f'vi. The difference is {listLabel[res[0]]}, {listLabel[res[1]]}, and {listLabel[res[2]]}.')


        # Scrap the first idea...
        '''
        # Case 1: No Days... (with or without microseconds)
        if len(dateDifference.split(':')) == 3:
            case1 = dateDifference.split(':')
            # Case 1a: No microseconds
            if case1[2].find('.') == -1:
                # Inner-most case, ALL ZERO.
                if int(case1[2]) == int(case1[1]) == int(case1[0]) == 0: # 0 0 0
                    logging.info('BASE Date is the same as COMPARISON Date. No Change.')

                elif int(case1[1]) == int(case1[0]) == 0: # 0 0 1
                    logging.info(f'The difference is {int(case1[2])} seconds.')

                elif int(case1[2]) == int(case1[0]) == 0: # 0 1 0
                    logging.info(f'The difference is {int(case1[1])} minutes.')

                elif int(case1[2]) == int(case1[1]) == 0:  # 1 0 0
                    logging.info(f'The difference is {int(case1[0])} hours.')

                elif int(case1[0]) == 0: # 0 1 1
                    logging.info(f'The difference is {int(case1[1])} minutes, and {int(case1[2])} seconds.')

                elif int(case1[1]) == 0: # 1 0 1
                    logging.info(f'The difference is {int(case1[0])} hours, and {int(case1[2])} seconds.')

                elif int(case1[2]) == 0: # 1 1 0
                    logging.info(f'The difference is {int(case1[0])} hours, and {int(case1[1])} minutes.')

                else: # 1 1 1
                    logging.info(f'The difference is {int(case1[0])} hours, {int(case1[1])} minutes, and {int(case1[2])} seconds.')


            # Case 1b: No microseconds
            elif case1[2].find('.') != -1:
                caseMicro = case1[2].split('.')
                if int(caseMicro[1]) == int(caseMicro[0]) == int(case1[1]) == int(case1[0]) == 0: # 0 0 0 0
                    logging.info('BASE Date is the same as COMPARISON Date. No Change.')

                elif int(caseMicro[0]) == int(case1[1]) == int(case1[0]) == 0:  # 0 0 0 1
                    logging.info(f'The difference is {int(caseMicro[1])} microseconds.')

                elif int(case1[1]) == int(case1[0]) == 0:  # 0 0 1
                    logging.info(f'The difference is {int(caseMicro[0])} seconds, and {int(caseMicro[1])} microseconds.')

                elif int(case1[2]) == int(case1[0]) == 0:  # 0 1 0
                    logging.info(f'The difference is {int(case1[1])} minutes, and {int(caseMicro[1])} microseconds.')

                elif int(case1[2]) == int(case1[1]) == 0:  # 1 0 0
                    logging.info(f'The difference is {int(case1[0])} hours, and {int(caseMicro[1])} microseconds.')

                elif int(case1[0]) == 0:  # 0 1 1
                    logging.info(f'The difference is {int(case1[1])} minutes {int(caseMicro[0])} seconds, and {int(caseMicro[1])} microseconds.')

                elif int(case1[1]) == 0:  # 1 0 1
                    logging.info(f'The difference is {int(case1[0])} hours {int(caseMicro[0])} seconds, and {int(caseMicro[1])} microseconds.')

                elif int(case1[2]) == 0:  # 1 1 0
                    logging.info(f'The difference is {int(case1[0])} hours {int(case1[1])} minutes, and {int(caseMicro[1])} microseconds.')

                else:  # 1 1 1
                    logging.info(
                        f'The difference is {int(case1[0])} hours, {int(case1[1])} minutes, {int(caseMicro[0])} seconds, and {int(caseMicro[1])} microseconds.')



        elif len(dateDifference.split(':')) == 4:
        '''

    else:
        raise ValueError('Wrong input for BASE DATE or COMPARISON DATE. (Please follow the format of the example above), please try again...')

    return dateDifference



def main():
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    logging.debug('initializing...')

    try:
        dateDifferential()


    except ValueError as wrongInput:
        logging.info(f'\nError: {wrongInput}')
        logging.error(ValueError)

    except Exception as errorGeneral:
        logging.info(f'\nException: {errorGeneral}')
        logging.exception(Exception)




#########################
if __name__ == '__main__':
    main()
